from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[TavilyTools()],
    debug_mode=True
)

agent.print_response('Use suas ferramentas para saber qual será a previsão do tempo para o Rio de Janeiro')