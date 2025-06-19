# Azure AI Foundry Exercise Summary

## ✅ **Exercise Overview: Audio-Enabled Chat App with Azure AI Foundry**

### 📌 **Objective**
Build a simple AI application using the **Phi-4-multimodal-instruct** model to summarize customer voice messages (audio) for a produce supplier company.

## 🔧 **Steps Completed**

### 1. **Azure AI Foundry Project Setup**
- Signed into Azure AI Foundry
- Deployed the `Phi-4-multimodal-instruct` model to a new project
- Noted the **endpoint** and **deployment name**

### 2. **Environment Preparation**
- Used Azure Cloud Shell (PowerShell) in classic mode
- Cloned the repo: `https://github.com/MicrosoftLearning/mslearn-ai-language`
- Installed dependencies:
  - **For Python**: `azure-identity`, `azure-ai-projects`, `azure-ai-inference`
  - **For C#**: relevant NuGet packages

### 3. **Configuration**
- Edited configuration files:
  - `.env` (Python)
  - `appsettings.json` (C#)
- Added your Azure AI project endpoint and model deployment name

### 4. **Code Enhancements**
- Initialized the **AIProjectClient** and **chat client**
- Built a request to send **audio and text prompts** to the deployed model
- Used example audio files:
  - `avocados.mp3`
  - `fresas.mp3`

### 5. **Execution**
- Logged in with `az login`
- Ran the app with prompts:
  - *"Can you summarize this customer's voice message?"*
  - *"Is it time-sensitive?"*
- Observed model responses based on audio inputs

## 🧠 **Key Concepts Learned**

- **Multimodal prompts**: Combining text and audio in the same request
- **Audio input formats**: Using `audio_url` (with hosted MP3s)
- **Azure AI Inference SDK**: Simplified interaction with deployed AI models
- **Statelessness**: No chat history maintained unless you implement it

## 🛠️ **Next Steps & Ideas**

- 📝 Implement chat history tracking
- 🎤 Let users record and upload live audio via UI
- 🧪 Test with your own audio files
- 🧠 Try different system messages (e.g., more formal, time-aware, etc.)
- 🔄 Experiment with different multimodal models
- 🌐 Build a web interface for the application
- 📊 Add analytics and logging capabilities