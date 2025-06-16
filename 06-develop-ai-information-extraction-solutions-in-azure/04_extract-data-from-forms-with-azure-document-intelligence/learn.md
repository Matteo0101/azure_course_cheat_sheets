# Azure Document Intelligence

## 🧩 Problem
Hai bisogno di estrarre dati strutturati—come testo, coppie chiave-valore, segni di selezione e tabelle—da documenti come fatture, ricevute, documenti d'identità o moduli aziendali. Costruire un modello ad alta precisione da zero richiederebbe competenze in deep learning, risorse computazionali elevate e lunghi tempi di addestramento, il che potrebbe non essere fattibile.

## ✅ Solution with Azure
**Azure Document Intelligence** è un servizio cloud-based di intelligenza artificiale che utilizza OCR e modelli di deep learning per estrarre informazioni dai documenti. Permette un'estrazione dati ad alta precisione con un minimo o nessun addestramento, grazie a modelli pre-addestrati.

---

## 🔧 Required Components
### 📄 Document Analysis Models
Accettano file **JPEG, PNG, PDF, TIFF** e restituiscono un file **JSON** con:
- Contenuto testuale
- Riquadri di delimitazione (bounding boxes)
- Tabelle
- Segni di selezione (checkbox, radio button)
- Struttura del documento
### 🧠 Prebuilt Models
Estraggono dati strutturati da documenti comuni:
- Moduli W-2
- Fatture
- Ricevute
- Documenti d'identità
- Biglietti da visita

### 🛠️ Custom Models
Addestrabili tramite **Azure Document Intelligence Studio** per moduli aziendali specifici.

---

## 🔌 Access Methods
- REST API
- SDK client (Python, .NET)
- Azure Document Intelligence Studio
- Azure AI Foundry

---

## 🏗️ Architecture / Development
- L'OCR cattura la struttura del documento creando riquadri attorno agli oggetti rilevati.
- Il servizio restituisce un output JSON strutturato con le relazioni preservate dal file originale.
- Gli sviluppatori possono usare:
  - REST API per qualsiasi linguaggio
  - SDK Python e .NET
  - Azure Studio per addestrare e testare modelli personalizzati
---

## ✅ Best Practices / Considerations
- Usa modelli predefiniti quando disponibili per evitare l’addestramento.
- Usa modelli personalizzati per documenti specifici del dominio.
- Alcune funzionalità potrebbero essere in anteprima—consulta la documentazione ufficiale per aggiornamenti.
- Scegli il metodo di accesso più adatto (API, SDK, Studio) in base all’ambiente di sviluppo e al caso d’uso.

---

## 📘 Sample Exam Questions

### ❓ You need to extract key-value pairs and tables from a scanned invoice. Which Azure service should you use?
- A. Azure Form Recognizer  
- B. **Azure Document Intelligence** ✅  
- C. Azure Cognitive Search  
- D. Azure Computer Vision  

---

### ❓ Which file formats are supported by Azure Document Intelligence for input documents?
- A. DOCX, XLSX  
- B. **JPEG, PNG, PDF, TIFF** ✅  
- C. HTML, XML  
- D. CSV, JSON  

---

### ❓ What is the output format of Azure Document Intelligence after analyzing a document?
- A. XML  
- B. CSV  
- C. **JSON** ✅  
- D. TXT  

# 🧠 Train Custom Models with Azure Document Intelligence

## 🟠 Problem
You need to extract structured data from form documents (e.g., invoices, receipts, contracts) that do not conform to standard templates.  
How can you train a custom model to recognize and extract labeled fields from these documents?

---

## 🟢 Solution with Azure
Use **Azure Document Intelligence** to train a **custom model** using supervised machine learning. You can choose between:
- **Custom template models** for structured documents.
- **Custom neural models** for semi-structured or unstructured documents.

---

## 🧩 Required Components
- Azure Blob Storage container with:
  - Sample form documents
  - `ocr.json` files (layout and text info)
  - `fields.json` (field definitions)
  - `labels.json` (field-to-location mapping per form)
- Shared Access Signature (SAS) URL for the container
- Azure Document Intelligence:
  - REST API or SDK
  - OR Azure Document Intelligence Studio

---

## 🏗️ Architecture / Development

### Option 1: Using REST API / SDK
1. Upload sample forms and JSON files to Azure Blob Storage.
2. Generate a **SAS URL** for the container.
3. Call the **Build model** API with the SAS URL.
4. Retrieve the **model ID** using the **Get model** API.

### Option 2: Using Document Intelligence Studio
1. Upload and label documents directly in the Studio.
2. Choose between:
   - **Custom template model**: Fast training, supports 100+ languages.
   - **Custom neural model**: Best for complex layouts and language-rich documents.

---

## ✅ Best Practices / Considerations
- Use **custom template models** for structured forms with consistent layouts.
- Use **custom neural models** for documents with variable structure or rich language content.
- Ensure accurate labeling in `labels.json` to improve model performance.
- Use **Document Intelligence Studio** for a visual and guided training experience.

