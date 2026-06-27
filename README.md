# 🤖 AI-Powered Customer Support Automation System using LangGraph

> **An Intelligent Multi-Agent Customer Support System powered by LangGraph, LangChain, Retrieval-Augmented Generation (RAG), SQLite Memory, and Human-in-the-Loop (HITL) Approval.**

---

## 📖 Overview

The **AI-Powered Customer Support Automation System** is designed to automate customer support operations by intelligently routing customer queries to specialized support agents.

The application uses **LangGraph** to orchestrate the workflow, **LangChain** and **FAISS** for Retrieval-Augmented Generation (RAG), **SQLite** for persistent conversation memory, and **Human-in-the-Loop (HITL)** approval for sensitive customer requests.

The workflow simulates how modern AI-driven customer support systems operate in real-world organizations by combining intelligent routing, knowledge retrieval, memory management, and human supervision.

---

# 🔗 GitHub Repository

The complete source code for this project is available on GitHub.

**Repository Link:**

```text
https://github.com/santhoshroyals/Customer_Support_System
```

Or directly visit:

👉 **https://github.com/santhoshroyals/Customer_Support_System**

---

# 🎯 Project Objectives

The main objectives of this project are:

* Automatically classify customer queries into appropriate departments.
* Route queries using a LangGraph workflow.
* Retrieve accurate information from a company knowledge base using RAG.
* Store customer conversation history using SQLite.
* Recall previous customer interactions.
* Support Human-in-the-Loop approval for critical requests.
* Validate responses using a Supervisor Agent.
* Generate an accurate final response.

---

# ✨ Key Features

* ✅ Multi-Agent Customer Support Workflow
* ✅ LangGraph-Based Workflow Orchestration
* ✅ Automatic Intent Classification
* ✅ Department-Based Query Routing
* ✅ Retrieval-Augmented Generation (RAG)
* ✅ FAISS Vector Database
* ✅ HuggingFace Embeddings
* ✅ SQLite Conversation Memory
* ✅ Memory Recall
* ✅ Human-in-the-Loop (HITL)
* ✅ Supervisor Agent Validation
* ✅ Modular Architecture
* ✅ Clean Console-Based Interface

---

# 🏢 Supported Departments

| Department            | Handles                                                |
| --------------------- | ------------------------------------------------------ |
| **Sales**             | Pricing, Products, Subscription Plans                  |
| **Technical Support** | Login Issues, Errors, Installation, Configuration      |
| **Billing**           | Payments, Refunds, Invoices, Compensation              |
| **Account**           | Password Reset, Profile Management, Account Operations |

---

# 🛠️ Technologies Used

| Technology                     | Purpose                 |
| ------------------------------ | ----------------------- |
| Python                         | Programming Language    |
| LangGraph                      | Workflow Orchestration  |
| LangChain                      | RAG Framework           |
| FAISS                          | Vector Database         |
| HuggingFace Embeddings         | Semantic Search         |
| SQLite                         | Persistent Memory       |
| RecursiveCharacterTextSplitter | Document Chunking       |
| VS Code                        | Development Environment |

---

# 🏗️ System Architecture

```text
Customer Query
       │
       ▼
Memory Check
       │
       ▼
Intent Classification
       │
       ▼
Department Routing
       │
 ┌─────┼─────┬─────┐
 ▼     ▼     ▼     ▼
Sales Technical Billing Account
       │
       ▼
Approval Check
       │
 ┌─────┴──────────┐
 ▼                ▼
Human Approval  Supervisor Agent
       │           │
       └─────┬─────┘
             ▼
      Save Conversation
        (SQLite Memory)
             ▼
      Final Response
```

---

# 📂 Project Structure

```text
CustomerSupportAutomation/
│
├── app.py
├── graph.py
├── state.py
├── nodes.py
├── agents.py
├── approval.py
├── supervisor.py
├── rag.py
├── memory.py
├── utils.py
├── requirements.txt
├── README.md
├── Project_Report.pdf
│
├── database/
│   ├── memory.db
│   └── schema.sql
│
├── knowledge_base/
│   ├── Company_Policy.txt
│   ├── Pricing_Guide.txt
│   ├── Technical_Manual.txt
│   └── FAQ.txt
│
├── workflow/
│   └── workflow_diagram.pdf
│
└── screenshots/
    └── Execution_Screenshots.pdf
```

---

# 🔍 Retrieval-Augmented Generation (RAG)

Instead of returning predefined answers, the system retrieves relevant information from company documents.

### RAG Workflow

1. Load Documents
2. Split Documents into Chunks
3. Generate Embeddings
4. Store Embeddings in FAISS
5. Retrieve Relevant Context
6. Generate Response

### Knowledge Base Documents

* Company Policy
* Pricing Guide
* Technical Manual
* FAQ

This enables the system to answer customer questions using actual company documentation.

---

# 💾 SQLite Memory

Customer conversations are stored in **SQLite** to maintain interaction history.

### Stored Information

* Customer ID
* Customer Name
* Customer Query

### Example

**Customer Query**

```text
I have a billing issue.
```

Later...

```text
What was my previous support issue?
```

**Response**

```text
Your previous support issue was:

I have a billing issue.
```

---

# 👨‍💼 Human-in-the-Loop (HITL)

Certain customer requests require manual approval.

Examples include:

* Refund Requests
* Subscription Cancellation
* Account Closure
* Compensation Requests
* Escalation Requests

The Human Supervisor reviews these requests before the workflow continues.

---

# 👨‍💻 Supervisor Agent

The Supervisor Agent performs the final quality check before sending the response to the customer.

Responsibilities include:

* Reviewing agent responses
* Verifying approval status
* Validating responses
* Generating the final response

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/santhoshroyals/Customer_Support_System.git
```

Move into the project directory

```bash
cd Customer_Support_System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app.py
```

---

# 🧪 Sample Test Queries

### Sales

```text
What are the pricing plans available for your software?
```

### Technical Support

```text
My application crashes whenever I upload a file.
```

### Account

```text
I forgot my account password.
```

### Billing

```text
I need a refund for my annual subscription.
```

### Human Approval

```text
Please cancel my subscription.
```

### SQLite Memory

```text
What was my previous support issue?
```

---

# 📊 Project Deliverables

This repository includes:

* Source Code
* LangGraph Workflow
* RAG Integration
* SQLite Memory
* Human-in-the-Loop Workflow
* Supervisor Agent
* Project Report
* Workflow Diagram
* Execution Screenshots
* SQLite Database & Schema

---

# 📈 Future Enhancements

* Integration with Large Language Models (LLMs)
* Web Interface using Streamlit or FastAPI
* Voice-Based Customer Support
* Multi-Language Support
* Customer Authentication
* Email & CRM Integration
* Cloud Deployment
* Analytics Dashboard
* AI-Based Intent Classification

---

# 👨‍💻 Author

**Santhosh**

Customer Support Automation Project

---

# 📚 References

* LangGraph Documentation
* LangChain Documentation
* Hugging Face Sentence Transformers
* FAISS Documentation
* SQLite Documentation
* Python Documentation

---

## ⭐ Acknowledgement

This project was developed as part of an academic assignment to demonstrate the practical implementation of **LangGraph**, **Retrieval-Augmented Generation (RAG)**, **SQLite Memory**, **Human-in-the-Loop Approval**, and **Multi-Agent Workflow Orchestration** in an AI-powered customer support system.
