

# tools.py
from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize the tool for internet searching capabilities
tool = DuckDuckGoSearchRun()
