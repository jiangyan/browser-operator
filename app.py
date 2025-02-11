from flask import Flask, request, render_template
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path=os.getenv('CHROME_INSTANCE_PATH', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'),  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
        
    )
)

async def main(task):
    try:
        agent = Agent(task=task, llm=llm, browser=browser)
        result = await agent.run()
        final_result = result.final_result() or "No result found"
        return final_result
    finally:
        # Ensure browser is closed even if an error occurs
        await browser.close()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        result = asyncio.run(main(task))
        # Create a new browser instance for the next request
        global browser
        browser = Browser(
            config=BrowserConfig(
                chrome_instance_path=os.getenv('CHROME_INSTANCE_PATH', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'),
            )
        )
        return render_template('result.html', result=result, task=task)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)