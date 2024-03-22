# template from https://github.com/joaomdmoura/crewAI-examples/tree/main/starter_template

from crewai import Task
from textwrap import dedent
from datetime import datetime

class BlogTasks():
  
  def researcher(self, agent, topic):
    return Task(description=dedent(f"""
        For topic: {topic}
        Collect and summarize top news stories, top company announcements, top research or academia announcements, and TOP analyst opinions.

        For news sites check news.google.com, VentureBeat.com, technologyreview.com, wired.com, Spectrum.ieee.org, AITrends.com, Engadget.com, techcrunch.com
        For research and academia check arxiv.org, aaai.org and dl.acm.org
        For specific AI Topics, check machinelearningmastery.com, openai.com
        For specific LLM check openai, antropic, and meta.

        AFTER COLLECTING THE INFORMATION,USE BELOW EXAMPLE ON HOW TO FORMAT THE DATA FOR EACH ARTICLE:

        1. 'Key Finding': Briefly state the main finding and supporting evidence.
        2. 'Optional Context': If relevant, include a sentence or two explaining the article or finding.
        3. 'Urls': List containing the URLs of websites used during the analysis.

        Your final answer MUST be a report
        
        {self.__tip_section()}
  
        Make sure to use the most recent data as possible. Today's date is {datetime.now().strftime("%Y-%m-%d")}
      """),
      agent=agent,
      expected_output=dedent(f"""  YOU MUST USE THE EXAMPLE TO WHAT INCLUDE AND FOLLOW UP THE EXAMPLE INSTRUCTIONS """)
    )

  def writer(self, agent):
    return Task(description=dedent(f"""
        Review and synthesize all the analyses provided by the Senior Research Analyst to form a comprehensive report.                                            

        Your final answer MUST be REPORT, keep it brief. 

        {self.__tip_section()}
      """),
      agent=agent,
      expected_output=dedent(f"""  
        The report has four sections and you will need to use markdown:
        
        1. Includes overall new blog 'Title', 'Date: {datetime.now().strftime("%Y-%m-%d")}' and 'Summary Analysis' of all articles.
        2. Shows a list for each article 'Title', 'key findings and supporting evidence', 'optional context', 'Urls' and 'Date'.
        4. Shows blog was created by AI'.
      """)
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll promote you!!!"