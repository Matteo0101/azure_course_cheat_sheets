# [Develop a vision-enabled chat app](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Labs/08-gen-ai-vision.html)

In this exercise, you use the Phi-4-multimodal-instruct generative AI model to generate responses to prompts that include images. You’ll develop an app that provides AI assistance with fresh produce in a grocery store by using Azure AI Foundry and the Azure AI Model Inference service.

This exercise takes approximately 30 minutes.

## Open Azure AI Foundry portal

Let’s start by signing into Azure AI Foundry portal.

1. In a web browser, open the Azure AI Foundry portal at [https://ai.azure.com](https://ai.azure.com) and sign in using your Azure credentials.
2. Close any tips or quick start panes that are opened the first time you sign in, and if necessary use the Azure AI Foundry logo at the top left to navigate to the home page.

## Choose a model to start a project

An Azure AI project provides a collaborative workspace for AI development. Let’s start by choosing a model that we want to work with and creating a project to use it in.

1. On the home page, in the **Explore models and capabilities** section, search for the **Phi-4-multimodal-instruct** model.
2. In the search results, select the **Phi-4-multimodal-instruct** model to see its details, and then at the top of the page for the model, select **Use this model**.
3. When prompted to create a project, enter a valid name for your project and expand **Advanced options**.
4. Select **Customize** and specify the following settings for your hub:

    - **Azure AI Foundry resource**: A valid name for your Azure AI Foundry resource
    - **Subscription**: Your Azure subscription
    - **Resource group**: Create or select a resource group
    - **Region**: Select any AI Services supported location

    > **Note**: Some Azure AI resources are constrained by regional model quotas. In the event of a quota limit being exceeded later in the exercise, there’s a possibility you may need to create another resource in a different region.

5. Select **Create** and wait for your project, including the Phi-4-multimodal-instruct model deployment you selected, to be created.

    > **Note**: Depending on your model selection you might receive additional prompts during the project creation process. Agree to the terms and finalize the deployment.

6. When your project is created, your model will be displayed in the **Models + endpoints** page.

## Test the model in the playground

Now you can test your multimodal model deployment with an image-based prompt in the chat playground.

1. Select **Open in playground** on the model deployment page.
2. In a new browser tab, download `mango.jpeg` from [this link](https://github.com/MicrosoftLearning/mslearn-ai-vision/raw/refs/heads/main/Labfiles/gen-ai-vision/mango.jpeg) and save it to a folder on your local file system.
3. On the chat playground page, in the **Setup** pane, ensure that your Phi-4-multimodal-instruct model deployment is selected.
4. In the main chat session panel, under the chat input box, use the attach button (📎) to upload the `mango.jpeg` image file, and then add the text `What desserts could I make with this fruit?` and submit the prompt.
5. Review the response, which should hopefully provide relevant guidance for desserts you can make using a mango.

## Create a client application

Now that you’ve deployed the model, you can use the deployment in a client application.

> **Tip**: You can choose to develop your solution using Python. Follow the instructions in the appropriate section for your chosen language.

### Prepare the application configuration

1. In the Azure AI Foundry portal, view the **Overview** page for your project.
2. In the **Endpoints and keys** area, ensure the Azure AI Foundry library is selected, and note the Azure AI Foundry project endpoint. You’ll use this connection string to connect to your project in a client application.
3. Clone the GitHub repo containing the code files for this exercise:

    ```bash
    rm -r mslearn-ai-vision -f
    git clone https://github.com/MicrosoftLearning/mslearn-ai-vision
    ```

4. Navigate to the folder containing the application code files:

    ```bash
    cd mslearn-ai-vision/Labfiles/gen-ai-vision/python
    ```

5. Install the libraries you’ll use:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt azure-identity azure-ai-projects azure-ai-inference
    ```

6. Edit the configuration file that has been provided:

    ```bash
    code .env
    ```

    Replace the `your_project_connection_string` placeholder with the connection string for your project (copied from the project **Overview** page in the Azure AI Foundry portal), and the `your_model_deployment` placeholder with the name you assigned to your Phi-4-multimodal-instruct model deployment.

7. Save your changes and close the editor.

### Write code to connect to your project and get a chat client for your model

1. Edit the code file that has been provided:

    ```bash
    code chat-app.py
    ```

2. Add the following code to reference the namespaces in the libraries you installed previously:

    ```python
    # Add references

    from dotenv import load_dotenv
    from azure.identity import DefaultAzureCredential
    from azure.ai.projects import AIProjectClient
    from azure.ai.inference.models import (
        SystemMessage,
        UserMessage,
        TextContentItem,
        ImageContentItem,
        ImageUrl,
    )
    ```

3. Add the following code to connect to your Azure AI Foundry project using the Azure credentials you are currently signed in with:

    ```python
    # Initialize the project client

    project_client = AIProjectClient(
        endpoint=project_connection,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True
        )
    )
    ```

4. Add the following code to create a client object for chatting with your model:

    ```python
    # Get a chat client

    chat_client = project_client.inference.get_chat_completions_client(model=model_deployment)
    ```

### Write code to submit a URL-based image prompt

1. Add the following code to submit a prompt that includes the following image:

    ```python
    # Get a response to image input

    image_url = "https://github.com/MicrosoftLearning/mslearn-ai-vision/raw/refs/heads/main/Labfiles/gen-ai-vision/orange.jpeg"
    image_format = "jpeg"
    request = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
    image_data = base64.b64encode(urlopen(request).read()).decode("utf-8")
    data_url = f"data:image/{image_format};base64,{image_data}"

    response = chat_client.complete(
        messages=[
            SystemMessage(system_message),
            UserMessage(content=[
                TextContentItem(text=prompt),
                ImageContentItem(image_url=ImageUrl(url=data_url))
            ]),
        ]
    )
    print(response.choices[0].message.content)
    ```

2. Save your changes to the code file.

### Modify the code to upload a local image file

1. In the loop section, find the code you added previously under the comment `Get a response to image input`. Then modify the code as follows, to upload this local image file:

    ```python
    # Get a response to image input

    script_dir = Path(__file__).parent  # Get the directory of the script
    image_path = script_dir / 'mystery-fruit.jpeg'
    mime_type = "image/jpeg"

    # Read and encode the image file

    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Include the image file data in the prompt

    data_url = f"data:{mime_type};base64,{base64_encoded_data}"
    response = chat_client.complete(
        messages=[
            SystemMessage(system_message),
            UserMessage(content=[
                TextContentItem(text=prompt),
                ImageContentItem(image_url=ImageUrl(url=data_url))
            ]),
        ]
    )
    print(response.choices[0].message.content)
    ```

2. Save your changes to the code file.

### Run the app

1. Run the application:

    ```bash
    python chat-app.py
    ```

2. When prompted, enter the following prompt:

    ```
    What is this fruit? What recipes could I use it in?
    ```

3. Review the response. Then enter `quit` to exit the program.

> **Note**: In this simple app, we haven’t implemented logic to retain conversation history; so the model will treat each prompt as a new request with no context of the previous prompt.

## Clean up

If you’ve finished exploring Azure AI Foundry portal, you should delete the resources you have created in this exercise to avoid incurring unnecessary Azure costs.

1. Open the Azure portal and view the contents of the resource group where you deployed the resources used in this exercise.
2. On the toolbar, select **Delete resource group**.
3. Enter the resource group name and confirm that you want to delete it.
