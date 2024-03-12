### TheBlend
Code that automatically populates a blog with latest news, deep dives and code updates




## Mac Dev Environment Setup
- 
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