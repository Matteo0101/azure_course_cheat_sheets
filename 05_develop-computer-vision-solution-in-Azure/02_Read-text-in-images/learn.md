# 📖 Optical Character Recognition (OCR) with Azure AI Vision

## 🔍 **Problem**

You have an image (photograph, scan, or screenshot) containing text that needs to be extracted for digital processing, indexing, or integration into applications. Examples include:

-   📇 Extracting contact info from a photographed business card
-   🆔 Reading text from scanned IDs or documents for applications
-   🍽️ Capturing text from menus, recipes, or street signs for storage or translation
-   ✍️ Digitizing handwritten notes from a photo

---

## ☁️ **Solution with Azure**

Use **Azure AI Vision** to perform optical character recognition (OCR) on images. Azure AI Vision's image analysis API can detect, locate, and extract text from unstructured images or scanned documents.

### 🔄 Alternative services (when applicable):

-   **📄 Azure AI Document Intelligence** – For structured documents like forms, invoices, receipts; supports key-value extraction, tables, prebuilt and custom models
-   **🎯 Azure AI Content Understanding** – For multimodal (image, audio, video, documents) content extraction and custom analyzers

---

## 🧩 **Components Required**

-   **🌐 Azure resource**:

    -   Azure AI Services multi-service resource (standalone or part of Azure AI Foundry hub/project)
    -   _or_ standalone Computer Vision resource

-   **📱 Client app / SDK**:

    -   REST API or Azure AI Vision SDK (e.g., Python, .NET)

-   **🔐 Authentication**:
    -   Key-based authentication (authorization key)
    -   Microsoft Entra ID (token or managed identity)

---

## 🏗️ **Architecture / Development**

### 1. **🚀 Provision Azure resource**

-   Create Azure AI Vision or AI Services resource in Azure subscription
-   Note the endpoint: `https://<resource_name>.cognitiveservices.azure.com/`

### 2. **🔌 Connect to resource**

-   Use key-based or Entra ID authentication

### 3. **📤 Submit image for OCR**

-   **Image requirements:**

    -   Format: JPEG, PNG, GIF, or BMP
    -   Size: < 4 MB
    -   Dimensions: > 50x50 pixels

-   **API call methods:**

    **REST:**

    ```
    https://<endpoint>/computervision/imageanalysis:analyze?features=read&...
    ```

    **SDK (Python example):**

    ```python
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential

    client = ImageAnalysisClient(
        endpoint="<YOUR_RESOURCE_ENDPOINT>",
        credential=AzureKeyCredential("<YOUR_AUTHORIZATION_KEY>")
    )

    result = client.analyze(
        image_data=<IMAGE_DATA_BYTES>,  # binary data
        visual_features=[VisualFeatures.READ],
        language="en"
    )
    ```

### 4. **📥 Process result**

-   **Response structure**: JSON or SDK object
-   **Organized by**: Blocks → Lines → Words
-   Each with text, bounding polygon, confidence score

**Example response:**

```json
{
  "metadata": { "width": 500, "height": 430 },
  "readResult": {
    "blocks": [
      {
        "lines": [
          {
            "text": "Hello World!",
            "boundingPolygon": [...],
            "words": [
              { "text": "Hello", "boundingPolygon": [...], "confidence": 0.996 },
              { "text": "World!", "boundingPolygon": [...], "confidence": 0.99 }
            ]
          }
        ]
      }
    ]
  }
}
```

---

## ⭐ **Best Practice / Considerations**

### 🎯 **Service choice:**

-   Use **🔍 AI Vision** for general unstructured OCR (photos, labels, menus, business cards)
-   Use **📋 Document Intelligence** for forms/invoices (structured data)
-   Use **🎭 Content Understanding** for multimodal extraction (documents, audio, video)

### 🔒 **Security:**

-   Prefer Microsoft Entra ID + managed identity in production
-   Use Azure Key Vault to store keys securely

### ⚡ **Performance:**

-   Optimize image quality (clear text, high resolution)
-   Use appropriate language hint when text is non-English

---

## 📝 **Sample Exam-Like Questions**

### 1️⃣ You need to extract text from scanned business cards and photos of street signs. Which Azure service do you use?

**✅ Answer:** Azure AI Vision

---

### 2️⃣ What authentication methods can be used with Azure AI Vision OCR?

**✅ Answer:** Key-based authentication and Microsoft Entra ID authentication

---

### 3️⃣ What image formats and size limits apply to images submitted for OCR using Azure AI Vision?

**✅ Answer:**

-   **Formats:** JPEG, PNG, GIF, BMP
-   **Size:** < 4 MB
-   **Dimensions:** > 50x50 pixels

---

### 4️⃣ What structure does the OCR response from Azure AI Vision provide?

**✅ Answer:** Response contains blocks → lines → words, each with text, bounding polygon, and confidence score
