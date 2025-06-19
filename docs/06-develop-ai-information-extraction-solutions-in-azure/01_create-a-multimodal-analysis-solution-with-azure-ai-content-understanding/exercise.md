# Extract information from multimodal content

In this exercise, you use Azure Content Understanding to extract information from a variety of content types; including an invoice, an images of a slide containing charts, an audio recording of a voice messages, and a video recording of a conference call.

This exercise takes approximately 40 minutes.

## Create an Azure AI Foundry hub and project

The features of Azure AI Foundry we’re going to use in this exercise require a project that is based on an Azure AI Foundry hub resource.

In a web browser, open the Azure AI Foundry portal at https://ai.azure.com and sign in using your Azure credentials. Close any tips or quick start panes that are opened the first time you sign in, and if necessary use the Azure AI Foundry logo at the top left to navigate to the home page, which looks similar to the following image (close the Help pane if it’s open):

Screenshot of Azure AI Foundry portal.

In the browser, navigate to https://ai.azure.com/managementCenter/allResources and select Create. Then choose the option to create a new AI hub resource.  
In the Create a project wizard, enter a valid name for your project, and use the Rename hub link to specify a valid name for your new hub. Then expand Advanced options and specify the following settings for your project:  
Subscription: Your Azure subscription  
Resource group: Create or select a resource group  
Region: Select one of the following locations (At the time of writing, Azure AI Content understanding is only available in these regions):  
- Australia East  
- Sweden Central  
- West US  

> Note: If you’re working in an Azure subscription in which policies are used to restrict allowable resource names, you may need to use the link at the bottom of the Create a new project dialog box to create the hub using the Azure portal.

> Tip: If the Create button is still disabled, be sure to rename your hub to a unique alphanumeric value.

Wait for your project to be created.

## Download content

The content you’re going to analyze is in a .zip archive. Download it and extract it in a local folder.

In a new browser tab, download content.zip from https://github.com/microsoftlearning/mslearn-ai-information-extraction/raw/main/Labfiles/content/content.zip and save it in a local folder.  
Extract the downloaded content.zip file and view the files it contains. You’ll use these files to build various Content Understanding analyzers in this exercise.

> Note: If you’re only interested in exploring analysis of a specific modality (documents, images, video, or audio), you can skip to the relevant task below. For the best experience, go through each task to learn how to extract information from different types of content.

## Extract information from invoice documents

You are going to build an Azure AI Content Understanding analyzer that can extract information from invoices. You’ll start by defining a schema based on a sample invoice.

### Define a schema for invoice analysis

In the browser tab containing the home page for your Azure AI Foundry project; in the navigation pane on the left, select Content Understanding.  
On the Content Understanding page, select the Custom task tab at the top.  
On the Content Understanding custom task page, select + Create, and create a task with the following settings:  
- Task name: Invoice analysis  
- Description: Extract data from an invoice  
- Single file content analysis: Selected  
- Advanced settings:  
  - Azure AI services connection: The Azure AI Services resource in your Azure AI Foundry hub  
  - Azure Blob Storage account: The default storage account in your Azure AI Foundry hub  

Wait for the task to be created.

> Tip: If an error accessing storage occurs, wait a minute and try again. Permissions for a new hub may take a few minutes to propagate.

On the Define schema page, upload the invoice-1234.pdf file from the folder where you extracted content files. This file contains the following invoice:

Image of an invoice number 1234.

On the Define schema page, after uploading the invoice file, select the Invoice data extraction template and select Create.

The Invoice analysis template includes common fields that are found in invoices. You can use the schema editor to delete any of the suggested fields that you don’t need, and add any custom fields that you do.

In the list of suggested fields, select BillingAddress. This field is not needed for the invoice format you have uploaded, so use the Delete field (🗑) icon that appears in the selected field row to delete it.  
Now delete the following suggested fields, which aren’t needed for your invoice schema:  
- BillingAddressRecipient  
- CustomerAddressRecipient  
- CustomerId  
- CustomerTaxId  
- DueDate  
- InvoiceTotal  
- PaymentTerm  
- PreviousUnpaidBalance  
- PurchaseOrder  
- RemittanceAddress  
- RemittanceAddressRecipient  
- ServiceAddress  
- ServiceAddressRecipient  
- ShippingAddress  
- ShippingAddressRecipient  
- TotalDiscount  
- VendorAddressRecipient  
- VendorTaxId  
- TaxDetails  

Use + Add new field button to add the following fields, selecting Save changes (✓) for each new field:

| Field name   | Field description         | Value type | Method  |
|--------------|---------------------------|------------|---------|
| VendorPhone  | Vendor telephone number   | String     | Extract |
| ShippingFee  | Fee for shipping          | Number     | Extract |

In the row for the Items field, note that this field is a table (it contains the collection of items in the invoice). Select it’s Edit (▦) icon to open a new page with its subfields.  
Remove the following subfields from the Items table:  
- Date  
- ProductCode  
- Unit  
- TaxAmount  
- TaxRate  

Use the OK button to confirm the changes and return to the top-level of the invoice schema.

Verify that your completed schema looks like this, and select Save.

Screenshot of a schema for an invoice.

On the Test Analyzer page, if analysis does not begin automatically, select Run analysis. Then wait for analysis to complete.

Review the analysis results, which should look similar to this:

Screenshot of invoice analysis test results.

View the details of the fields that were identified in the Fields pane.

### Build and test an analyzer for invoices

Now that you have trained a model to extract fields from invoices, you can build an analyzer to use with similar documents.

Select the Analyzer list page, and then select + Build analyzer and build a new analyzer with the following properties (typed exactly as shown here):  
- Name: invoice-analyzer  
- Description: Invoice analyzer  

Wait for the new analyzer to be ready (use the Refresh button to check).  
When the analyzer has been built, select the invoice-analyzer link. The fields defined in the analyzer’s schema will be displayed.  
In the invoice-analyzer page, select the Test tab.  
Use the + Upload test files button to upload invoice-1235.pdf from the folder where you extracted the content files, and run the analysis to extract field data from the invoice.

The invoice being analyzed looks like this:

Image of an invoice number 1235.

Review the Fields pane, and verify that the analyzer extracted the correct fields from the test invoice.  
Review the Results pane to see the JSON response that the analyzer would return to a client application.  
On the Code example tab, view the sample code that you could use to develop a client application that uses the Content Understanding REST interface to call your analyzer.  
Close the invoice-analyzer page.
