# 🧩 RAG Implementation with Azure OpenAI and Azure AI Search

## OBJECTIVE
Develop an application that uses **RAG** (Retrieval Augmented Generation) with **Azure OpenAI** and **Azure AI Search** to generate responses based on your own data (e.g., Margie's Travel Agency brochures).

---

## 1. Provisioning Azure Resources

**Create 3 main resources:**

### Azure OpenAI
- Subscription approved for OpenAI
- Region: one of *East US, North Central US, West US, Sweden Central, etc.*
- SKU: Standard S0

### Azure AI Search
- Same subscription and resource group as Azure OpenAI
- SKU: Basic

### Azure Storage Account
- Blob Storage or Data Lake Gen2
- Redundancy: LRS
- Performance: Standard

### 🔍 Retrieve:
- Azure OpenAI endpoint and key
- Azure AI Search endpoint and admin key

---

## 2. Upload User Data

1. Download brochures from https://aka.ms/own-data-brochures
2. Go to Azure Portal > Storage account > **Storage browser**
3. Create container named `margies-travel`
4. Upload extracted `.pdf` files to the root of the container

---

## 3. Deploy AI Models

Open **Azure Cloud Shell** (Bash):

### Deploy Embedding Model:
```bash
az cognitiveservices account deployment create \
-g <resource_group> \
-n <openai_resource> \
--deployment-name text-embedding-ada-002 \
--model-name text-embedding-ada-002 \
--model-version "2" \
--model-format OpenAI \
--sku-name "Standard" \
--sku-capacity 5
```

### Deploy GPT-4o Model:
```bash
az cognitiveservices account deployment create \
-g <resource_group> \
-n <openai_resource> \
--deployment-name gpt-4o \
--model-name gpt-4o \
--model-version "2024-05-13" \
--model-format OpenAI \
--sku-name "Standard" \
--sku-capacity 5
```

---

## 4. Create AI Search Index

1. Go to Azure Portal > your AI Search resource > **Import and vectorize data**
2. Configure:
   - Source: Azure Blob Storage
   - Container: `margies-travel`
   - Embedding model: `text-embedding-ada-002`
   - Enable **semantic ranking**
   - Index name: `margies-index`

---

## 5. Clone Sample Code from GitHub

1. Open VS Code
2. Execute: `Git: Clone` from repo → `https://github.com/MicrosoftLearning/mslearn-openai`
3. Open folder: → `Labfiles/02-use-own-data/`
4. Choose between `Python` or `CSharp`

---

## 6. Install SDK Dependencies

**In integrated terminal:**

### C#:
```bash
dotnet add package Azure.AI.OpenAI --version 2.1.0
dotnet add package Azure.Search.Documents --version 11.6.0
```

### Python:
```bash
pip install openai==1.65.2
```

---

## 7. Configure Files

Open:
- `appsettings.json` (C#)
- `.env` (Python)

Insert:
- OpenAI endpoint + key
- GPT-4o deployment name
- AI Search endpoint + key
- Index name: `margies-index`

### Example Configuration Files

**.env (Python):**
```env
AZURE_OPENAI_ENDPOINT=https://your-openai-resource.openai.azure.com/
AZURE_OPENAI_KEY=your-openai-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_SEARCH_ENDPOINT=https://your-search-service.search.windows.net
AZURE_SEARCH_KEY=your-search-admin-key
AZURE_SEARCH_INDEX=margies-index
```

**appsettings.json (C#):**
```json
{
  "AzureOpenAI": {
    "Endpoint": "https://your-openai-resource.openai.azure.com/",
    "Key": "your-openai-key",
    "DeploymentName": "gpt-4o"
  },
  "AzureSearch": {
    "Endpoint": "https://your-search-service.search.windows.net",
    "Key": "your-search-admin-key",
    "IndexName": "margies-index"
  }
}
```

---

## 8. Add Code to Use Your Data

Open the file `ownData.cs` or `ownData.py` and insert code to configure data source:

### Python Implementation:
```python
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_KEY"],
    api_version="2024-02-15-preview"
)

# Configure data source
extra_body = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": os.environ["AZURE_SEARCH_ENDPOINT"],
                "index_name": os.environ["AZURE_SEARCH_INDEX"],
                "authentication": {
                    "type": "api_key",
                    "key": os.environ["AZURE_SEARCH_KEY"]
                }
            }
        }
    ]
}

# Make the chat completion request
response = client.chat.completions.create(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    messages=[
        {"role": "system", "content": "You are a helpful travel assistant."},
        {"role": "user", "content": "Tell me about London"}
    ],
    extra_body=extra_body
)

print(response.choices[0].message.content)
```

### C# Implementation:
```csharp
using Azure;
using Azure.AI.OpenAI;
using Microsoft.Extensions.Configuration;

// Load configuration
var config = new ConfigurationBuilder()
    .AddJsonFile("appsettings.json")
    .Build();

string azureOpenAIEndpoint = config["AzureOpenAI:Endpoint"];
string azureOpenAIKey = config["AzureOpenAI:Key"];
string deploymentName = config["AzureOpenAI:DeploymentName"];
string azureSearchEndpoint = config["AzureSearch:Endpoint"];
string azureSearchKey = config["AzureSearch:Key"];
string azureSearchIndex = config["AzureSearch:IndexName"];

// Initialize Azure OpenAI client
AzureOpenAIClient client = new AzureOpenAIClient(
    new Uri(azureOpenAIEndpoint),
    new AzureKeyCredential(azureOpenAIKey)
);

// Configure chat completion options with data source
ChatCompletionsOptions chatCompletionsOptions = new ChatCompletionsOptions()
{
    DeploymentName = deploymentName,
    Messages =
    {
        new ChatRequestSystemMessage("You are a helpful travel assistant."),
        new ChatRequestUserMessage("Tell me about London")
    }
};

// Add data source
chatCompletionsOptions.AddDataSource(new AzureSearchChatDataSource()
{
    Endpoint = new Uri(azureSearchEndpoint),
    IndexName = azureSearchIndex,
    Authentication = DataSourceAuthentication.FromApiKey(azureSearchKey)
});

// Get response
Response<ChatCompletions> response = await client.GetChatCompletionsAsync(chatCompletionsOptions);
Console.WriteLine(response.Value.Choices[0].Message.Content);
```

---

## 9. Run the Application

From terminal in the correct folder:

### Python:
```bash
python ownData.py
```

### C#:
```bash
dotnet run
```

### Test with prompts like:
- *"Tell me about London"*
- *"What activities are available in Paris?"*
- *"Recommend hotels in New York"*

Verify that the response is based on the uploaded data. If you enable `show citations`, you'll also see the sources from the search index.

---

## 🔧 Troubleshooting Tips

1. **Index Creation Issues**: Ensure all PDFs are properly uploaded to the blob container
2. **Authentication Errors**: Double-check all endpoint URLs and API keys
3. **No Results**: Verify the index name matches exactly in configuration
4. **Poor Quality Results**: Enable semantic ranking for better search relevance
5. **Token Limits**: Monitor response lengths and adjust chunk sizes if needed

---

## 📝 Additional Configuration Options

### Enable Citations:
```python
extra_body = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": os.environ["AZURE_SEARCH_ENDPOINT"],
                "index_name": os.environ["AZURE_SEARCH_INDEX"],
                "authentication": {
                    "type": "api_key",
                    "key": os.environ["AZURE_SEARCH_KEY"]
                },
                "include_contexts": ["citations"]
            }
        }
    ]
}
```

### Customize Search Parameters:
```python
"parameters": {
    "endpoint": os.environ["AZURE_SEARCH_ENDPOINT"],
    "index_name": os.environ["AZURE_SEARCH_INDEX"],
    "authentication": {
        "type": "api_key",
        "key": os.environ["AZURE_SEARCH_KEY"]
    },
    "top_n_documents": 5,
    "strictness": 3,
    "role_information": "You are a travel assistant specializing in luxury destinations."
}
```