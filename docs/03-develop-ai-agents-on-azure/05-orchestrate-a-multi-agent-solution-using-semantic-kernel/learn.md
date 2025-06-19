# 05 Orchestrate a multi-agent solution using Semantic Kernel

## 🎯 Problem

You need to address complex DevOps challenges, such as:

- Monitoring application performance
- Detecting and analyzing issues
- Deploying automated fixes
- Reporting outcomes to stakeholders

Single agents may not suffice for such tasks. A collaborative multi-agent system is required to divide responsibilities and orchestrate solutions effectively.

## ☁️ Solution with Azure and Semantic Kernel

Use the Semantic Kernel SDK to create a multi-agent architecture in which several AI agents collaborate within the same conversation using the Semantic Kernel Agent Framework. These agents operate independently yet work together through a shared chat interface and can:

- Analyze logs
- Correlate events
- Trigger actions (e.g., via CI/CD)
- Notify users with reports

The Agent Framework in Semantic Kernel provides architecture on top of existing Semantic Kernel resources, including:

- **Agents**: Agents are intelligent, AI-driven entities capable of reasoning and executing tasks. They use language models, functions, and memory to make decisions dynamically.

- **Agent collaboration**: Agents can collaborate together through an agent group chat, which enables multiple agents to join the same chat, even of different agent types. Agent group chats determine which agent should respond and how to determine if the conversation is finished.

## Semantic Kernel Features:
They are also still available within the Agent Framework, including:

1. **Kernel**: The kernel is the central component of the Semantic Kernel. The kernel acts as the execution engine, managing AI interactions, function orchestration, and memory.

2. **Tools and plugin**s: Plugins align with existing Semantic Kernel features, enabling agents to dynamically interact with external services or execute complex tasks through function calling. Within the Agent Framework, tools are available to provide extra functionality to your agents, such as file searching or code interpreter, similar to tool usage in Azure AI Foundry Agent Service. Agents use tools and plugins to perform specific tasks.

3. **History**: Agents can maintain chat history across multiple interactions, allowing them to track previous interactions and adapt responses accordingly. The conversation history is always accessible by the agents, either as a whole or for a specific agent's chat history.

### Types of agents:
The Semantic Kernel Agent Framework supports several different types of agents, including:

1. **Azure AI Agent**: a specialized agent within the Semantic Kernel Agent Framework. The AzureAIAgent type is designed to provide advanced conversational capabilities with seamless tool integration. It automates tool calling and securely manages conversation history using threads, reducing the overhead of maintaining state. The AzureAIAgent also supports a variety of built-in tools, including file retrieval, code execution, and data interaction via Bing, Azure AI Search, Azure Functions, and OpenAPI.

2. **Chat Completion Agent**: designed for chat completion and conversation interfaces. The ChatCompletionAgent type mirrors the features and patterns in the underlying AI Service to support natural language processing, contextual understanding, and dialogue management.

3. **OpenAI Assistant Agent**: designed for more advanced capabilities and multi-step tasks. The OpenAIAssistantAgent type supports goal-driven interactions with additional features like code interpretation and file search.

## Core concepts:
### 1. Create the AgentGroupChat:
A key feature of the Semantic Kernel Agent Framework is its ability to facilitate interactions between multiple agents. Using AgentGroupChat, developers can create dynamic, multi-agent conversations where different types of agents collaborate to generate responses.

The AgentGroupChat class extends the AgentChat framework, providing a structured way to manage multi-agent collaboration. It offers built-in mechanisms to control conversation flow, define collaboration strategies, and support both single-turn and multi-turn interactions.

### 2. Add messages to the chat
Once your chat is created, you can create a ChatMessageContent object and add it to the chat thread. The ChatMessageContent object takes a role parameter in addition to the content.


### 3. Conversation Modes in AgentGroupChat

Agent group chats can operate in two distinct modes, depending on the conversation requirements:

- **In single-turn conversations**, a designated agent provides a response based on user input.

1. ***Intent recognition***: The framework analyzes the user's query to identify the intent and match it with the most relevant agent.

2. ***Predefined rules***: Developers can configure routing rules to direct specific queries to designated agents in their application.

You can invoke a response from a single-turn chat by using ```AgentGroupChat.invoke``` and specifying the agent that should respond.

- **In multi-turn conversations**, multiple agents take turns responding, continuing the conversation until a termination condition is met.
Agent responses are returned asynchronously as they are generated, allowing the conversation to unfold in real-time.

1. ***Context tracking***: The framework maintains a record of the conversation history to understand the user's intent and select the appropriate agent.

