# Text Translation with Azure AI Translator 🌐

## 🧩 Problem

You need to build an application that translates text from any supported language to a target language, detecting the source language automatically.

## 💡 Solution with Azure

Use **Azure AI Translator** to:

- Translate text between supported languages
- Auto-detect source language
- Build client applications (C#/Python) using Azure AI Translator SDK

## ⚙️ Components Required

- Azure AI Translator resource
- Azure subscription with Azure portal access
- Visual Studio Code
- GitHub repo: `https://github.com/MicrosoftLearning/mslearn-ai-language`
- Azure AI Translator SDK:
  - **C#**: `Azure.AI.Translation.Text 1.0.0-beta.1`
  - **Python**: `azure-ai-translation-text==1.0.0b1`

## 🏗️ Architecture / Development

### 1️⃣ Provision Azure AI Translator Resource

In Azure portal:
- Create new **Azure AI Translator** resource
- Supported region: Any available region
- Pricing tier: F0 (free) or S (standard)

Retrieve:
- **Key**
- **Region** (⚠ Required by SDK)

### 2️⃣ Clone Code Repository

- Clone repo: `https://github.com/MicrosoftLearning/mslearn-ai-language`
- Open repo in Visual Studio Code: `Labfiles/06b-translator-sdk/translate-text`

### 3️⃣ Install SDK Package

**C#:**
```bash
dotnet add package Azure.AI.Translation.Text --version 1.0.0-beta.1
```

**Python:**
```bash
pip install azure-ai-translation-text==1.0.0b1
```

### 4️⃣ Configure Application

Edit config files:
- **C#**: `appsettings.json`
- **Python**: `.env`

Set:
- `translatorKey`
- `translatorRegion` (⚠ Not endpoint)

### 5️⃣ Add Code to Import SDK Namespaces

**C#:**
```csharp
using Azure;
using Azure.AI.Translation.Text;
```

**Python:**
```python
from azure.ai.translation.text import *
from azure.ai.translation.text.models import InputTextItem
```

### 6️⃣ Create Translator Client

**C#:**
```csharp
AzureKeyCredential credential = new(translatorKey);
TextTranslationClient client = new(credential, translatorRegion);
```

**Python:**
```python
credential = TranslatorCredential(translatorKey, translatorRegion)
client = TextTranslationClient(credential)
```

### 7️⃣ Get Supported Languages & Select Target Language

**C#:**
```csharp
Response<GetLanguagesResult> languagesResponse = await client.GetLanguagesAsync(scope:"translation");
GetLanguagesResult languages = languagesResponse.Value;
string targetLanguage = Console.ReadLine();
```

**Python:**
```python
languagesResponse = client.get_languages(scope="translation")
targetLanguage = input()
```

### 8️⃣ Translate Text

**C#:**
```csharp
Response<IReadOnlyList<TranslatedTextItem>> translationResponse = await client.TranslateAsync(targetLanguage, inputText);
TranslatedTextItem translation = translationResponse.Value[0];
```

**Python:**
```python
input_text_elements = [InputTextItem(text=inputText)]
translationResponse = client.translate(content=input_text_elements, to=[targetLanguage])
translation = translationResponse[0]
```

### 9️⃣ Run Application

**C#:**
```bash
dotnet run
```

**Python:**
```bash
python translate.py
```

## 🔧 Best Practice / Considerations

- Use correct region parameter, not the full endpoint URL
- Use latest SDK version supported for Azure Translator
- Validate supported languages at runtime using `GetLanguages`
- Auto-detect source language (included in SDK response)
- Handle possible errors (invalid language codes, empty input)

## ❓ Exam-like Sample Questions

### Question 1:
Which SDK package is used for Azure AI Translator in C#?

A. Azure.AI.TextAnalytics  
B. Azure.AI.Translation.Text  
C. Azure.AI.Language

**✅ Answer: B**

### Question 2:
What parameter must be provided alongside the API key when creating the client?

A. Endpoint URL  
B. Subscription ID  
C. Region

**✅ Answer: C**

### Question 3:
Which method retrieves the list of supported translation languages?

A. GetLanguagesAsync  
B. ListLanguages  
C. FetchSupportedLanguages

**✅ Answer: A**

### Question 4:
What SDK version was used in this lab?

A. 1.0.0-beta.1  
B. 5.3.0  
C. 4.2.0

**✅ Answer: A**

### Question 5:
Which Python object is used to send input text for translation?

A. InputTextItem  
B. TranslateRequest  
C. TextItem

**✅ Answer: A**