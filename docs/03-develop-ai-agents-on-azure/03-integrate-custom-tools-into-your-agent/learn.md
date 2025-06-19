# 03 Integrate Custom Tools Into Your Agent

## Problem 🎯
A company needs to create an intelligent agent that goes beyond the standard capabilities of language models. It must carry out specific actions such as:

- Retrieving order status from a CRM system  
- Automating the creation of IT tickets  
- Interacting with external systems through APIs  

In addition, a solution is required that improves productivity, increases accuracy, and reduces human intervention in repetitive tasks.

## Solution with Azure ☁️
Use **Azure AI Foundry Agent Service** integrated with **custom tools** options, including tools described by an OpenAPI specification, Azure Functions, and function calling. These tools make it easy to integrate external APIs, event-driven applications, and custom functions:

- **Custom function**: Function calling lets you describe the structure of custom functions to an agent and return the functions that need to be called along with their arguments. The agent can dynamically identify the appropriate functions based on their definitions. This feature is useful for integrating custom logic and workflows—written in several programming languages—into your AI agents.

- **Azure Functions**:  
  Azure Functions let you build intelligent, event-driven applications with minimal overhead. They support triggers and bindings, which simplify how your AI agents interact with external systems and services. Triggers determine when a function runs, while bindings provide streamlined connections to input or output data sources.

- **OpenAPI specification tools**:  
  These tools enable your Azure AI agent to connect to an external API described by an OpenAPI 3.0 specification. This provides standardized, automated, and scalable API integrations that enhance your agent’s capabilities. OpenAPI specifications describe HTTP APIs, helping people understand how an API works, generate client code, create tests, and apply design standards.

- **Azure Logic Apps**:  
  A low-code/no-code option for adding workflows that connect apps, data, and services through Logic Apps.

## Required Components 🛠️
- **Azure AI Foundry Agent Service**  
- One or more of the following tools:  
  - Function Tool (Python or another supported language)  
  - Azure Functions (event-driven, serverless)  
  - OpenAPI Specification Tools (for HTTP APIs)  
  - Azure Logic Apps (low-code workflows)  
- `azure-identity` (e.g., `DefaultAzureCredential`)  
- Azure CLI or Cloud Shell for deployment and configuration  
- `.env` file with the Foundry project endpoint  

## Architecture / Development 🏗️

### 1. Function Calling
Start by defining a function that the agent can call. For example, here’s a fake snowfall-tracking function:

```python
import json

def recent_snowfall(location: str) -> str:
    """
    Fetch recent snowfall totals for a given location.
    :param location: The city name.
    :return: Snowfall details as a JSON string.
    """
    mock_snow_data = {"Seattle": "0 inches", "Denver": "2 inches"}
    snow = mock_snow_data.get(location, "Data not available.")
    return json.dumps({"location": location, "snowfall": snow})

user_functions: Set[Callable[..., Any]] = {
    recent_snowfall,
}

```
Register the function with your agent using the Azure AI SDK:

```python
functions = FunctionTool(user_functions)
toolset = ToolSet()
toolset.add(functions)

agent = agent_client.create_agent(
    model="gpt-4o-mini",
    name="snowfall-agent",
    instructions="You are a weather assistant...",
    toolset=toolset
)
```
### 2. Azure Functions 
```python
storage_service_endpoint = "https://<your-storage>.queue.core.windows.net"

azure_function_tool = AzureFunctionTool(
    name="get_snowfall",
    description="Get snowfall information using Azure Function",
    parameters={
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The location to check snowfall."
            },
        },
        "required": ["location"],
    },
    input_queue=AzureFunctionStorageQueue(
        queue_name="input",
        storage_service_endpoint="https://<your-storage>.queue.core.windows.net"
    ),
    output_queue=AzureFunctionStorageQueue(
        queue_name="output",
        storage_service_endpoint="https://<your-storage>.queue.core.windows.net"
    ),
)

agent = agent_client.create_agent(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    name="azure-function-agent",
    instructions="You are a snowfall tracking agent...",
    tools=azure_function_tool.definitions,
)
```
### 3. OpenAPI Specification Tool
Example OpenAPI file (JSON):

```json
{
  "openapi": "3.0.0",
  "info": { "title": "Snowfall API", "version": "1.0.0" },
  "paths": {
    "/snow": {
      "get": {
        "summary": "Get snowfall information",
        "parameters": [
          { "name": "location", "in": "query", "required": true, "schema": { "type": "string" } }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "location": { "type": "string" },
                    "snow": { "type": "string" }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```
Integrating the OpenAPI tool:

```python
with open("snowfall_openapi.json", "r") as f:
    openapi_spec = json.load(f)

auth = OpenApiAnonymousAuthDetails()

openapi_tool = OpenApiTool(
    name="snowfall_api",
    spec=openapi_spec,
    auth=auth
)

agent = agent_client.create_agent(
    model="gpt-4o-mini",
    name="openapi-agent",
    instructions="You are a snowfall tracking assistant...",
    tools=[openapi_tool]
)
```

# Best Practices / Considerations ✅
- Functions should have descriptive names and well-documented parameters; the agent will decide when to invoke them.

- The approach is declarative, not imperative—you do not write code that calls the tools directly.

- Supported OpenAPI authentication methods: anonymous, API key, managed identity.

- Use Azure Functions for event and queue integrations (e.g., HTTP or queue triggers).

- Use Logic Apps to automate complex flows through a low-code approach.

# Domande simulate d’esame 🧠
1. What advantage do custom tools offer over the agent’s built-in tools?
✅ They allow the execution of specific logic that cannot be handled directly by the language model.

2. When is it preferable to use an Azure Function instead of a Python-defined function tool?
✅ When you need serverless processing based on events or asynchronous triggers.

3. What does a tool defined by an OpenAPI specification enable?
✅ Easy integration of external APIs using a documented and scalable standard.

4. Which of the following is not a valid authentication option for an OpenAPI tool?
✅ Correct answer: currently only anonymous, API key, and managed identity are supported.

5. How does the agent decide whether to use a particular tool?
✅ Based on the user prompt and the definitions of the available tools.