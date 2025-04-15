import json
import os
import argparse
from agno.agent import Agent
from agno.models.base import Model
from agno.media import File


def load_alerts(file_path):
    """Load alerts from a JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading alerts file: {e}")
        return None


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
        description="You are an expert in computer security and data analysis.",
    )

    return agent


def summarize_alerts(args) -> str:
    """Use Agno to summarize alerts by category."""
    model_choice = get_model(args.provider, args.model_name)

    # Initialize Agno agent
    agent = get_agent(model_choice)

    # Create a prompt for the AI
    prompt = """
    You are a SOC analyst assistant. Please analyze the following security alerts and provide:
    
    1. A summary of alerts by category
    2. Key findings or patterns
    3. Recommended actions for the SOC team
    
    Format your response in markdown with clear sections.
    
    """

    try:
        # Call the Agno agent
        # setting the mimetype to text/plain
        # since automatically detecting the mimetype is not working correctly
        agent.instructions = prompt
        response = agent.run(
            "Please summarize the alerts",
            files=[File(filepath=args.file, mime_type="text/plain")],
        )

        # Return the generated summary
        # remove the markdown code blocks
        summary = response.content.replace("```markdown", "").replace("```", "")
        return summary
    except Exception as e:
        print(f"Error calling Agno API: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Summarize security alerts by category"
    )
    parser.add_argument(
        "--file",
        default="alerts.json",
        help="Path to the alerts JSON, CSV or markdown file",
    )
    parser.add_argument(
        "--output", default="summary.md", help="Output file for the summary"
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

    # Generate summary
    summary = summarize_alerts(args)
    if not summary:
        return

    # Save summary to file
    with open(args.output, "w") as file:
        file.write(summary)

    print(f"Summary saved to {args.output}")
    print("\nSummary:")
    print("=" * 80)
    print(summary)
    print("=" * 80)


if __name__ == "__main__":
    main()
