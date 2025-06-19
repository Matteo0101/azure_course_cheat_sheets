# Azure AI Language - Question Answering Solution

## 🧩 Problem

You need to provide automated question-answering support using a large FAQ knowledge base. Static FAQ pages are hard to search, especially as the number of Q&A pairs grows.

## 💡 Solution with Azure

Use the **Custom Question Answering** feature in Azure AI Language to build a knowledge base that can be queried using natural language. The service allows integration with bots or custom applications for real-time Q&A.

## 🧱 Required Components

- Azure AI Language resource (with Custom Question Answering enabled)
- Azure AI Search resource (same global region)
- Language Studio
- Knowledge base sources (e.g., URL, documents, chit-chat sets)
- Deployment name and project name
- SDK (azure-ai-language-questionanswering for Python/C#)
- VS Code for app development

## 🏗️ Architecture & Development

### 1. Provision the AI Language + Azure Search Resources

- Create a Language Service in Azure
- Enable Custom Question Answering
- Select same region for Azure Search
- Pricing tier: F0 (free) or S
- Retrieve endpoint and subscription key from Keys and Endpoint

### 2. Create a Question Answering Project in Language Studio

- Go to: https://language.cognitive.azure.com
- Select Custom question answering
- Set language (English), project name (e.g. LearnFAQ), and default fallback answer
- Complete the wizard

### 3. Add Sources to the Knowledge Base

**Add FAQ from URL:**
https://docs.microsoft.com/en-us/learn/support/faq

**Add Chit-chat dataset:** Friendly

**Edit KB:**
- Add Q: What are Microsoft credentials?
- A: Microsoft credentials enable you to validate and prove your skills...
- Add alternate question: How can I demonstrate my Microsoft technology skills?
- Add follow-up prompt to link to: https://docs.microsoft.com/learn/credentials/
- Show in contextual flow only

### 4. Train and Test the Knowledge Base

Click **Save**, then **Test**

**Sample test queries:**
- "Hello" → chit-chat
- "What is Microsoft Learn?" → FAQ
- "Tell me about Microsoft credentials" → your custom Q&A

### 5. Deploy the Knowledge Base

- In Language Studio, click **Deploy**
- After success, click **Get prediction URL**
- Note projectName and deploymentName (e.g., LearnFAQ, production)

### 6. Build a Question Answering App

Clone repo: https://github.com/MicrosoftLearning/mslearn-ai-language

Navigate to:
- `Labfiles/02-qna/CSharp/qna-app` or
- `Labfiles/02-qna/Python/qna-app`

**Install SDK:**

**C#:**
```bash
dotnet add package Azure.AI.Language.QuestionAnswering
```

**Python:**
```bash
pip install azure-ai-language-questionanswering
```

### 7. Configure App

Open:
- `.env` for Python
- `appsettings.json` for C#

Set:
- `ai_key`
- `ai_endpoint`
- `project_name`
- `deployment_name`

### 8. Implement Q&A Logic

**Python:**
```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

credential = AzureKeyCredential(ai_key)
ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

while True:
    user_question = input("Question:\n")
    if user_question.lower() == "quit":
        break
    response = ai_client.get_answers(
        question=user_question,
        project_name=ai_project_name,
        deployment_name=ai_deployment_name
    )
    for candidate in response.answers:
        print(candidate.answer)
        print("Confidence:", candidate.confidence)
        print("Source:", candidate.source)
```

**C#:**
```csharp
using Azure;
using Azure.AI.Language.QuestionAnswering;

AzureKeyCredential credentials = new AzureKeyCredential(aiSvcKey);
Uri endpoint = new Uri(aiSvcEndpoint);
QuestionAnsweringClient aiClient = new QuestionAnsweringClient(endpoint, credentials);

string user_question = "";
while (true)
{
    Console.Write("Question: ");
    user_question = Console.ReadLine();
    if (user_question.ToLower() == "quit") break;

    QuestionAnsweringProject project = new QuestionAnsweringProject(projectName, deploymentName);
    var response = aiClient.GetAnswers(user_question, project);
    foreach (var answer in response.Value.Answers)
    {
        Console.WriteLine(answer.Answer);
        Console.WriteLine($"Confidence: {answer.Confidence:P2}");
        Console.WriteLine($"Source: {answer.Source}");
    }
}
```

**Run with:**
- `dotnet run` (C#)
- `python qna-app.py` (Python)

## ✅ Best Practices & Considerations

- Use chit-chat datasets to handle casual messages
- Enable multi-turn prompts for refinement
- Deploy to production after thorough testing
- Use alternate questions to improve matching
- Test edge cases where no answer is returned
- Configure fallback responses thoughtfully

## ❓ Sample Exam Questions

**Q: Which Azure service is used to create a searchable Q&A knowledge base?**
→ Azure AI Language - Custom Question Answering

**Q: What is required to support Custom Question Answering indexing?**
→ Azure AI Search

**Q: How do you handle multiple ways of asking the same question?**
→ Use alternate questions in the knowledge base

**Q: What enables follow-up questions in Q&A projects?**
→ Multi-turn prompts

**Q: Where do you define the project and deployment name?**
→ In the deployment settings and application config files