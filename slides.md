% Bsides Seattle 2025
% Jeff Bryner
% https://github.com/jeffbryner/bsidesSeattle2025

# AI FOR security

## Big Idea

- Security teams should USE AI
- AI can help you reduce toil
- AI can give you that time back to do other things
- AI can help you do things you wouldn't normally be able to do

## What this talk is
- An actionable talk on how to use AI in your security program
- Live DEMOS (demo gods beware)
- Practical

## What this talk is not
- An intro to AI
- Threat modeling *of AI*
- A discussion of what model is best
- Perfect. I'm not a perfect speaker, I don't know everything, AI moves fast!


# General productivity

## Off the shelf FTW

- Video/meeting note taking
- Summarizing compliance docs like HITRUST, NIST, etc or customer contracts
- Write Policy documents

## Demo
- Writing policy without writing policy
- Vibe GRC-ing? 
- Input: HITRUST
- Output: Policy

## Policy
 ![](./demos/HITRUST-policy-writing.mp4)

# Summarize yer SOC

## Idea 

- How much effort do you put into daily summaries, shift turnover notes, upstream reporting, etc from your SOC? 
- Maybe you don't do it at all because it's a pain? 
- AI can help you with repeatable, punctual, predictable summaries
- Gives you that time back, or creates insights you wouldn't have otherwise had

## Demo
- Summarizing daily SOC activity
- Input: SOC alerts
- Output: Daily summary

## SOC Summary
 ![](./demos/AlertSummary.mp4)

## SOC Summary via code
- see ./demos/summarize-the-soc/
- The sample file of alerts is from: https://github.com/FrankHassanabad/suricata-sample-data/blob/master/samples/wrccdc-2018/alerts-only.json

# Get credit for your work

## Idea

- Follow [Daniel Meissler’s](https://danielmiessler.com/blog/fabric-origin-story) [alma security program markdown template](https://github.com/danielmiessler/fabric/blob/main/Alma.md) and use it to get credit for those big projects you got across the line, or remind you of why you pivoted.

## Demo
- Manage your security program with AI
- Input: Security program described in markdown
- Output: Conversations about your security program

## Alma Security Program Demo
- see ./demos/get-credit-for-your-work/
- The alma.md file is from https://github.com/danielmiessler/fabric/blob/main/Alma.md
- The main.py uses this file to have a conversation about your security program using your selected LLM


# Risk analysis

## Idea

- Give AI the framing of a project/initiative and have it prompt you through a risk analysis to highlight next steps

## Demo
- Use a team of risk experts acting together to get a risk analysis of a sample project
- Input: Project description
- Output: Risk analysis
- Code available at: https://github.com/aniket-work/Lets-Build-Enterprise-Cybersecurity-Risk-Assessment-Using-AI-Agents

# Agents to explore your data

## Idea

- Chat with your SOC, ticketing or other data stores to see what insights they may have without writing SQL/etc

## Demo
- Have a conversation with your data.
- Input: SOC data, vulnerability data
- Output: Conversational interaction with your data.
- Code available at: https://github.com/jeffbryner/illuminAIte

## Conversation with data
[![video session](https://img.youtube.com/vi/KnX_4-sD7Hg/0.jpg)](https://www.youtube.com/watch?v=KnX_4-sD7Hg)





# Thank you!
## Jeff Bryner
- @0x7eff
- https://jeffbryner.com
- https://github.com/jeffbryner