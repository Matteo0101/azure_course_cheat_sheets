# [Read text in images](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Labs/02-ocr.html)

Optical character recognition (OCR) is a subset of computer vision that deals with reading text in images and documents. The Azure AI Vision Image Analysis service provides an API for reading text, which you’ll explore in this exercise.

This exercise takes approximately 30 minutes.

## Provision an Azure AI Vision resource

If you don’t already have one in your subscription, you’ll need to provision an Azure AI Vision resource.

Note: In this exercise, you’ll use a standalone Computer Vision resource. You can also use Azure AI Vision services in an Azure AI Services multi-service resource, either directly or in an Azure AI Foundry project.

1. Open the Azure portal at https://portal.azure.com, and sign in using your Azure credentials.
2. Select **Create a resource**.
3. In the search bar, search for **Computer Vision**, select **Computer Vision**, and create the resource with the following settings:

    - **Subscription**: Your Azure subscription
    - **Resource group**: Create or select a resource group
    - **Region**: Choose from East US, West US, France Central, Korea Central, North Europe, Southeast Asia, West Europe, or East Asia\*
    - **Name**: A valid name for your Computer Vision resource
    - **Pricing tier**: Free F0

    \*Azure AI Vision 4.0 full feature sets are currently only available in these regions.

4. Select the required checkboxes and create the resource.
5. Wait for deployment to complete, and then view the deployment details.
6. When the resource has been deployed, go to it and under the **Resource management** node in the navigation pane, view its **Keys and Endpoint** page. You will need the endpoint and one of the keys from this page in the next procedure.

## Develop a text extraction app with the Azure AI Vision SDK

In this exercise, you’ll complete a partially implemented client application that uses the Azure AI Vision SDK to extract text from images.

### Prepare the application configuration

1. Clone the GitHub repo containing the code files for this exercise:

    ```bash
    rm -r mslearn-ai-vision -f
    git clone https://github.com/MicrosoftLearning/mslearn-ai-vision
    ```

2. Navigate to the language-specific folder containing the application code files:

    ```bash
    cd mslearn-ai-vision/Labfiles/ocr/python/read-text
    ls -a -l
    ```

    The folder contains application configuration and code files for your app. It also contains an `/images` subfolder, which contains some image files for your app to analyze.

3. Install the Azure AI Vision SDK package and other required packages:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt azure-ai-vision-imageanalysis==1.0.0
    ```

4. Edit the configuration file for your app:

    ```bash
    code .env
    ```

    Update the configuration values it contains to reflect the endpoint and an authentication key for your Computer Vision resource (copied from its **Keys and Endpoint** page in the Azure portal). Save your changes.

### Add code to read text from an image

1. Open the code file for the client application:

    ```bash
    code read-text.py
    ```

2. Find the comment `# import namespaces`, and add the following code to import the namespaces you will need to use the Azure AI Vision SDK:

    ```python
    # import namespaces
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential
    ```

3. In the `Main` function, find the comment `# Authenticate Azure AI Vision client`, and add the following code to create and authenticate an Azure AI Vision Image Analysis client object:

    ```python
    # Authenticate Azure AI Vision client
    cv_client = ImageAnalysisClient(
        endpoint=ai_endpoint,
        credential=AzureKeyCredential(ai_key))
    ```

4. Under the code you just added, find the comment `# Read text in image`, and add the following code to use the Image Analysis client to read the text in the image:

    ```python
    # Read text in image
    with open(image_file, "rb") as f:
        image_data = f.read()
    print (f"\nReading text in {image_file}")

    result = cv_client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.READ])
    ```

5. Find the comment `# Print the text`, and add the following code to print the lines of text that were found and call a function to annotate them in the image:

    ```python
    # Print the text
    if result.read is not None:
        print("\nText:")

        for line in result.read.blocks[0].lines:
            print(f" {line.text}")
        # Annotate the text in the image
        annotate_lines(image_file, result.read)

        # Find individual words in each line
    ```

6. Find the comment `# Find individual words in each line`, and add the following code:

    ```python
    # Find individual words in each line
    print ("\nIndividual words:")
    for line in result.read.blocks[0].lines:
        for word in line.words:
            print(f"  {word.text} (Confidence: {word.confidence:.2f}%)")
    # Annotate the words in the image
    annotate_words(image_file, result.read)
    ```

7. Save your changes and run the program locally to extract text from images:

    ```bash
    python read-text.py images/Lincoln.jpg
    ```

    Observe the output, which should include each individual word in the image and the confidence associated with their prediction.

8. Download and view the resulting `words.jpg` file:

    ```bash
    download words.jpg
    ```

9. Rerun the program for `images/Business-card.jpg` and `images/Note.jpg`, viewing the `words.jpg` file generated for each image.

### Clean up resources

If you’ve finished exploring Azure AI Vision, you should delete the resources you have created in this exercise to avoid incurring unnecessary Azure costs:

1. Open the Azure portal at https://portal.azure.com, and sign in using the Microsoft account associated with your Azure subscription.
2. In the top search bar, search for **Computer Vision**, and select the Computer Vision resource you created in this lab.
3. On the resource page, select **Delete** and follow the instructions to delete the resource.
