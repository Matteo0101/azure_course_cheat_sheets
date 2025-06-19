# Azure OpenAI - Complete Guide

## PROBLEM
You need to create an application that leverages LLM (Large Language Models) to generate text, code, or images, or to calculate embeddings or transcribe audio. How can you do this using Azure OpenAI?

## SOLUTION
Use the Azure OpenAI service to access and manage models like gpt-4, gpt-35-turbo, text-embedding-ada, dall-e, whisper, etc.

## REQUIRED COMPONENTS

| Component | Description |
|-----------|-------------|
| Azure OpenAI Resource | Main resource to create in the portal or via CLI |
| Azure CLI / Azure Portal | To create and manage resources and model deployments |
| API Key and Endpoint | To authenticate and make REST calls or via SDK |
| Model to deploy | E.g.: gpt-35-turbo, text-embedding-ada, dall-e, whisper |
| Deployment Name | Model alias for the application |
| SDK (Python: openai) | To integrate models into your code (chat, completions, embeddings, etc.) |

## OPERATIONAL PROCEDURE

### 1. Create Azure OpenAI Resource (CLI)
```bash
az cognitiveservices account create \
-n MyOpenAIResource \
-g OAIResourceGroup \
-l eastus \
--kind OpenAI \
--sku s0 \
--subscription subscriptionID
```

### 2. Deploy a Model (e.g., GPT-35 Turbo)
```bash
az cognitiveservices account deployment create \
   -g OAIResourceGroup \
   -n MyOpenAIResource \
   --deployment-name MyModel \
   --model-name gpt-35-turbo \
   --model-version "0125"  \
   --model-format OpenAI \
   --sku-name "Standard" \
   --sku-capacity 1
```

### 3. Usage via API (REST – chat completions example)
```bash
curl https://<ENDPOINT>.openai.azure.com/openai/deployments/<DEPLOYMENT_NAME>/chat/completions?api-version=2023-03-15-preview \
  -H "Content-Type: application/json" \
  -H "api-key: <API_KEY>" \
  -d '{
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is Azure OpenAI?"}
    ]
}'
```

### 4. Usage via Python SDK
```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="<YOUR_ENDPOINT_NAME>",
    api_key="<YOUR_API_KEY>",
    api_version="2024-02-15-preview"
)

response = client.chat.completions.create(
    model="<YOUR_DEPLOYMENT_NAME>",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]
)
print(response.choices[0].message.content)
```

## AVAILABLE MODEL TYPES

| Category | Model (example) | Description |
|----------|-----------------|-------------|
| LLM Chat | gpt-4, gpt-35-turbo | Text generation/conversations/chatbots |
| Code | gpt-35-turbo | Code generation |
| Embedding | text-embedding-ada:002 | Transforms text into numerical vectors |
| Images | dall-e | Generates images from prompts (preview) |
| Speech-to-text | whisper | Transcribes audio to text |
| Text-to-speech | text-to-speech | Generates voice from text |

## REQUIRED PERMISSIONS

| Azure Role | Permissions |
|------------|-------------|
| Cognitive Services OpenAI User | Resource viewing, playground |
| Cognitive Services OpenAI Contributor | Deployment creation |

## COMMON USE CASES

| Objective | Recommended Model | Endpoint |
|-----------|-------------------|----------|
| Chatbot / Assistant | gpt-35-turbo | chat/completions |
| Semantic search engine | text-embedding-ada:002 | embeddings |
| Code generation | gpt-4 or gpt-35-turbo | completions |
| Text similarity analysis | text-similarity-* | embeddings |
| Image generation | dall-e | images/generations |
| Voice transcription | whisper | audio/transcriptions |

## SIMULATED EXAM QUESTIONS

1. **You need an enterprise chatbot for a website. Which Azure OpenAI model would you use and how would you configure it?**

2. **You need to implement semantic search to compare product descriptions. Which model do you use?**

3. **You want to automatically generate Python code from natural language prompts. Which model and endpoint?**

4. **You want to integrate AI into your Python code: what parameters are needed to connect?**

5. **What RBAC roles are required to create a GPT model deployment in an enterprise?**



