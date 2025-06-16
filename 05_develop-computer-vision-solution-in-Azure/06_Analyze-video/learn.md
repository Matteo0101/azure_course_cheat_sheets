# Azure Video Indexer

## Service
**Azure Video Indexer**

## Problem
You have video content (e.g., recorded meetings, events, presentations) and need to extract insights for indexing, analysis, and content moderation.

## Solution with Azure
Use **Azure Video Indexer** to analyze videos using prebuilt AI models for transcription, sentiment analysis, OCR, facial recognition, and more. You can also train custom models to extract domain-specific insights.

## Componenti richiesti
- **Azure Video Indexer Portal** – for uploading and analyzing videos interactively.
- **Azure Video Indexer REST API** – for programmatic access to upload, analyze, and retrieve video insights.
- **Video Indexer Widgets** – to embed analysis capabilities in custom applications.
- **ARM Templates** – to deploy Video Indexer resources automatically.
- **Limited Access Approval** – required for facial recognition and custom people models.

## Architettura / Sviluppo

### Upload e Analisi
- **Upload videos** via portal or API.
- **Analyze video** to extract:
  - Speech transcription
  - Optical Character Recognition (OCR)
  - Facial recognition *(Limited Access)*
  - Scene segmentation
  - Sentiment detection
  - Topic and label identification
  - Content moderation

### Modelli Personalizzati
- **Use custom models** for:
  - Recognizing custom people (via uploaded images)
  - Recognizing brand names
  - Custom language models (e.g., domain-specific terms)

### Integrazione
- **Embed widgets** in HTML to allow controlled sharing of analyzed content.
- **Access data via REST API**, including:
  - Authentication using access token
  - Retrieve video insights
  - Manage custom models (e.g., custom logos, brands)

### API Examples
**Retrieve access token:**
```
https://api.videoindexer.ai/Auth/<location>/Accounts/<accountId>/AccessToken
```

**Retrieve videos:**
```
https://api.videoindexer.ai/<location>/Accounts/<accountId>/Videos?<accessToken>
```

## Best practice / Considerazioni
- Ensure **Responsible AI compliance** when using facial recognition or creating custom people models.
- Use **custom language and brand models** to improve recognition for domain-specific content.
- Embed widgets only when controlled access is required — avoid exposing full portal access.
- Automate deployment and scaling using **ARM templates**.
- Use **metadata and insights** for improved video search and user engagement.

## Domande simulate d'esame

**Q1.** You need to extract spoken dialog and key topics from a recorded meeting. Which Azure service should you use?  
**A.** Azure Video Indexer

**Q2.** What feature must be enabled with Limited Access approval in Azure Video Indexer?  
**A.** Facial recognition

**Q3.** How can you integrate Azure Video Indexer analysis into a custom web application?  
**A.** Embed Video Indexer widgets

**Q4.** You need to detect a specific brand name that appears in a product demo video. How should you proceed?  
**A.** Train a custom brand model in Azure Video Indexer

**Q5.** Which endpoint retrieves your account's access token for the Video Indexer REST API?  
**A.** `https://api.videoindexer.ai/Auth/<location>/Accounts/<accountId>/AccessToken`