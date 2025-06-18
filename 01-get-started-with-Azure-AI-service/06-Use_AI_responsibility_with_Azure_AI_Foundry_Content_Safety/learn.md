# Azure AI Foundry Content Safety Guide

## 🔍 Problem
You need to detect and moderate harmful, offensive, or inappropriate content—whether user-generated or AI-generated—across various formats (text, image, multimodal) and languages, ensuring compliance with regulations and protecting user safety and brand integrity.

## ✅ Solution with Azure
Use **Azure AI Foundry Content Safety**, an AI-powered content moderation service that analyzes text, images, and multimodal inputs to detect content that falls into four core categories:
* **Violence**
* **Hate speech**
* **Sexual content**
* **Self-harm**

It replaces the deprecated Azure Content Moderator and provides more advanced, multilingual and multimodal content safety tools.

## 🧩 Required Components
* **Azure AI Foundry Portal** (access via Azure portal)
* **Content Safety Studio** or **Azure AI Content Studio**
* **Moderation APIs** for:
   * Text content
   * Image content
   * Multimodal content (OCR + analysis)
* **Custom Categories** (optional)
* **Prompt Shields API** for LLM prompt protection
* **Protected Material Detection**
* **Groundedness Detection API**
* **Safety System Messages**

## 🏗️ Architecture / Development

### 🧠 Text Moderation
* Input analyzed by NLP across four categories
* Severity levels (0–6) returned per category
* Use **blocklists** for specific terms
* API returns structured moderation data

### 🖼️ Image Moderation
* Uses **Florence foundation model**
* Returns severity: *safe*, *low*, *high*
* Developer sets threshold: *low*, *medium*, *high*
* Evaluated per category

### 🧾 Multimodal Moderation
* Uses OCR to extract and analyze text within images
* Same four categories evaluated

### 🛡️ Prompt Shields
* Blocks prompt-based jailbreaks on LLMs
* Applies to user input and embedded document content

### 🧾 Protected Material Detection
* Flags copyright violations in AI-generated content

### 📉 Groundedness Detection
* Compares LLM responses to source data
* Optionally returns **reasoning** for ungrounded flags

### 🎛️ Custom Categories
* Define categories using positive/negative examples
* Train a model for customized moderation

## 📌 Best Practices / Considerations
* **Test on real data** before deploying
* Continuously **monitor accuracy** post-deployment
* Use human moderators for edge cases and appeals
* Communicate clearly to users why content is flagged
* Understand AI limits: possibility of **false positives/negatives**
* Evaluate using:
   * ✅ True Positives
   * ❌ False Positives
   * ✅ True Negatives
   * ❌ False Negatives

## ❓ Simulated Exam Questions
1. 🧠 *How does Azure AI Foundry Content Safety determine if text should be blocked or approved?* ➤ By assigning severity levels (0–6) across four categories: violence, hate, sexual content, and self-harm.

2. 🧠 *What model powers image analysis in Foundry Content Safety?* ➤ Florence foundation model.

3. 🧠 *How does the system evaluate multimodal content?* ➤ It uses OCR to extract text from images, then analyzes both the image and text across the four categories.

4. 🧠 *Which service should you use to prevent prompt-based jailbreaks in LLM inputs?* ➤ Prompt Shields.

5. 🧠 *What should you do before deploying Foundry Content Safety in a live environment?* ➤ Test on real data and plan continuous monitoring.

6. 🧠 *Which functionality detects grounded vs. ungrounded responses from LLMs?* ➤ Groundedness Detection.

7. 🧠 *Can you define custom moderation rules? How?* ➤ Yes, using the **Custom Categories** feature by training with example content.

8. 🧠 *What are the severity levels used for image moderation?* ➤ Safe, Low, High — combined with threshold settings (Low, Medium, High) to determine action.