# Understand How to Ground Your Language Model

## Problem  
You want to ensure that your LLM-based agent provides accurate, domain-specific, and factual responses.  
How can you ground the language model on your own data to improve reliability?

## Solution with Azure  
Use **Retrieval Augmented Generation (RAG)** to ground your language model.  
RAG retrieves relevant data based on the user’s prompt, augments the prompt with that data, and then uses the LLM to generate a grounded response.

## Required Components  
- Azure AI Foundry project  
- Grounding data (e.g., documents, files, datasets)  
- Supported data sources:
  - Azure Blob Storage  
  - Azure Data Lake Storage Gen2  
  - Microsoft OneLake  
  - Uploaded files/folders  
- RAG pattern implementation

## Architecture / Development  

### RAG Pattern Steps  
1. **Retrieve**: Search for relevant grounding data based on the user’s prompt  
2. **Augment**: Add the retrieved data to the prompt  
3. **Generate**: Use the LLM to produce a grounded response

### Adding Grounding Data in Azure AI Foundry  
- Connect to supported storage services (Blob, Data Lake, OneLake)  
- Upload files or folders directly to the project’s storage  
- Use the connected data as the source for RAG-based flows

## Best Practices / Considerations  
- Ensure grounding data is accurate, up-to-date, and relevant  
- Use RAG when the LLM lacks domain-specific knowledge  
- Monitor the quality of grounded responses using evaluation metrics  
- Protect sensitive data when uploading or connecting sources

## Sample Exam Questions  
1. **What is the purpose of Retrieval Augmented Generation (RAG)?**  
   A. To fine-tune a language model  
   B. To generate synthetic training data  
   C. To ground LLM responses using external data  
   D. To monitor LLM performance  

   **Correct Answer:** C

2. **Which of the following is NOT a supported data source for grounding in Azure AI Foundry?**  
   A. Azure Blob Storage  
   B. Microsoft OneLake  
   C. Google Drive  
   D. Azure Data Lake Storage Gen2  

   **Correct Answer:** C

3. **What are the three main steps in the RAG pattern?**  
   A. Train, Test, Deploy  
   B. Retrieve, Augment, Generate  
   C. Input, Process, Output  
   D. Connect, Monitor, Evaluate  

   **Correct Answer:** B

# Make Your Data Searchable with Azure AI Search

## Problem  
You want your LLM-based agent to retrieve accurate and relevant information from your own data.  
How can you make your data searchable and integrate it into your chat flow?

## Solution with Azure  
Use **Azure AI Search** integrated with **Azure AI Foundry** to index your data and enable efficient retrieval using keyword, semantic, vector, or hybrid search.  
This allows your LLM application to retrieve relevant context and generate grounded responses.

## Required Components  
- Azure AI Foundry project  
- Azure AI Search  
- Data source (e.g., documents, files)  
- Embedding model (e.g., Azure OpenAI)  
- Search index (text-based or vector-based)

## Architecture / Development  

### Creating a Search Index  
- Upload or connect your data to Azure AI Foundry  
- Use Azure AI Search to create an index  
- Choose the indexing method:
  - **Keyword search**: Exact term matching  
  - **Semantic search**: Meaning-based retrieval  
  - **Vector search**: Embedding-based similarity  
  - **Hybrid search**: Combines keyword + vector + optional semantic ranking

### Using Vector Indexes  
- **Embeddings**: Represent text as vectors of floating-point numbers  
- **Cosine similarity**: Measures semantic similarity between query and documents  
- **Embedding model**: Use Azure OpenAI to generate embeddings during indexing  
- **Benefits**:
  - Retrieve semantically similar content  
  - Support multilingual and multimodal data  
  - Improve relevance in generative AI applications

### Querying the Index  
- **Keyword search**: Matches exact terms  
- **Semantic search**: Matches meaning  
- **Vector search**: Matches vector similarity  
- **Hybrid search**: Combines all for best accuracy and flexibility

## Best Practices / Considerations  
- Use **vector search** for semantic-rich applications  
- Use **hybrid search** for optimal balance of precision and relevance  
- Choose the right embedding model for your data type  
- Regularly update your index as data changes

## Sample Exam Questions  
1. **What is the purpose of using vector embeddings in Azure AI Search?**  
   A. To compress data  
   B. To store documents  
   C. To enable semantic similarity search  
   D. To encrypt search queries  

   **Correct Answer:** C
2. **Which search method combines keyword, vector, and semantic ranking?**  
   A. Semantic search  
   B. Hybrid search  
   C. Full-text search  
   D. Indexed search  

   **Correct Answer:** B

3. **What is cosine similarity used for in vector search?**  
   A. To sort documents alphabetically  
   B. To measure the angle between keyword matches  
   C. To calculate semantic similarity between vectors  
   D. To encrypt vector data  

   **Correct Answer:** C


