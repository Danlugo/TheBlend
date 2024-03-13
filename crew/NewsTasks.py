# template from https://github.com/joaomdmoura/crewAI-examples/tree/main/starter_template

from crewai import Task
from textwrap import dedent
from datetime import datetime

class NewsTasks():
  
  def researcher(self, agent, topic):
    return Task(description=dedent(f"""
        For topic: {topic}
        Collect and summarize top news stories, top company announcements, top research or academia announcements, and TOP analyst opinions.

        For news sites check news.google.com, VentureBeat.com, technologyreview.com, wired.com, Spectrum.ieee.org, AITrends.com, Engadget.com, techcrunch.com
        For research and academia check arxiv.org, aaai.org and dl.acm.org
        For specific AI Topics, check machinelearningmastery.com, openai.com
        For specific LLM check openai, antropic, and meta.

        AFTER COLLECTING THE INFORMATION,USE BELOW EXAMPLE ON HOW TO FORMAT THE DATA FOR EACH ARTICLE:

        1. 'Key Finding': Briefly state the main finding.
        2. 'Supporting Evidence': Provide a statistic or quote from a reliable source to substantiate the claim. 
        3. 'Optional Context': If relevant, include a sentence or two explaining the article or finding.
        4. 'Urls': List containing the URLs of websites used during the analysis.
        5. 'Date': Date when article was prepared (i.e. {datetime.now().strftime("%Y-%m-%d")}).                                   

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

        Your final answer MUST be REPORT. 

        {self.__tip_section()}
      """),
      agent=agent,
      expected_output=dedent(f"""  
        The report has four sections and you will need to use markdown:
        
        1. Section 1: Includes overall new blog Title and Summary Analysis
        2. Section 2: Shows a list for each article provided, and for each article, it shows 'key findings', 'supporting evidence' and any 'optional context'.
        3. Section 3: A valid list of urls collected during the analysis.
        4. Section 4: Shows the news blog was created by AI and the date when the report was prepared on {datetime.now().strftime("%Y-%m-%d")} by AI.
      """)
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll promote you!!!"