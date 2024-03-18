


class FormatOutput:

    def __init__(self) -> None:
        pass

    def load_blog(self, file_name) -> str:
        with open(file_name, 'r') as file:
            data = file.read()
            return data

    def format_gpt4(self, text) -> str:
        print('Format GPT4 created content')
        new_text = text
        new_text = new_text.replace('# Blog Report','')
        new_text = new_text.replace('## Section 1: Overview','')
        new_text = new_text.replace('**Summary Analysis**: ','')        
        new_text = new_text.replace('## Section 2: Article Analysis','')
        new_text = new_text.replace('**Title**: ', '')
        new_text = new_text.replace('**Key Finding**: ', '')
        new_text = new_text.replace('**Supporting Evidence**: ', '')
        new_text = new_text.replace('**Optional Context**: ','')
        new_text = new_text.replace('**Urls**: ','')
        new_text = new_text.replace('**Date**: ','Date: ')
        new_text = new_text.replace('## Section 3: AI Creation', '')
        new_text = new_text.replace('This blog was created by AI.','This blog was created by AI, GPT4')
        return new_text
                      

if __name__ == "__main__":
    print("## Start Formatting")
    f = FormatOutput()
    raw_content = f.load_blog('blog/2024-03-18_blog.md')
    formatted_content = f.format_gpt4(raw_content)
    print(formatted_content)

        
