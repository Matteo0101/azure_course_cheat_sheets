# What is the Azure AI Foundry SDK?

The Azure AI Foundry SDK is a set of packages and services designed to work together to enable developers to write code that uses resources in an Azure AI Foundry project. With the Azure AI Foundry SDK, developers can create applications that connect to a project, access the resource connections and models in that project, and use them to perform AI operations, such as sending prompts to a generative AI model and processing the responses

The SDK provides Python and Microsoft C# .NET libraries that you can use to build AI applications based on Azure AI Foundry projects.

## Installing SDK packages
The core package for working with projects in the Azure AI Foundry SDK is the Azure AI Projects library, which enables you to connect to an Azure AI Foundry project and access the resources defined within it.

To use the Azure AI Projects library in Python, you can use the pip package installation utility to install the azure-ai-projects package from PyPi:
```bash
pip install azure-ai-projects
```

## Using the SDK to connect to a project
The first task in most Azure AI Foundry SDK code is to connect to an Azure AI Foundry project. Each project has a unique endpoint, which you can find on the project's Overview page in the Azure AI Foundry portal.

### Note: The project provides multiple endpoints and keys, including:

- An endpoint for the project itself; which can be used to access project connections, agents, and models in the Azure AI Foundry resource.
- An endpoint for Azure OpenAI Service APIs in the project's Azure AI Foundry resource.
- An endpoint for Azure AI services APIs (such as Azure AI Vision and Azure AI Language) in the Azure AI Foundry resource.

You can use the project endpoint in your code to create an AIProjectClient object, which provides a programmatic proxy for the project.

The following code snippet shows how to create an AIProjectClient object in Python.

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
...

project_endpoint = "https://......"
project_client = AIProjectClient(            
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint)
```

### Note: The code uses the default Azure credentials to authenticate when accessing the project. To enable this authentication, in addition to the azure-ai-projects package, you need to install the azure-identity package:
```bash
pip install azure-identity
```

### Tip: To access the project successfully, the code must be run in the context of an authenticated Azure session. For example, you could use the Azure command-line interface (CLI) az-login command to sign in before running the code.

# Work with project connections

Each Azure AI Foundry project includes connected resources, which are defined both at the parent (Azure AI Foundry resource or hub) level, and at the project level. Each resource is a connection to an external service, such as Azure storage, Azure AI Search, Azure OpenAI, or another Azure AI Foundry resource.

With the Azure AI Foundry SDK, you can connect to a project and retrieve connections; which you can then use to consume the connected services.

The AIProjectClient object in Python has a connections property, which you can use to access the resource connections in the project. Methods of the connections object include:

connections.list(): Returns a collection of connection objects, each representing a connection in the project. You can filter the results by specifying an optional connection_type parameter with a valid enumeration, such as ConnectionType.AZURE_OPEN_AI.
connections.get(connection_name, include_credentials): Returns a connection object for the connection with the name specified. If the include_credentials parameter is True (the default value), the credentials required to connect to the connection are returned - for example, in the form of an API key for an Azure AI services resource.
The connection objects returned by these methods include connection-specific properties, including credentials, which you can use to connect to the associated resource.

The following code example lists all of the resource connections that have been added to a project:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

try:

    # Get project client
    project_endpoint = "https://....."
    project_client = AIProjectClient(            
            credential=DefaultAzureCredential(),
            endpoint=project_endpoint,
        )

    ## List all connections in the project
    connections = project_client.connections
    print("List all connections:")
    for connection in connections.list():
        print(f"{connection.name} ({connection.type})")

except Exception as ex:
    print(ex)
```

# Create a chat client

A common scenario in an AI application is to connect to a generative AI model and use prompts to engage in a chat-based dialog with it. You can use the Azure AI Foundry SDK to chat with models that you have deployed in your Azure AI Foundry project.

The specific libraries and code used to build a chat client depends on how the target model has been deployed in the Azure AI Foundry project. You can deploy models to the following model hosting solutions:

- Azure AI Foundry Models: A single endpoint for multiple models of different types, including OpenAI models and others from the Azure AI Foundry model catalog. Models are consumed through an Azure AI Foundry resource connection in the project (either the default Azure AI Foundry resource for the project or another resource connection that has been added to the project).
- Azure OpenAI: A single endpoint for OpenAI models hosted in Azure. Models are consumed through an Azure OpenAI resource connection in the project.
- Serverless API: A model-as-a-service solution in which each deployed model is accessed through a unique endpoint and hosted in the Azure AI Foundry project.
- Managed compute: A model-as-a-service solution in which each deployed model is accessed through a unique endpoint hosted in custom compute.

### Note: To deploy models to an Azure AI model inference endpoint, you must enable the Deploy models to Azure AI model inference service option in Azure AI Foundry.

In this module, we'll focus on models deployed to the Azure AI Foundry Models endpoint.

## Building a client app for Azure AI Foundry Models

When you have deployed models to the Azure AI model inference service, you can use the Azure AI Foundry SDK to write code that creates a ChatCompletionsClient object, which you can then use to chat with a deployed model. One of the benefits of using this model deployment type is that you can easily switch between deployed models by changing one parameter in your code (the model deployment name), making it a great way to test against multiple models while developing an app.

The following Python code sample uses a ChatCompletionsClient object to chat with a model deployment named phi-4-model.

```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.inference.models import SystemMessage, UserMessage

try:

    # Initialize the project client
    project_client = AIProjectClient(            
        credential=DefaultAzureCredential(),
        endpoint=project_endpoint)

    ## Get a chat client
    chat_client = project_client.inference.get_chat_completions_client()

    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question:")

    response = chat_client.complete(
        model="phi-4-model",
        messages=[
            SystemMessage("You are a helpful AI assistant that answers questions."),
            UserMessage(user_prompt)
        ],
    )
    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)
```

### Note: The ChatCompletionsClient class uses Azure AI Inference library. In addition to the azure-ai-projects and azure-identity packages discussed previously, the sample code shown here assumes that the azure-ai-inference package has been installed:
```bash
pip install azure-ai-inference
```

## Using the Azure OpenAI SDK

In the Azure AI Foundry SDK for Python, the AIProjectClient class provides a get_azure_openai_client() method that you can use to create an Azure OpenAI client object. You can then use the classes and methods defined in the Azure OpenAI SDK to consume an OpenAI model deployed to Azure Foundry Models.

The following Python code sample uses the Azure AI Foundry and Azure OpenAI SDKs to chat with a model deployment named gpt-4o-model.

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI


try:
    # Initialize the project client
    project_connection_string = "https://......"
    project_client = AIProjectClient(            
        credential=DefaultAzureCredential(),
        endpoint=project_endpoint)

    ## Get an Azure OpenAI chat client
    openai_client = project_client.inference.get_azure_openai_client(api_version="2024-10-21")

    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question:")
    response = openai_client.chat.completions.create(
        model="gpt-4o-model",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."},
            {"role": "user", "content": user_prompt},
        ]
    )
    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)
```

### Note: In addition to the azure-ai-projects and azure-identity packages discussed previously, the sample code shown here assumes that the openai package has been installed:
```bash
pip install openai
```
