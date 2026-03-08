# # AI PDF Email Automation System

An AI-powered backend system that allows users to upload a PDF, automatically analyze its content using AI agents, generate a summary, and send the summary via email.

This project demonstrates the use of **CrewAI multi-agent architecture**, **LangChain tools**, **FastAPI backend**, and **SendGrid email automation**.

---

# Features

* Upload PDF files via API
* Extract text from PDF
* AI-powered document analysis
* Automatic summary generation
* Automated email delivery
* Multi-agent workflow using CrewAI
* REST API with FastAPI

---

# Technologies Used

* Python
* FastAPI
* CrewAI
* LangChain
* OpenAI API
* SendGrid
* PyMuPDF (PDF processing)
* python-dotenv

---

# Project Structure

```
ai_pdf_email_system/

main.py
agents.py
tools.py
requirements.txt
.env
README.md
uploads/
```

### File Description

**main.py**

FastAPI server that provides the API endpoint to upload PDF files and trigger the AI workflow.

**agents.py**

Defines the CrewAI agents and tasks responsible for:

* PDF analysis
* Summary generation
* Email sending

**tools.py**

Contains custom tools used by agents:

* PDF reading tool
* Email sending tool

**requirements.txt**

List of project dependencies.

**.env**

Environment variables for API keys and email configuration.

---

# System Workflow

```
User uploads PDF
      │
      ▼
PDF text extraction
      │
      ▼
AI Agent analyzes document
      │
      ▼
Summary Agent generates summary
      │
      ▼
Email Agent sends summary
```

---

# Installation Guide

## 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai_pdf_email_system.git

cd ai_pdf_email_system
```

## 2. Create virtual environment

```
python -m venv env
```

Activate environment

Windows:

```
env\Scripts\activate
```

Mac/Linux:

```
source env/bin/activate
```

---

# Install Dependencies

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

Example:

```
OPENAI_API_KEY=your_openai_api_key
SENDGRID_API_KEY=your_sendgrid_api_key

EMAIL_FROM=verified_sender@email.com
EMAIL_TO=receiver@email.com
```

---

# Running the Server

Start the FastAPI server:

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## Upload PDF

Endpoint:

```
POST /upload
```

Description:

Uploads a PDF file and starts the AI analysis workflow.

Example request using curl:

```
curl -X POST "http://127.0.0.1:8000/upload" \
 -H "Content-Type: multipart/form-data" \
 -F "file=@document.pdf"
```

Response:

```
{
  "result": "Summary generated and email sent successfully"
}
```

---

# Email Automation

This project uses **SendGrid** to send email summaries automatically.

Steps:

1. Create SendGrid account
2. Generate API Key
3. Verify sender email
4. Add credentials to `.env`

---

# AI Agent Architecture

The system uses a **multi-agent architecture** built with CrewAI.

### Agents

**PDF Analyzer Agent**

Responsible for analyzing the content of the uploaded PDF.

**Summary Agent**

Generates a concise summary of the analyzed document.

**Email Agent**

Sends the generated summary to the configured email address.

---

# Example Use Case

1. User uploads a research paper PDF
2. AI analyzes the document
3. A summary is generated
4. The summary is emailed to the user
