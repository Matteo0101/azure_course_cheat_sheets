# 02 Develop an AI agent with Azure AI Foundry Agent Service

---

## 1. 🧩 Problem

**How can you build a scalable, secure, and customizable AI agent in Azure to automate complex tasks (e.g., customer service, report generation, workflow automation) without managing infrastructure or writing excessive amounts of code?**

---

## 2. 🚀 Solution with Azure

Use **Azure AI Foundry Agent Service** — a fully managed service that enables developers to:

- Build, deploy, and scale high-quality AI agents  
- Leverage generative AI models, integrated tools, and custom functions  
- Avoid managing compute or storage resources  

---

## 3. 🧱 Required Components

| Component                    | Description                                                             |
|-----------------------------|-------------------------------------------------------------------------|
| ✅ Azure AI Hub              | Central workspace for managing AI assets                               |
| ✅ Azure AI Project          | Scoped environment for building and managing agents                    |
| ✅ Deployed AI Model         | e.g., Azure OpenAI, Llama 3, Mistral                                   |
| ✅ Azure AI Services         | Underlying cognitive and ML services                                   |
| ➕ Optional:                 |                                                                         |
| • Azure Key Vault            | Secure secrets and credentials                                          |
| • Azure AI Search            | Enable semantic search for knowledge grounding                         |
| • Azure Storage              | External file access and management                                     |

**Agent Tools:**

- **Knowledge Tools:** Bing Search, File Search, Azure AI Search, Microsoft Fabric  
- **Action Tools:** Code Interpreter, Azure Function, Custom Function, OpenAPI Spec  

---

## 4. 🏗️ Architecture / Development

### 🔁 Development Flow

1. **Connect to Azure AI Foundry Project**  
   - Use project endpoint  
   - Authenticate via Microsoft Entra ID  

2. **Create or Reference an Agent**  
   - Specify model deployment  
   - Define behavior using **Instructions**  
   - Assign tools and resources  

3. **Create a Thread** (stateful conversation container)  
4. **Send Messages** and invoke the agent  
5. **Check Status** and retrieve responses and generated artifacts  
6. **Repeat** the conversation loop  
7. **Delete** the agent and thread to clean up resources  

### 🛠️ Development Options

- Azure AI Foundry Portal (low-code)
- SDKs / REST APIs (e.g., Python)
- Bicep templates (for provisioning resources)

---

## 5. ✅ Best Practices / Considerations

- 🔐 Use **threads** to securely manage conversation state  
- 🧰 Assign tools that match agent responsibilities  
- 🔑 Prefer **keyless authentication** for secure access  
- ☁️ Use your own Azure Blob Storage if full control is required  
- 🔄 Use **Copilot Studio** or **Semantic Kernel** for:
  - Multi-agent orchestration  
  - Microsoft 365 integration  

---

## 6. 📝 Sample Exam Questions

**Q1.** What are the key benefits of using Azure AI Foundry Agent Service over building agents manually via APIs?  
**A1.** Simplifies development, requires less code, manages infrastructure, and includes built-in tools like Code Interpreter and Azure Functions.

**Q2.** Which component manages the state and context of an AI agent's conversation in Foundry?  
**A2.** Thread

**Q3.** When would you choose Copilot Studio or Semantic Kernel over Foundry Agent Service?  
**A3.** When integrating with Microsoft 365 or orchestrating multiple agents.

**Q4.** What’s the difference between a knowledge tool and an action tool?  
**A4.** Knowledge tools provide grounding data (e.g., Bing Search); action tools perform tasks (e.g., Azure Function).

**Q5.** Which models are compatible with Foundry Agent Service?  
**A5.** Azure OpenAI, Llama 3, Mistral, Cohere

