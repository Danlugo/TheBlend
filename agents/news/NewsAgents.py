# template from https://github.com/joaomdmoura/crewAI-examples/tree/main/starter_template

from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from textwrap import dedent

class NewsAgents:

    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")
        self.default_llm = self.Ollama

    def analyst(self):
        return Agent(
            role="News Research Analyst",
            goal=dedent(f"""Being the best at gather, interpret data and amaze your customer with it"""),          
            backstory=dedent(f"""Known as the BEST research analyst, you're
                             skilled in sifting through news, company announcements, 
                             and market sentiments. Now you're working on a super 
                             important customer"""),
            allow_delegation=False,
            verbose=True,
            llm=self.default_llm,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news
                ]
                )

    def writer(self):
        return Agent(
            role="Senior News Content Writer",
            backstory=dedent(f"""Craft compelling content on news articles"""),
            goal=dedent(f"""You are a renowned Content Writer, known for your insightful and engaging articles. You analyze and resume articles so they are easy to understand and provide why is it important."""),
            allow_delegation=False,
            verbose=True,
            llm=self.default_llm,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news
                ]
                )
    


