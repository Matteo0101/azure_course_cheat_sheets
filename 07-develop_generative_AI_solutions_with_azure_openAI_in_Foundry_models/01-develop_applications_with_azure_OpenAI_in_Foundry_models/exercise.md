# 📅 AI-102 Study Guide — Application Development with Azure OpenAI

---

## ✅ 1. Problem (Use Case)

You need to develop an application that:

* Understands natural language
* Generates personalized responses
* Maintains conversation context (chat history)
* Can generate promotional emails, categorize articles, and interact with provided content

---

## 🧬 2. Azure Solution

Use **Azure OpenAI Service** and GPT models (e.g., **GPT-4o**) through:

* **SDK (Python or C#)** or REST API
* Prompt engineering to control tone, format, and content
* Grounding context for responses based on external sources

---

## 🔧 3. Required Components

| Component                        | Description                                       |
| -------------------------------- | ------------------------------------------------- |
| Azure OpenAI Resource            | To be created in Azure portal                     |
| GPT-4o Model                     | Deploy from Cloud Shell                          |
| Azure.AI.OpenAI SDK              | C# (.NET) or Python (openai)                     |
| Keys/API Endpoint                | Available in Azure OpenAI resource               |
| `.env` or `appsettings.json` file| To configure endpoint, key, deployment           |
| Prompt + System Message          | To control model response                         |
| Grounding context (optional)     | For responses based on provided textual context  |

---

## 🛠️ 4. Architecture/Development

### A. Provisioning

* Create Azure OpenAI resource (regions: East US, West US, etc.)
* Deploy model via Bash in Cloud Shell with:

```bash
az cognitiveservices account deployment create \
  -g <resource_group> \
  -n <service_name> \
  --deployment-name gpt-4o \
  --model-name gpt-4o \
  --model-version 2024-05-13 \
  --model-format OpenAI \
  --sku-name "Standard" \
  --sku-capacity 5
```

### B. SDK Configuration

**Python:**

```python
from openai import AsyncAzureOpenAI
client = AsyncAzureOpenAI(
    azure_endpoint=azure_oai_endpoint,
    api_key=azure_oai_key,
    api_version="2024-02-15-preview"
)
```

**C#:**

```csharp
AzureOpenAIClient azureClient = new (new Uri(oaiEndpoint), new ApiKeyCredential(oaiKey));
ChatClient chatClient = azureClient.GetChatClient(oaiDeploymentName);
```

### C. Execution with Prompt Engineering

Use different types of prompts:

* Generic: "You are an AI assistant"
* Formatted: "You help write promotional emails"
* Specific: instructions on tone, content, table formatting

### D. Grounding Context + Chat History

* Load `grounding.txt`
* Initialize chat with grounding text
* Add system and user messages to historical context
* Maintain conversation history for consecutive questions

---

## 🔧 5. Prompt Engineering (Examples)

### Prompt 1

* **System:** You are an AI assistant
* **User:** Write an intro for a new wildlife Rescue

### Prompt 2

* **System:** You are an AI assistant helping to write emails
* **User:** Write a promotional email for a new wildlife rescue...

### Prompt 3 (with specific tone)

* **System:** You are an AI assistant that writes in a light, chit-chat style...

### Prompt 4 (grounding)

* **Grounding:** text from `grounding.txt`
* **System:** You are an AI assistant who helps people find information...
* **User:** What animal is the favorite of children at Contoso?

---

## 📆 6. Exercise and Testing

* Files to modify: `system.txt`, `grounding.txt`
* Run via `dotnet run` or `python application.py`
* Observe how responses change as the prompt varies

---

## ❓ 7. Possible Exam Questions

* How do you connect an application to Azure OpenAI?
* How do you influence the tone and content of a GPT model's response?
* How do you use grounding context to improve responses?
* How do you maintain chat history in a conversation with a GPT model?

---

*Study guide for AI-102 Microsoft Azure AI Engineer Associate certification*