from crewai import Task
from textwrap import dedent
import datetime

class NewsTasks():
  
  def research(self, agent, company):
    return Task(description=dedent(f"""
        Collect and summarize recent news articles, press
        releases, and market analyses related to the stock and
        its industry.                                   

        EXAMPLE RESEARCH DATA CONTENT:

        Market Research Reports: Recent reports on the global robotics AI chipset market size, growth projections, and impact of Generative AI (GenAI) on this market. Look for reputable market research firms like Gartner, IDC, or McKinsey & Company.
        Industry News Articles: Articles discussing the integration of GenAI with robotics and the potential benefits for the robotics market. Sources could include technology news websites, robotics industry publications, or press releases from AI or robotics companies.
        Analyst Opinions: Insights from industry analysts regarding the impact of GenAI on the future of robotics. These can be found in analyst reports, interviews, or articles featuring analyst commentary.
        
        Once the research is complete, the information should be summarized for the content writer in a concise and easy-to-understand format. Here's what to include:

        1. Key Finding: Briefly state the main finding, such as "GenAI is expected to significantly boost the global robotics AI chipset market."
        2. Supporting Evidence: Provide a statistic or quote from a reliable source to substantiate the claim. For instance, "According to a recent Gartner report, the market is expected to reach $XX billion by 20XX, driven largely by the adoption of GenAI in robotics."
        3. Optional Context: If relevant, include a sentence or two explaining how GenAI will contribute to market growth. This could involve its ability to create more intelligent robots, improve robot adaptability, or personalize robot functionalities.
        
        Your final answer MUST be a report
        
        {self.__tip_section()}
  
        Make sure to use the most recent data as possible.
      """),
      agent=agent,
      expected_output=dedent(f"""  """)
    )

  def writer(self, agent):
    return Task(description=dedent(f"""
        Review and synthesize the analyses provided by the
        Research Analyst to form a comprehensive news report. 

        Make sure to include a section that shows top 10 insights and 
        provide valid urls to the articles.

        Below is an Inverted Pyramid news example.
       
        AI Races Forward: Top 10 Developments Shaping the Future                        
        Artificial intelligence continues its rapid evolution, impacting various aspects of our lives. From advancements in chip design to responsible AI practices, here's a breakdown of the top 10 headlines making waves in the AI landscape:

        GenAI Drives Robotics Market Growth: Generative AI (GenAI) is projected to significantly boost the global robotics AI chipset market, opening doors for more intelligent and adaptable robots.
        SAP Leverages AI for Cloud Growth: Tech giant SAP sees AI as a key strategy to accelerate its cloud revenue growth, highlighting the increasing reliance on AI in business operations.
        Anthropic Unveils Safer AI Models: AI startup Anthropic claims its latest models minimize the risk of hallucinations, a major concern in AI development, potentially leading to more reliable AI outputs.
        The Race for Global AI Chip Supremacy Heats Up: Rumors swirl about a multi-trillion dollar project to develop a groundbreaking global AI chip, signifying the intense competition in this crucial area.
        Elon Musk and OpenAI Clash Over Responsible AI: A lawsuit filed by Elon Musk against OpenAI regarding its leadership raises questions about the direction of AI development and the importance of responsible AI practices.
        Human Oversight Remains Critical for AI Success: Experts emphasize the need for "human-in-the-loop" approaches, where humans collaborate with AI systems, ensuring proper evaluation and responsible use of AI.
        AI Startups Continue to Disrupt Industries: The AI startup scene remains vibrant, with new ventures emerging to tackle challenges in various sectors, from healthcare to finance.
        Securities and Exchange Commission Investigates OpenAI: The US Securities and Exchange Commission reportedly probes OpenAI following the CEO's dismissal, adding another layer of scrutiny to the organization.
        Generative AI Democratizes Knowledge and Skills: Analysts predict Generative AI will make knowledge and skills more accessible, potentially transforming how we learn and work.
        Preparing for an AI-Driven Future: Businesses and organizations are urged to develop strategies to adapt to the changing landscape brought about by advancements in AI.

        This news blog was created by AI.
        Created on 2023-01-01  

        Your final answer MUST be news blog using Inverted Pyramid style. 
        Make it pretty and well formatted for your customer.
        {self.__tip_section()}
      """),
      agent=agent
      expected_output=dedent(f"""  YOU MOST USED THE PROVIDED EXAMPLE AS FORMAT FOR BUILDING THE NEWS""")
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll promote you!!!"