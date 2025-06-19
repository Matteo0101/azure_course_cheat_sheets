# 03 Exercise 🛠️: Use a Custom Function in an AI Agent

## Objective 🎯 
Create a technical-support agent that collects the details of a technical issue and generates a ticket using a custom function.

## Step 1 🚀: Create an Agent in Azure AI Foundry

1. Go to <https://ai.azure.com> and sign in with your Azure credentials.  
2. On the **Home** page, select **Create an agent**.  
3. Enter a **project name** and expand **Advanced options**.  
4. Verify the settings: **Azure AI Foundry resource**, **Subscription**, **Resource group**, and **Region**. *If you later hit a quota limit, create the project in a different region.*  
5. Click **Create** and wait for the project to finish provisioning.  
6. When the **Agents playground** opens, note that a **GPT-4o** model is automatically deployed.  
7. In the left navigation, select **Overview** and copy the **Project endpoint**—you’ll need it for your client application.  


## Step 2 ✍️: Define the custom function

Install the dependencies:
```python
pip install azure-ai-projects
```
Add the function:

```python
# 1. Create a function to submit a support ticket
def submit_support_ticket(email_address: str, description: str) -> str:
    script_dir = Path(__file__).parent
    ticket_number = str(uuid.uuid4()).replace('-', '')[:6]
    file_name = f"ticket-{ticket_number}.txt"
    file_path = script_dir / file_name
    text = f"Support ticket: {ticket_number}\nSubmitted by: {email_address}\nDescription:\n{description}"
    file_path.write_text(text)
    
    message_json = json.dumps({"message": f"Support ticket {ticket_number} submitted. The ticket file is saved as {file_name}"})
    return message_json
```
Register the function:

```python
# Define a set of callable functions
user_functions: Set[Callable[..., Any]] = {
    submit_support_ticket
}
```

## Step 3 🤖: Create the agent 
```python
# 1. Import the libraries
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FunctionTool, ToolSet, ListSortOrder, MessageRole
from user_functions import user_functions

# 2. Connect the client
agent_client = AgentsClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True
    )
)

# 3. Define an agent that can use the custom functions
with agent_client:
    functions = FunctionTool(user_functions)
    toolset = ToolSet()
    toolset.add(functions)
    agent_client.enable_auto_function_calls(toolset)

    agent = agent_client.create_agent(
        model=model_deployment,
        name="support-agent",
        instructions="""You are a technical support agent.
        When a user has a technical issue, you get their email address and a description of the issue.
        Then you use those values to submit a support ticket using the function available to you.
        If a file is saved, tell the user the file name.
        """,
        toolset=toolset
    )

    thread = agent_client.threads.create()
    print(f"You're chatting with: {agent.name} ({agent.id})")

# 4. Send a prompt to the agent
message = agent_client.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_prompt
)
run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)

# 5. Check the run status for failures
if run.status == "failed":
    print(f"Run failed: {run.last_error}")

# 6. Show the latest response from the agent
last_msg = agent_client.messages.get_last_message_text_by_role(
    thread_id=thread.id,
    role=MessageRole.AGENT,
)
if last_msg:
    print(f"Last Message: {last_msg.text.value}")

# 7. Show the conversation history
print("\nConversation Log:\n")
messages = agent_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
for message in messages:
    if message.text_messages:
        last_msg = message.text_messages[-1]
        print(f"{message.role}: {last_msg.text.value}\n")

# 8. Final cleanup
agent_client.delete_agent(agent.id)
print("Deleted agent")
```
## Run the application
```python
az login
python agent.py
```
