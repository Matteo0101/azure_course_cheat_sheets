# Development Lifecycle of a Large Language Model (LLM) Application

## Problem  
You want to build and deploy a robust LLM-based application (e.g., for classifying news articles).  
How do you structure the development process to ensure quality, scalability, and maintainability?

## Solution with Azure  
Follow the **LLM application development lifecycle**, which includes four iterative stages:
1. Initialization
2. Experimentation
3. Evaluation and refinement
4. Production

## Required Components  
- Sample dataset (small and large)
- Prompt design
- Flow design (e.g., using Prompt Flow)
- Monitoring tools for production

## Architecture / Development  

### 1. Initialization  
- **Define the objective** (e.g., classify news articles into categories)  
- **Collect a sample dataset** (diverse, representative, privacy-compliant)  
- **Build a basic prompt**  
- **Design the flow** (how input is processed and output is generated)

### 2. Experimentation  
- Run the flow against the sample dataset  
- Evaluate prompt performance  
- If results are unsatisfactory, modify the prompt or flow  
- Iterate until results are acceptable

### 3. Evaluation and Refinement  
- Test the flow with a larger dataset  
- Assess generalization and identify bottlenecks  
- Refine the flow and re-test with smaller datasets before scaling  
- Repeat until the solution is robust

### 4. Production  
- Optimize the flow for performance  
- Deploy the flow to an endpoint  
- Monitor usage and collect feedback  
- Continuously improve based on real-world performance
## Best Practices / Considerations  
- Ensure datasets are diverse and anonymized  
- Use small datasets for quick iteration during refinement  
- Monitor deployed flows to detect drift or performance issues  
- Be prepared to revert to experimentation if needed

## Sample Exam Questions  
1. **Which phase involves defining the use case and designing the solution?**  
   A. Experimentation  
   B. Initialization  
   C. Production  
   D. Refinement  

   **Correct Answer:** B

2. **What is the purpose of the experimentation phase?**  
   A. Deploy the application  
   B. Collect user feedback  
   C. Test and refine the flow using a sample dataset  
   D. Monitor performance  

   **Correct Answer:** C

3. **Why should you test changes on a small dataset before using a large one?**  
   A. It’s more accurate  
   B. It’s faster and helps catch issues early  
   C. It’s required by Azure  
   D. It avoids overfitting  

   **Correct Answer:** B

# Core Components and Flow Types in Prompt Flow

## Problem  
You want to build an LLM application using Prompt Flow in Azure AI Foundry.  
How do you structure the flow and choose the right tools and flow type?

## Solution with Azure  
Use **Prompt Flow**, a feature in Azure AI Foundry, to create executable workflows (flows) composed of inputs, nodes (tools), and outputs.  
Choose the appropriate **flow type** based on your application needs: standard, chat, or evaluation.

## Required Components  
- **Inputs**: Data passed into the flow (e.g., strings, integers, booleans)  
- **Nodes**: Tools that perform tasks (e.g., LLM, Python, Prompt tools)  
- **Outputs**: Results produced by the flow  
- **Flow types**: Standard, Chat, Evaluation

## Architecture / Development  

### Flow Structure  
- **Inputs**: Define the data the flow will receive  
- **Nodes**: Add tools to perform operations  
  - **LLM Tool**: For custom prompt execution using LLMs  
  - **Python Tool**: For executing custom Python scripts  
  - **Prompt Tool**: For preparing and formatting prompts  
- **Outputs**: Define what the flow should return

### Node Connectivity  
- Nodes can use:
  - Flow-level inputs  
  - Outputs from other nodes  
- You can reuse tools and chain nodes to build complex logic

### Flow Types  
- **Standard Flow**: General-purpose LLM applications  
- **Chat Flow**: Designed for conversational agents  
- **Evaluation Flow**: Used to assess and improve model performance
## Best Practices / Considerations  
- Use the appropriate tool for each task  
- Define clear input/output interfaces for each node  
- Use evaluation flows to iteratively improve your application  
- Create custom tools if built-in tools don’t meet your needs

## Sample Exam Questions  
1. **Which component represents a processing step in a prompt flow?**  
   A. Input  
   B. Node  
   C. Output  
   D. Dataset  

   **Correct Answer:** B

2. **What is the purpose of the Prompt Tool in a flow?**  
   A. To execute Python code  
   B. To call external APIs  
   C. To prepare prompts for LLMs  
   D. To monitor flow performance  

   **Correct Answer:** C
3. **Which flow type is best suited for evaluating model performance?**  
   A. Standard Flow  
   B. Chat Flow  
   C. Evaluation Flow  
   D. Custom Flow  

   **Correct Answer:** C

# Explore Connections and Runtimes in Prompt Flow

