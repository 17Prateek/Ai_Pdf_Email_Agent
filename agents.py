import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

from tools import ReadPDFTool, SendEmailTool

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini")

read_pdf_tool = ReadPDFTool()
send_email_tool = SendEmailTool()


analyzer_agent = Agent(
    role="PDF Analyzer",
    goal="Analyze PDF documents",
    backstory="Expert in document analysis",
    tools=[read_pdf_tool],
    llm=llm,
)

summary_agent = Agent(
    role="Summary Generator",
    goal="Generate document summaries",
    backstory="Expert in summarizing text",
    llm=llm,
)

email_agent = Agent(
    role="Email Sender",
    goal="Send summary via email",
    backstory="Automation specialist",
    tools=[send_email_tool],
    llm=llm,
)


def run_workflow(file_path):

    task1 = Task(
        description=f"Read and analyze the PDF located at {file_path}",
        agent=analyzer_agent,
    )

    task2 = Task(
        description="Create a short summary of the analysis",
        agent=summary_agent,
    )

    task3 = Task(
        description="Send the summary via email",
        agent=email_agent,
    )

    crew = Crew(
        agents=[analyzer_agent, summary_agent, email_agent],
        tasks=[task1, task2, task3],
    )

    result = crew.kickoff()

    return result