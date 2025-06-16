# Explore foundation models and capabilities in Azure AI Foundry

## 🧩 Problem Statement

Building generative AI applications requires:
- Selecting the right foundation model from thousands available
- Understanding model capabilities and limitations
- Deploying models efficiently for production use
- Optimizing model performance through prompt engineering
- Scaling solutions for real-world workloads

### Key Challenges:
- How to choose between LLMs vs SLMs?
- When to use proprietary vs open-source models?
- How to evaluate model precision and performance?
- How to optimize outputs through prompt engineering?
- How to deploy and scale models effectively?

## 💡 Solution with Azure

**Azure AI Foundry** provides a comprehensive model catalog with tools for exploration, deployment, and optimization of foundation models. The platform supports both proprietary models (GPT-4, Mistral) and open-source alternatives from Hugging Face, enabling developers to build scalable generative AI applications.

## 🧩 Required Components

### Foundation Model Types

**Language Models**
- Generate, understand, and interact with natural language
- Common use cases: speech-to-text, translation, text classification, entity extraction, summarization, Q&A, reasoning

**Model Categories**
- **Large Language Models (LLMs)**: GPT-4, Mistral Large, Llama3 70B - for deep reasoning and complex content
- **Small Language Models (SLMs)**: Phi3, Mistral OSS, Llama3 8B - efficient and cost-effective
- **Chat Completion Models**: GPT-4, Mistral Large - generate contextual text responses
- **Reasoning Models**: DeepSeek-R1, o1 - enhanced performance for math, coding, science
- **Multi-Modal Models**: GPT-4o, Phi3-vision - process text and images
- **Image Generation**: DALL-E 3, Stability AI - create visuals from text
- **Embedding Models**: Ada, Cohere - convert text to numerical representations
- **Regional/Domain-Specific**: Core42 JAIS (Arabic), NorlaTimeGEN-1 (time series)

### Model Catalogs
- **Hugging Face**: Vast catalog of open-source models
- **GitHub**: Access via GitHub Marketplace and Copilot
- **Azure AI Foundry**: Comprehensive catalog with deployment tools

## 🛠 Architecture & Development

### 🔹 Model Selection Framework

**Step 1: Can AI solve my use case?**
- Explore available models through three catalogs
- Filter and deploy models based on needs
- Test with different model types

**Step 2: How do I select the best model?**

**Evaluation Criteria:**
- **Task Type**: Text only vs multi-modal requirements
- **Precision**: Base model vs fine-tuned for specific skills
- **Openness**: Fine-tuning capability requirements
- **Deployment**: Local vs serverless endpoint needs

**Step 3: Can I scale for real-world workloads?**

**Scaling Considerations:**
- Model deployment strategy
- Model monitoring and optimization
- Prompt management
- Model lifecycle (GenAIOps)

### 🔹 Performance Evaluation

**Model Benchmarks:**
| Benchmark | Description |
|-----------|-------------|
| **Accuracy** | Compares generated text with correct answers (1 if exact match, 0 otherwise) |
| **Coherence** | Measures if output flows smoothly and resembles human language |
| **Fluency** | Assesses grammatical rules, syntax, and vocabulary usage |
| **Groundedness** | Measures alignment between generated answers and input data |
| **GPT Similarity** | Semantic similarity between ground truth and AI predictions |
| **Quality Index** | Aggregate score 0-1, higher is better |
| **Cost** | Price per token for model usage |

**Evaluation Methods:**
- Manual evaluations for initial quality assessment
- Automated evaluations using metrics (precision, recall, F1 score)
- Traditional ML metrics + AI-assisted metrics

### 🔹 Model Deployment

**Deployment Process:**
1. Select model from catalog
2. Deploy to endpoint (creates unique URI and key)
3. Send API requests to endpoint
4. Receive and process responses

**Deployment Options:**

