## Assess the Model Performance

**Problem**  
How can you evaluate the effectiveness, quality, and safety of a language model or generative AI application during development and deployment?

**Solution with Azure**  
Use a combination of model benchmarks, manual evaluations, AI-assisted metrics, and NLP metrics to assess model performance. Evaluate both individual models and complete chat flows to ensure reliability and alignment with user expectations.

**Required Components**  
- Azure AI Foundry portal (for model benchmarks)
- Human evaluators (for manual assessments)
- AI-assisted evaluation tools
- NLP metric tools (e.g., BLEU, ROUGE, METEOR)

**Architecture / Development**  
1. **Model Benchmarks**  
   - Use public benchmarks to compare models.
   - Common metrics:
     - **Accuracy**: Exact match with expected output.
     - **Coherence**: Logical flow and natural language.
     - **Fluency**: Grammatical correctness and vocabulary use.
     - **GPT Similarity**: Semantic similarity to ground truth.

2. **Manual Evaluations**  
   - Human raters assess responses for:
     - Relevance
     - Informativeness
     - Engagement
   - Useful for capturing subjective quality aspects.

3. **AI-Assisted Metrics**  
   - **Generation Quality**: Creativity, coherence, tone.
   - **Risk and Safety**: Detection of harmful or biased content.

4. **Natural Language Processing (NLP) Metrics**  
   - **F1-score**: Shared word ratio between generated and ground truth.
   - **BLEU**: Measures translation quality.
   - **METEOR**: Considers synonymy and word order.
   - **ROUGE**: Measures recall of overlapping units.

5. **Evaluation Scope**  
   - Evaluate both:
     - Individual model responses
     - Full chat flows with multiple nodes and logic

**Best Practices / Considerations**  
- Start with individual model testing, then expand to full app evaluation.
- Combine manual and automated methods for comprehensive insights.
- Use Azure AI Foundry to explore and compare model benchmarks.
- Continuously monitor and refine evaluation criteria.

**Sample Exam Questions**  
1. What are the key differences between manual and AI-assisted evaluations?
2. Which metrics are commonly used to assess the fluency and coherence of model outputs?
3. How does the F1-score help evaluate model performance?
4. What is the purpose of using model benchmarks in Azure AI Foundry?

## Manually Evaluate the Performance of a Model

**Problem**  
How can you assess the quality and relevance of a language model’s responses during development and after deployment?

**Solution with Azure**  
Use the Azure AI Foundry portal to manually evaluate models and prompt flows. This includes testing individual prompts in the chat playground and evaluating multiple prompts using uploaded datasets.

**Required Components**  
- Azure AI Foundry portal
- Chat playground
- Manual evaluations feature
- Test prompt dataset (with optional expected responses)

**Architecture / Development**  
1. **Prepare Test Prompts**  
   - Create a diverse set of prompts covering typical use cases, edge cases, and failure scenarios.

2. **Test in the Chat Playground**  
   - Interact with the model directly.
   - Modify prompts or system messages and observe changes in output.
   - Use this for quick iteration during early development.

3. **Evaluate Multiple Prompts**  
   - Use the manual evaluations feature to upload a dataset of prompts.
   - Optionally include expected responses for comparison.
   - Rate responses using thumbs up/down.
   - Use feedback to adjust prompts, system messages, or model parameters.

4. **Evaluate Prompt Flows**  
   - After validating individual models, integrate them into prompt flows.
   - Evaluate entire flows manually or automatically to ensure end-to-end performance.

**Best Practices / Considerations**  
- Use manual evaluations early and throughout the development lifecycle.
- Include a wide range of prompt types to uncover weaknesses.
- Combine manual insights with automated metrics for a holistic view.
- Continuously refine prompts and flows based on evaluation results.

**Sample Exam Questions**  
1. What is the purpose of the chat playground in Azure AI Foundry?
2. How can you evaluate multiple prompts efficiently in Azure AI Foundry?
3. Why are manual evaluations important even after deploying a model?
4. What types of feedback can be collected during manual evaluation?

## Automated Evaluations

**Problem**  
How can you efficiently and consistently assess the quality and safety of model outputs at scale?

**Solution with Azure**  
Use automated evaluations in the Azure AI Foundry portal to evaluate models, datasets, or prompt flows using predefined metrics and AI-based evaluators.

**Required Components**  
- Dataset of prompts and responses (with optional ground truth)
- Azure AI Foundry portal
- Evaluation metrics and evaluators (AI Quality, Risk and Safety)

**Architecture / Development**  
1. **Evaluation Data**  
   - Prepare a dataset of prompts and responses.
   - Optionally include expected responses as ground truth.
   - You can generate initial data using an AI model and refine it manually.

2. **Evaluation Metrics**  
   - Choose evaluators based on your evaluation goals:
     - **AI Quality**:
       - Coherence
       - Relevance
       - NLP metrics: F1 score, BLEU, METEOR, ROUGE
     - **Risk and Safety**:
       - Detection of content related to violence, hate, sexual content, and self-harm

3. **Execution**  
   - Run evaluations in the Azure AI Foundry portal.
   - Analyze results to identify areas for improvement in model performance or safety.

**Best Practices / Considerations**  
- Use AI-generated data to bootstrap evaluation datasets.
- Combine automated evaluations with manual reviews for comprehensive insights.
- Regularly update evaluation datasets and metrics to reflect evolving use cases and risks.

**Sample Exam Questions**  
1. What types of metrics are used in automated evaluations in Azure AI Foundry?
2. How can you generate evaluation data for automated testing?
3. What are the two main categories of evaluators available in automated evaluations?
4. Why is it beneficial to include ground truth responses in your evaluation dataset?
