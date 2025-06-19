# 04 Develop an AI agent with Semantic Kernel

AI agents are reshaping application design by using generative AI to interpret data, take decisions, and complete tasks with little human oversight. Powered by large-language models, they can automate intricate workflows and are well-suited to business-process automation.

### Semantic Kernel SDK and Agent Framework

- **Semantic Kernel SDK** is an open-source toolkit that makes it easy to embed AI models in applications.

- The **Agent Framework** built into Semantic Kernel supports several agent types—ChatCompletionAgent, OpenAIAssistantAgent, and AzureAIAgent—with this module focusing on AzureAIAgent.

### Azure AI Foundry Agent Service

- A fully managed service that lets developers securely build, deploy, and scale extensible AI agents without managing compute or storage.

- When combined with the Semantic Kernel Agent Framework, developers can spin up agents on Foundry quickly, gaining natural-language capabilities and access to built-in tools through only a few lines of code.

### Why pair Semantic Kernel with Foundry Agent Service?

- Flexibility & scalability: Keep existing Semantic Kernel code and simply add Azure AI Agent features (built-in tools, deployment pipelines).

- Consistency: Use the same SDK to manage multiple agent types in one solution.

- Multi-agent orchestration: Semantic Kernel’s GroupChat feature coordinates collaborative agents—ideal for complex, multi-agent scenarios.

### Problem  🎯
You need an **AI-driven process that automatically extracts data from submitted expense reports, formats them, and e-mails the finished documents to the right recipients**. The solution must:  

* Operate **autonomously** without manual oversight.  
* **Scale securely** without the team managing compute or storage resources.  
* Keep the full conversation state so follow-up questions (for example, “Resend last month’s report to HR”) work seamlessly.

### Solution with Azure and Semantic Kernel ☁️
Leverage **Azure AI Foundry Agent Service** through the **Semantic Kernel SDK**—specifically the `AzureAIAgent` class. 

#### Understand Semantic Kernel AI agents

An AI agent is a program that uses generative AI to interpret data, make decisions, and perform tasks on behalf of users or other applications. AI agents rely on large language models to perform their tasks. Unlike conventional programs, AI agents can function autonomously, handling complex workflows and automating processes without requiring continuous human oversight.

AI Agents can be developed using many different tools and platforms, including the Semantic Kernel SDK. Semantic Kernel is an open-source SDK that enables developers to easily integrate the latest AI models into their applications. Part of that SDK includes the Semantic Kernel Agent Framework, which allows developers to quickly create functional agents that can use natural language processing to complete tasks.

#### Semantic Kernel core components:
The Semantic Kernel offers different components that can be used individually or combined.

1. **AI service connectors** - connect the code to AI services from different providers under a common interface. Supported services include Chat Completion, Text Generation, and more.

2. **Memory connectors** - expose vector stores from other providers under a common interface.

3. **Functions and plugins** - containers for functions that are registered with the kernel. Once registered, functions can be invoked by the AI or through prompt templates.

4. **Prompt template**s - combine instructions, user input, and function outputs into a reusable format. Prompt templates allow AI models to execute predefined steps dynamically.

5. **Filters** - allow custom actions to be performed before and after a function or prompt is invoked. When registered, function filters act as outer layers and prompt filters as inner layers.

#### Agent framework components:
The Agent Framework within Semantic Kernel helps streamline the creation of agents and enables multi-agent collaboration in conversations while integrating human input. The framework supports different types of agents, including `ChatCompletionAgent`, `OpenAIAssistantAgent`, and `AzureAIAgent`.

#### What is an Azure AI Agent?
The `AzureAIAgent` class provides a seamless way to build and interact with AI agents using the Foundry Agent Service. It abstracts the complexity of managing AI agents by offering a more structured and intuitive interface within the Semantic Kernel Agent Framework. Key benefits include:

- **Simplified agent creation** – The AzureAIAgent class allows developers to define AI agents with minimal configuration, leveraging the power of Foundry Agent Service without managing the underlying infrastructure.

- **Automatic tool invocation** – The agent can automatically call and execute tools, integrating seamlessly with Azure AI Search, Bing, Azure Functions, and more.

- **Thread and conversation management** – Provides built-in mechanisms for managing conversation states, ensuring smooth multi-agent interactions.

- **Secure enterprise integration** – Enables secure and compliant AI agent development with keyless authentication and customizable storage options.

By using the AzureAIAgent class, developers can take full advantage of Foundry Agent Service while taking advantage of the features offered by the Semantic Kernel SDK. This allows for robust AI-driven workflows that scale efficiently across enterprise applications.

#### Agent framework core concepts:
- **Agent** - abstraction for AI agents, with specialized subclasses like AzureAIAgent, allowing for task completion and human interaction in conversations.

- **Agent threads** - manage conversation state and stores conversations.

- **Agent chat** - the foundation for multi-agent interactions, allows for structured conversations and collaboration.

- **Agent channel** - used for custom agent development, allows different types of agents to participate in AgentChat.

- **Agent messages** - a unified structure for agent communication, provides seamless communication and integration with existing AI workflows.

- **Templating** - like Semantic Kernel prompt templates, templates use dynamic prompt configurations to shape agent behavior.

Functions and plugins - like Semantic Kernel plugins, agent plugin functions allow developers to extend agent capabilities by incorporating custom functions.

