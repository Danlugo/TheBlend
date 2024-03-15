![Alt text](https://github.com/Danlugo/TheBlend/blob/main/images/theblendai_logo.png "Logo")


# TheBlend

Its the program used by TheBlend.ai Blog website that uses AI to create blog content for the most complex topics or topics that require tools to access the internet, scrape web sites and more.


## How does it work?
The app uses Crewai concepts (Crew) to run multiple LLMs (Agents) to do the work (Tasks). 
The Agents & Tasks are setup to search the internet for the latest AI technologies and asked to resturn the results into a specific format so they can later be posted in a website.


### Mac Dev Environment Setup

1. Install Brew https://brew.sh/
2. Install Python 3.12 https://www.python.org/downloads/release/python-3122/ (download, run macos installer)
3. Install Visual Studio https://visualstudio.microsoft.com/vs/mac/ 
4. In Mac Terminal, run: git clone https://github.com/Danlugo/TheBlend.git
5. Open Visual Studio App
6. In Visual Studio, click open and select new folder created by github

### Setup Python Virtual Environment
1. In Visual Studio, click view from top menu and select terminal
2. In the terminal window, copy paste below code
    python3.12 -m venv env
    source env/bin/activate
    pip install --upgrade pip
3. Type pip install -r requirements.txt
4. Update the .env files with needed keys and the Agent and Tasks files to change topics.
5. Run news_crew.py to run agents


### Finally, It uses a GoDaddy website to show the feeds.
Check out TheBlend.ai


### Main Page
![Alt text](https://github.com/Danlugo/TheBlend/blob/main/images/TheBlendai_home.png "Home")



### Blog
![Alt text](https://github.com/Danlugo/TheBlend/blob/main/images/TheBlendai_blog.png "Blog")



