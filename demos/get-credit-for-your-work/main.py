import json
import os
import argparse
from agno.agent import Agent
from agno.models.base import Model
from agno.tools.file import FileTools
from agno.storage.agent.sqlite import SqliteAgentStorage

agent_storage: str = "tmp/agent_storage.db"


# select the provider and model
def get_model(provider: str, model_name: str) -> Model:
    if provider == "openai":
        try:
            from agno.models.openai import OpenAIChat

            return OpenAIChat(id=model_name)
        except ImportError:
            print("OpenAI support requires additional packages. Install with:")
            print("pip install openai")
            raise SystemExit(1)

    elif provider == "ollama":
        try:
            from agno.models.ollama import Ollama

            return Ollama(id=model_name)
        except ImportError:
            print("Ollama support requires additional packages. Install with:")
            print("pip install ollama")
            raise SystemExit(1)
    else:  # default is google
        try:
            from agno.models.google import Gemini

            if os.environ.get("GEMINI_API_KEY"):

                model_gemini = Gemini(
                    id=model_name,
                    vertexai=False,
                    api_key=os.environ.get("GEMINI_API_KEY"),
                )
            else:
                # no api key, we are using vertex
                import google.auth

                credentials, PROJECT_ID = google.auth.default()
                LOCATION = "us-central1"

                model_gemini = Gemini(
                    id=model_name,
                    vertexai=True,
                    project_id=PROJECT_ID,
                    location=LOCATION,
                )
            return model_gemini
        except ImportError:
            print("Google/Gemini support requires additional packages. Install with:")
            print("pip install google-genai, google-auth")
            raise SystemExit(1)


def get_agent(model_choice: Model) -> Agent:

    # TODO toggle debug mode from command line switch

    agent = Agent(
        model=model_choice,
        markdown=True,
        show_tool_calls=False,
        telemetry=False,
        monitoring=False,
        debug_mode=False,
        description="You are an expert in computer security and security program management.",
        tools=[FileTools(read_files=True, save_files=False, list_files=True)],
        instructions=[
            "You have a local .md markdown file that describes a security program.",
            "Before answering any questions, use your list_files tool to identify any potentially relevant files based on the question.",
            "Then, use your read_file tool to read the contents of those files.",
            "Your goal is to have a conversation about the security program described in this file and help answer questions, suggest improvements and ensure that the folks involved get credit for their work.",
            "If you don't know the answer offhand, it is likely contained within these markdown files.",
        ],
        storage=SqliteAgentStorage(
            table_name="security_program_chat", db_file=agent_storage
        ),
        # Adds the current date and time to the instructions
        add_datetime_to_instructions=True,
        # Adds the history of the conversation to the messages
        add_history_to_messages=True,
        # Number of history responses to add to the messages
        num_history_responses=50,
    )

    return agent


def main():
    parser = argparse.ArgumentParser(
        description="Have a conversation about your security program"
    )

    parser.add_argument(
        "--provider",
        choices=["openai", "google", "ollama"],
        default="google",
        help="Choose the AI provider (openai, google, ollama)",
    )
    parser.add_argument(
        "--model-name",
        help="Specify the model name/id (e.g. gpt-4, gemini-2.0-flash, llama2)",
        default="gemini-2.0-flash",
    )
    parser.add_argument(
        "--location",
        help="Specify the GCP location (e.g. us-central1)",
        default="us-central1",
    )
    args = parser.parse_args()

    # create the  agent and invoke command line chat
    model_choice = get_model(args.provider, args.model_name)

    # Initialize Agno agent
    agent = get_agent(model_choice)
    agent.cli_app(stream=True)


if __name__ == "__main__":
    main()
