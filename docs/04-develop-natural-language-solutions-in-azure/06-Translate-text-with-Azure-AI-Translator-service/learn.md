Azure AI Translator Service - Complete Guide
🧩 Problem
You need to build an application that can translate text between multiple languages, detect the language of input, or adapt to specific vocabulary/industry requirements with custom translations.
💡 Solution with Azure
Use the Azure AI Translator service to detect languages, translate text, transliterate scripts, and apply domain-specific custom translations via the REST API or SDKs.
🧱 Required Components

Azure AI Translator resource (or Azure AI Services multi-resource)
Subscription key and endpoint
REST API or SDK (Python, C#, etc.)
(Optional) Custom Translator portal for specialized translation models

🏗️ Architecture & Development
1. Provision the Translator Resource

In Azure Portal, create an Azure AI Translator resource
Alternatively, create a multi-service Azure AI Services resource and use the Translator API
Collect your subscription key and region, needed for API calls

2. Core Capabilities
a. Language Detection
Endpoint: POST https://api.cognitive.microsofttranslator.com/detect?api-version=3.0
Sample input:
json[{ "Text": "こんにちは" }]
Sample output:
json[{ "language": "ja", "score": 1.0 }]
b. Text Translation
Endpoint: POST https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=ja&to=en&to=fr
Sample output:
json[
  {
    "translations": [
      { "text": "Hello", "to": "en" },
      { "text": "Bonjour", "to": "fr" }
    ]
  }
]
c. Transliteration
Endpoint: POST https://api.cognitive.microsofttranslator.com/transliterate?api-version=3.0&fromScript=Jpan&toScript=Latn
Output:
json[{ "script": "Latn", "text": "Kon'nichiwa" }]
3. Translation Options
Word Alignment
Helps map parts of source to target:
json"alignment": { "proj": "0:4-0:1 6:13-2:3" }
Sentence Length
Include includeSentenceLength=true to get:
json"sentLen": { "srcSentLen": [12], "transSentLen": [20] }
Profanity Filtering
Options:

NoAction: translate as-is
Deleted: remove profanity
Marked: replace with asterisks (profanityMarker=Asterisk) or tags (profanityMarker=Tag)

Example:
json{ "text": "JSON ist *** erstaunlich." }
4. Define Custom Translations
Use the Custom Translator Portal to:

Create a workspace linked to your Translator resource
Create a project
Upload training data
Train and publish the model

Each model is assigned a category ID
Call the Translator API with the category=<category-id> parameter:
bashcurl -X POST \
  "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=nl&category=<category-id>" \
  -H "Ocp-Apim-Subscription-Key: <your-key>" \
  -H "Content-Type: application/json" \
  -d "[{ 'Text': 'Where can I find my employee details?' }]"
✅ Best Practices & Considerations

Use language detection when the source language is unknown
Use transliteration for script transformation without changing language
Apply profanity filtering where needed based on context
Implement custom models when domain-specific terms are poorly translated by default
Test with multiple target languages in a single request
Monitor status codes and error handling for failed requests

❓ Sample Exam Questions
Q: What endpoint is used to detect the language of a text input in Azure Translator?
→ https://api.cognitive.microsofttranslator.com/detect?api-version=3.0
Q: What is the purpose of the category parameter in a translation request?
→ It applies a custom translation model instead of the default.
Q: How can profanity be filtered in a translation?
→ By setting profanityAction to Deleted, Marked, or NoAction.
Q: Which function allows rendering text in a different script (e.g., Hiragana → Latin)?
→ Transliteration (/transliterate endpoint)
Q: How can you align words from source to translated text in the output?
→ Use the includeAlignment=true parameter.