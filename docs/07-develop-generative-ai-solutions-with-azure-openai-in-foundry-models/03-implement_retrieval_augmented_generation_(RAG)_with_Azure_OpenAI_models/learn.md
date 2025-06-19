# Implement Retrieval Augmented Generation (RAG) with Azure OpenAI Models

Azure OpenAI on your data allows developers to implement **RAG** with supported AI chat models to reference specific sources of data to ground the response.

---

## 🎯 Learning Objectives

By the end of this module, you'll be able to:
- Describe the capabilities of Azure OpenAI on your data  
- Configure Azure OpenAI to use your own data  
- Use Azure OpenAI API to generate responses based on your own data  

---

## 🔍 What is RAG?

**Retrieval Augmented Generation (RAG)** allows supported AI models to retrieve and ground answers on specific external data sources, in addition to their pretrained knowledge. Azure OpenAI integrates with **Azure AI Search** to:

1. Receive user prompt  
2. Analyze the content and intent  
3. Query the AI Search index  
4. Insert retrieved chunks into the prompt  
5. Call Azure OpenAI model with augmented prompt  
6. Return grounded response and (optional) citation  

---

## 🧠 Fine-tuning vs RAG

| Feature       | Fine-tuning                                 | RAG (Azure OpenAI on your data)                      |
|---------------|----------------------------------------------|------------------------------------------------------|
| Data Training | Required (costly and time-intensive)         | Not required                                         |
| Prompt size   | Useful for large contexts beyond prompt size | Works within token limits                            |
| Flexibility   | Customizes the model permanently             | Keeps model stateless and flexible                   |

---

## 📁 Add Your Own Data

You can connect your data through:
- **Azure AI Studio (Chat playground)**  
- **Blob Storage**  
- **Manual AI Search index connection**

### Supported File Types
- `.md`, `.txt`, `.html`, `.pdf`, `.docx`, `.pptx`

> 📝 If documents contain images, make sure text is extractable.

### Best Practices
- Use **Azure AI Studio** for data chunking & index creation  
- Use **data preparation scripts** for large documents  
- Enable **semantic search** to improve results (may increase cost)

---

## 🔗 Connect Data in Azure AI Studio

1. Go to **Chat playground**
2. Open the **Add your data** tab
3. Click **Add a data source**
4. Follow the wizard to map fields (especially content fields)

---

## 💬 Chat with Your Data

You can now chat:
- In **Azure AI Studio**, or  
- Through the **API**

### 🔑 Token Considerations

- Max system message: ~4000 tokens  
- Response limited to **1500 tokens**  
- Include in token count:
  - System message
  - Prompt
  - History
  - Search results
  - Response

> ➕ Use prompt engineering techniques like **chain-of-thought prompting**

---

## 📡 Using the API with Your Data

### Request Example

```json
{
  "dataSources": [
    {
      "type": "AzureCognitiveSearch",
      "parameters": {
        "endpoint": "<your_search_endpoint>",
        "key": "<your_search_key>",
        "indexName": "<your_search_index>"
      }
    }
  ],
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant assisting users with travel recommendations."
    },
    {
      "role": "user",
      "content": "I want to go to New York. Where should I stay?"
    }
  ]
}
```

### API Endpoint Format

```
<your_azure_openai_resource>/openai/deployments/<deployment_name>/chat/completions?api-version=<version>
```

### Headers Required

```
Content-Type: application/json
api-key: <your_api_key>
```

---

## 🚀 Complete Implementation Example

### Python SDK Implementation

```python
from openai import AzureOpenAI
import json

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint="<your_azure_openai_endpoint>",
    api_key="<your_api_key>",
    api_version="2024-02-15-preview"
)

# Define your data source
data_sources = [
    {
        "type": "AzureCognitiveSearch",
        "parameters": {
            "endpoint": "<your_search_endpoint>",
            "key": "<your_search_key>",
            "indexName": "<your_search_index>"
        }
    }
]

# Make the request
response = client.chat.completions.create(
    model="<your_deployment_name>",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What information do you have about our products?"}
    ],
    extra_body={"dataSources": data_sources}
)

print(response.choices[0].message.content)
```

### cURL Example

```bash
curl -X POST \
  "<your_azure_openai_endpoint>/openai/deployments/<deployment_name>/chat/completions?api-version=2024-02-15-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: <your_api_key>" \
  -d '{
    "dataSources": [
      {
        "type": "AzureCognitiveSearch",
        "parameters": {
          "endpoint": "<your_search_endpoint>",
          "key": "<your_search_key>",
          "indexName": "<your_search_index>"
        }
      }
    ],
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Tell me about our company policies."
      }
    ]
  }'
```

---

## ✅ Best Practices Summary

1. **Data Preparation**: Ensure your documents are well-structured and text-extractable
2. **Index Configuration**: Use Azure AI Studio for optimal chunking and indexing
3. **Token Management**: Monitor token usage to stay within limits
4. **Semantic Search**: Enable for better retrieval quality (consider cost implications)
5. **Prompt Engineering**: Use techniques like chain-of-thought for better responses
6. **Citation Handling**: Leverage the citation features for transparency and trust

---

## 🔧 Troubleshooting Common Issues

- **Large Documents**: Use data preparation scripts for better chunking
- **Poor Results**: Check field mappings and enable semantic search
- **Token Limits**: Reduce context or use summarization techniques
- **API Errors**: Verify endpoint URLs and API keys are correct