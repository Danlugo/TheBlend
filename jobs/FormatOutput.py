
from datetime import datetime

class FormatOutput:

    def __init__(self) -> None:
        pass

    def load_blog(self, file_name=None) -> str:
        
        if file_name is None:
            now = datetime.now().strftime("%Y-%m-%d")
            file_name = f"blog/{now}_blog.md"

        with open(file_name, 'r') as file:
            data = file.read()
            return data

    def format_gpt4(self, text) -> str:
        new_text = text
        new_text = new_text.replace('# Blog Report','')
        new_text = new_text.replace('## Section 1: Overview','')
        new_text = new_text.replace('# Section 1: Overall Summary','')
        new_text = new_text.replace('**Summary Analysis**:','')        
        new_text = new_text.replace('## Section 2: Article Analysis','')
        new_text = new_text.replace('# Section 2: Article Summaries','')

        new_text = new_text.replace('**Article 1**','')
        new_text = new_text.replace('**Article 2**','')
        new_text = new_text.replace('## Section 2:','')
        new_text = new_text.replace('Section 3:','')
                                    
        new_text = new_text.replace('**Title**:', '')
        new_text = new_text.replace('**Key Findings**:', '')
        new_text = new_text.replace('**Supporting Evidence**:', '')
        new_text = new_text.replace('**Optional Context**:','')
        new_text = new_text.replace('**Urls**:','')
        new_text = new_text.replace('**Date**:','Date: ')
        new_text = new_text.replace('## Section 3: AI Creation', '')
        new_text = new_text.replace('This blog was created by AI.','This blog was created by AI, GPT4')
        return new_text
    
    def run(self) -> str:
        data = self.load_blog()
        text = self.format_gpt4(data)
        return text
                      

if __name__ == "__main__":
    print("-- start --\n")
    f = FormatOutput()
    text = f.run
    print(text)
    print("\n-- end --")

        
