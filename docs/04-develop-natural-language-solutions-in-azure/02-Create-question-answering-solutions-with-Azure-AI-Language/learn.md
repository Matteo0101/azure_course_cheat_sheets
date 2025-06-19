# Azure AI Language - Question Answering Solutions

## 🧩 Problem

You need to build an application that can automatically respond to user questions in natural language, such as an intelligent FAQ system, providing accurate and relevant answers.

## 💡 Solution with Azure

Use the **question answering capability** of the Azure AI Language service to create, test, and publish a knowledge base of question-answer pairs. This knowledge base can be integrated into applications or conversational bots.

## 🧱 Required Components

- **Azure AI Language resource**
- **Azure AI Search resource** (to index the KB)
- **Language Studio** (for GUI-based creation and management)
- **REST API or SDK** (optional, for programmatic access)

### Data Sources:
- Web pages with FAQs
- Structured documents (e.g., brochures, user guides)
- Built-in chit-chat datasets
- (Optional) JSON file to define synonyms

## 🏗️ Architecture & Development

### 1. Create the Knowledge Base

1. Sign in to **Azure Portal**
2. Create a Language resource and enable question answering
3. Associate it with an **Azure AI Search** index
4. In **Language Studio**:
   - Create a Custom question answering project
   - Add data sources (URLs, files, chit-chat sets)

### 2. Implement Multi-Turn Conversations

- Add follow-up prompts to questions to clarify user intent
- Link follow-ups to existing answers or create new ones
- Ensure responses are context-aware within multi-turn flow

### 3. Test and Publish the KB

- Test questions interactively in Language Studio
- Review confidence scores and possible answer alternatives
- When ready, deploy the KB to a REST endpoint for external use

### 4. Use the Knowledge Base via API

Send HTTP POST requests with JSON like:

```json
{
  "question": "What do I need to do to cancel a reservation?",
  "top": 2,
  "scoreThreshold": 20,
  "strictFilters": [
    {
      "name": "category",
      "value": "api"
    }
  ]
}
```

**Response includes:** matched question, answer, score, and metadata

### 5. Improve Performance with Active Learning

- Enable automatic suggestion of alternate phrasings
- Use Review suggestions pane to approve/reject them
- Add alternate questions manually if needed

### 6. Enhance with Synonyms

Improve understanding of user input by submitting synonyms like:

```json
{
  "synonyms": [
    {
      "alterations": ["reservation", "booking"]
    }
  ]
}
```

## ✅ Best Practices & Considerations

- Combine question answering with language understanding when user input triggers different actions or intents
- Use multi-turn interactions to clarify ambiguous queries
- Regularly review suggestions from active learning
- Add synonyms for domain-specific terminology
- Define appropriate score thresholds for reliable responses

## ❓ Sample Exam Questions

**Q: What is the primary difference between question answering and language understanding in Azure AI Language?**
→ Question answering returns a static answer; language understanding identifies intents and entities.

**Q: Which component is required to host the index for a custom question answering project?**
→ Azure AI Search

**Q: How can you improve the accuracy of a knowledge base over time?**
→ Enable active learning and define alternate phrasings

**Q: What does the scoreThreshold parameter control in a question answering API request?**
→ Minimum confidence score required for an answer to be returned

**Q: What is the purpose of defining synonyms in a question answering project?**
→ To handle variations in terminology and improve answer matching