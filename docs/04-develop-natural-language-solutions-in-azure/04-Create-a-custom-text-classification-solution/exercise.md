# Custom Text Classification Lab 🧪 (Azure AI Language Service)

## 🧩 Problem

You need to build, train, deploy, and test a custom text classification model using Azure AI Language, including:

- Provisioning the service
- Preparing and labeling data
- Training and deploying the model
- Consuming the model from a client application

## 💡 Solution with Azure

Use **Azure AI Language Service - Custom Text Classification** via:

- **Azure portal & Language Studio** for configuration, data labeling, and model training
- **Azure SDK (C# / Python)** to consume the model from a client application

## ⚙️ Components Required

- Azure AI Language resource (Custom text classification enabled)
- Azure Storage account (blob storage)
- Language Studio
- Role assignment: **Storage Blob Data Contributor** 🛑
- Sample data (from https://aka.ms/classification-articles)
- Visual Studio Code with:
  - Azure AI Text Analytics SDK (Azure.AI.TextAnalytics 5.3.0)
  - Git clone of repository https://github.com/MicrosoftLearning/mslearn-ai-language

## 🏗️ Architecture / Development

### 1️⃣ Provision Azure AI Language Resource

- Create new Language resource in Azure portal
- Enable **Custom text classification & extraction**
- Choose supported region (e.g. East US, West Europe, UK South...)
- Pricing tier: F0 (free) or S (standard)
- Create new Storage account (Standard LRS)
- Assign role: **Storage Blob Data Contributor** to your user

### 2️⃣ Upload Training Data

- Download sample data: https://aka.ms/classification-articles
- Upload to blob container named **articles** (anonymous read access enabled)

### 3️⃣ Create Project in Language Studio

- Resource: Select previously created Azure AI Language resource
- Project type: **Single label classification**
- Project name: **ClassifyLab**
- Language: **English (US)**
- Use storage container **articles**
- Choose option to label files as part of the project

### 4️⃣ Label Data

Define 4 classes: **Classifieds**, **Sports**, **News**, **Entertainment**.

Assign documents manually to training or testing dataset:

| Article | Class | Dataset |
|---------|-------|---------|
| Article 1 | Sports | Training |
| Article 10 | News | Training |
| Article 11 | Entertainment | Testing |
| Article 12 | News | Testing |
| Article 13 | Sports | Testing |
| Article 2 | Sports | Training |
| Article 3 | Classifieds | Training |
| Article 4 | Classifieds | Training |
| Article 5 | Entertainment | Training |
| Article 6 | Entertainment | Training |
| Article 7 | News | Training |
| Article 8 | News | Training |
| Article 9 | Entertainment | Training |

Save labels.

### 5️⃣ Train Model

- Model name: **ClassifyArticles**
- Split type: **Manual split**
- Start training
- Wait for completion

### 6️⃣ Evaluate Model

- Review performance metrics (precision, recall, F1 score)
- Use **Model performance** and **Test set details** to analyze errors
- Toggle "Show mismatches only" for evaluation

### 7️⃣ Deploy Model

- Deployment name: **articles**
- Deploy **ClassifyArticles** model

### 8️⃣ Develop Client Application

Clone repo:
```bash
https://github.com/MicrosoftLearning/mslearn-ai-language
```

Open project in VS Code (`Labfiles/04-text-classification/classify-text`).

Install SDK:

**C#:**
```bash
dotnet add package Azure.AI.TextAnalytics --version 5.3.0
```

**Python:**
```bash
pip install azure-ai-textanalytics==5.3.0
```

Configure app settings:
- **C#**: `appsettings.json`
- **Python**: `.env`

Set: `aiSvcKey`, `aiSvcEndpoint`, `projectName`, `deploymentName`.

### 9️⃣ Add Code to Classify Documents

#### Import namespaces:

**C#:**
```csharp
using Azure;
using Azure.AI.TextAnalytics;
```

**Python:**
```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
```

#### Create client:

**C#:**
```csharp
AzureKeyCredential credentials = new AzureKeyCredential(aiSvcKey);
Uri endpoint = new Uri(aiSvcEndpoint);
TextAnalyticsClient aiClient = new TextAnalyticsClient(endpoint, credentials);
```

**Python:**
```python
credential = AzureKeyCredential(ai_key)
ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)
```

#### Get classifications:

**C#:**
```csharp
ClassifyDocumentOperation operation = await aiClient.SingleLabelClassifyAsync(
    WaitUntil.Completed, batchedDocuments, projectName, deploymentName);
```

**Python:**
```python
operation = ai_client.begin_single_label_classify(
    batchedDocuments, project_name=project_name, deployment_name=deployment_name)
document_results = operation.result()
```

### 🔟 Test Application

Run the app:

**C#:**
```bash
dotnet run
```

**Python:**
```bash
python classify-text.py
```

**Output:** Shows predicted class and confidence score for each document.

## 🔧 Best Practice / Considerations

- Ensure correct role assignments (**Storage Blob Data Contributor**) to avoid authorization errors
- Use manual split for small datasets to control class balance
- Review test set mismatches to improve model
- Secure blob storage access in production (avoid anonymous access)
- API keys must be stored securely and never hard-coded

## ❓ Exam-like Sample Questions

### Question 1:
Which role must be assigned to the user for storage access during project creation?

A. Storage Blob Data Owner  
B. Storage Blob Data Contributor  
C. Reader

**✅ Answer: B**

### Question 2:
Which access level was configured for the container when uploading training data?

A. Private  
B. Blob (anonymous read access for blobs only)  
C. Container (anonymous read access for containers and blobs)

**✅ Answer: C**

### Question 3:
Which split option is recommended for small datasets?

A. Automatic split  
B. Manual split

**✅ Answer: B**

### Question 4:
Which deployment name was used in this lab?

A. articles  
B. classifyLab  
C. classifyArticles

**✅ Answer: A**

### Question 5:
Which SDK version was used for the Azure Text Analytics Client?

A. 4.2.0  
B. 5.3.0  
C. 3.1.0

**✅ Answer: B**