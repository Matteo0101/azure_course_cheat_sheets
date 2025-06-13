# Azure AI Language - Conversational Language Understanding (CLU)

## 🧩 Problem

You need to create an application that understands users' natural language input and responds appropriately based on their intent (e.g., request information, take action, etc.).

## 💡 Solution with Azure

Use **Conversational Language Understanding (CLU)** in **Azure AI Language** to build, train, and deploy a **custom language model** that can identify user intents and extract entities from utterances.

## 🧱 Required Components

- **Azure AI Language resource**
- **Language Studio** or **REST API/SDK** (C# / Python)
- Sample data including:
  - **Utterances**
  - **Intents**
  - **Entities**
- (Optional) Prebuilt entities (e.g., datetime, number, organization)

## 🏗️ Architecture & Development

### 1. Provision Resources

- In Azure Portal → Create Azure AI Language Resource
- Retrieve **endpoint** and **subscription key**
- Use **Language Studio** to visually manage the CLU project

### 2. Understand Azure AI Language Capabilities

**Preconfigured features** (no training required):
- Summarization, NER, PII detection, Key Phrase Extraction, Sentiment Analysis, Language Detection

**Learned features** (require training):
- **CLU**, Custom Text Classification, Custom Named Entity Recognition, Question Answering

### 3. Define Intents, Utterances, and Entities

- **Intents**: actions the user wants (e.g., GetWeather, TurnOnDevice)
- **Utterances**: example user phrases mapped to intents
- **Entities**: extractable details within utterances (e.g., device, location)

**Types of entities:**
- **Learned**
- **List**
- **Prebuilt**

### 4. Use Patterns to Disambiguate Similar Utterances

Use templated utterance patterns to distinguish similar phrases:

**Example:**
- `Turn on the {DeviceName}` → *TurnOnDevice*
- `Is the {DeviceName} on?` → *GetDeviceStatus*

### 5. Add Prebuilt Entity Components

- Add up to 5 **prebuilt entities** per project to detect common values (e.g., email, date)
- Saves time and improves recognition for common types

### 6. Train, Test, Publish, Review

- **Train**: use labeled examples to teach the model
- **Test**: interactively or via datasets
- **Publish**: deploy to public endpoint
- **Review & Iterate**: refine model based on real user input

### 7. Query the Model

**SDK Example (Python):**
```python
result = client.analyze_conversation(
    task={
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "participantId": "1",
                "id": "1",
                "modality": "text",
                "language": "en",
                "text": query
            }
        },
        "parameters": {
            "projectName": project_name,
            "deploymentName": deployment_name,
            "verbose": True
        }
    }
)
```

**REST API Example:**
```http
POST {ENDPOINT}/language/analyze-conversations?api-version={API-VERSION}
```

```json
{
  "kind": "Conversation",
  "analysisInput": {
    "conversationItem": {
      "id": "1",
      "participantId": "1",
      "text": "Turn on the light"
    }
  },
  "parameters": {
    "projectName": "myProject",
    "deploymentName": "staging",
    "stringIndexType": "TextElement_V8"
  }
}
```

## ✅ Best Practices & Considerations

- Provide **diverse and varied utterances** for each intent
- Include **correct and incorrect grammar** in examples
- **Label consistently and precisely** across training data
- Use **patterns** and **prebuilt entities** to reduce manual work
- Iterate often: **train → test → deploy → review**

## ❓ Sample Exam Questions

**Q: Which service enables intent detection and entity extraction from user utterances?**
→ *Conversational Language Understanding (CLU)*

**Q: What are utterances and intents in Azure AI Language?**
→ *Utterances are example user inputs; intents represent the meaning or goal of those inputs.*

**Q: How can you reduce the need for manually labeled entity data in a CLU model?**
→ *Use prebuilt entity components.*

**Q: What's the purpose of using patterns in CLU?**
→ *To disambiguate similar utterances and improve intent classification.*

**Q: What is the correct lifecycle of a CLU model?**
→ *Train → Test → Publish → Review*