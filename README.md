![Alt text](https://github.com/Danlugo/TheBlend/blob/main/images/theblendai_logo.png "Logo")


### TheBlend

Its a program that uses crewai to search the internet for the latest AI and then serves them into a RSS feed so it can be exposed in a website as blogs.



## Mac Dev Environment Setup

1. Install Brew https://brew.sh/
2. Install Python 3.12 https://www.python.org/downloads/release/python-3122/ (download, run macos installer)
3. Install Visual Studio https://visualstudio.microsoft.com/vs/mac/ 
4. In Mac Terminal, run: git clone https://github.com/Danlugo/TheBlend.git
5. Open Visual Studio App
6. In Visual Studio, click open and select new folder created by github

## Setup Python Virtual Environment
1. In Visual Studio, click view from top menu and select terminal
2. In the terminal window, copy paste below code
    python3.12 -m venv env
    source env/bin/activate
    pip install --upgrade pip
3. Type pip install -r requirements.txt
4. Update config file to select topics
5. Run app.py to run agents

# Deploy to Streamlit in order to be the rss feder
1. Go to Streamlit, setup an account that points to Github.
2. Deploy


# Finally, It uses a GoDaddy website to show the feeds.
Check out TheBlend.ai

![Alt text](https://github.com/Danlugo/TheBlend/blob/main/images/TheBlendai_home.png "Home")
![Alt text](https://github.com/Danlugo/TheBlend/blob/main/images/TheBendai_blog.png "Blog")