# Create a RAG-based client application

When you've created an Azure AI Search index for your contextual data, you can use it with an OpenAI model. To ground prompts with data from your index, the Azure OpenAI SDK supports extending the request with connection details for the index. The pattern for using this approach when working with an Azure AI Foundry project is shown in the following diagram.
1. Use an Azure AI Foundry project client to retrieve connection details for the Azure AI Search index and an OpenAI ChatClient object.
2. Add the index connection information to the ChatClient configuration so that it can be searched for grounding data based on the user prompt.
3. Submit the grounded prompt to the Azure OpenAI model to generate a contextualized response.
The following code example shows how to implement this pattern.

The following code example shows how to implement this pattern.
```python
from openai import AzureOpenAI

# Get an Azure OpenAI chat client
chat_client = AzureOpenAI(
    api_version = "2024-12-01-preview",
    azure_endpoint = open_ai_endpoint,
    api_key = open_ai_key
)

# Initialize prompt with system message
prompt = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

# Add a user input message to the prompt
input_text = input("Enter a question: ")
prompt.append({"role": "user", "content": input_text})

# Additional parameters to apply RAG pattern using the AI Search index
rag_params = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": search_url,
                "index_name": "index_name",
                "authentication": {
                    "type": "api_key",
                    "key": search_key,
                }
            }
        }
    ],
}

# Submit the prompt with the index information
response = chat_client.chat.completions.create(
    model="<model_deployment_name>",
    messages=prompt,
    extra_body=rag_params
)

# Print the contextualized response
completion = response.choices[0].message.content
print(completion)
```
In this example, the search against the index is keyword-based - in other words, the query consists of the text in the user prompt, which is matched to text in the indexed documents. When using an index that supports it, an alternative approach is to use a vector-based query in which the index and the query use numeric vectors to represent text tokens. Searching with vectors enables matching based on semantic similarity as well as literal text matches.

To use a vector-based query, you can modify the specification of the Azure AI Search data source details to include an embedding model; which is then used to vectorize the query text.

```python
rag_params = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": search_url,
                "index_name": "index_name",
                "authentication": {
                    "type": "api_key",
                    "key": search_key,
                },
                # Params for vector-based query
                "query_type": "vector",
                "embedding_dependency": {
                    "type": "deployment_name",
                    "deployment_name": "<embedding_model_deployment_name>",
                },
            }
        }
    ],
}
```
# Implement RAG in a Prompt Flow

## Problem  
You want to build a generative AI application that uses your own data to generate accurate, grounded responses.  
How can you implement the Retrieval Augmented Generation (RAG) pattern in a Prompt Flow using Azure AI Foundry?

## Solution with Azure  
Use **Prompt Flow** to define a flow that implements the **RAG pattern** by retrieving relevant data from an index and using it to augment prompts sent to a language model (LLM).

## Required Components  
- Azure AI Foundry project  
- Uploaded data and created search index (via Azure AI Search)  
- Prompt Flow with:
  - LLM tool  
  - Index Lookup tool  
  - Python tool (optional for formatting)  
  - Prompt variants  
- Sample: **Multi-round Q&A on your data**

## Architecture / Development  

### Flow Structure  
1. **Modify Query with History**  
   - Use an LLM node to combine the user’s latest question with chat history  
   - Output: a contextualized query

2. **Look Up Relevant Information**  
   - Use the **Index Lookup tool** to query the search index  
   - Retrieve top N relevant documents

3. **Generate Prompt Context**  
   - Use a **Python node** to:
     - Iterate over retrieved documents  
     - Combine content and sources into a single string  
   - Output: formatted context string

4. **Define Prompt Variants**  
   - Use variants to test different system messages or prompt structures  
   - Goal: improve groundedness and factual accuracy

5. **Chat with Context**  
   - Use an LLM node to generate a response using the augmented prompt  
   - Output: final response to user

## Best Practices / Considerations  
- Use the **Multi-round Q&A** sample as a starting point  
- Ensure your index is optimized for vector or hybrid search  
- Use prompt variants to experiment with different grounding strategies  
- Format retrieved context clearly to improve LLM comprehension  
- Deploy the flow to an endpoint for real-time use

## Sample Exam Questions  
1. **Which tool is essential for retrieving data from an index in a RAG-based flow?**  
   A. Python tool  
   B. Prompt tool  
   C. Index Lookup tool  
   D. Variant tool  

   **Correct Answer:** C

2. **What is the purpose of the Python node in a RAG flow?**  
   A. To generate embeddings  
   B. To format retrieved documents into a prompt context  
   C. To deploy the flow  
   D. To store chat history  

   **Correct Answer:** B

3. **What does a prompt variant allow you to do?**  
   A. Change the LLM model  
   B. Create multiple versions of a prompt for comparison  
   C. Switch between different flows  
   D. Encrypt user input  

   **Correct Answer:** B
