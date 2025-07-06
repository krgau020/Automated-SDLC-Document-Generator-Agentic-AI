






from crewai_tools import SerperDevTool, BaseTool
from dotenv import load_dotenv
import os
from docx import Document
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

# Load environment variables
load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Web search tool
web_search_tool = SerperDevTool()

