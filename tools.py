import fitz
import os
from dotenv import load_dotenv

from crewai.tools import BaseTool
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")


class ReadPDFTool(BaseTool):
    name: str = "Read PDF Tool"
    description: str = "Reads text from a PDF file"

    def _run(self, file_path: str) -> str:

        text = ""
        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        return text


class SendEmailTool(BaseTool):
    name: str = "Send Email Tool"
    description: str = "Send email with summary"

    def _run(self, summary: str) -> str:

        message = Mail(
            from_email=EMAIL_FROM,
            to_emails=EMAIL_TO,
            subject="PDF Summary",
            html_content=summary,
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)

        return "Email Sent Successfully"