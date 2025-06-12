# 🧩 AI-102 Study Card – Image Generation with Azure AI Foundry (DALL-E)

## ✅ 1. Problem

You need to generate **original images** (not from catalogs) based on **natural language descriptions**. Real-world examples:
- Illustrations for articles or marketing campaigns
- Creating logos or product graphics
- Unique content for websites, e-commerce, social media

---

## 🧠 2. Solution in Azure

Use **Azure AI Foundry** with generative AI models like **DALL-E 3** or **GPT-Image 1**.

✅ These models allow you to:
- Generate images from text prompts (e.g., *"a squirrel on a motorcycle"*)
- Customize output in terms of **resolution**, **style**, and **quality**
- Obtain **original and synthetic** images, not searched online

---

## 🔩 3. Required Components and Tools

| Component | Description |
|-----------|-------------|
| Azure AI Foundry | Platform that hosts and orchestrates generative models |
| DALL-E 3 | Specific model for image generation |
| REST API or SDK | To make programmatic requests |
| Azure AI Foundry Playground | UI to test prompts and generate images |

---

## 🧱 4. Architecture/Development

- **Input**: Text prompt (e.g., "A badger wearing a tuxedo")
- **API Call**: POST with JSON payload
- **Output**: URL of generated image in PNG format

### Example JSON Request:
```json
{
  "prompt": "A badger wearing a tuxedo",
  "n": 1,
  "size": "1024x1024",
  "quality": "hd",
  "style": "vivid"
}
```

### Response:
```json
{
  "data": [
    {
      "url": "<Generated image URL>",
      "revised_prompt": "<System-rewritten prompt>"
    }
  ]
}
```

---

## 💡 5. Best Practices / Considerations

- **DALL-E 3 only supports** `n = 1`
- Supported resolutions: `1024x1024`, `1792x1024`, `1024x1792`
- Quality: `standard` or `hd` (default: `standard`)
- Style: `vivid` or `natural` (default: `vivid`)
- Prompt automatically improved by the system
- Output is **synchronous** and directly provides the image URL

### Additional Technical Details:

#### API Endpoint Format:
```
POST https://<your-resource-name>.openai.azure.com/openai/deployments/<deployment-name>/images/generations?api-version=2024-02-15-preview
```

#### Required Headers:
```http
Content-Type: application/json
api-key: <your-api-key>
```

#### Complete Code Example (Python):
```python
import requests
import json
import os

# Configuration
endpoint = "https://<your-resource>.openai.azure.com"
api_key = "<your-api-key>"
deployment_name = "<your-dalle-deployment>"

# API request
url = f"{endpoint}/openai/deployments/{deployment_name}/images/generations?api-version=2024-02-15-preview"

headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

payload = {
    "prompt": "A futuristic city with flying cars at sunset",
    "n": 1,
    "size": "1024x1024",
    "quality": "hd",
    "style": "vivid"
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()

# Get the generated image URL
image_url = result["data"][0]["url"]
print(f"Generated image URL: {image_url}")
```

#### Complete Code Example (C#):
```csharp
using Azure;
using Azure.AI.OpenAI;

// Initialize client
var client = new AzureOpenAIClient(
    new Uri("https://<your-resource>.openai.azure.com"),
    new AzureKeyCredential("<your-api-key>")
);

// Generate image
var imageOptions = new ImageGenerationOptions()
{
    Prompt = "A futuristic city with flying cars at sunset",
    Size = ImageSize.Size1024x1024,
    Quality = ImageGenerationQuality.High,
    Style = ImageGenerationStyle.Vivid
};

Response<ImageGenerations> response = await client.GetImageGenerationsAsync(
    "<your-dalle-deployment>", 
    imageOptions
);

// Get the generated image URL
string imageUrl = response.Value.Data[0].Url.ToString();
Console.WriteLine($"Generated image URL: {imageUrl}");
```

---

## 🔧 Configuration Parameters

| Parameter | Type | Options | Description |
|-----------|------|---------|-------------|
| `prompt` | string | Any descriptive text | The description of the image to generate |
| `n` | integer | 1 (only supported value) | Number of images to generate |
| `size` | string | `1024x1024`, `1792x1024`, `1024x1792` | Resolution of the generated image |
| `quality` | string | `standard`, `hd` | Quality level of the image |
| `style` | string | `vivid`, `natural` | Style of the generated image |

---

## 📊 Pricing and Limitations

- **DALL-E 3 pricing** is based on image resolution and quality
- **Rate limits** apply per deployment
- Images are **temporarily stored** and URLs expire after a certain period
- **Content filtering** is applied to both prompts and generated images

---

## ❓ 6. Simulated Exam Questions

1. 🔹 **You need to generate images from text. Which Azure service do you use?**  
   ➜ **Azure AI Foundry + DALL-E 3**

2. 🔹 **What parameters can you set in the payload to control image quality?**  
   ➜ `size`, `quality`, `style`, `prompt`, `n`

3. 🔹 **How do you get the result from DALL-E 3 via API?**  
   ➜ The **URL of the generated image** is returned in the JSON response.

4. 🔹 **What are the supported image resolutions for DALL-E 3?**  
   ➜ `1024x1024`, `1792x1024`, `1024x1792`

5. 🔹 **Can you generate multiple images in a single API call with DALL-E 3?**  
   ➜ No, DALL-E 3 only supports `n = 1`

6. 🔹 **What happens to the original prompt when using DALL-E 3?**  
   ➜ The system automatically improves and rewrites the prompt for better results

---

## 🚀 Quick Start Checklist

- [ ] Create Azure AI Foundry resource
- [ ] Deploy DALL-E 3 model
- [ ] Get endpoint and API key
- [ ] Test in Azure AI Foundry Playground
- [ ] Implement via REST API or SDK
- [ ] Handle image URL response
- [ ] Implement proper error handling
- [ ] Consider content filtering policies