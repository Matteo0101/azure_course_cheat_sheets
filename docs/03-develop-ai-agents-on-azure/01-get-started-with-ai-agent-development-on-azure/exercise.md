# 01 Exercise 🛠️: Explore AI Agent Development 🤖

## 📚 Table of Contents

1. [📌 Overview](#overview)  
2. [🛠️ Prerequisites](#prerequisites)  
3. [🚀 Create an Azure AI Foundry Project and Agent](#create-an-azure-ai-foundry-project-and-agent)  
4. [🧠 Create Your Agent](#create-your-agent)  
5. [🧪 Test Your Agent](#test-your-agent)  
6. [🧹 Clean Up](#clean-up)  

---

## 📌 Overview

In this exercise, you will use the **Azure AI Agent** service in the Azure AI Foundry portal to create a simple AI agent that assists employees with expense claims.

---

## 🛠️ Prerequisites

- An active Azure subscription  
- Access to the [Azure AI Foundry portal](https://ai.azure.com)  
- **Optional but recommended:** A resource group dedicated to AI exercises  

---

## 🚀 Create an Azure AI Foundry Project and Agent

1. **Sign in to Azure AI Foundry**  
   - Open your browser and go to:  
     ```
     https://ai.azure.com
     ```  
   - Sign in with your Azure credentials.  
   - Close any tips or quick-start panes.  
   - If needed, click the Azure AI Foundry logo (top-left) to return to the Home page.  

2. **Start Agent Creation**  
   - On the Home page, click **Create an agent**.

3. **Configure Project**  
   - **Project name:** Enter a valid name (e.g., `ExpensesAgentProject`).  
   - Expand **Advanced options** and fill in:  
     - **Azure AI Foundry resource:** a valid resource name  
     - **Subscription:** your Azure subscription  
     - **Resource group:** select an existing group or create a new one  
     - **Region:** any AI Services–supported region<sup>1</sup>  
   - Click **Create** and wait for provisioning.

4. **Deployment**  
   - Once the project is created, the **Agents playground** opens automatically.  
   - A **GPT-4o** base model is deployed by default.

> <sup>1</sup> Some AI resources have regional model quotas. If you hit quota limits later, consider deploying in another region.

---

## 🧠 Create Your Agent

You will build a simple agent that answers questions based on a corporate expenses policy.

1. **Download the Policy Document** 📄  
   - In a new browser tab, download the Contoso expenses policy:  
     ```
     https://raw.githubusercontent.com/MicrosoftLearning/mslearn-ai-agents/main/Labfiles/01-agent-fundamentals/Expenses_Policy.docx
     ```  
   - Save it locally as `Expenses_Policy.docx`.

2. **Open the Setup Pane** 🧩  
   - Return to the Agents playground tab.  
   - Locate the **Setup** pane (side or below the chat window).

3. **Agent Settings** ⚙️  
   - **Agent name:** `ExpensesAgent`  
   - **Model deployment:** ensure your GPT-4o deployment is selected  
   - **Instructions:** click into the Instructions box and paste:

     ```text
     You are an AI assistant for corporate expenses.
     You answer questions about expenses based on the expenses policy data.
     If a user wants to submit an expense claim, you get their email address,
     a description of the claim, and the amount to be claimed and write the
     claim details to a text file that the user can download.
     ```

4. **Add Knowledge** 📚  
   - Under **Knowledge**, click **+ Add** → **Files**.  
   - In the dialog, create a new vector store named `Expenses_Vector_Store` and upload `Expenses_Policy.docx`.  
   - Verify that `Expenses_Vector_Store` appears in the Setup pane with **1 file**.

5. **Add Actions** 🧠💻  
   - Under **Actions**, click **+ Add** → **Code interpreter**, then click **Save**.  
   - (No additional files are needed for the code interpreter.)

---

## 🧪 Test Your Agent

Use the playground chat to verify your agent’s behavior.

1. **Basic Query** 💬  
   - Prompt:
     ```
     What's the maximum I can claim for meals?
     ```
   - The agent should answer based on the policy document.

2. **Submit a Claim – Part 1** 📝  
   - Prompt:
     ```
     I'd like to submit a claim for a meal.
     ```
   - The agent should ask for your email address.

3. **Submit a Claim – Part 2** 📧  
   - Provide an email (e.g., `fred@contoso.com`).  
   - The agent will then ask for a description and amount.

4. **Submit a Claim – Part 3** 💲  
   - Prompt:
     ```
     Breakfast cost me $20.
     ```
   - The agent will use the code interpreter to generate a text file and provide a download link.

5. **Verify** ✅  
   - Download the generated `.txt` file and open it to confirm the expense claim details.