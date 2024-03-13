# template from https://github.com/joaomdmoura/crewAI-examples/tree/main/starter_template

from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from textwrap import dedent
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool,
    ScrapeWebsiteTool)

class NewsAgents:

    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="llama2", base_url="http://10.0.0.148:11434")
        self.default_llm = self.Ollama
        self.search_tool = SerperDevTool()
        self.scrape_website_tool = ScrapeWebsiteTool()

    def researcher(self):
        return Agent(
            role="Senior Research Analyst",
            goal=dedent(f"""Being the best at gather, interpret data and amaze your customer with it"""),          
            backstory=dedent(f"""Known as the BEST analyst, you're skilled in sifting through market research, industry news, company announcements, and analyst opinions. Now you're working on a super important customer"""),
            allow_delegation=False,
            verbose=True,
            llm=self.default_llm,
            tools=[
                SearchTools.search_internet,
                SearchTools.search_news,
                self.scrape_website_tool
                ]
                )

    def writer(self):
        return Agent(
            role="Senior Content Writer",
            backstory=dedent(f"""Craft compelling, well structured news article blog"""),
            goal=dedent(f"""You are a renowned Content Writer, known for your insightful and engaging articles. You analyze and resume articles so they are easy to understand and provide why is it important."""),
            allow_delegation=False,
            verbose=True,
            llm=self.default_llm
            )
    


