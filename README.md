# Browser Agent Web Interface

A simple Flask web application that provides a user interface for running browser automation tasks using the browser-use library. Users can input natural language tasks, and the application will execute them using a combination of LLM (Language Model) and browser automation.

## Features

- Clean and intuitive web interface
- Powered by Claude 3.5 Sonnet for task understanding
- Browser automation using browser-use library
- Automatic Chrome instance management
- Responsive design

## Prerequisites

- Python 3.11+
- Google Chrome browser
- uv (Python package installer)
- Playwright

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jiangyan/browser-operator.git
cd browser-operator
```

2. Create and activate virtual environment:
```bash
# Create virtual environment using uv
uv venv --python 3.11

# Activate virtual environment
# For Mac/Linux:
source .venv/bin/activate
# For Windows:
# .venv\Scripts\activate
```

3. Install dependencies:
```bash
# Install browser-use and its dependencies
uv pip install browser-use flask python-dotenv langchain-anthropic

# Install Playwright browsers
playwright install
```

4. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

5. Update the `.env` file with your configuration:
```
ANTHROPIC_API_KEY=your_api_key_here
CHROME_INSTANCE_PATH=/path/to/your/chrome  # Adjust based on your OS
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Enter your task in the input field and click "Execute Task"

## Environment Variables

- `ANTHROPIC_API_KEY`: Your Anthropic API key for Claude
- `CHROME_INSTANCE_PATH`: Path to Chrome executable (OS-specific)
  - macOS: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
  - Windows: `C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe`
  - Linux: `/usr/bin/google-chrome`

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 