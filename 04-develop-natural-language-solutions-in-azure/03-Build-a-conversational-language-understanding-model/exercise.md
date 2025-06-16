# Azure AI Language - Create a Language Understanding Model

## 🧩 Problem

You need to develop an application that can interpret user input in natural language, predict what the user wants (intent), and extract contextual data (entities) to take the appropriate action.

## 💡 Solution with Azure

Use **Conversational Language Understanding (CLU)** in the Azure AI Language service to define a custom language model capable of intent recognition and entity extraction. This solution is especially suited for apps like chatbots or voice assistants.

## 🧱 Required Components

- Azure AI Language Resource (with CLU feature)
- Language Studio (https://language.cognitive.azure.com/)
- Visual Studio Code (with C# or Python SDK)
- **SDKs:**
  - `azure-ai-language-conversations` (Python)
  - `Azure.AI.Language.Conversations` (C#)
- Predefined project name (e.g., Clock)
- Deployment name (e.g., production)

## 🏗️ Architecture & Development

### 1. Provision the Resource

- In Azure Portal → Create Language Service → Select Supported Region
- Choose Pricing Tier F0 or S
- Once deployed → Go to Keys and Endpoint tab

### 2. Create a CLU Project

- Go to Language Studio
- Create project:
  - Name: Clock
  - Language: English
  - Description: Natural language clock
  - Skip multi-language option

### 3. Define Intents

- **GetTime**
- **GetDay**
- **GetDate**
- (Includes default **None** intent)

### 4. Add Sample Utterances

**GetTime:**
- what is the time?
- what's the time?
- what time is it?
- tell me the time

**GetDay:**
- what day is it?
- what's the day?
- what is the day today?
- what day of the week is it?

**GetDate:**
- what date is it?
- what's the date?
- what is the date today?
- what's today's date?

### 5. Train and Evaluate the Model

- Start training (Standard mode) → Name: Clock
- Review precision, recall, F1 score, and confusion matrix after training
- Deploy with name: production

### 6. Test the Deployment

Test utterances like:
- what's the time now?
- what's the day today?
- tell me the time

### 7. Add Entities

#### a. Learned Entity: Location

**Examples:**
- what time is it in London?
- tell me the time in Paris
- what's the time in New York?

#### b. List Entity: Weekday

**Add values:**
- Sunday → Syn: Sun
- Monday → Mon
- …
- Saturday → Sat

**Utterances:**
- what date was it on Saturday?
- what date will it be on Friday?
- what will the date be on Thurs?

#### c. Prebuilt Entity: Date

- Select prebuilt DateTime

**Examples:**
- what day was 01/01/1901?
- what day will it be on Dec 31st 2099?

### 8. Retrain and Deploy Again

- Overwrite the Clock model
- Redeploy to production
- Retest with:
  - what time is it in Tokyo?
  - what date is it on Friday?
  - what's the date on Weds?
  - what day was 01/01/2020?

### 9. Client App Integration

#### SDK Setup

**Python:**
```bash
pip install azure-ai-language-conversations
```

**C#:**
```bash
dotnet add package Azure.AI.Language.Conversations --version 1.1.0
```

#### Import Namespaces

**Python:**
```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient
```

**C#:**
```csharp
using Azure;
using Azure.AI.Language.Conversations;
```

#### Create Client

**Python:**
```python
client = ConversationAnalysisClient(ls_prediction_endpoint, AzureKeyCredential(ls_prediction_key))
```

**C#:**
```csharp
Uri endpoint = new Uri(predictionEndpoint);
AzureKeyCredential credential = new AzureKeyCredential(predictionKey);
ConversationAnalysisClient client = new ConversationAnalysisClient(endpoint, credential);
```

## 🔁 Prediction Flow and Action Logic

### 1. Analyze User Utterance
Submit input → Get top intent + confidence → Extract entities

### 2. Map Intent to Logic

**Example: GetTime**
- Extract Location entity
- Call GetTime(location) function

**Example: GetDate**
- Extract Weekday entity
- Call GetDate(weekday)

**Example: GetDay**
- Extract Date entity
- Call GetDay(date)

**If intent is unknown:**
```python
print('Try asking me for the time, the day, or the date.')
```

## ✅ Best Practices & Considerations

- Label diverse utterances per intent
- Mix grammatical/colloquial forms
- Retrain often as you refine entities
- Use prebuilt entities when applicable
- Deploy after satisfactory testing
- Client must handle the predicted intent (CLU ≠ action executor)

## ❓ Sample Exam Questions

**Q: What is the role of a conversational language understanding model?**
→ Identify intent and extract entities from user input

**Q: Which entity type helps identify structured data like weekdays or categories?**
→ List entity

**Q: What does the prediction response include?**
→ Top intent, confidence score, extracted entities

**Q: When is a prebuilt entity like DateTime useful?**
→ When extracting structured time/date information

**Q: Which SDK is used in Python to submit utterances to a CLU project?**
→ azure-ai-language-conversations