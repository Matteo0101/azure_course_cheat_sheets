# Azure Multimodal Chat Application Guide

## 🎯 Problem
You need to build a **chat application** that accepts **both text and audio inputs**, and uses **multimodal generative AI** to understand and respond.

## ✅ Solution with Azure
Use **multimodal models** in **Azure AI Foundry**, like:
* `Microsoft Phi-4-multimodal-instruct`
* `OpenAI gpt-4o`
* `OpenAI gpt-4o-mini`

These models support **text + audio input** and can generate intelligent responses.

## 🧩 Componenti richiesti
* ✅ Azure AI Foundry (portal access)
* ✅ A deployed **multimodal model**
* ✅ Chat Playground (for testing)
* ✅ Python or .NET SDK (for app development)
* ✅ Proper formatting of multi-part messages (JSON structure)

## 🛠️ Architettura / Sviluppo

### 🔹 Deploy a Multimodal Model
1. Go to Azure AI Foundry portal
2. Select a model like `gpt-4o` or `phi-4-multimodal-instruct`
3. Deploy the model
4. Test in **Chat Playground** with audio + text prompts:
   * Upload audio file
   * Combine with text to form a prompt

### 🔹 Structure of Audio-Based Prompt (JSON)
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Transcribe this audio:"
        },
        {
          "type": "audio_url",
          "audio_url": {
            "url": "https://..."
          }
        }
      ]
    }
  ]
}
```

🟨 Alternatively, use **base64-encoded binary audio data**:
```json
{
  "type": "audio_url",
  "audio_url": {
    "url": "data:audio/mp3;base64,<binary_audio_data>"
  }
}
```

### 🔹 Develop Audio-Enabled Chat App
* Use **Python** or **.NET** SDK for:
  * Azure AI Model Inference
  * OpenAI API
* Your client application should:
  * Connect to the model endpoint
  * Submit **multi-part prompts** (text + audio)
  * Receive and process the model's response

## 🔁 Prompt Submission Options
* ✅ Text + Audio URL (hosted audio file)
* ✅ Text + Base64 binary audio (inline submission)

## 🧠 Best Practice / Considerazioni
* 🌐 Ensure audio files are in supported format (e.g., MP3)
* 📂 If using base64, avoid large files (limits may apply)
* 🔒 Secure any URLs and ensure CORS/permissions are handled if using remote files
* 🧪 Test prompts using **Chat Playground** before coding

## ❓ Domande simulate d'esame

1. **Q:** What is the correct JSON structure for submitting a multimodal audio prompt?
   **A:** A `messages` array with a `content` array including both `text` and `audio_url` objects.

2. **Q:** Which models in Azure AI Foundry support audio-based prompts?
   **A:** `Microsoft Phi-4-multimodal-instruct`, `OpenAI gpt-4o`, and `OpenAI gpt-4o-mini`.

3. **Q:** How can you submit local audio data directly in a prompt?
   **A:** By encoding it in base64 and using a `data:` URL format in the `audio_url`.

4. **Q:** Which tools can be used to test audio prompts before writing application code?
   **A:** Azure AI Foundry **Chat Playground**.