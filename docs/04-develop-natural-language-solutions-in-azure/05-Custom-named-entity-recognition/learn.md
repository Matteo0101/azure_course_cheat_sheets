# Custom Named Entity Recognition (Custom NER) 📄 (Azure AI Language Service)

## 🧩 Problem

You need to extract specific entities (user-defined) from unstructured text where built-in NER is insufficient or unavailable. Entities may include legal terms, financial fields, or domain-specific information.

## 💡 Solution with Azure

Use **Azure AI Language - Custom Named Entity Recognition (Custom NER)** to:

- Define your own entities
- Label and train the model
- Deploy and integrate via API

## ⚙️ Components Required

- Azure AI Language resource (Custom NER feature enabled)
- Azure Storage account (blob storage)
- Labeled dataset (training + testing)
- Language Studio for labeling and training
- Azure REST API for deployment and extraction
- Role assignment: Storage Blob Data Contributor if storage access needed

## 🏗️ Architecture / Development

### 1️⃣ Custom vs Built-in NER

| Feature | Built-in NER | Custom NER |
|---------|--------------|------------|
| Entity Types | Predefined (person, location, organization, URL, etc.) | User-defined |
| Configuration | Minimal | Full training cycle |
| Use Cases | Generic extraction | Domain-specific extraction |

### 2️⃣ Custom NER Project Lifecycle

#### Define Entities
- Clearly define each entity you want to extract
- Avoid ambiguity
- Split complex fields (e.g. contact info ➔ phone, email, social)

#### Tag Data (Labeling)
- Use Language Studio to select and tag text fragments as entities

#### Train Model
- After labeling, train the model

#### Evaluate Model
Metrics used:
- **Precision** (Correct labels / total predictions)
- **Recall** (Correct labels / total actual entities)
- **F1 Score** (Harmonic mean of precision & recall)

#### Improve Model
Analyze underperforming entities via:
- Model metrics
- Confusion matrix

#### Deploy Model
- After acceptable performance, deploy for production use

#### Extract Entities (Inference)
- Use deployed model via API to extract entities

### 3️⃣ Example API Request (CustomEntityRecognition)

```json
{
  "displayName": "string",
  "analysisInput": {
    "documents": [
      { "id": "doc1", "text": "string" },
      { "id": "doc2", "text": "string" }
    ]
  },
  "tasks": [
    {
      "kind": "CustomEntityRecognition",
      "taskName": "MyRecognitionTaskName",
      "parameters": {
        "projectName": "MyProject",
        "deploymentName": "MyDeployment"
      }
    }
  ]
}
```

### 4️⃣ Accepted Training Data Format (JSON schema example)

```json
{
  "projectFileVersion": "{DATE}",
  "stringIndexType": "Utf16CodeUnit",
  "metadata": {
    "projectKind": "CustomEntityRecognition",
    "storageInputContainerName": "{CONTAINER-NAME}",
    "projectName": "{PROJECT-NAME}",
    "language": "en-us"
  },
  "assets": {
    "entities": [
      { "category": "Entity1" }, 
      { "category": "Entity2" }
    ],
    "documents": [
      {
        "location": "{DOCUMENT-NAME}",
        "language": "{LANGUAGE-CODE}",
        "dataset": "{DATASET}",
        "entities": [
          {
            "regionOffset": 0,
            "regionLength": 500,
            "labels": [
              { "category": "Entity1", "offset": 25, "length": 10 },
              { "category": "Entity2", "offset": 120, "length": 8 }
            ]
          }
        ]
      }
    ]
  }
}
```

### 5️⃣ Model Evaluation Scenarios

| Precision | Recall | Interpretation |
|-----------|--------|----------------|
| Low | Low | Model struggles on both recognition and labeling |
| High | Low | Correct labels but missing entities |
| Low | High | Finds entities but often assigns wrong labels |

### 6️⃣ Confusion Matrix

- Visual table of predicted vs actual entities
- Identifies which entities need more training data

### 7️⃣ Project Limits (Service Quotas)

| Resource | Limit |
|----------|-------|
| Training files | 10 - 100,000 |
| Deployments | 10 per project |
| Authoring API limits | 10 POST / 100 GET per min |
| Analyze API limits | 20 GET or POST |
| Projects | 500 per resource |
| Models | 50 trained models per project |
| Entity types | 200 |
| Entity character length | 500 |

## 🔧 Best Practice / Considerations

- Use high-quality, diverse, and real-world-like data for training
- Label with consistency, precision, completeness
- Avoid ambiguous entity definitions
- Separate compound entities into distinct categories
- Use confusion matrix to drive iterative improvement
- Secure storage accounts properly in production
- Monitor quota limits when scaling

## ❓ Exam-like Sample Questions

### Question 1:
Which task type should be specified for Custom NER when submitting a request?

A. CustomTextClassification  
B. CustomEntityRecognition  
C. EntityDetection

**✅ Answer: B**

### Question 2:
Which metric indicates that the model correctly labels entities it finds?

A. Precision  
B. Recall  
C. F1 Score

**✅ Answer: A**

### Question 3:
What is the maximum number of entity types allowed in a Custom NER project?

A. 100  
B. 200  
C. 500

**✅ Answer: B**

### Question 4:
What tool can you use to visually identify misclassified entities during model evaluation?

A. Model Matrix  
B. Confusion Matrix  
C. Precision Report

**✅ Answer: B**

### Question 5:
Which labeling practice improves model accuracy?

A. Label only obvious entities  
B. Use synthetic data exclusively  
C. Maintain precision, consistency, completeness

**✅ Answer: C**