# 🤖 Azure AI Foundry Agent Service

## ❓ **Problem**
You need to build AI agents that can handle tasks such as customer service, data analysis, or workflow automation with minimal code, secure data handling, and without managing underlying infrastructure. Traditional approaches require significant effort to integrate grounding data and custom logic, increasing development complexity.

## ✅ **Solution with Azure**
Use **Azure AI Foundry Agent Service**, a fully managed platform that allows you to create, deploy, and scale extensible AI agents securely. It supports agent development through a portal UI or minimal code (less than 50 lines), automatically handles infrastructure, tool invocation, and conversation state.

## 🧩 **Required Components**
* **Azure AI Hub** with an **AI Project**
* **Azure AI Foundry Agent Service**
* (Optional) **Azure Key Vault**, **Azure AI Search**, **Azure Storage**, **Azure Functions**
* SDK or REST API for application integration
* Supported AI models: **Azure OpenAI**, **Llama 3**, **Mistral**, **Cohere**

## 🏗️ **Architecture / Development**

### 🔧 Agent Setup Options

1. **Basic Setup**
   * Azure AI Hub
   * AI Project
   * AI Services

2. **Standard Setup**
   * Basic Setup + Key Vault, AI Search, Azure Storage

### 🔁 Development Pattern

1. Connect to AI Project (via endpoint + Entra ID)
2. Reference or define an agent:
   * Choose model
   * Define instructions
   * Attach tools (e.g., code interpreter, custom functions)
3. Create a thread for a chat session
4. Send messages and invoke the agent
5. Monitor thread status, retrieve responses
6. Repeat for chat loop
7. Clean up by deleting agent and thread

## 📦 Tools for Agents

### **Knowledge Tools:**
* Bing Search
* File Search (vector store)
* Azure AI Search
* Microsoft Fabric

### **Action Tools:**
* Code Interpreter (Python sandbox)
* Custom Function
* Azure Function
* OpenAPI Spec (external APIs)

## 🧠 **Best Practices / Considerations**

* Use **threads** to manage conversation state securely and avoid manual state handling.
* Prefer **custom storage** (Azure Blob) if you require full control over data visibility.
* Choose **appropriate tools** based on the agent's tasks (e.g., Bing for real-time info, Azure Functions for serverless execution).
* Use **built-in security features**: secure data handling, keyless auth, Entra ID integration.
* Evaluate your scenario: Foundry Agent is best for extensible, code-light agents. Consider **Copilot Studio** for M365 integration or **Semantic Kernel** for agent orchestration.

## ❓💡 **Sample Exam Questions**

1. **You need to build an AI agent that queries real-time data from the web and performs code-based analysis. Which two tools should you include in your agent?**
   * A. Bing Search ✅
   * B. Azure Storage
   * C. Azure Function
   * D. Code Interpreter ✅

2. **What is the minimum setup required to deploy an agent using Azure AI Foundry Agent Service?**
   * A. Azure AI Hub, AI Project, Key Vault
   * B. Azure AI Hub, AI Project, AI Services ✅
   * C. Azure AI Hub, AI Search, Azure Storage
   * D. Azure Functions, AI Project

3. **Which feature allows an agent to maintain conversation state across multiple interactions?**
   * A. Azure Blob Storage
   * B. Threads ✅
   * C. SDK initialization
   * D. Code Interpreter

4. **Why might you choose Azure AI Foundry Agent Service over the Inference API?**
   * A. Requires more custom coding
   * B. Supports Microsoft 365 directly
   * C. Simplifies agent development with built-in infrastructure management ✅
   * D. Supports OpenAI models only Sonnet 4