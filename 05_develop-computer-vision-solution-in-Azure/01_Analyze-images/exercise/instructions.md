# [Analyze Images with Azure AI Vision](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Labs/01-analyze-images.html)

Azure AI Vision is an artificial intelligence capability that enables software systems to interpret visual input by analyzing images. In Microsoft Azure, the Vision Azure AI service provides pre-built models for common computer vision tasks, including analysis of images to suggest captions and tags, detection of common objects and people. You can also use the Azure AI Vision service to remove the background or create a foreground matting of images.

## Exercise Overview

This exercise takes approximately **30 minutes**.

### Provision an Azure AI Vision Resource

If you don’t already have one in your subscription, you’ll need to provision an Azure AI Vision resource.

1. Open the Azure portal at [https://portal.azure.com](https://portal.azure.com), and sign in using your Azure credentials.
2. Close any welcome messages or tips that are displayed.
3. Select **Create a resource**.
4. In the search bar, search for **Computer Vision**, select **Computer Vision**, and create the resource with the following settings:

    - **Subscription**: Your Azure subscription
    - **Resource group**: Create or select a resource group
    - **Region**: Choose from East US, West US, France Central, Korea Central, North Europe, Southeast Asia, West Europe, or East Asia\*
    - **Name**: A valid name for your Computer Vision resource
    - **Pricing tier**: Free F0

    > _Azure AI Vision 4.0 full feature sets are currently only available in these regions._

5. Select the required checkboxes and create the resource.
6. Wait for deployment to complete, and then view the deployment details.
7. When the resource has been deployed, go to it and under the **Resource management** node in the navigation pane, view its **Keys and Endpoint** page. You will need the endpoint and one of the keys from this page in the next procedure.

---

### Develop an Image Analysis App with the Azure AI Vision SDK

In this exercise, you’ll complete a partially implemented client application that uses the Azure AI Vision SDK to analyze images.

> **Note**: You can choose to use the SDK for **Python**. Perform the actions appropriate for your preferred language.

#### Prepare the Application Configuration

1. Clone the GitHub repo containing the code files for this exercise:

    ```bash
    rm -r mslearn-ai-vision -f
    git clone https://github.com/MicrosoftLearning/mslearn-ai-vision
    ```

2. After the repo has been cloned, use the following commands to navigate to and view the language-specific folder containing the application code files:

    **Python**:

    ```bash
    cd mslearn-ai-vision/Labfiles/analyze-images/python/image-analysis
    ls -a -l
    ```

    The folder contains application configuration and code files for your app. It also contains a `/images` subfolder, which contains some image files for your app to analyze.

3. Install the Azure AI Vision SDK package and other required packages by running the appropriate commands:

    **Python**:

    ```bash
    python -m venv labenv
    source labenv/bin/activate
    pip install -r requirements.txt azure-ai-vision-imageanalysis==1.0.0
    ```

4. Edit the configuration file for your app:

    **Python**:

    ```bash
    nano .env
    ```

5. In the code file, update the configuration values it contains to reflect the endpoint and an authentication key for your Computer Vision resource (copied from its **Keys and Endpoint** page in the Azure portal).

6. After you’ve replaced the placeholders, save your changes and close the editor.

---

### Add Code to Suggest a Caption

1. Open the code file for the client application:

    **Python**:

    ```bash
    nano image-analysis.py
    ```

2. In the code file, find the comment `Import namespaces`, and add the following code to import the namespaces you will need to use the Azure AI Vision SDK:

    **Python**:

    ```python
    # import namespaces
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential
    ```

3. In the `Main` function, note that the code to load the configuration settings and determine the image file to be analyzed has been provided. Then find the comment `Authenticate Azure AI Vision client` and add the following code to create and authenticate an Azure AI Vision client object:

    ```python
    # Authenticate Azure AI Vision client
    cv_client = ImageAnalysisClient(
        endpoint=ai_endpoint,
        credential=AzureKeyCredential(ai_key))
    ```

4. In the `Main` function, under the code you just added, find the comment `Analyze image` and add the following code:

    ```python
    # Analyze image
    with open(image_file, "rb") as f:
        image_data = f.read()
        print(f'\nAnalyzing {image_file}\n')

    result = cv_client.analyze(
        image_data=image_data,
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.DENSE_CAPTIONS,
            VisualFeatures.TAGS,
            VisualFeatures.OBJECTS,
            VisualFeatures.PEOPLE],
    )
    ```

---

### Additional Steps

Follow the instructions in the original document to add code for generating suggested tags, detecting and locating objects, detecting and locating people, and cleaning up resources.

---

### Clean Up Resources

If you’ve finished exploring Azure AI Vision, delete the resources you have created in this exercise to avoid incurring unnecessary Azure costs:

1. Open the Azure portal at [https://portal.azure.com](https://portal.azure.com), and sign in using the Microsoft account associated with your Azure subscription.
2. In the top search bar, search for **Computer Vision**, and select the Computer Vision resource you created in this lab.
3. On the resource page, select **Delete** and follow the instructions to delete the resource.
