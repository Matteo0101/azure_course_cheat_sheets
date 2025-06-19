# 01 Get started with AI agent development on Azure

## 1. Problem ❓

**How can you build intelligent AI agents that autonomously automate business tasks using generative AI models in Azure?**

---

## 2. Solution with Azure ✅

Leverage the following to develop, manage, and deploy AI agents that combine generative AI, contextual data, and programmatic tools:

- **Azure AI Foundry Agent Service**
- **OpenAI Assistants API**
- **Frameworks:**
  - Semantic Kernel
  - AutoGen
  - Microsoft Copilot Studio

---

## 3. Required Components 🧩

- **Model:**  
  - OpenAI or Azure AI Foundry catalog models

- **Knowledge Sources:**  
  - Azure AI Search  
  - Bing  
  - Custom documents

- **Tools:**  
  - Built-in: e.g., code interpreter, Bing  
  - Custom: e.g., Azure Functions

- **Conversation Thread:**  
  - Maintains context and data exchange history

- **Agent Frameworks / SDKs:**  
  - Azure AI Foundry SDK  
  - OpenAI Assistants API (OpenAI models only)  
  - Semantic Kernel Agent Framework  
  - AutoGen  
  - Microsoft 365 Agents SDK  
  - Microsoft Copilot Studio / Agent Builder

---

## 4. Architecture / Development 🏗️

### Single-Agent Scenario (e.g., Expense Agent)

1. User submits a question  
2. Agent grounds the prompt using a knowledge source  
3. Model generates a response  
4. Agent performs an action (e.g., submits an expense claim)  

### Multi-Agent Scenario (e.g., Travel + Expense Agents)

1. User provides trip details to Travel Agent  
2. Travel Agent books and collects receipts  
3. Travel Agent invokes Expense Agent  
4. Expense Agent submits the claim  

### Agent Construction in Foundry Agent Service ⚙️

- Use **visual interface** or **SDK**  
- Define:  
  - Model (LLM)  
  - Knowledge source  
  - Tools (built-in/custom)  
- Manage conversations via threads

---

## 5. Best Practices / Considerations 🧭

- **Copilot Studio Agent Builder:**  
  Ideal for business users with no coding skills

- **Copilot Studio (low-code):**  
  Best for Power Platform users

- **Microsoft 365 Agents SDK:**  
  Suitable for agents in Teams, Slack, etc.

- **Foundry Agent Service:**  
  Best for enterprise-grade, scalable agent development

- **Semantic Kernel:**  
  Recommended for multi-agent orchestration

- **Tool Selection Criteria:**  
  - User skill level  
  - Target channels (e.g., Teams, Web)  
  - Required integrations  
  - Flexibility and scalability

> ✅ **Tip:** Prefer **Foundry Agent Service** over **OpenAI Assistants API** for richer integration with Azure.

---

## 6. Exam-like Questions 📝

**Q1:** What are the three core components required when building an agent in Azure AI Foundry Agent Service?  
**A1:** Model, Knowledge, Tools

**Q2:** Which framework is best suited for orchestrating multi-agent solutions in Azure?  
**A2:** Semantic Kernel

**Q3:** What distinguishes Azure AI Foundry Agent Service from the OpenAI Assistants API?  
**A3:** Foundry provides greater model choice, integration with Azure services, and enterprise-grade features

**Q4:** A business user with no coding experience wants to build a simple task automation agent. Which tool should they use?  
**A4:** Copilot Studio Agent Builder in Microsoft 365 Copilot

**Q5:** What Azure component allows agents to retain user interaction context and generated files?  
**A5:** Conversation threads

---

## 7. Module Assessment 🎓

**Q1:** Which of the following best describes an AI agent?  
**A1:** A software service that uses AI to assist users with information and task automation.

**Q2:** Which AI agent development service offers a choice of generative AI models from multiple vendors in the Azure AI Foundry model catalog?  
**A2:** Azure AI Foundry Agent Service

**Q3:** What element of a Foundry Agent Service agent enables it to ground prompts with contextual data?  
**A3:** Knowledge