2. ***Dynamic switching***: If the topic shifts, the framework dynamically switches to an agent specializing in the new domain in the middle of the conversation.

You can invoke a response from a multi-turn chat by using ```AgentGroupChat.invoke```.

Both modes allow agents to collaborate by building on each other's responses, resulting in dynamic, intelligent interactions.

### 4. Design an agent selection strategy
One key feature of the Semantic Kernel Agent Framework is its support for intelligent, multi-agent interactions. Agent collaboration can be achieved using AgentGroupChat, which has some critical components to consider that aren't necessary with single agents or non-agentic Semantic Kernel applications.
It's important to choose the agent that's best suited to respond to a user's query, especially in multi-agent systems where the agents specialize in different domains.

For multi-turn agents, agent selection is determined by a selection strategy. The selection strategy is defined within the framework, either by using a predefined selection strategy or by extending a SelectionStrategy class to define custom selection behavior. You can define the selection strategy when you create the AgentGroupChat object.

1. **SequentialSelectionStrategy**: The ```SequentialSelectionStrategy class``` offers a predefined selection strategy where the agent turn order is based on the order in which the agents were added to the chat. The option to specify an initial agent is also available.
KernelFunctionSelectionStrategy

2. **KernelFunctionSelectionStrategy**: The ```KernelFunctionSelectionStrategy class``` allows you to define your selection strategy by creating a kernel function from a prompt. In our writer and reviewer example, your selection strategy prompt might be:

If your preferred interaction should always have a certain agent respond first, that can be specified in your selection strategy as seen in the prompt above.

3. **SelectionStrategy base class**: The ```SelectionStrategy base class``` contains an overridable select_agent method where you can define custom logic for selecting the next agent. The return value must be an agent that is present in the group chat.
Once you decide on your selection strategy, you can assign it to the selection_strategy parameter of the AgentGroupChat object.

**Truncating chat history**

Since the selection strategy will typically rely on the last message in the chat to determine the next agent, you can truncate the chat history to reduce token usage and help improve performance. The KernelFunctionSelectionStrategy accepts a history_reducer parameter which you can specify as:

```python
history_reducer = ChatHistoryTruncationReducer(target_count=1)
```

### 5. Define a chat termination strategy

Multi-turn conversations have responses returned asynchronously, so the conversation can develop naturally. However, the agents need to know when to stop a conversation, which is determined by the termination strategy.

**Termination strategy**

A termination strategy ensures that conversations or tasks conclude appropriately. This strategy prevents unnecessary messages to the user, limits resource usage, and improves the overall user experience.

Similar to how the selection strategy is specified, developers can define a termination strategy or use a predefined strategy. Each termination strategy supports a maximum_iterations parameter that will end the chat after a maximum number of iterations. The default value is 99 iterations. Each termination strategy also requires the agents which should run the strategy. In the writer-reviewer agent scenario, the ReviewingDirectorAgent should determine when the chat should terminate.

1. **DefaultTerminationStrategy**: The ```DefaultTerminationStrategy class``` will only terminate after the specified number of maximum iterations.
2. **KernelFunctionTerminationStrategy**: The ```KernelFunctionTerminationStrategy class``` allows you to define your termination strategy by creating a kernel function from a prompt. 

This class requires a result_parser parameter. The result_parser is a function that processes the output of your prompt function to determine whether the termination condition has been met. It takes the output of the prompt function and processes it to return True or False.

3. **TerminationStrategy base class**: The ```TerminationStrategy base class``` contains an overridable should_agent_terminate method where you can define custom logic for concluding the agent group chat. The return value must be a Boolean. For example, you could define a termination function that checks the most recent history entry for just the word "yes", however you would need to provide explicit instructions to your agent to return the termination keyword.

Once you've decided on your termination strategy, you can assign it to the termination_strategy parameter of the AgentGroupChat object.

**Truncating chat history**

Since the termination strategy will typically rely on the last message in the chat to determine whether the chat should terminate, you can truncate the chat history to reduce token usage and help improve performance. The KernelFunctionTerminationStrategy accepts a history_reducer parameter which you can specify as:

```python
history_reducer = ChatHistoryTruncationReducer(target_count=1)
```
**Conversation state**

Whether you use AgentGroupChat for a single-turn or multi-turn conversation, the state updates to completed once it meets the termination criteria. However, you may want to use the group chat instance again. To keep using the same chat instance, you'll need to reset the completion state to False. Without a state reset, the AgentGroupChat can't accept new interactions.

When a conversation hits the maximum number of iterations allowed, the conversation will end but won't be marked as completed. In this case, you can extend the conversation without resetting the conversation state.