| Service | Supported Models | Hosting | Cost Model | Inferencing |
|---------|-----------------|---------|------------|-------------|
| **Azure OpenAI Service** | Azure OpenAI models | Azure OpenAI resource | - | Token-based billing |
| **Azure AI Foundry Models** | Flagship models (OpenAI + MaaS) | Azure AI Services resource | - | Token-based billing |
| **Serverless compute** | MaaS service models | AI Project resource | Minimal endpoint cost | Token-based billing |
| **Managed compute** | Open and custom models | AI Project resource | Charged per minute | - |

### 🔹 Prompt Engineering Optimization

**Core Patterns:**
1. **Persona Instructions**: "Act as a seasoned marketing professional"
2. **Better Questions**: Guide model to suggest clarifying questions
3. **Format Specification**: Provide templates for output structure
4. **Reasoning Explanation**: Use chain-of-thought for step-by-step logic
5. **Context Addition**: Provide relevant background information

**Advanced Optimization Strategies:**

```
Context Optimization (What model needs to know)
↓
- Retrieval Augmented Generation (RAG): Grounding with data sources
- Prompt Engineering: Optimize through patterns
- Combined Strategies: Mix approaches
- Fine-tuning: Extend training with examples

→ Model Optimization (How model needs to act)
```

## 🆚 Model Comparison Framework

| Aspect | LLMs | SLMs |
|--------|------|------|
| **Use Cases** | Deep reasoning, complex content | Common NLP tasks |
| **Resources** | High compute requirements | Edge device compatible |
| **Cost** | Higher operational cost | Cost-effective |
| **Speed** | Slower processing | Faster response times |
| **Examples** | GPT-4, Mistral Large | Phi3, Mistral OSS |

| Aspect | Proprietary | Open-Source |
|--------|-------------|-------------|
| **Performance** | Cutting-edge, enterprise support | Flexible, customizable |
| **Control** | Limited customization | Full control, fine-tuning |
| **Security** | Built-in enterprise features | Self-managed |
| **Cost** | Higher licensing | Cost-effective |

## 🧠 Best Practices & Considerations

### Transformer Architecture Foundation
- **Parallel Processing**: Words processed independently using attention mechanism
- **Positional Encoding**: Maintains word position information in sentences
- Based on "Attention is all you need" paper (Vaswani et al., 2017)

### Model Selection Best Practices
1. Start with task requirements (text-only vs multi-modal)
2. Consider precision needs (base vs fine-tuned)
3. Evaluate deployment constraints (local vs cloud)
4. Test with benchmarks before production
5. Plan for scaling from prototype to production

### Prompt Engineering Guidelines
- Use system prompts to set model behavior
- Apply one-shot/few-shot examples for pattern recognition
- Request specific output formats with templates
- Implement chain-of-thought for complex reasoning
- Add grounding context for accuracy (RAG pattern)

### Performance Optimization
- Start with prompt engineering (lowest cost/complexity)
- Consider RAG for grounding responses with data
- Use fine-tuning only when necessary
- Combine strategies for optimal results
- Monitor and iterate based on metrics

## 🎯 Exam Simulation Questions

**Q: Which models are best for tasks requiring deep reasoning and extensive context understanding?**
✅ Large Language Models (LLMs) like GPT-4, Mistral Large, Llama3 70B

**Q: What technique involves using a data source to provide grounding context to prompts?**
✅ Retrieval Augmented Generation (RAG)

**Q: Which benchmark measures whether model output flows smoothly and resembles human language?**
✅ Coherence

**Q: What are the four key criteria for selecting the best language model?**
✅ Task type, Precision, Openness, Deployment

**Q: Which deployment option is best for open-source models with custom requirements?**
✅ Managed compute

**Q: What prompt engineering pattern helps models provide step-by-step explanations?**
✅ Chain-of-thought (asking for reasoning explanation)

**Q: Which models are ideal for edge devices with limited resources?**
✅ Small Language Models (SLMs) like Phi3, Mistral OSS

**Q: What is the unique identifier format when deploying a model to Azure AI Foundry?**
✅ https://ai-[hubname].openai.azure.com/openai/deployments/[model-name]/chat/completions?api-version=[version]