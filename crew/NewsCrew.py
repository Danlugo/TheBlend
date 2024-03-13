# template from https://github.com/joaomdmoura/crewAI-examples/tree/main/starter_template

from crewai import Crew
from crew.NewsAgents import NewsAgents
from crew.NewsTasks import NewsTasks
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class NewsCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
        agents = NewsAgents()
        tasks = NewsTasks()

        research_agent = agents.researcher()
        writer_agent = agents.writer()

        research_task = tasks.researcher(research_agent, self.topic)
        writer_task = tasks.writer(writer_agent)

        crew = Crew(
        agents=[ research_agent, writer_agent ],
        tasks=[ research_task, writer_task ],
        verbose=True
        )

        result = crew.kickoff()
        self.save_result(result)
        return result
  
    def save_result(self, content, filename="blog"):
        now = datetime.now().strftime("%Y-%m-%d")

        # Create the filename with timestamp
        filename_path = f"blog/{now}_{filename}.md"

        # Save the content to the file
        with open(filename_path, "w") as file:
            file.write(content)
        return 'Saved Results'


if __name__ == "__main__":
  print("## Welcome to your blog crew")
  print('-------------------------------')
  topic = """ Latest AI top stories """
  crew = NewsCrew(topic)
  results = crew.run()

  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(results)