## Problem  
You want your LLM application to interact with external services (e.g., Azure OpenAI, Azure AI Search) and run reliably in a controlled compute environment.  
How do you securely configure these integrations and execute your flows?

## Solution with Azure  
Use **Prompt Flow connections** to securely link your flow to external services, and **Prompt Flow runtimes** to provide the compute and environment needed to run your flows.

## Required Components  
- **Connections** to external services (e.g., Azure OpenAI, Azure AI Search)  
- **Runtimes**: Compute + Environment  
- **Azure Key Vault** (for secure credential storage)

## Architecture / Development  

### Connections  
- Secure links between Prompt Flow and external services  
- Store credentials (e.g., API keys, endpoints) securely in Azure Key Vault  
- Required for tools that access external APIs or services

| Connection Type   | Required By Tools             |
|-------------------|-------------------------------|
| Azure OpenAI      | LLM, Python                   |
| OpenAI            | LLM, Python                   |
| Azure AI Search   | Vector DB Lookup, Python      |
| Serp              | Serp API, Python              |
| Custom            | Python                        |

- Connections automate credential management and enable secure data transfer  
- Reusable across multiple flows

### Runtimes  
- A **runtime** = Compute instance + Environment  
- **Compute**: Provides the resources to run the flow  
- **Environment**: Defines packages and libraries needed  
- Default environment available for quick testing  
- Custom environments can be created for specific dependencies

## Best Practices / Considerations  
- Always configure required connections before running flows  
- Use Azure Key Vault to avoid exposing secrets  
- Use default runtime for development; switch to custom environments for production  
- Monitor runtime performance and resource usage

## Sample Exam Questions  
1. **What is the purpose of a connection in Prompt Flow?**  
   A. To define the flow's output  
   B. To store datasets  
   C. To securely link to external services  
   D. To monitor runtime performance  

   **Correct Answer:** C

2. **Which component defines the packages and libraries needed to run a flow?**  
   A. Connection  
   B. Node  
   C. Environment  
   D. Dataset  

   **Correct Answer:** C

3. **Where are secrets like API keys stored when using connections?**  
   A. In the flow definition  
   B. In Azure Key Vault  
   C. In the runtime  
   D. In the tool configuration  

   **Correct Answer:** B

# Explore Variants and Monitoring Options in Prompt Flow

## Problem  
You want to optimize your LLM application's performance and ensure it meets real-world expectations.  
How can you fine-tune your flow, deploy it for real-time use, and monitor its effectiveness?

## Solution with Azure  
Use **variants** to optimize LLM tool nodes, **deploy flows to endpoints** for real-time integration, and **monitor evaluation metrics** to assess and improve performance.

## Required Components  
- LLM tool with variant support  
- Online endpoint for deployment  
- Evaluation metrics (e.g., groundedness, relevance, fluency)  
- End-user feedback and ground truth data

## Architecture / Development  

### Variants  
- **Definition**: Versions of an LLM tool node with different prompt content or connection settings  
- **Use cases**: Summarization, classification, etc.  
- **Benefits**:
  - Improve generation quality
  - Simplify prompt tuning and version tracking
  - Enable side-by-side comparisons
  - Increase productivity through faster iteration

### Deployment to Endpoint  
- Deploy flow to an **online endpoint** to integrate with external applications  
- Prompt Flow generates:
  - **URL** for API access  
  - **Key** for secure invocation  
- Real-time execution of flows (e.g., chat or agentic responses)

### Monitoring Evaluation Metrics  
- **Purpose**: Ensure LLM output meets quality standards  
- **Methods**:
  - Collect end-user feedback  
  - Compare predictions with ground truth  
- **Key Metrics**:
  - **Groundedness**: Alignment with source data  
  - **Relevance**: Pertinence to input  
  - **Coherence**: Logical flow and readability  
  - **Fluency**: Grammatical correctness  
  - **Similarity**: Semantic match with expected output
## Best Practices / Considerations  
- Use variants to test and compare prompt strategies  
- Deploy only after thorough evaluation  
- Monitor flows continuously using metrics and feedback  
- Revert to experimentation when performance drops

## Sample Exam Questions  
1. **What is a variant in Prompt Flow?**  
   A. A different flow type  
   B. A version of a tool node with distinct settings  
   C. A runtime configuration  
   D. A deployment environment  

   **Correct Answer:** B

2. **Which metric evaluates how well the LLM output aligns with the source data?**  
   A. Fluency  
   B. Groundedness  
   C. Coherence  
   D. Similarity  

   **Correct Answer:** B

3. **What happens when you deploy a flow to an endpoint?**  
   A. It becomes read-only  
   B. It is converted to a Python script  
   C. It can be invoked via a URL and key  
   D. It is automatically optimized  

   **Correct Answer:** C
