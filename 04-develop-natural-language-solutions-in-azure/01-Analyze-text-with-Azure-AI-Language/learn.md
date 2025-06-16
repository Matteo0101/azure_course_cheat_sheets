# Azure AI Language - Complete Guide

## 🧩 Problem Statement

You need to analyze unstructured text automatically to extract meaning, sentiment, entities, or language from large amounts of textual data such as:
- Emails
- Reviews  
- Social media posts
- Documents

### Key Requirements:
- Detect the language of each document
- Extract key phrases or entities
- Determine the sentiment expressed
- Link entities to a knowledge base like Wikipedia

## 💡 Solution with Azure

**Azure AI Language** provides a comprehensive set of APIs and SDKs offering:

- Language Detection
- Key Phrase Extraction
- Sentiment Analysis
- Named Entity Recognition & Entity Linking

## 🧩 Required Components

- Azure AI Language resource (created via Azure Portal or Azure AI Foundry)
- API endpoint and key
- REST client or SDK (e.g., Python, C#)
- JSON-formatted request payloads

## 🛠 Architecture & Development

### 🔹 Provisioning

1. Create an Azure AI Language resource
2. Use the endpoint and key to authenticate your app
3. Send HTTP requests using REST or use SDKs that wrap those calls

### 🔹 Language Detection

Automatically identifies the language of submitted text documents.

**Sample Request:**
```json
{
  "kind": "LanguageDetection",
  "parameters": { "modelVersion": "latest" },
  "analysisInput": {
    "documents": [
      { "id": "1", "text": "Hello world", "countryHint": "US" },
      { "id": "2", "text": "Bonjour tout le monde" }
    ]
  }
}
```

**Sample Response:**
```json
{
  "documents": [
    { "id": "1", "detectedLanguage": { "name": "English", "confidenceScore": 1 } },
    { "id": "2", "detectedLanguage": { "name": "French", "confidenceScore": 1 } }
  ]
}
```

**Important Notes:**
- Multilingual inputs return the dominant language, with lower confidence scores if mixed
- If detection fails, the result shows `"name": "(Unknown)"` and `"confidenceScore": 0.0`

### 🔹 Key Phrase Extraction

Identifies the main concepts or key points in a document.

**Sample Request:**
```json
{
  "kind": "KeyPhraseExtraction",
  "parameters": { "modelVersion": "latest" },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": "You must be the change you wish to see in the world."
      }
    ]
  }
}
```

**Sample Response:**
```json
{
  "documents": [
    { "id": "1", "keyPhrases": ["change", "world"] }
  ]
}
```

### 🔹 Sentiment Analysis

Determines if the sentiment is positive, neutral, negative, or mixed.

**Sample Request:**
```json
{
  "kind": "SentimentAnalysis",
  "parameters": { "modelVersion": "latest" },
  "analysisInput": {
    "documents": [
      { "id": "1", "language": "en", "text": "Good morning!" }
    ]
  }
}
```

**Sample Response:**
```json
{
  "documents": [
    {
      "id": "1",
      "sentiment": "positive",
      "confidenceScores": { "positive": 0.89, "neutral": 0.1, "negative": 0.01 }
    }
  ]
}
```

**Sentiment Rules:**
- All sentences neutral → document = neutral
- Positive + neutral → document = positive  
- Negative + neutral → document = negative
- Mixed sentiments → document = mixed

### 🔹 Entity Linking

Disambiguates named entities (e.g., "Venus") and links them to external sources like Wikipedia.

**Sample Request:**
```json
{
  "kind": "EntityLinking",
  "parameters": { "modelVersion": "latest" },
  "analysisInput": {
    "documents": [
      { "id": "1", "language": "en", "text": "I saw Venus shining in the sky" }
    ]
  }
}
```

**Sample Response:**
```json
{
  "documents": [
    {
      "id": "1",
      "entities": [
        {
          "name": "Venus",
          "url": "https://en.wikipedia.org/wiki/Venus"
        }
      ]
    }
  ]
}
```

## 🧠 Best Practices & Considerations

- **Max 1,000 documents per request**
- **Max 5,120 characters per document**
- Use `countryHint` for better language detection accuracy
- Multilingual content is handled by picking the dominant language
- Unknown or corrupt inputs will result in `(Unknown)` language with `confidenceScore: 0`

## 🎯 Exam Simulation Questions

**Q: Which field in the Language Detection response shows model confidence?**
✅ `confidenceScore`

**Q: What happens if a document contains multiple languages?**
✅ The service returns the language with the highest representation, with reduced confidence.

**Q: Which service should you use to link "Venus" to the correct Wikipedia article?**
✅ Entity Linking

**Q: What is the maximum supported text size per document?**
✅ 5,120 characters

**Q: What does a confidence score of 0.0 and language name (Unknown) mean?**
✅ The service couldn't determine the language (e.g., due to unreadable input)