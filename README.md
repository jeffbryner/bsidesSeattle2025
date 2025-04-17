# Bsides Seattle 2025

## Track: Push It: New and exciting topics in security and privacy

## AI FOR security

### Abstract
Much the information about AI and security seems to be why you should fear it, ban it, slow roll it, secure it, etc. Very little attention is paid to how security teams can benefit from embracing AI in their own programs.

This talk will present 5 practical, actionable ways to adopt, make use of and get value from AI as part of your security program.

1) General productivity
Beyond email, document writing, summarizing. AI is great for

- Video/meeting note taking. Use it to help your remote/distributed team connect and stay in tune with what is happening in your program.
- Summarizing compliance docs like HITRUST, NIST, etc or customer contracts
- Write Policy documents

2) Summarize yer SOC

- How much effort do you put into daily summaries, shift turnover notes, upstream reporting, etc from your SOC? AI can help you with repeatable, punctual, predictable summaries and give you that time back

3) Get credit for your work

- Follow Daniel Meissler’s program/markdown and use it to get credit for those big projects you got across the line, or remind you of why you pivoted.


4) Risk analysis

- Give AI the framing of a project/initiative and have it prompt you through a risk analysis to highlight next steps

5) Agents to explore your data

- Chat with your SOC, ticketing or other data stores to see what insights they may have without writing SQL/etc
- vuln management

### Slides
The slides are available in reveal.js format at https://blog.jeffbryner.com/bsidesSeattle2025/slides.html


#### Running the sample code
Best to run the code in a virtual environment. I like using uv: 

- https://docs.astral.sh/uv/getting-started/installation/

### tl;dr installation
``` 
# mac
brew install uv

# windows
powershell -c "irm https://astral.sh/uv/install.ps1 | more"

# or install from https://github.com/astral-sh/uv/releases

```
### Clone the repository for this talk

```
git clone https://github.com/jeffbryner/bsidesseattle2025.git
cd bsidesseattle2025
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```
### Run the code
```
cd demos/<whichever demo>
python main.py
```

