## 🧠 Extract Data from Forms

### 🟠 Problem
A company currently requires employees to manually fill out purchase order sheets and enter the data into a database. They want to improve the data entry process using AI services.

### 🟢 Solution with Azure
Build a machine learning model using **Azure AI Document Intelligence** to read forms and produce structured data that can be used to automatically update a database.

Azure AI Document Intelligence is an Azure AI service that enables users to build automated data processing software. This software can extract text, key/value pairs, and tables from form documents using optical character recognition (OCR). Azure AI Document Intelligence has pre-built models for recognizing invoices, receipts, and business cards. The service also provides the capability to train custom models.

In this exercise, we will focus on building custom models.

### 🧩 Required Components
- Azure AI Document Intelligence or Azure AI Services resource
- Visual Studio Code
- GitHub repository: mslearn-ai-document-intelligence
- Azure subscription
- Resource group
- Storage account (optional for advanced scenarios)

### 🏗️ Architecture / Development

#### Prepare to develop an app in Visual Studio Code
1. Start Visual Studio Code.
2. Open the palette (`SHIFT+CTRL+P`) and run `Git: Clone`.
3. Clone the repository:  
   `https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence`
4. Open the cloned folder in Visual Studio Code.

> 💡 Tip: If prompted, click **Yes, I trust the authors**.

> ⚠️ Notes:
> - Wait while additional files are installed to support the C# code projects.
> - If prompted to add required assets to build and debug, select **Not Now**.
> - If prompted with the message *Detected an Azure Function Project*, you can safely close it.

