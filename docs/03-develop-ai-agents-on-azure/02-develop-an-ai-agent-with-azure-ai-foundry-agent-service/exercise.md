# 02 Exercise 🛠️: Build an AI Agent with Code Interpreter

In this hands-on lab, you will use **Azure AI Agent Service** to build an agent that analyzes data and dynamically generates charts using the built-in **Code Interpreter** tool.  
---

## 📌 Table of Contents

1. [Create Azure AI Foundry Project](#create-azure-ai-foundry-project)
2. [Create an Agent Client App](#create-an-agent-client-app)
3. [Configure Application Settings](#configure-application-settings)
4. [Write Code for the Agent App](#write-code-for-the-agent-app)
5. [Sign into Azure and Run the App](#sign-into-azure-and-run-the-app)
6. [📊 Summary](#-summary)
7. [🧹 Clean Up](#-clean-up)

---

## 🔧 Create Azure AI Foundry Project

1. Open [https://ai.azure.com](https://ai.azure.com) and sign in.
2. Click **Create an agent**.
3. When prompted:
   - Provide a valid **Project name**
   - Expand **Advanced options**:
     - **Azure AI Foundry resource**: your resource name  
     - **Subscription**: your Azure subscription  
     - **Resource group**: existing or new  
     - **Region**: any supported region  
4. Click **Create** and wait for provisioning.
5. The **Agents Playground** will open automatically.
6. In the left pane, click **Overview**.
7. Copy your **project endpoint** and save it for later use.

---

## 💻 Create an Agent Client App

1. Clone the provided GitHub repo:

```bash
git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
cd ai-agents/Labfiles/02-build-ai-agent/Python
ls -a -l
```
2. The folder includes:
    - Application code
    - Configuration file (.env)
    - Sample data file: data.txt

## ⚙️ Configure Application Settings
 1. Set up your Python virtual environment:
 ```bash
python -m venv labenv
./labenv/Scripts/Activate.ps1
pip install -r requirements.txt azure-ai-projects
```
2. Open the .env config file:
 ```bash
 code .env
  ```
3. Replace your_project_endpoint with your actual Foundry project endpoint.

4. Save (CTRL+S) and close (CTRL+Q) the editor.

## 🧠 Write Code for the Agent App
Assicurati di rispettare l’indentazione corretta durante l’inserimento del codice.

1. Apri il file
 ```bash
 code agent.py
  ```

2. Import needed classes
```bash
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FilePurpose, CodeInterpreterTool, ListSortOrder, MessageRole
  ```

3. Connect to the project
```bash
agent_client = AgentsClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True
    )
)
with agent_client:
  ```

4. Upload data and create a Code Interpreter Tool
```bash
file = agent_client.files.upload_and_poll(file_path=file_path, purpose=FilePurpose.AGENTS)
print(f"Uploaded {file.filename}")

code_interpreter = CodeInterpreterTool(file_ids=[file.id])
  ```

5. Define the Agent
```bash
agent = agent_client.create_agent(
    model=model_deployment,
    name="data-agent",
    instructions="You are an AI agent that analyzes the data in the file that has been uploaded. If the user requests a chart, create it and save it as a .png file.",
    tools=code_interpreter.definitions,
    tool_resources=code_interpreter.resources,
)
print(f"Using agent: {agent.name}")
  ```

6. Create a thread for the conversation
```bash
thread = agent_client.threads.create()
  ```

7. Send the prompt to the Agent
```bash
message = agent_client.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_prompt,
)

run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
  ```

8. Check errors
```bash
if run.status == "failed":
    print(f"Run failed: {run.last_error}")
  ```

9. Retrieve the last agent answer
```bash
last_msg = agent_client.messages.get_last_message_text_by_role(
    thread_id=thread.id,
    role=MessageRole.AGENT,
)
if last_msg:
    print(f"Last Message: {last_msg.text.value}")
  ```

10. Show history of the conversation
```bash
print("\nConversation Log:\n")
messages = agent_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
for message in messages:
    if message.text_messages:
        last_msg = message.text_messages[-1]
        print(f"{message.role}: {last_msg.text.value}\n")
  ```


11. Download generated files
```bash
for msg in messages:
    for img in msg.image_contents:
        file_id = img.image_file.file_id
        file_name = f"{file_id}_image_file.png"
        agent_client.files.save(file_id=file_id, file_name=file_name)
        print(f"Saved image file to: {Path.cwd() / file_name}")
  ```

12. Delete resources
```bash
agent_client.delete_agent(agent.id)
  ```

## 🔐 Sign into Azure and Run the App
1. Autenticate yourself:
```bash
az login 
```

2. Esecute the app:
```bash
python agent.py 
```

3. Insert the prompt:
```bash
"What's the category with the highest cost?"
"Create a pie chart showing cost by category"
```

4. Continue the conversation, so insert 'quit' to exit.

5. Download the generated files .png:
```bash
download ./<file_name>.png
```