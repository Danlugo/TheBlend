from crewai import Crew
from textwrap import dedent

from agents.news.NewsAgents import NewsAgents
from agents.news.NewsTasks import NewsTasks

from dotenv import load_dotenv
import datetime

load_dotenv()

class NewsCrew:
    def __init__(self, company):
        self.company = company

    def run(self):
        agents = NewsAgents()
        tasks = NewsTasks()

        research_agent = agents.analyst()
        writer_agent = agents.writer()

        research_task = tasks.research(research_agent, self.company)
        writer_task = tasks.writer(writer_agent)

        crew = Crew(
        agents=[ research_agent, writer_agent ],
        tasks=[ research_task, writer_task ],
        verbose=True
        )

        result = crew.kickoff()
        return result
  
    def save_markdown(self, content, filename_prefix="markdown"):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Create the filename with timestamp
        filename = f"results/{now}_{filename_prefix}.md"

        # Save the content to the file
        with open(filename, "w") as file:
            file.write(content)

        return 'Saved Results'


if __name__ == "__main__":
  print("## Welcome to your blog crew")
  print('-------------------------------')
  news = """ Latest AI """
  
  news_crew = FinancialCrew(company)
  results = news_crew.run()

  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)