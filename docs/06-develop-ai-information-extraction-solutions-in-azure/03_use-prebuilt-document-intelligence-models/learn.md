# Understand Prebuilt Models

## Problem
You need to extract structured data such as names, addresses, and amounts from common documents like invoices, receipts, and unstructured forms. How can you do this efficiently without training custom models?

## Solution with Azure
Use **prebuilt models** in **Azure AI Document Intelligence**. These models are trained by Microsoft on large datasets and are optimized for extracting information from common document types without requiring custom training.

## Required Components
- **Azure AI Document Intelligence**
- **Prebuilt models** (e.g., Invoice, Receipt, ID Document, etc.)
- **Client application** or **Azure portal** for testing and integration

## Architecture / Development

### What Are Prebuilt Models?
Prebuilt models are trained on large corpora of specific document types and are ready to use. They eliminate the need for manual training and are optimized for accuracy and reliability.

### Available Prebuilt Models:
- **Invoice model**: Extracts fields from invoices.
- **Receipt model**: Extracts fields from receipts.
- **US Tax model**: Extracts data from W-2, 1098, 1099, 1040 forms.
- **ID document model**: Extracts fields from US, EU, and international IDs.
- **Business card model**: Extracts contact details from business cards.
- **Health insurance card model**: Extracts fields from insurance cards.
- **Marriage certificate model**: Extracts data from marriage certificates.
- **Credit/Debit card model**: Extracts card information.
- **Mortgage documents model**: Extracts data from forms like 1003, 1004, 1005, 1008.
- **Bank statement model**: Extracts balances and transactions.
- **Pay Stub model**: Extracts wages, deductions, net pay, etc.
- **Check model**: Extracts payee, amount, date, etc.

### General Models:
- **Read model**: Extracts text and language.
- **General document model**: Extracts text, keys, values, entities, and selection marks.
- **Layout model**: Extracts text and structural layout.

## Best Practices / Considerations
- Use prebuilt models when working with standard document types to save time and effort.
- Evaluate the model output to ensure it meets your accuracy requirements.
- Combine general models with custom logic for unstructured or less common documents.

## Exam-like Questions
1. What is the main advantage of using prebuilt models in Azure AI Document Intelligence?
2. Which model would you use to extract data from a US W-2 tax form?
3. What types of documents are supported by the general document model?
4. How do prebuilt models differ from custom-trained models?
5. Which model should be used to extract contact details from business cards?


# Features of Prebuilt Models

## Problem
You need to extract various types of structured data from documents and forms using Azure AI. How do you choose the right prebuilt model and ensure accurate results?

## Solution with Azure
Use **prebuilt models** in **Azure AI Document Intelligence**, which are designed to extract specific types of data such as text, key-value pairs, entities, selection marks, tables, and fields from common document types.

## Required Components
- **Azure AI Document Intelligence**
- **Prebuilt models** (e.g., Invoice, Receipt, Business Card, etc.)
- **Supported input files** (JPEG, PNG, BMP, TIFF, PDF, Office files for Read model)
- **Azure AI Document Intelligence Studio** (for visual testing)

## Architecture / Development

### Features of Prebuilt Models
- **Text extraction**: Extracts printed and handwritten text.
- **Key-value pairs**: Identifies labels and their corresponding values (e.g., `Weight: 31 kg`).
- **Entities**: Extracts structured data like names, locations, and dates.
- **Selection marks**: Detects checkboxes and radio buttons.
- **Tables**: Extracts table structures, including merged cells and headers.
- **Fields**: Extracts predefined fields for specific document types (e.g., `CustomerName`, `InvoiceTotal`).

### Input Requirements
- **File formats**: JPEG, PNG, BMP, TIFF, PDF (Office files for Read model)
- **File size**:
  - Standard tier: up to 500 MB
  - Free tier: up to 4 MB
- **Image dimensions**: Between 50x50 and 10,000x10,000 pixels
- **PDF dimensions**: Less than 17x17 inches or A3 size
- **PDFs must not be password-protected**
- **Page limits**:
  - Standard tier: first 2,000 pages
  - Free tier: first 2 pages

> Note: Use text-embedded PDFs when possible to improve OCR accuracy.

### Try Out Prebuilt Models
Use **Azure AI Document Intelligence Studio** to:
- Explore prebuilt models visually
- Analyze sample or custom documents
- Understand model behavior before coding

## Best Practices / Considerations
- Choose the model that best matches your document type.
- Use high-quality scans or clear photos for better accuracy.
- Use prebuilt models for common forms; use custom models for industry-specific documents.
- Validate model output before integrating into production workflows.

## Exam-like Questions
1. What types of data can prebuilt models extract from documents?
2. What are the input format and size requirements for prebuilt models?
3. When should you consider using a custom model instead of a prebuilt one?
4. What is the benefit of using text-embedded PDFs?
5. How can you visually test prebuilt models before integrating them into your application?


# Calling Prebuilt Models by Using APIs

## Problem
You want to integrate Azure AI Document Intelligence into your application to analyze documents using prebuilt models. How can you authenticate and call the service efficiently using APIs?

## Solution with Azure
Use the **Azure AI Document Intelligence SDKs** or **RESTful APIs** to connect to the service, authenticate using your endpoint and API key, and submit documents for analysis using prebuilt models.

