# 04 Exercise 🛠️: Develop an Azure AI Agent with the Semantic Kernel SDK

## Objective 🎯
Create an Azure AI Agent (via Semantic Kernel) that reads expense data, e-mails an itemised claim to **expenses@contoso.com**, and confirms completion. 

## Step 1 🚀: Deploy a model in an Azure AI Foundry project

1. Sign in at https://ai.azure.com.
2. In **Explore models and capabilities**, search for **gpt-4o** and choose **Use this model**.
3. When prompted, specify a **project name**, **resource**, **subscription**, **resource group**, and **region**. *If you later hit a quota limit, recreate the resource in a different region.*
4. Select **Create** and wait for provisioning.
5. In the chat playground, note the **deployment name** (`gpt-4o`) and copy the **project endpoint** from **Overview**.

## Step 2 🤖: Create the agent

Install the dependencies:
```python
pip install python-dotenv azure-identity semantic-kernel[azure] 
```

```python
# 1. Add references
from dotenv import load_dotenv
from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents import (
    AzureAIAgent,
    AzureAIAgentSettings,
    AzureAIAgentThread
)
from semantic_kernel.functions import kernel_function
from typing import Annotated

# 2. Email plug-in
class EmailPlugin:
    @kernel_function(description="Sends an email.")
    def send_email(
        self,
        to: Annotated[str, "Recipient"],
        subject: Annotated[str, "Subject"],
        body: Annotated[str, "Body"]
    ):
        print("\nTo:", to)
        print("Subject:", subject)
        print(body, "\n")

async def process_expenses_data(expenses_data: str, prompt: str):
    # 3. Load .env settings
    load_dotenv()
    ai_agent_settings = AzureAIAgentSettings()
    
    # 4. Connect to the Azure AI Foundry project
    async with (
        DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True
        ) as creds,
        AzureAIAgent.create_client(credential=creds) as project_client,
    ):
        # 5. Define an Azure AI agent that e-mails the claim
        agent_def = await project_client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="expenses_agent",
            instructions="""
            You are an AI assistant for expense claim submission.
            When the user requests an expense claim, email expenses@contoso.com 
            with subject 'Expense Claim', an itemised list, and the total.
            Then confirm to the user that you have done so.
            """
        )
        
        # 6. Create the Semantic Kernel agent
        agent = AzureAIAgent(
            client=project_client,
            definition=agent_def,
            plugins=[EmailPlugin()]
        )
        
        # 7. Run the agent
        thread = AzureAIAgentThread(client=project_client)
        try:
            prompt_messages = [f"{prompt}: {expenses_data}"]
            response = await agent.get_response(
                thread_id=thread.id,
                messages=prompt_messages
            )
            print(f"\n# {response.name}:\n{response}")
        finally:
            await thread.delete()
            await project_client.agents.delete_agent(agent.id)
```

## Run the application
```python
az login
python semantic-kernel.py
```
