# 🤖 Explore AI Agent Development with Azure AI Foundry

## 🛑 Problem
You want to create a generative AI agent that helps employees with expense-related tasks, such as answering questions about corporate expense policies and assisting in submitting expense claims—using a no-code/low-code approach within the Azure AI Foundry portal.

## ✅ Solution with Azure
Use Azure AI Foundry Agent Service to:

- Deploy a GPT-4o-based model
- Ground it with policy documents
- Enable it to execute code-based actions via a code interpreter tool
- Interact through a conversational UI for testing and iteration

## 🧩 Required Components

| Component | Description |
|-----------|-------------|
| Azure AI Foundry Portal | Web interface to create and manage agent projects |
| Model | GPT-4o model (auto-deployed) |
| Knowledge Source | Expenses_policy.docx uploaded and stored in a Vector Store |
| Tool | Code interpreter to perform dynamic actions like writing files |
| Thread / Playground | Interface to test and interact with the agent |
| Project Resource Settings | Subscription, Resource Group, Region, and Azure AI Foundry resource |

## 🏗️ Architecture / Development

### 🧱 Step-by-step Setup

#### Create Project and Agent
1. Go to: https://ai.azure.com
2. Create a project (e.g., ExpenseClaimsProject)
3. Choose Azure resource, subscription, region, and resource group
4. Project includes default GPT-4o model deployment

#### Rename and Configure Agent
1. Set name to: **ExpensesAgent**
2. Instructions:
```
You are an AI assistant for corporate expenses.
You answer questions about expenses based on the expenses policy data.
If a user wants to submit an expense claim, you get their email address, a description of the claim, and the amount to be claimed and write the claim details to a text file that the user can download.
```

#### Upload Knowledge Document
1. Download Expenses_policy.docx
2. Add it as a file-based knowledge source using:
   - New vector store: **Expenses_Vector_Store**

#### Add Code Interpreter Tool
Add the Code Interpreter in the Actions section (no upload needed)

## 🔄 Test the Agent

### Test Prompt 1:
**"What's the maximum I can claim for meals?"**
➤ Agent should answer based on uploaded document.

### Test Prompt 2:
**"I'd like to submit a claim for a meal."**
➤ Agent prompts for email, claim description, and amount.

### Follow-up Prompt:
**"fred@contoso.com"** → agent confirms and continues
**"Breakfast cost me $20."** → agent uses code interpreter to:
- Generate .txt expense claim file
- Provide download link for user

## 📁 Output Example
The file generated contains:
```
Email: fred@contoso.com
Description: Breakfast
Amount: $20
```

## 🧠 Best Practices / Considerations

- Ensure uploaded documents are relevant and clean, as they directly impact agent grounding accuracy.
- The code interpreter enables agents to handle simple automations like file generation, making the solution extensible.
- Use GPT-4o for multimodal and advanced language capabilities.
- Test iteratively in the Playground to verify behavior and improve prompts.
- Be aware of rate limits and regional quotas—switch regions or models if necessary.

## ❓ Sample Exam Questions

### 🧠 What is the purpose of uploading a .docx file as knowledge in an AI agent?
A. To log all chat history  
B. To replace model instructions  
✅ **C. To ground agent responses in document-based data**  
D. To store training data

### 💬 What is the function of the "Code Interpreter" in Azure AI Foundry agents?
A. To send API calls to other Azure services  
✅ **B. To generate and run Python code for dynamic tasks like creating text files**  
C. To translate user input to SQL queries  
D. To analyze user sentiment

### ⚙️ In the agent setup, what is the function of the 'Instructions' field?
A. It defines user authentication steps  
✅ **B. It sets the behavioral logic and task scope for the agent**  
C. It lists prohibited topics for the agent  
D. It initializes the model weights

### 📦 What is a 'Vector Store' used for in Azure AI Foundry Agent Service?
A. Caching model responses  
✅ **B. Storing and indexing documents for semantic search grounding**  
C. Managing agent credentials  
D. Persisting chat threads

### ⚠️ If your agent does not respond due to model quota limits, what should you do?
A. Change model deployment to Copilot Studio  
✅ **B. Try again later or increase model quota in the Azure portal**  
C. Restart your browser  
D. Disable the code interpreter