# 🤖 AI Agents on Azure

## 🛑 **Problem**
You need to **automate tasks** or **coordinate business processes** using generative AI in a way that responds to user input and environmental context. The goal is to move beyond chatbots and build **intelligent agents** that can act autonomously.

## ✅ **Solution with Azure**
Use **AI agents**, powered by generative models and contextual data, to perform intelligent actions. Azure provides several frameworks and services for agent development, including **Azure AI Foundry Agent Service**, **Semantic Kernel**, and **Microsoft Copilot Studio**.

## 🧩 **Required Components**
1. **Model**
   * Generative AI model from Azure OpenAI or Foundry model catalog
2. **Knowledge Sources**
   * Azure AI Search
   * Bing Search
   * Custom document/data sources
3. **Tools**
   * Built-in tools (e.g., Azure AI Search, Bing)
   * Code interpreter
   * Custom tools (e.g., Azure Functions)
4. **Agent Framework**
   * Azure AI Foundry Agent Service
   * Semantic Kernel SDK
   * Microsoft Copilot Studio (low-code)
5. **Thread (context)**
   * Maintains chat history and associated data

## 🏗️ **Architecture / Development**

### 📌 Basic Agent Flow Example: Expense Claim Agent
1. User submits question → "What expenses can I claim?"
2. Agent grounds prompt using knowledge base (e.g., policy documents).
3. Prompt is processed by generative model.
4. Agent generates response (e.g., policy explanation).
5. Agent takes action (e.g., submits recurring expense claim).
6. Agent triggers automation (e.g., payment processing).

### 📌 Multi-Agent Flow Example: Travel + Expense Coordination
1. User gives trip details to Travel Agent.
2. Travel Agent books flights/hotels.
3. Travel Agent sends claim details to Expense Agent.
4. Expense Agent submits expense claim.

### 📌 Development Options on Azure:

| Use Case | Recommended Tool |
|----------|------------------|
| No-code/Business Users | Copilot Studio agent builder |
| Low-code developers | Microsoft Copilot Studio |
| Code-first, 365 ecosystem | Microsoft 365 Agents SDK |
| Complex backend agents | Azure AI Foundry Agent Service |
| Multi-agent orchestration | Semantic Kernel |
| Experimental/R&D agents | AutoGen |

## 🧠 **Best Practices / Considerations**
* Start with **Foundry Agent Service** for single agents.
* Use **Semantic Kernel** for **multi-agent** orchestration.
* Consider **Copilot Studio** for empowering business users with no dev experience.
* Choose based on:
   * Security needs
   * Custom integration requirements
   * Developer skill level
* Threads maintain **stateful conversations** and can include **data assets**.

## ❓ **Sample Exam Questions**

1. 🧠 **What is the role of "knowledge" in an AI agent built with Azure AI Foundry Agent Service?**
   - A. It defines the tools the agent uses
   - B. It holds the agent's conversational memory
   - ✅ **C. It grounds prompts with contextual data**
   - D. It stores user profiles

2. 🔧 **Which framework allows orchestration of multiple agents in a solution?**
   - A. Microsoft 365 Agents SDK
   - B. Azure AI Foundry Agent Service
   - ✅ **C. Semantic Kernel**
   - D. Copilot Studio agent builder

3. 🤖 **Which Azure service provides a visual and code-first environment to develop agents with model, tools, and knowledge integration?**
   - A. AutoGen
   - ✅ **B. Azure AI Foundry Agent Service**
   - C. Semantic Kernel
   - D. Copilot Studio

4. 💬 **In a multi-agent architecture, how would a Travel Agent interact with an Expense Agent?**
   - A. By sharing a knowledge base
   - B. By invoking the same model endpoint
   - ✅ **C. By sending expense data to the Expense Agent for submission**
   - D. By sharing a prompt history

5. 👥 **What should business users with no coding skills use to build basic agents?**
   - A. AutoGen
   - B. Foundry Agent Service
   - ✅ **C. Copilot Studio agent builder**
   - D. Semantic Kernel