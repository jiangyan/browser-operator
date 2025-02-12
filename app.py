from flask import Flask, request, render_template
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
llm = ChatOpenAI(model="gpt-4o")

app = Flask(__name__)

def create_browser():
    """Create a new browser instance"""
    config = BrowserConfig(
        chrome_instance_path=os.getenv('CHROME_INSTANCE_PATH', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    )
    return Browser(config=config)

browser = None  # Initialize as None

async def run_agent(task: str):
    """Handle the agent interaction"""
    global browser
    try:
        if browser is None:
            browser = create_browser()
        agent = Agent(task=task, llm=llm, browser=browser)
        result = await agent.run()
        return result.final_result() or "No result found"
    finally:
        if browser:
            await browser.close()
            browser = None

@app.route("/", methods=["GET", "POST"])
def index():
    """Handle web routes"""
    if request.method == "POST":
        task = request.form["task"]
        result = asyncio.run(run_agent(task))
        return render_template('result.html', result=result, task=task)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)