#### Create an Azure AI Document Intelligence resource
1. Open the [Azure portal](https://n.
2. In the top search box, type **Document Intelligence** and press Enter.
3. On the Document Intelligence page, select **Create**.
4. On the Create page, configure the resource:
   - **Subscription**: Your Azure subscription
   - **Resource group**: Create or select one (e.g., `DocIntelligenceResources`)
   - **Region**: Choose a region near you
   - **Name**: Enter a globally unique name
   - **Pricing tier**: Select **Free F0** (or **Standard S0** if F0 is unavailable)
5. Select **Review + create**, then **Create**.
6. When deployment is complete, select **Go to resource** to view the Overview page.

### ✅ Best Practices / Considerations
- Use representative sample forms for training custom models.
- Use the SDK and Visual Studio Code for full control over development.
- Trust the workspace in VS Code to enable full functionality.
- Choose the Free tier for testing and development to minimize cost.

## Gather documents for training
You’ll use the sample forms such as this one to train a test a model:

> An image of an invoice used in this project.

1. Return to Visual Studio Code. In the Explorer pane, open the `Labfiles/02-custom-document-intelligence` folder and expand the `sample-forms` folder. Notice there are files ending in `.json` and `.jpg` in the folder.

You will use the `.jpg` files to train your model.

The `.json` files have been generated for you and contain label information. The files will be uploaded into your blob storage container alongside the forms.

You can view the images we are using in the `sample-forms` folder by selecting them on Visual Studio Code.

2. Return to the Azure portal and navigate to your resource’s Overview page if you’re not already there. Under the Essentials section, view the Resource group in which you created the Document Intelligence resource.

3. On the Overview page for your resource group, note the Subscription ID and Location. You will need these values, along with your resource group name in subsequent steps.

> An example of the resource group page.

4. In Visual Studio Code, in the Explorer pane, browse to the `Labfiles/02-custom-document-intelligence` folder and expand the `CSharp` or `Python` folder depending on your language preference. Each folder contains the language-specific files for an app into which you’re you’re going to integrate Azure OpenAI functionality.

5. Right-click the `CSharp` or `Python` folder containing your code files and select **Open an integrated terminal**.

6. In the terminal, run the following command to login to Azure. The `az login` command will open the Microsoft Edge browser, login with the same account you used to create the Azure AI Document Intelligence resource. Once you are logged in, close the browser window.

```bash
az login
```
7. Return to Visual Studio Code. In the terminal pane, run the following command to list the Azure locations.

```bash
az account list-locations -o table
```
8. In the output, find the Name value that corresponds with the location of your resource group (for example, for East US the corresponding name is `eastus`).
### Important: Record the Name value and use it in Step 11.

9. In Visual Studio Code, in the Labfiles/02-custom-document-intelligence folder, select setup.cmd. You will use this script to run the Azure command line interface (CLI) commands required to create the other Azure resources you need.

10. In the setup.cmd script, review the commands. The program will:
   - Create a storage account in your Azure resource group
   - Upload files from your local sampleforms folder to a container called sampleforms in the storage account
   - Print a Shared Access Signature URI
11. Modify the subscription_id, resource_group, and location variable declarations with the appropriate values for the subscription, resource group, and location name where you deployed the Document Intelligence resource. Then save your changes.

Leave the expiry_date variable as it is for the exercise. This variable is used when generating the Shared Access Signature (SAS) URI. In practice, you will want to set an appropriate expiry date for your SAS. You can learn more about SAS here.

12. In the terminal for the Labfiles/02-custom-document-intelligence folder, enter the following command to run the script:
```bash 
$currentdir=(Get-Item .).FullName
 cd ..
 ./setup.cmd
 cd $currentdir

```
13. When the script completes, review the displayed output.

14. In the Azure portal, refresh your resource group and verify that it contains the Azure Storage account just created. Open the storage account and in the pane on the left, select Storage browser. Then in Storage Browser, expand Blob containers and select the sampleforms container to verify that the files have been uploaded from your local 02-custom-document-intelligence/sample-forms folder.

## Train the model using Document Intelligence Studio

Now you will train the model using the files uploaded to the storage account.

1. In your browser, navigate to the Document Intelligence Studio at https://documentintelligence.ai.azure.com/studio.  
2. Scroll down to the Custom models section and select the Custom extraction model tile.  
3. If you are asked to sign into your account, use your Azure credentials.  
4. If you are asked which Azure AI Document Intelligence resource to use, select the subscription and resource name you used when you created the Azure AI Document Intelligence resource.

5. Under My Projects, select Create a project. Use the following configurations:

- **Project name**: Enter a unique name.
- Select **Continue**.

**Configure service resource**:  
- Select the subscription, resource group, and document intelligence resource you created previously in this lab.  
- Check the **Set as default** box.  
- Keep the default API version.  
   -  Select **Continue**.

**Connect training data source**:  
- Select the subscription, resource group, and storage account that was created by the setup script.  
- Check the **Set as default** box.  
- Select the `sampleforms` blob container, and leave the folder path blank.  
   - Select **Continue**.

- Select **Create project**.

6. Once your project is created, on the top right of the screen, select **Train** to train your model. Use the following configurations:

- **Model ID**: Provide a globally unique name (you’ll need the model ID name in the next step).
- **Build Mode**: Template.

7. Select **Go to Models**.

8. Training can take some time. You’ll see a notification when it’s complete.

## Test your custom Document Intelligence model

1. Return to Visual Studio Code. In the terminal, install the Document Intelligence package by running the appropriate command for your language preference:

```bash
pip install azure-ai-formrecognizer==3.3.3
```
2. In Visual Studio Code, in the Labfiles/02-custom-document-intelligence folder, select the language you are using. Edit the configuration file (appsettings.json or .env, depending on your language preference) with the following values:
   - Your Document Intelligence endpoint.
   - Your Document Intelligence key.
   - The Model ID you provided when training your model. You can find this on the Models page of the Document Intelligence Studio. Save your changes.
3. In Visual Studio Code, open the code file for your client application (Program.cs for C#, test-model.py for Python) and review the code it contains, particularly that the image in the URL refers to the file in this GitHub repo on the web.

4. Return the terminal, and enter the following command to run the program:
```bash
 python test-model.py
```
5. View the output and observe how the output for the model provides field names like Merchant and CompanyPhoneNumber.

## Clean up
If you’re done with your Azure resource, remember to delete the resource in the Azure portal to avoid further charges.

## More information
For more information about the Document Intelligence service, see the Document Intelligence documentation.