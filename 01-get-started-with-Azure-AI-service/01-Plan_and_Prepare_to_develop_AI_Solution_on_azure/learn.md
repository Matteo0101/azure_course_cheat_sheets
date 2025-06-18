# Azure AI Solution Design Guide

## 🔍 Problem
You need to design and develop a comprehensive AI solution using Microsoft Azure, which involves choosing the right services, tools, and architectural patterns to support capabilities such as generative AI, computer vision, speech, and natural language processing — while ensuring responsible AI practices.

## ✅ Solution with Azure
Use **Azure AI services** and the **Azure AI Foundry platform** to plan, develop, and manage AI-powered applications. Foundry supports generative AI development, agent-based workflows, and orchestrations like Prompt Flow, enabling robust, scalable solutions.

## 🧩 Required Components
* **Azure AI Services**: Vision, Speech, Language, Translator, OpenAI, Document Intelligence, Content Safety, Face, Custom Vision
* **Azure AI Foundry** (portal + SDK)
* **Azure AI Hub (optional)** for advanced workflows
* **Development Tools**:
   * VS Code (local or container image in browser)
   * Azure CLI / Bicep / ARM for provisioning
   * GitHub + GitHub Copilot
* **SDKs and APIs**:
   * Azure AI Foundry SDK
   * Azure AI Services SDKs
   * Prompt Flow SDK
   * REST APIs

## 🏗️ Architecture / Development

### Azure AI Foundry Structure
* **Foundry Projects**:
   * Centralize development of chat apps and agent-based solutions
   * Connect to Azure AI services
* **Hub-based Projects**:
   * Include managed compute, storage, key vault
   * Ideal for Prompt Flow, fine-tuning, multi-role teams (developers, data scientists)

### Provisioning Options
* **Single-service resources**: Ideal for small apps or evaluation (includes free tier)
* **Multi-service resource**: Easier management across services like OpenAI, Speech, Translator, Vision, etc.
* **Important**: Select the correct **Azure AI Services** resource type (🧠 icon), not legacy Cognitive Services

### Developer Environments
* VS Code container (pre-configured for Foundry)
* Visual Studio / VS Code with GitHub integration
* SDKs available for: C#, Python, Node, Java, TypeScript

## ✅ Best Practices / Considerations

### Responsible AI Principles (Microsoft):
* **Fairness**: Avoid bias, ensure representativity in training data
* **Reliability & Safety**: Use thresholds, validate confidence scores, rigorous testing
* **Privacy & Security**: Protect sensitive data during training/inference
* **Inclusiveness**: Diverse team input during development
* **Transparency**: Communicate system limitations, decision logic

### Additional Considerations:
* **Regional Availability**: Check availability per service/model
* **Cost Management**: Use pricing calculator and Foundry's centralized cost control
* **Quota Awareness**: Especially for VS Code compute containers and model usage
* **Tool Selection**: Match IDE and SDKs to your language and workflow preference

## ❓ Sample Exam Questions

**Q1**: You are planning to build an AI application that extracts key information from scanned receipts. Which Azure service should you use?
**A1**: Azure AI Document Intelligence

**Q2**: What is the benefit of using Azure AI Foundry instead of provisioning services individually?
**A2**: Centralized project/resource management, integrated portal + SDKs, simplified deployment of multi-service solutions

**Q3**: You need to develop a generative AI agent that can act autonomously based on prompts. What Azure components should you consider?
**A3**: Azure OpenAI (via Foundry), Azure AI Foundry Agent Service, optionally Prompt Flow SDK

**Q4**: A teammate wants to build a model fine-tuning workflow and securely store data and secrets. Which type of project is most suitable?
**A4**: Hub-based project in Azure AI Foundry

**Q5**: What is a key difference between the Azure AI services icon and the Azure Cognitive Services icon when provisioning in the portal?
**A5**: The Azure AI services icon provides access to the latest services (e.g., OpenAI, Content Understanding), while the older Cognitive Services icon does not.

**Q6**: Your development team prefers working in-browser and wants pre-configured SDKs. What is the recommended approach?
**A6**: Use the VS Code container image via Azure AI Foundry portal