By understanding these components, you can better utilize the Semantic Kernel Agent Framework to build intelligent multi-agent systems.


## 🛠️ Required Components

- Semantic Kernel SDK
- Semantic Kernel Agent Framework
- AzureAIAgent, ChatCompletionAgent, OpenAIAssistantAgent
- Agent types for different roles (e.g., Monitoring, Deployment, Reporting)
- Tools/plugins support (e.g., file search, OpenAPI, Azure Functions)
- Chat management classes: AgentGroupChat, ChatMessageContent, etc.

## 🏗️ Architecture / Development

### 🔹 Fondamentals:

- **Agents**: Autonomous entities powered by language models + traditional code.
- **Agent Collaboration**: Enabled via AgentGroupChat.
- **Kernel**: Core executor handling memory, orchestration, and tools.
- **Tools & Plugins**: Functions or external APIs for action execution.
- **History**: Persistent chat memory available across interactions.

### 🔹 Core concepts:

1. **Create the AgentGroupChat**  
   Initialize a group chat to coordinate multiple agents in a shared conversation.

2. **Add messages to the chat**  
   Insert initial or ongoing messages to drive agent interactions.

3. **Conversation Modes in AgentGroupChat**  
   Choose how agents interact—e.g., single-turn, multi-turn.

4. **Design an agent selection strategy**  
   Define logic to select which agent should respond to each message.

5. **Define a chat termination strategy**  
   Set rules for ending the conversation, like reaching a goal or max turns.

### 🔹 1. Create the AgentGroupChat

```python
# Define agents
agent_writer = AzureAIAgent(...)
agent_reviewer = AzureAIAgent(...)

# Create chat
chat = AgentGroupChat(agents=[agent_writer, agent_reviewer])
```

Or dynamically:

```python
chat = AgentGroupChat()
chat.add_agent(agent=agent_writer)
chat.add_agent(agent=agent_reviewer)
```

### 🔹 2. Add messages to the chat

```python
chat_message = ChatMessageContent(role=AuthorRole.USER, content="This is the message content.")
await chat.add_chat_message(message=chat_message)
```

### 🔹 3. Conversation Modes in AgentGroupChat

**Single-turn:**
```python
async for message in chat.invoke(agent):
    # Process response
```

**Multi-turn:**
```python
async for message in chat.invoke():
    # Process responses from multiple agents
```

### 🔹 4. Design an agent selection strategy

Choose who responds next in a multi-agent chat:

- **KernelFunctionSelectionStrategy**: Uses a custom prompt to determine next agent.

Example prompt:
```python
prompt=f"""
Determine the next agent:
Participants:
- ReviewingDirectorAgent
- CopywriterAgent
Rules:
- After user input -> CopywriterAgent
- Then -> ReviewingDirectorAgent
History:
{{$history}}
"""
```

Assign selection strategy:
```python
chat = AgentGroupChat(..., selection_strategy=KernelFunctionSelectionStrategy(...))
```

### 🔹 5. Define a chat termination strategy

Used to determine when a conversation is complete:

- **DefaultTerminationStrategy**: Ends after max iterations.
- **KernelFunctionTerminationStrategy**: Uses prompt and logic.

Example prompt:
```python
prompt="""
Determine if the copy is approved. If so, reply with one word: yes
History:
{{$history}}
"""
```

Assign termination strategy:
```python
chat = AgentGroupChat(..., termination_strategy=KernelFunctionTerminationStrategy(...))
```

### 🔹 [EXTRA] Manage Chat State

- `chat.completed = False` to reset chat for reuse
- Truncate history to reduce token usage:
  ```python
  history_reducer = ChatHistoryTruncationReducer(target_count=1)
  ```

## ✅ Best Practices / Considerations

- Define roles clearly per agent.
- Use history truncation to optimize performance.
- Handle agent selection carefully to ensure accuracy.
- Always use a termination strategy to avoid endless loops.
- Monitor token usage and response times.

## Exam-style Questions 🧠

**How can you orchestrate task distribution among AI agents using Semantic Kernel?**
✅ By implementing a AgentGroupChat with multiple agents and defining a SelectionStrategy.

**Which Semantic Kernel component ensures tasks stop appropriately?**
✅ A TerminationStrategy such as KernelFunctionTerminationStrategy.

**How do agents collaborate in a conversation?**
✅ Through AgentGroupChat where agents interact and pass context via shared chat history.

**Which class would you use to define a prompt-based next-agent selector?**
✅ KernelFunctionSelectionStrategy

**What happens when a chat hits max iterations?**
✅ The chat ends but is not marked completed; it can be continued without a state reset.