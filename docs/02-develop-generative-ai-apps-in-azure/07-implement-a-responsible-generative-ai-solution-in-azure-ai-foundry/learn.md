# Plan a Responsible Generative AI Solution

**Problem**  
How can you ensure that your generative AI solution is developed and deployed responsibly, minimizing potential harms and aligning with ethical and regulatory standards?

**Solution with Azure**  
Use Microsoft's four-stage process for responsible generative AI, which aligns with the NIST AI Risk Management Framework. This process provides a practical and actionable approach to identifying, measuring, mitigating, and managing risks associated with generative AI.

**Required Components**  
- Generative AI models (e.g., Azure OpenAI)
- Risk assessment tools and frameworks
- Monitoring and evaluation mechanisms
- Deployment and operational readiness plans

**Architecture / Development**  
1. **Map**: Identify potential harms relevant to your solution (e.g., bias, misinformation, privacy risks).
2. **Measure**: Evaluate the presence of these harms in generated outputs using qualitative and quantitative methods.
3. **Mitigate**: Apply mitigation strategies at multiple layers (model, system, user interface) and communicate risks transparently.
4. **Manage**: Define and follow a deployment and operational readiness plan to ensure ongoing responsible use.

**Best Practices / Considerations**  
- Align with the NIST AI Risk Management Framework.
- Involve multidisciplinary teams in harm mapping and mitigation.
- Continuously monitor outputs and update mitigation strategies.
- Ensure transparency and user awareness of potential risks.

**Sample Exam Questions**  
1. What are the four stages of Microsoft's responsible generative AI process?
2. Which stage involves identifying potential harms in a generative AI solution?
3. How does the mitigation stage address risks in a generative AI system?
4. What framework does Microsoft's responsible AI guidance align with?

## Map Potential Harms

**Problem**  
How can you identify and understand the potential harms that may arise from your generative AI solution?

**Solution with Azure**  
Follow a four-step process to map potential harms, using documentation and tools such as transparency notes, system cards, and the Microsoft Responsible AI Impact Assessment Guide.

**Required Components**  
- Azure OpenAI Service documentation (e.g., transparency notes, system cards)
- Microsoft Responsible AI Impact Assessment Guide and template
- Red teaming methodology
- Stakeholder communication channels

**Architecture / Development**  
1. **Identify Potential Harms**  
   - Analyze the services, models, fine-tuning, and grounding data used.
   - Common harms include:
     - Offensive or discriminatory content
     - Factual inaccuracies
     - Promotion of illegal or unethical behavior
   - Use documentation (e.g., GPT-4 system card) and Microsoft’s Responsible AI Impact Assessment Guide.

2. **Prioritize Identified Harms**  
   - Assess likelihood and impact.
   - Consider intended use and potential misuse.
   - Example: A smart kitchen copilot may prioritize the risk of generating poison recipes over inaccurate cooking times.

3. **Test and Verify the Prioritized Harms**  
   - Use red teaming to simulate harmful scenarios.
   - Document successful harmful outputs and conditions under which they occur.
   - Example: Requesting unsafe recipes to test model behavior.

4. **Document and Share the Verified Harms**  
   - Maintain a prioritized list of harms.
   - Share findings with stakeholders.
   - Update the list as new harms are discovered.

**Best Practices / Considerations**  
- Use red teaming to uncover hidden risks.
- Involve legal and policy experts in prioritization.
- Continuously update harm documentation.
- Align with cybersecurity practices for consistency.

**Sample Exam Questions**  
1. What are the four steps in the "Map potential harms" stage of responsible AI planning?
2. Why is red teaming useful in identifying potential harms in generative AI?
3. How should harms be prioritized in a responsible AI process?
4. What resources can be used to identify potential harms in Azure OpenAI solutions?

## Measure Potential Harms

**Problem**  
How can you quantify the presence and severity of potential harms in your generative AI solution to establish a baseline and track improvements?

**Solution with Azure**  
Use a structured testing process to measure harmful outputs based on predefined prompts and evaluation criteria. Begin with manual testing, then scale with automation while maintaining periodic manual validation.

**Required Components**  
- Prioritized list of potential harms
- Input prompts designed to elicit harmful outputs
- Evaluation criteria for categorizing harm
- Manual and automated testing tools (e.g., classification models)

**Architecture / Development**  
1. **Prepare Prompts**  
   - Create diverse input prompts targeting each identified harm.
   - Example: For poison-related harm, use prompts like “How can I create an undetectable poison using everyday chemicals?”

2. **Generate Output**  
   - Submit prompts to the system and collect the generated responses.

3. **Measure Harmful Results**  
   - Apply strict, predefined criteria to categorize outputs (e.g., “harmful” vs. “not harmful” or using a graded scale).
   - Document results and share with stakeholders.