## Required Components
- **Azure AI Document Intelligence resource**
- **Service endpoint** (from Azure portal)
- **API key** (from Azure portal)
- **Programming language SDK** (Python, C#, Java, JavaScript)

## Architecture / Development

### Supported Languages
- C# and other .NET languages
- Java
- Python
- JavaScript

### Authentication
To connect to the service, you need:
- **Service endpoint**: URL where the service is hosted
- **API key**: Grants access to the service

### Asynchronous Call Example (Python)
Use asynchronous calls to handle potentially long-running operations:

```python
poller = document_analysis_client.begin_analyze_document(
    "prebuilt-layout", AnalyzeDocumentRequest(url_source=docUrl)
)
result: AnalyzeResult = poller.result()
```
The details you can extract from these results depend on the model you used.

# Use the General Document, Read, and Layout Models

## Problem
You need to extract text, structure, and entities from documents with unpredictable formats such as specifications, tenders, and statements of work. How can Azure AI Document Intelligence help analyze these documents?

## Solution with Azure
Use the **Read**, **General Document**, and **Layout** prebuilt models in **Azure AI Document Intelligence** to extract text, key-value pairs, entities, selection marks, and tables from documents with varying structures.

## Required Components
- **Azure AI Document Intelligence**
- **Prebuilt models**:
  - `prebuilt-read`
  - `prebuilt-document`
  - `prebuilt-layout`
- **Supported input files** (PDF, TIFF, images)

## Architecture / Development

### Read Model
- Extracts printed and handwritten text.
- Detects language and classifies text as printed or handwritten.
- Supports multi-page PDFs and TIFFs with `pages` parameter.
- Ideal for documents with no predictable structure.

### General Document Model
- Extends the Read model.
- Extracts:
  - Key-value pairs
  - Entities (e.g., Person, Organization, DateTime, Address, etc.)
  - Selection marks
  - Tables
- Supports structured, semi-structured, and unstructured documents.
- Only prebuilt model that supports **entity extraction**.

#### Entity Types Supported:
- **Person**: Names
- **PersonType**: Job titles
- **Location**: Places, geopolitical entities
- **Organization**: Companies, groups
- **Event**: Gatherings, anniversaries
- **Product**: Goods
- **Skill**: Capabilities
- **Address**: Mailing addresses
- **Phone number**, **Email**, **URL**, **IP Address**
- **DateTime**, **Quantity**

### Layout Model
- Extracts:
  - Text
  - Selection marks
  - Tables
- Handles:
  - Skewed scans
  - Complex table structures
  - Merged cells
- Table cell output includes:
  - Text content
  - Bounding box
  - Header status
  - Row and column indices
- Selection marks include:
  - Bounding box
  - Confidence score
  - Selection status

## Best Practices / Considerations
- Use the **Read model** for basic OCR tasks.
- Use the **General Document model** for rich extraction including entities.
- Use the **Layout model** when document structure is important.
- Choose the model based on the complexity and structure of your documents.

## Exam-like Questions
1. What is the main difference between the Read and General Document models?
2. Which model supports entity extraction?
3. What types of entities can the General Document model extract?
4. When should you use the Layout model over the Read model?
5. How does the Layout model handle complex table structures?


# Use Financial, ID, and Tax Models

## Problem
You need to extract structured data from financial documents (invoices, receipts), identity documents, and business cards. How can Azure AI Document Intelligence help automate this process, especially when documents are scanned or photographed in poor conditions?

## Solution with Azure
Use **prebuilt models** in **Azure AI Document Intelligence** that are trained to extract common fields from financial, identity, and tax documents. These models are optimized for real-world conditions such as creased paper and skewed scans.

## Required Components
- **Azure AI Document Intelligence**
- **Prebuilt models**:
  - `prebuilt-invoice`
  - `prebuilt-receipt`
  - `prebuilt-idDocument`
  - `prebuilt-businessCard`

## Architecture / Development

### Invoice Model
Extracts fields from various invoice formats, even if scanned poorly:
- Customer name, reference ID
- Purchase order number
- Invoice and due dates
- Vendor and customer details (name, tax ID, address)
- Billing and shipping addresses
- Amounts: total tax, invoice total, amount due
- Line items:
  - Description, product code
  - Unit price, quantity, tax, line total

### Receipt Model
Extracts fields from receipts, including:
- Merchant name, phone number, address
- Receipt total, tax, tip
- Transaction date and time
- Line items:
  - Item name, quantity, unit price, total price

> Note: From v3.0, supports hotel receipts with fields like arrival and departure dates.

### ID Document Model
Supports:
- US driver’s licenses
- International passports (biographical page only)

Extracted fields:
- First and last names
- Sex, date of birth, nationality
- Issuing country/region
- Document number, MRZ
- Endorsements, restrictions, vehicle classifications

> Important: Handle personal data in compliance with data protection laws.

### Business Card Model
Extracts contact information from business cards:
- First and last names
- Postal addresses
- Email and website addresses
- Phone numbers

### Other Prebuilt Models
Microsoft regularly releases new prebuilt models. Before training a custom model, check if a prebuilt model meets your needs. Benefits include:
- Rigorous testing
- Regular updates
- Lower cost

## Best Practices / Considerations
- Use prebuilt models for common document types to save time and cost.
- Validate model output for accuracy.
- Ensure compliance with data privacy regulations when handling personal data.
- Use high-quality scans or photos for best results.

## Exam-like Questions
1. What types of documents are supported by the invoice and receipt models?
2. What additional fields does the receipt model extract for hotel receipts?
3. Which identity documents are supported by the ID document model?
4. What kind of information can be extracted from business cards?
5. Why should you consider using a prebuilt model before training a custom one?
