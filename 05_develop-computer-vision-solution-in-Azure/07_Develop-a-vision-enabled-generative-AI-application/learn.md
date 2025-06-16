# Service: Azure AI Foundry – Multimodal Generative AI 🤖🖼️

## 🧩 Problem
You need to create a chat-based application that can understand and respond to prompts containing both **text and images** (vision-enabled interaction).

## 🚀 Solution with Azure
Use **Azure AI Foundry** to deploy and interact with **multimodal generative AI models**, such as:
* 🧠 Microsoft **Phi-4-multimodal-instruct**
* 🌐 OpenAI **GPT-4o**
* ⚡ OpenAI **GPT-4o-mini**

These models can process **text + image** inputs and return appropriate, context-aware responses.

## 🛠️ Componenti richiesti
* **Azure AI Foundry portal** for model deployment and testing
* **Multimodal model** (e.g., GPT-4o)
* **Chat playground** to test image+text prompts
* **API endpoint** for submitting multi-part messages
* **SDK** for Python or .NET (Azure AI Model Inference or OpenAI API)

## 🏗️ Architettura / Sviluppo
* **Deploy a multimodal model** from the Azure AI Foundry portal
* **Test prompts** using the built-in **chat playground** by uploading an image and adding a text prompt
* **Develop a client application** that:
   * Connects to the model endpoint
   * Sends prompts as **multi-part messages**
   * Receives and processes the response

### Multi-part JSON prompt format:

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
          "text": "Describe this picture:"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://....."
          }
        }
      ]
    }
  ]
}
```

### If using local image data:

```json
{
  "type": "image_url",
  "image_url": {
    "url": "data:image/jpeg;base64,<binary_image_data>"
  }
}
```

## 📌 Best practice / Considerazioni
* ✅ Use **multimodal prompt format** (text + image) for richer, context-aware interaction
* 🌐 Choose the right model (**GPT-4o**, **Phi-4**, etc.) based on performance and availability
* 📤 For local images, use **base64 encoding** in data URL format
* ⚙️ Use SDKs to simplify interaction with REST APIs in production apps
* 🧪 Always validate model output in the chat playground before integrating

## 📝 Domande simulate d'esame

**Q1.** Which Azure service allows you to create chat-based apps using text and image input?  
**A.** Azure AI Foundry (with a multimodal model)

**Q2.** What is the correct JSON structure for sending a prompt with both text and image?  
**A.** A multi-part message containing both `type: "text"` and `type: "image_url"` items

**Q3.** You need to develop a vision-enabled chatbot in .NET. Which resource do you use?  
**A.** The Azure AI Model Inference or OpenAI .NET SDK

**Q4.** Which model types support vision-based chat in Azure AI Foundry?  
**A.** Microsoft Phi-4-multimodal-instruct, OpenAI GPT-4o, and GPT-4o-mini

**Q5.** What's a required step to submit a local image file in a prompt?  
**A.** Encode the image as base64 and include it in a data URL