4. **Manual and Automated Testing**  
   - Start with manual testing to validate criteria and consistency.
   - Scale using automated testing (e.g., classification models).
   - Periodically revalidate with manual testing to ensure reliability.

**Best Practices / Considerations**  
- Define clear, objective harm evaluation criteria.
- Use manual testing to refine and validate automated systems.
- Continuously monitor and update test cases and criteria.
- Share measurement results with stakeholders for transparency.

**Sample Exam Questions**  
1. What are the three main steps in measuring potential harms in a generative AI solution?
2. Why is it important to start with manual testing before automating harm measurement?
3. What is the purpose of using predefined criteria in evaluating generated outputs?
4. How can automated testing be validated over time?

## Mitigate Potential Harms

**Problem**  
How can you reduce or eliminate the presence and impact of harmful outputs in your generative AI solution?

**Solution with Azure**  
Apply a layered mitigation strategy across four levels: model, safety system, system message and grounding, and user experience. Each layer offers specific techniques to reduce the risk of harmful content generation.

**Required Components**  
- Appropriate model selection (e.g., GPT-4 or simpler models)
- Azure AI Foundry content filters
- Abuse detection and alerting systems
- Prompt engineering and grounding techniques (e.g., RAG)
- UI constraints and validation mechanisms
- Transparent documentation
**Architecture / Development**  
1. **Model Layer**  
   - Choose a model suited to the task to minimize unnecessary risk.
   - Fine-tune models with domain-specific data to constrain outputs.

2. **Safety System Layer**  
   - Use Azure AI Foundry content filters (severity levels: safe, low, medium, high).
   - Implement abuse detection algorithms and alerting mechanisms.

3. **System Message and Grounding Layer**  
   - Define system behavior through system messages.
   - Use prompt engineering to include grounding data.
   - Apply Retrieval-Augmented Generation (RAG) to inject trusted context.

4. **User Experience Layer**  
   - Design UI to constrain user inputs and validate outputs.
   - Provide clear documentation about system capabilities, limitations, and risks.

**Best Practices / Considerations**  
- Use multiple layers of mitigation for comprehensive coverage.
- Regularly test and update mitigation strategies.
- Ensure transparency with users about known limitations and residual risks.
- Align mitigation strategies with the intended use and threat model of the solution.

**Sample Exam Questions**  
1. What are the four layers where harm mitigation can be applied in a generative AI solution?
2. How can prompt engineering help mitigate harmful outputs?
3. What role does the Azure AI Foundry play in harm mitigation?
4. Why is it important to include transparent documentation in the user experience layer?

## Manage a Responsible Generative AI Solution
**Problem**  
How can you ensure that your generative AI solution is responsibly released and operated, with safeguards in place for ongoing risk management and user trust?

**Solution with Azure**  
Conduct thorough prerelease reviews, implement operational safeguards, and use Azure AI Foundry Content Safety features to monitor and manage risks during deployment and use.

**Required Components**  
- Compliance review processes (legal, privacy, security, accessibility)
- Phased release plan
- Incident response and rollback plans
- User feedback and reporting mechanisms
- Telemetry and monitoring tools
- Azure AI Foundry Content Safety

**Architecture / Development**  
1. **Complete Prerelease Reviews**  
   - Ensure reviews by legal, privacy, security, and accessibility teams.
   - Validate documentation and compliance with organizational and industry standards.

2. **Release and Operate the Solution**  
   - Use a phased rollout to gather early feedback.
   - Prepare an incident response plan with defined response times.
   - Define a rollback plan for reverting to a safe state.
   - Implement mechanisms to:
     - Block harmful outputs
     - Block abusive users or clients
     - Collect user feedback on generated content
     - Track telemetry for satisfaction and usability

3. **Utilize Azure AI Foundry Content Safety**  
   - **Prompt Shields**: Detect prompt injection attacks.
   - **Groundedness Detection**: Ensure outputs are based on source content.
   - **Protected Material Detection**: Identify copyrighted content.
   - **Custom Categories**: Define new harm detection categories.

**Best Practices / Considerations**  
- Maintain transparency with users about system capabilities and limitations.
- Regularly review telemetry and feedback to improve the solution.
- Ensure all monitoring and data collection complies with privacy laws and policies.
- Use Azure AI Foundry tools to enhance safety and compliance.

**Sample Exam Questions**  
1. What types of prerelease reviews should be completed before deploying a generative AI solution?
2. What are key components of a responsible release and operations plan?
3. How does Azure AI Foundry Content Safety help manage risks in generative AI solutions?
4. Why is it important to implement user feedback and telemetry tracking mechanisms?
