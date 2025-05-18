# AI Terraform Assistant

An AI-powered conversational assistant designed to generate Terraform code snippets, provide AWS infrastructure guidance, and streamline Infrastructure as Code (IaC) workflows using OpenAI's GPT models.

---

## Architecture Overview

- **Backend**: FastAPI application serving REST endpoints, interfacing with OpenAI’s GPT API.  
- **AI Model**: OpenAI GPT-3.5-turbo (configurable to GPT-4o or others) for natural language processing and code generation.  
- **Client**: Terminal-based Python CLI that sends user prompts to the backend and displays AI-generated responses and Terraform snippets.  
# AI Terraform Assistant

An AI-powered conversational assistant designed to generate Terraform code snippets, provide AWS infrastructure guidance, and assist with DevOps tasks.

---

## Architecture Overview

- **Backend**: FastAPI application serving REST endpoints, interfacing with OpenAI’s GPT API.
- **AI Model**: OpenAI GPT-3.5-turbo (configurable to GPT-4o or others) for natural language processing and code generation.
- **Client**: Terminal-based Python CLI that sends user prompts to the backend and displays AI-generated responses and Terraform snippets.
- **Code Handling**: Extracts Terraform code blocks from AI responses and saves them automatically as `.tf` files for immediate use.
- **CI/CD**: Designed to integrate with GitHub workflows for automated linting, validation, and deployment pipelines (optional).

---

## Features

- Natural language querying for Terraform and AWS infrastructure.
- Automatic parsing and saving of Terraform snippets to local `.tf` files.
- Modular backend easily extendable for other IaC tools or cloud providers.
- Support for environment variable based API key management for security.
- Scaffold for integrating advanced workflows, including Git automation and cloud deployment.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher  
- Terraform CLI installed locally ([https://www.terraform.io/downloads.html](https://www.terraform.io/downloads.html))  
- OpenAI API key ([https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))  
- Git (optional, for version control and CI/CD integration)  

### Installation

```bash
git clone https://github.com/YourUsername/ai-terraform-assistant.git
cd ai-terraform-assistant
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt- **Code Handling**: Extracts Terraform code blocks from AI responses and saves them automatically as `.tf` files for immediate use.  
- **CI/CD**: Designed to integrate with GitHub workflows for automated linting, validation, and deployment pipelines (optional).  

---

## Features

- Natural language querying for Terraform and AWS infrastructure.  
- Automatic parsing and saving of Terraform snippets to local files.  
- Modular backend easily extendable for other IaC tools or cloud providers.  
- Support for environment variable based API key management for security.  
- Scaffold for integrating advanced workflows, including Git automation and cloud deployment.  

---

## Getting Started

### Prerequisites

- Python 3.10 or higher  
- Terraform CLI installed locally (https://www.terraform.io/downloads.html)  
- OpenAI API key (https://platform.openai.com/account/api-keys)  
- Git (optional, for version control and CI/CD integration)  

### Installation

```bash
git clone https://github.com/YourUsername/ai-terraform-assistant.git
cd ai-terraform-assistant
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt# AI Terraform Assistant

An AI-powered conversational assistant designed to generate Terraform code snippets, provide AWS infrastructure guidance, and assist with DevOps tasks.

---

## Architecture Overview

- **Backend**: FastAPI application serving REST endpoints, interfacing with OpenAI’s GPT API.
- **AI Model**: OpenAI GPT-3.5-turbo (configurable to GPT-4o or others) for natural language processing and code generation.
- **Client**: Terminal-based Python CLI that sends user prompts to the backend and displays AI-generated responses and Terraform snippets.
- **Code Handling**: Extracts Terraform code blocks from AI responses and saves them automatically as `.tf` files for immediate use.
- **CI/CD**: Designed to integrate with GitHub workflows for automated linting, validation, and deployment pipelines (optional).

---

## Features

- Natural language querying for Terraform and AWS infrastructure.
- Automatic parsing and saving of Terraform snippets to local `.tf` files.
- Modular backend, easily extendable for other IaC tools or cloud providers.
- Secure API key management through environment variables.
- Scaffold for integrating advanced workflows, including Git automation and cloud deployment.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Terraform CLI installed locally ([Download](https://www.terraform.io/downloads.html))
- OpenAI API key ([Get API key](https://platform.openai.com/account/api-keys))
- Git (optional, for version control and CI/CD integration)

### Installation

```bash
git clone https://github.com/YourUsername/ai-terraform-assistant.git
cd ai-terraform-assistant
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt# ai-terraform-assistant
# AI Terraform Assistant

An AI-powered conversational assistant designed to generate Terraform code snippets, provide AWS infrastructure guidance, and assist with DevOps tasks.

---

## Architecture Overview

* **Backend**: FastAPI application serving REST endpoints, interfacing with OpenAI’s GPT API.
* **AI Model**: OpenAI GPT-3.5-turbo (configurable to GPT-4o or others) for natural language processing and code generation.
* **Client**: Terminal-based Python CLI that sends user prompts to the backend and displays AI-generated responses and Terraform snippets.
* **Code Handling**: Extracts Terraform code blocks from AI responses and saves them automatically as `.tf` files for immediate use.
* **CI/CD**: Designed to integrate with GitHub workflows for automated linting, validation, and deployment pipelines (optional).

---

## Features

* Natural language querying for Terraform and AWS infrastructure.
* Automatic parsing and saving of Terraform snippets to local `.tf` files.
* Modular backend easily extendable for other IaC tools or cloud providers.
* Support for environment variable based API key management for security.
* Scaffold for integrating advanced workflows, including Git automation and cloud deployment.

---

## Getting Started

### Prerequisites

* Python 3.10 or higher
* Terraform CLI installed locally ([https://www.terraform.io/downloads.html](https://www.terraform.io/downloads.html))
* OpenAI API key ([https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))
* Git (optional, for version control and CI/CD integration)

---

### Installation

```bash
git clone https://github.com/YourUsername/ai-terraform-assistant.git
cd ai-terraform-assistant
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Environment Setup

To run this project, you must provide your own OpenAI API key. This key is not included in the repository to keep it secure.

**How to Set Your OpenAI API Key**

**macOS/Linux**

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

**Windows CMD**

```cmd
set OPENAI_API_KEY="your_openai_api_key_here"
```

**.env file (optional)**

```
OPENAI_API_KEY=your_openai_api_key_here
```

Make sure to add `.env` to your `.gitignore`. The app reads this key at runtime via environment variables.

---

## Running the Application

**Start the Backend API Server**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Start the Terminal CLI**

```bash
python3 ai_terraform_cli.py
```

---

## Usage

* Type infrastructure or DevOps-related requests into the CLI (e.g., “Deploy an EC2 instance in a private subnet”).
* AI will respond with relevant Terraform code and explanations.
* Any `.tf` code blocks are automatically saved to files like `terraform_snippet_1.tf`.
* You can apply the generated code using standard Terraform commands:

```bash
terraform init
terraform plan
terraform apply
```

---
