# [Generate images with AI](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Labs/09-dall-e.html)

In this exercise, you use the OpenAI DALL-E generative AI model to generate images. You’ll develop your app by using Azure AI Foundry and the Azure OpenAI service.

This exercise takes approximately 30 minutes.

## Open Azure AI Foundry portal

Let’s start by signing into Azure AI Foundry portal.

In a web browser, open the Azure AI Foundry portal at [https://ai.azure.com](https://ai.azure.com) and sign in using your Azure credentials. Close any tips or quick start panes that are opened the first time you sign in, and if necessary use the Azure AI Foundry logo at the top left to navigate to the home page.

Review the information on the home page.

## Choose a model to start a project

An Azure AI project provides a collaborative workspace for AI development. Let’s start by choosing a model that we want to work with and creating a project to use it in.

> **Note:** AI Foundry projects can be based on an Azure AI Foundry resource, which provides access to AI models (including Azure OpenAI), Azure AI services, and other resources for developing AI agents and chat solutions. Alternatively, projects can be based on AI hub resources; which include connections to Azure resources for secure storage, compute, and specialized tools. Azure AI Foundry based projects are great for developers who want to manage resources for AI agent or chat app development. AI hub based projects are more suitable for enterprise development teams working on complex AI solutions.

1. In the home page, in the **Explore models and capabilities** section, search for the `dall-e-3` model; which we’ll use in our project.
2. In the search results, select the `dall-e-3` model to see its details, and then at the top of the page for the model, select **Use this model**.
3. When prompted to create a project, enter a valid name for your project and expand **Advanced options**.

    - **Azure AI Foundry resource**: A valid name for your Azure AI Foundry resource
    - **Subscription**: Your Azure subscription
    - **Resource group**: Create or select a resource group
    - **Region**: Select any AI Services supported location\*

    > \*Some Azure AI resources are constrained by regional model quotas. In the event of a quota limit being exceeded later in the exercise, there’s a possibility you may need to create another resource in a different region.

4. Select **Create** and wait for your project, including the `dall-e-3` model deployment you selected, to be created.

    > **Note:** Depending on your model selection you might receive additional prompts during the project creation process. Agree to the terms and finalize the deployment.

5. When your project is created, your model will be displayed in the **Models + endpoints** page.

## Test the model in the playground

Before creating a client application, let’s test the DALL-E model in the playground.

1. Select **Playgrounds**, and then **Images playground**.
2. Ensure your DALL-E model deployment is selected. Then, in the box near the bottom of the page, enter a prompt such as `Create an image of a robot eating spaghetti` and select **Generate**.
3. Review the resulting image in the playground.
4. Enter a follow-up prompt, such as `Show the robot in a restaurant` and review the resulting image.
5. Continue testing with new prompts to refine the image until you are happy with it.

## Create a client application

The model seems to work in the playground. Now you can use the Azure OpenAI SDK to use it in a client application.

> **Tip:** You can choose to develop your solution using Python. Follow the instructions below for Python.

### Prepare the application configuration

1. In the Azure AI Foundry portal, view the **Overview** page for your project.
2. Select **Models + endpoints** area, then select the **Get endpoint** button. You’ll use this connection string to connect to your model in a client application.
3. Open a terminal on your local machine and clone the GitHub repo containing the code files for this exercise:

    ```bash
    rm -r mslearn-ai-vision -f
    git clone https://github.com/MicrosoftLearning/mslearn-ai-vision
    ```

4. Navigate to the language-specific folder containing the application code files for Python:

    ```bash
    cd mslearn-ai-vision/Labfiles/dalle-client/python
    ```

5. Install the libraries you’ll use:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt azure-identity azure-ai-projects openai requests
    ```

6. Edit the configuration file that has been provided:

    ```bash
    code .env
    ```

    Replace the `your_project_endpoint` placeholder with the connection string (copied from the **Models + endpoints** page in the Azure AI Foundry portal), and the `your_model_deployment` placeholder with the name you assigned to your `dall-e-3` model deployment.

7. Save your changes and close the editor.

### Write code to connect to your project and chat with your model

1. Edit the code file that has been provided:

    ```bash
    code dalle-client.py
    ```

2. Note the existing statements that have been added at the top of the file to import the necessary SDK namespaces. Then, under the comment `# Add references`, add the following code to reference the namespaces in the libraries you installed previously:

    ```python
    # Add references

    from dotenv import load_dotenv
    from azure.identity import DefaultAzureCredential
    from azure.ai.projects import AIProjectClient
    import requests
    ```

3. In the main function, under the comment `# Get configuration settings`, note that the code loads the project connection string and model deployment name values you defined in the configuration file.

4. Under the comment `# Initialize the client`, add the following code to connect to your Azure AI Foundry project using the Azure credentials you are currently signed in with:

    ```python
    # Initialize the OpenAI client

    project_client = AIProjectClient(
        endpoint=project_connection,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True
        )
    )

    openai_client = project_client.inference.get_azure_openai_client(api_version="2024-06-01")
    ```

5. Note that the code includes a loop to allow a user to input a prompt until they enter “quit”. Then in the loop section, under the comment `# Generate an image`, add the following code to submit the prompt and retrieve the URL for the generated image from your model:

    ```python
    # Generate an image

    result = openai_client.images.generate(
        model=model_deployment,
        prompt=input_text,
        n=1
    )

    json_response = json.loads(result.model_dump_json())
    image_url = json_response["data"][0]["url"]
    ```

6. Note that the code in the remainder of the main function passes the image URL and a filename to a provided function, which downloads the generated image and saves it as a `.png` file.

7. Save your changes to the code file and close the editor.

### Run the client application

1. In the terminal, enter the following command to run the app:

    ```bash
    python dalle-client.py
    ```

2. When prompted, enter a request for an image, such as `Create an image of a robot eating pizza`. After a moment or two, the app should confirm that the image has been saved.

3. Try a few more prompts. When you’re finished, enter `quit` to exit the program.

    > **Note:** In this simple app, we haven’t implemented logic to retain conversation history; so the model will treat each prompt as a new request with no context of the previous prompt.

4. To download and view the images that were generated by your app, use the following command - specifying the `.png` file that was generated:

    ```bash
    cp ./images/image_1.png ~/Downloads
    ```

## Summary

In this exercise, you used Azure AI Foundry and the Azure OpenAI SDK to create a client application that uses a DALL-E model to generate images.

## Clean up

If you’ve finished exploring DALL-E, you should delete the resources you have created in this exercise to avoid incurring unnecessary Azure costs.

1. Return to the browser tab containing the Azure portal (or re-open the Azure portal at [https://portal.azure.com](https://portal.azure.com) in a new browser tab) and view the contents of the resource group where you deployed the resources used in this exercise.
2. On the toolbar, select **Delete resource group**.
3. Enter the resource group name and confirm that you want to delete it.