---

## ❓ Sample Exam Questions

**Q1.** You need to extract labeled fields from semi-structured documents. Which model type should you use?  
- A. Prebuilt model  
- B. Custom template model  
- ✅ C. Custom neural model  
- D. Layout model

**Q2.** Which file describes the fields you want to extract in a custom model training setup?  
- A. `ocr.json`  
- ✅ B. `fields.json`  
- C. `labels.json`  
- D. `model.json`

**Q3.** What is required to initiate training using the Build model API?  
- A. Azure Key Vault  
- ✅ B. SAS URL to a blob container  
- C. Azure SQL Database  
- D. Azure Kubernetes Service

# Final version: Write the complete Markdown content to a file

markdown_content = """
# 🧠 Train Custom Models with Azure Document Intelligence

## 🟠 Problem
You need to extract structured data from form documents (e.g., invoices, receipts, contracts) that do not conform to standard templates.  
How can you train a custom model to recognize and extract labeled fields from these documents?

---

## 🟢 Solution with Azure
Use **Azure Document Intelligence** to train a **custom model** using supervised machine learning. You can choose between:
- **Custom template models** for structured documents.
- **Custom neural models** for semi-structured or unstructured documents.

---

## 🧩 Required Components
- Azure Blob Storage container with:
  - Sample form documents
  - `ocr.json` files (layout and text info)
  - `fields.json` (field definitions)
  - `labels.json` (field-to-location mapping per form)
- Shared Access Signature (SAS) URL for the container
- Azure Document Intelligence:
  - REST API or SDK
  - OR Azure Document Intelligence Studio

---

## 🏗️ Architecture / Development

### Option 1: Using REST API / SDK
1. Upload sample forms and JSON files to Azure Blob Storage.
2. Generate a **SAS URL** for the container.
3. Call the **Build model** API with the SAS URL.
4. Retrieve the **model ID** using the **Get model** API.

### Option 2: Using Document Intelligence Studio
1. Upload and label documents directly in the Studio.
2. Choose between:
   - **Custom template model**: Fast training, supports 100+ languages.
   - **Custom neural model**: Best for complex layouts and language-rich documents.

---

## ✅ Best Practices / Considerations
- Use **custom template models** for structured forms with consistent layouts.
- Use **custom neural models** for documents with variable structure or rich language content.
- Ensure accurate labeling in `labels.json` to improve model performance.
- Use **Document Intelligence Studio** for a visual and guided training experience.

---

## ❓ Sample Exam Questions

**Q1.** You need to extract labeled fields from semi-structured documents. Which model type should you use?  
- A. Prebuilt model  
- B. Custom template model  
- ✅ C. Custom neural model  
- D. Layout model

**Q2.** Which file describes the fields you want to extract in a custom model training setup?  
- A. `ocr.json`  
- ✅ B. `fields.json`  
- C. `labels.json`  
- D. `model.json`

**Q3.** What is required to initiate training using the Build model API?  
- A. Azure Key Vault  
- ✅ B. SAS URL to a blob container  
- C. Azure SQL Database  
- D. Azure Kubernetes Service

# 📄 Use Azure Document Intelligence Models

## 🟠 Problem
You have trained a custom model using Azure Document Intelligence and now need to extract structured data from new documents using that model.  
How do you use the model to analyze documents and retrieve the extracted content?

## 🟢 Solution with Azure
Use the **Analyze Document** function from the Azure Document Intelligence **REST API** or **SDK**, providing the **model ID** obtained during training.  
This function initiates the analysis and returns structured data in JSON format.

## 🧩 Required Components
- Azure Document Intelligence endpoint and API key
- Custom model ID
- Document URL (publicly accessible or via SAS)
- SDK (e.g., C#, Python) or REST API

 
```python

endpoint = "YOUR_DOC_INTELLIGENCE_ENDPOINT"
key = "YOUR_DOC_INTELLIGENCE_KEY"

model_id = "YOUR_CUSTOM_BUILT_MODEL_ID"
formUrl = "YOUR_DOCUMENT"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze
task = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
result = task.result()
```
A successful JSON response contains analyzeResult that contains the content extracted and an array of pages containing information about the document content.

Example analyze document JSON response:

```python
{
	"status": "succeeded",
	"createdDateTime": "2023-10-18T23:39:50Z",
	"lastUpdatedDateTime": "2023-10-18T23:39:54Z",
	"analyzeResult": {
		"apiVersion": "2022-08-31",
		"modelId": "DocIntelModel",
		"stringIndexType": "utf16CodeUnit",
		"content": "Purchase Order\nHero Limited\nCompany Phone: 555-348-6512 Website: www.herolimited.com Email: accounts@herolimited.com\nPurchase Order\nDated As: 12/20/2020 Purchase Order #: 948284\nShipped To Vendor Name: Balozi Khamisi Company Name: Higgly Wiggly Books Address: 938 NE Burner Road Boulder City, CO 92848 Phone: 938-294-2949\nShipped From Name: Kidane Tsehaye Company Name: Jupiter Book Supply Address: 383 N Kinnick Road Seattle, WA 38383\nPhone: 932-299-0292\nDetails\nQuantity\nUnit Price\nTotal\nBindings\n20\n1.00\n20.00\nCovers Small\n20\n1.00\n20.00\nFeather Bookmark\n20\n5.00\n100.00\nCopper Swirl Marker\n20\n5.00\n100.00\nSUBTOTAL\n$140.00\nTAX\n$4.00\nTOTAL\n$144.00\nKidane Tsehaye\nManager\nKidane Tsehaye\nAdditional Notes: Do not Jostle Box. Unpack carefully. Enjoy. Jupiter Book Supply will refund you 50% per book if returned within 60 days of reading and offer you 25% off you next total purchase.",
		"pages": [
			{
				"pageNumber": 1,
				"angle": 0,
				"width": 1159,
				"height": 1486,
				"unit": "pixel",
				"words": [
					{
						"content": "Purchase",
						"polygon": [
							89,
							90,
							174,
							91,
							174,
							112,
							88,
							112
						],
						"confidence": 0.996,
						"span": {
							"offset": 0,
							"length": 8
						}
					},
					{
						"content": "Order",
						"polygon": [
							178,
							91,
							237,
							91,
							236,
							113,
							178,
							112
						],
						"confidence": 0.997,
						"span": {
							"offset": 9,
							"length": 5
						}
					},
                    ...
                    {
						"content": "Email",
						"polygon": [
							89,
							90,
							174,
							91,
							174,
							112,
							88,
							112
						],
						"confidence": 0.996,
						"span": {
							"offset": 0,
							"length": 8
						}
					}
``` 
## Understanding confidence scores
If the confidence values of the analyzeResult are low, try to improve the quality of your input documents.

You want to make sure that the form you're analyzing has a similar appearance to forms in the training set if the confidence values are low. If the form appearance varies, consider training more than one model, with each model focused on one form format.

Depending on the use case, you might find that a confidence score of 80% or higher is acceptable for a low-risk application. For more sensitive cases, like reading medical records or billing statements, a score of 100% is recommended.

## 🧠 Use Azure Document Intelligence Studio

### 🟠 Problem
You need to extract structured data (text, tables, key-value pairs, entities) from documents such as forms, receipts, or IDs, and possibly train custom models for specific document types.

### 🟢 Solution with Azure
Use **Azure Document Intelligence Studio**, a visual interface for exploring and integrating Azure Document Intelligence capabilities. It supports document analysis, prebuilt models, and custom model training.

### 🧩 Required Components
- Azure Document Intelligence or Azure AI Services resource
- Azure Storage account (for custom models)
- Azure Document Intelligence Studio (web interface)
- Endpoint and key for the Azure resource
- Sample documents (PDF, TIFF, JPG, PNG, BMP)

### 🏗️ Architecture / Development

#### Document Analysis Models
- **Read**: Extracts printed/handwritten text, locations, and languages.
- **Layout**: Extracts text, tables, selection marks, and structure.
- **General Documents**: Extracts key-value pairs, selection marks, and entities.

Steps:
1. Create Azure Document Intelligence or AI Services resource.
2. Choose a model type (Read, Layout, General Documents).
3. Analyze documents using endpoint and key.

#### Prebuilt Models
- Extract data from common forms (e.g., invoices, receipts, IDs, health insurance, business cards).
- Steps:
  1. Create Azure resource.
  2. Select a prebuilt model.
  3. Analyze document using endpoint and key.

#### Custom Models
- Train models using labeled data.
- Steps:
  1. Create Azure resource and storage account.
  2. Upload 5–6 sample forms to a container.
  3. Configure CORS on the storage account.
  4. Create a custom model project in the Studio.
  5. Label data using the Studio.
  6. Train the model (receive Model ID and accuracy).
  7. Test the model with new documents.

### ✅ Best Practices / Considerations
- Ensure CORS is configured correctly for custom model training.
- Use diverse and representative samples for training.
- Store training files in a structured format (ocr.json, labels.json, fields.json).
- Use the Studio for visual feedback and model evaluation.

### ❓ Exam-style Questions

**Q1:** What are the three main project types supported by Azure Document Intelligence Studio?  
**A1:** Document analysis models, prebuilt models, and custom models.

**Q2:** What is required to train a custom model in Azure Document Intelligence Studio?  
**A2:** Azure resource, storage account with sample forms, CORS configuration, labeled data, and Studio project setup.

**Q3:** Which model type would you use to extract key-value pairs and entities from a general document?  
**A3:** General Documents under Document Analysis Models.

**Q4:** What file types are supported for document analysis in the Studio?  
**A4:** PDF, TIFF, JPG, PNG, BMP.

**Q5:** What information do you need to analyze a document using the Studio?  
**A5:** Azure endpoint and key for the Document Intelligence or AI Services resource.

