# Extract Custom Entities with Azure AI Language Service 🔍

## 🧩 Problem

You need to build, train, deploy, and test a custom entity extraction model using Azure AI Language Service for unstructured text (classified ads in this case).

## 💡 Solution with Azure

Use **Azure AI Language Service - Custom Named Entity Recognition (Custom NER)** via:

- **Azure portal + Language Studio** for project creation and labeling
- **Azure SDK (C# / Python)** to consume the model from a client application

## ⚙️ Components Required

- Azure AI Language resource (Custom Text Classification & Extraction feature enabled)
- Azure Storage account (blob storage)
- Azure Role assignment: **Storage Blob Data Contributor**
- Sample ads dataset: https://aka.ms/entity-extraction-ads
- Language Studio
- Visual Studio Code with:
  - Azure AI Text Analytics SDK Azure.AI.TextAnalytics 5.3.0
  - Git clone of repository: https://github.com/MicrosoftLearning/mslearn-ai-language

## 🏗️ Architecture / Development

### 1️⃣ Provision Azure AI Language Resource

- Create Language resource in Azure portal
- Enable **Custom named entity recognition extraction**
- Supported regions: East US, West Europe, UK South, etc.
- Pricing tier: F0 (free) or S (standard)
- Create new storage account (Standard LRS)
- Assign role: **Storage Blob Data Contributor** to your user

### 2️⃣ Upload Training Data

- Download sample ads: https://aka.ms/entity-extraction-ads
- Upload files to blob container **classifieds** (anonymous read access enabled)

### 3️⃣ Create Project in Language Studio

- Project type: **Custom Named Entity Recognition**
- Project name: **CustomEntityLab**
- Language: **English (US)**
- Container: **classifieds**
- Files are not pre-labeled: select "No, I need to label my files as part of this project."

### 4️⃣ Label Data

Create 3 entities:
- **ItemForSale**
- **Price**
- **Location**

Label text in files:

| File | Entity | Example |
|------|--------|---------|
| Ad 1.txt | ItemForSale | face cord of firewood |
| Ad 1.txt | Location | Denver, CO |
| Ad 1.txt | Price | $90 |

Label all ads and save labels.

### 5️⃣ Train Model

- Model name: **ExtractAds**
- Split type: **Automatically split the testing set**
- Start training

### 6️⃣ Evaluate Model

- Review model metrics (precision, recall, F1 score)
- Use **Model performance** and check testing documents
- Analyze failed extractions to guide improvements

### 7️⃣ Deploy Model

- Deployment name: **AdEntities**
- Deploy trained model **ExtractAds**

### 8️⃣ Develop Client Application

Clone repo:
```bash
https://github.com/MicrosoftLearning/mslearn-ai-language
```

Open project: `Labfiles/05-custom-entity-recognition/custom-entities` in VS Code.

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

### 9️⃣ Add Code to Extract Entities

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
AzureKeyCredential credentials = new(aiSvcKey);
Uri endpoint = new(aiSvcEndpoint);
TextAnalyticsClient aiClient = new(endpoint, credentials);
```

**Python:**
```python
credential = AzureKeyCredential(ai_key)
ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)
```

#### Extract entities:

**C#:**
```csharp
RecognizeCustomEntitiesOperation operation = await aiClient.RecognizeCustomEntitiesAsync(
    WaitUntil.Completed, batchedDocuments, projectName, deploymentName);
```

**Python:**
```python
operation = ai_client.begin_recognize_custom_entities(
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
python custom-entities.py
```

**Output:** Lists recognized entities with confidence score for each document.

## 🔧 Best Practice / Considerations

- Assign role **Storage Blob Data Contributor** to avoid authorization errors
- Use high-quality, diverse real-world data for training
- Avoid ambiguous entity definitions
- Use confusion matrix and model metrics to iteratively improve
- Secure storage access in production (avoid anonymous access)

## ❓ Exam-like Sample Questions

### Question 1:
Which task kind should be specified when submitting extraction jobs for custom entity recognition?

A. CustomTextClassification  
B. CustomEntityRecognition  
C. RecognizeEntities

**✅ Answer: B**

### Question 2:
Which dataset was used in this lab for custom entity extraction?

A. Classified ads  
B. News articles  
C. Financial statements

**✅ Answer: A**

### Question 3:
Which entities were defined for extraction?

A. Category, Price, Description  
B. ItemForSale, Price, Location  
C. ItemName, Country, Contact

**✅ Answer: B**

### Question 4:
What SDK version was installed?

A. 4.2.0  
B. 5.3.0  
C. 3.1.0

**✅ Answer: B**

### Question 5:
Which split type was used for training in this lab?

A. Manual split  
B. No split  
C. Automatic split

**✅ Answer: C**