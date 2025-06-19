# Azure AI Content Understanding

## Problem
You need to extract structured insights and data from various types of unstructured content (documents, images, audio, video) to automate and optimize business processes.

## Solution with Azure
Use **Azure AI Content Understanding**, a generative AI service within Azure AI Services, to analyze multimodal content and generate actionable outputs. It supports consistent development across content types and can be accessed via the Azure AI Foundry portal or REST API.

## Required Components
- **Azure AI Services resource** (provisioned in your Azure subscription)
- **Azure AI Foundry portal** or **Content Understanding REST API**

## Architecture / Development
- **Documents and Forms**: Extract specific field values (e.g., invoice data for payment automation).
- **Images**: Analyze visuals to detect objects, defects, or infer information (e.g., charts, people).
- **Audio**: Summarize calls, detect sentiment, or extract key data from recordings.
- **Video**: Extract insights from recordings (e.g., summarize meetings, detect activities in surveillance footage).

## Best Practices / Considerations
- Use a **single service** for multimodal content to streamline development.
- Ensure proper **resource provisioning** and **API integration** for scalable deployment.
- Choose the appropriate **content type pipeline** (document, image, audio, video) based on your scenario.

## Sample Exam Questions
1. **You need to extract key data from scanned invoices and automate payment processing. Which Azure service should you use?**
   - A. Azure AI Vision  
   - B. Azure AI Content Understanding  
   - C. Azure Form Recognizer  
   - D. Azure Cognitive Search  
   **→ Correct Answer: B**

2. **Which of the following content types can be analyzed using Azure AI Content Understanding? (Select all that apply)**
   - A. Documents  
   - B. Images  
   - C. Audio  
   - D. Video  
   **→ Correct Answers: A, B, C, D**


# Create a Content Understanding Analyzer

## Problem
You need to extract structured information from unstructured content (documents, images, audio, or video). How can you build a solution that identifies and extracts specific fields from this content using Azure services?

## Solution with Azure
Use **Azure AI Foundry** to create a **Content Understanding analyzer**. This analyzer is trained using a schema that defines the fields to extract and can be tested and deployed through the Azure AI services resource.

## Required Components
- **Azure AI Services resource**
- **Azure AI Foundry portal**
- **AI Hub (optional, for project organization)**
- **Schema editor**
- **Analyzer templates**
- **Storage and Key Vault resources** (provisioned with AI Hub)

## Architecture / Development
1. **Create a Project** in Azure AI Foundry (within an existing or new AI Hub).
2. **Define a Schema**:
   - Upload a sample file (document, image, audio, or video).
   - Apply a schema template.
   - Define fields to extract.
3. **Build the Analyzer**:
   - Use the schema to train the analyzer.
   - Build and publish the analyzer to make it accessible via the Azure AI services endpoint.
4. **Test the Analyzer**:
   - Run analysis on sample or uploaded files.
   - Review extracted fields and JSON output.

> Note: Templates and field types vary by content type. Some types support additional features like barcode or formula extraction.

## Best Practices / Considerations
- Use **minimal training data** with schema-by-example to accelerate development.
- **Explicitly label fields** in sample content to improve accuracy.
- Ensure the **Azure region** supports Content Understanding for your content type.
- Use **named versions** to manage schema iterations and capabilities.

## Exam-like Questions
1. What is the purpose of defining a schema in a Content Understanding project?
2. Which Azure portal is recommended for building Content Understanding solutions?
3. What resources are provisioned when creating an AI Hub in Azure AI Foundry?
4. How can you improve the performance of an analyzer when using minimal training data?
5. What output format is returned by the analyzer to client applications?

# Use the Content Understanding REST API

## Problem
You need to programmatically analyze content using a previously built Content Understanding analyzer. How can your application interact with the analyzer and retrieve results?

## Solution with Azure
Use the **Content Understanding REST API** to submit content to an analyzer and retrieve the results of the analysis asynchronously.

## Required Components
- **Azure AI Services resource**
- **Content Understanding analyzer**
- **Authorization key** (from Azure portal or Azure AI Foundry)
- **Endpoint URL** for the Content Understanding API

## Architecture / Development
1. **Submit Content for Analysis**:
   - Send a `POST` request to the analyzer endpoint:
     ```
     POST {endpoint}/contentunderstanding/analyzers/{analyzer}:analyze?api-version={api version}
     {
       "url": "https://host.com/doc.pdf"
     }
     ```
   - Alternatively, include the binary content of the file in the request.

2. **Receive Operation ID**:
   - The response includes:
     - `Operation-Id`
     - `Operation-Location`
     - Initial `status` (e.g., `NotStarted`)

3. **Poll for Results**:
   - Use a `GET` request with the operation ID to check the status:
     ```
     GET {endpoint}/contentunderstanding/analyzers/{analyzer}/results/{operation-id}?api-version={api version}
     ```
   - Repeat until the status is `Succeeded` or `Failed`.

4. **Retrieve Results**:
   - When complete, the response contains a JSON payload with the extracted data based on the schema.

## Best Practices / Considerations
- Use **Azure AI Foundry API** to programmatically retrieve endpoint and keys.
- Ensure proper **authentication** using the authorization key in the request header.
- Handle **asynchronous operations** by polling the operation status until completion.
- Choose between **URL-based** or **binary content** submission based on your application needs.

## Exam-like Questions
1. What is the purpose of the `Operation-Id` in the Content Understanding REST API?
2. How does a client application retrieve the results of a content analysis?
3. What are two ways to provide content to the analyzer using the REST API?
4. Where can you obtain the endpoint and authorization key for the Content Understanding API?
5. What format is used to return the analysis results from the REST API?