### Required Components in Azure Ai Agents 🛠️
| Component | Details from the official material |
|-----------|------------------------------------|
| **AzureAIAgentSettings** | Reads model deployment name and Foundry connection string from environment variables. |
| **AzureAIAgent client** | Manages the connection to the Foundry project and exposes agent operations. |
| **Agent service** | the AzureAIAgent client also contains an agent operations service. This service helps streamline the process of creating, managing, and running the agents for your project. |
| **Agent definition** | Declares the model, agent name, and instructions on the service. |
| **AzureAIAgentThread** | Stores conversation history and state between user and agent. |

### How to use a plugin with AzureAiAgent: 
Custom APIs exposed with the `@kernel_function` decorator so the agent can call them. In Semantic Kernel, plugins allow your AI agent to use existing APIs to perform tasks it couldn't do on its own. Plugins work through function calling, allowing AI to request and use specific functions. Semantic Kernel routes the request to the appropriate function in your codebase and returns the results back to the LLM so the LLM can generate a final response. To enable automatic orchestration with function calling, plugins also need to provide details that describe how they behave. The function's input, output, and side effects should be described in a way that the AI can understand, otherwise, the AI will not correctly call the function. 

1. Define your plugin

You can create a plugin by defining a class and annotating its methods with the kernel_function decorator. The decorator lets Semantic Kernel know that this function can be called by the AI or referenced in a prompt. The kernel_function decorator also supports a description attribute to help the AI understand how to use the function.

2. Add the plugin to your agent

Once you define your plugin, you can add it to your AzureAIAgent by creating a new instance of the plugin and adding it to the agent's plugin collection.

3. Invoke the plugin's functions

You can invoke your plugin's functions by using prompts on your agent's message thread. For example, if you have a plugin function called get_tasks, your prompt to the agent might be "What tasks do I have?".

### Architecture / Development 🏗️ 

#### Create an Azure AI agent with Semantic Kernel

AzureAIAgent is a specialized agent within the Semantic Kernel framework, designed to provide advanced conversational capabilities with seamless tool integration. It automates tool calling, eliminating the need for manual parsing and invocation. The agent also securely manages conversation history using threads, reducing the overhead of maintaining state. The AzureAIAgent class supports many built-in tools, including file retrieval, code execution, and data interaction via Bing, Azure AI Search, Azure Functions, and OpenAPI.

1. **Create an Azure AI Foundry project** and record its connection string.  
2. **Add the project connection string** to your Semantic Kernel application code so `AzureAIAgentSettings` can load it.  
3. **Create an AzureAIAgentSettings object**.
4. **Create an AzureAIAgent client**.
5. **Create an agent definition** on the agent service provided by the client.
6. **Create an agent based on the definition**. 

   ```python
   from azure.identity.aio import DefaultAzureCredential
   from semantic_kernel.agents import (
       AzureAIAgent, AzureAIAgentThread, AzureAIAgentSettings
   )
    # 1. Create an AzureAIAgentSettings object
   ai_agent_settings = AzureAIAgentSettings()
    
    # 2. Create an AzureAIAgent client
   async with (@
       DefaultAzureCredential() as creds,
       AzureAIAgent.create_client(credential=creds) as client,
   ):
        # 3. Create an agent definition on the agent service provided by the client
       agent_definition = await client.agents.create_agent(
           model=ai_agent_settings.model_deployment_name,
           name="<name>", # es: ExpenseReportAgent
           instructions="<instructions>" # es: Format and e-mail employee expense reports.
       )
        # 4. Create the AI agent based on the agent definition
       agent = AzureAIAgent(
        client=client, 
       definition=agent_definition
       )

Once your agent is defined, you can create a thread to interact with your agent and invoke responses for inputs. For example:
```python
# Create the agent thread
thread = AzureAIAgentThread(client=client)
try:
    # Create prompts 
    prompt = ["Generate and e-mail the latest expense report for Alex."]
    
    # Invoke a response from the agent
    response = await agent.get_response(messages=prompt, thread_id=thread.id)
    
    # View the response
    print(response)
finally:
    
    # Clean up the thread
    await thread.delete() if thread else None
```

### Extend with plugins (automatic function calling): [EXTRA]

```python
from semantic_kernel import kernel_function

class ExpensePlugin:
    @kernel_function(description="Retrieve raw expense data.")
    def get_expenses(self, employee_id: str):
        ...

class MailPlugin:
    @kernel_function(description="Send a formatted e-mail.")
    def send_mail(self, to: str, body: str):
        ...

agent.add_plugin(ExpensePlugin())
agent.add_plugin(MailPlugin())
```

# Best Practice / Considerations ✅
- Describe every plugin function with the description attribute, including its inputs, outputs, and side effects.

- Let Foundry perform automatic tool invocation instead of manual JSON parsing.

- Use threads for every interaction to preserve state and clean them up when finished.

- GroupChat (covered in a later module) orchestrates multi-agent collaboration without redesigning code.

- Rely on keyless enterprise security built into Azure AI Foundry rather than storing secrets in code.

### Exam-style Questions 🧠
1. What SK class encapsulates planning, function execution, and memory for Foundry agents?
✅ AzureAIAgent

2. List all five built-in tools cited in the material that an AzureAIAgent can call automatically.
✅ File retrieval, code execution, Bing, Azure AI Search, Azure Functions, OpenAPI

3. Which object maintains conversation history for each interaction?
✅ AzureAIAgentThread

4. Place these steps in order to create an Azure AI agent with SK:
✅ Create Foundry project → Add connection string → Instantiate AzureAIAgentSettings → Create client → Create agent definition → Create AzureAIAgent → Interact via thread

5. Why must each plugin function include a clear description?
✅ So the agent understands when and how to call the function during automatic orchestration.

6. Which Semantic Kernel feature enables structured collaboration among multiple agents?
✅ GroupChat
