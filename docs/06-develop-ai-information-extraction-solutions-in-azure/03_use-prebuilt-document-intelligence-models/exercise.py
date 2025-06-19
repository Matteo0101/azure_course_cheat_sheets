"""
Use prebuilt Document Intelligence models
In this exercise, you’ll set up an Azure AI Document Intelligence resource in your Azure subscription. You’ll use both the Azure AI Document Intelligence Studio and C# or Python to submit forms to that resource for analysis.

Create an Azure AI Document Intelligence resource
Before you can call the Azure AI Document Intelligence service, you must create a resource to host that service in Azure:

In a browser tab, open the Azure portal at https://portal.azure.com, signing in with the Microsoft account associated with your Azure subscription.
On the Azure portal home page, navigate to the top search box and type Document Intelligence and then press Enter.
On the Document Intelligence page, select Create Document Intelligence.
On the Create Document Intelligence page, use the following to configure your resource:
Subscription: Your Azure subscription.
Resource group: Select or create a resource group with a unique name such as DocIntelligenceResources.
Region: select a region near you.
Name: Enter a globally unique name.
Pricing tier: select Free F0 (if you don’t have a Free tier available, select Standard S0).
Then select Review + create, and Create. Wait while Azure creates the Azure AI Document Intelligence resource.
When the deployment is complete, select Go to resource. Keep this page open for the rest of this exercise.
Use the Read model
Let’s start by using the Azure AI Document Intelligence Studio and the Read model to analyze a document with multiple languages. You’ll connect Azure AI Document Intelligence Studio to the resource you just created to perform the analysis:

Open a new browser tab and go to the Azure AI Document Intelligence Studio at https://documentintelligence.ai.azure.com/studio.
Under Document Analysis, select the Read tile.
If you are asked to sign into your account, use your Azure credentials.
If you are asked which Azure AI Document Intelligence resource to use, select the subscription and resource name you used when you created the Azure AI Document Intelligence resource.
In the list of documents on the left, select read-german.pdf.

Screenshot showing the Read page in Azure AI Document Intelligence Studio.

At the top-left, select Analyze options, then enable the Language check-box (under Optional detection) in the Analyze options pane and click on Save.
At the top-left, select Run Analysis.
When the analysis is complete, the text extracted from the image is shown on the right in the Content tab. Review this text and compare it to the text in the original image for accuracy.
Select the Result tab. This tab displays the extracted JSON code.
Scroll to the bottom of the JSON code in the Result tab. Notice that the read model has detected the language of each span indicated by locale. Most spans are in German (language code de) but you can find other language codes in the spans (e.g. English - language code en - in one of the last span).

Screenshot showing the detection of language for two spans in the results from the read model in Azure AI Document Intelligence Studio.

"""



# In integrated terminal, run:
"pip install azure-ai-formrecognizer==3.3.3"

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

# Store connection information
endpoint = "<Endpoint URL>"
key = "<API Key>"

fileUri = "https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence/blob/main/Labfiles/01-prebuild-models/sample-invoice/sample-invoice.pdf?raw=true"
fileLocale = "en-US"
fileModelId = "prebuilt-invoice"

print(f"\nConnecting to Forms Recognizer at: {endpoint}")
print(f"Analyzing invoice at: {fileUri}")

# Create the client
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)
# Analyse the invoice
poller = document_analysis_client.begin_analyze_document_from_url(
    fileModelId, fileUri, locale=fileLocale
)
# Display invoice information to the user
receipts = poller.result()
    
for idx, receipt in enumerate(receipts.documents):
    
    vendor_name = receipt.fields.get("VendorName")
    if vendor_name:
        print(f"\nVendor Name: {vendor_name.value}, with confidence {vendor_name.confidence}.")

    customer_name = receipt.fields.get("CustomerName")
    if customer_name:
        print(f"Customer Name: '{customer_name.value}, with confidence {customer_name.confidence}.")


    invoice_total = receipt.fields.get("InvoiceTotal")
    if invoice_total:
        print(f"Invoice Total: '{invoice_total.value.symbol}{invoice_total.value.amount}, with confidence {invoice_total.confidence}.")

print("\nAnalysis complete.\n")

