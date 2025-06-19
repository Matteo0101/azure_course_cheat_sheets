# Custom Text Classification with Azure AI Language Service 🌐

## 🧩 Problem

You need to classify text documents into categories using Azure AI services, including:

- **Custom single-label classification** (only one category per document)
- **Custom multi-label classification** (multiple categories per document)

## 💡 Solution with Azure

Use **Azure AI Language Service - Custom Text Classification** to build, train, deploy, and consume classification models for text data.

## ⚙️ Components Required

- Azure AI Language resource
- Labeled dataset (training & testing)
- Azure AI Language Studio or REST API
- Authentication key (Ocp-Apim-Subscription-Key)
- REST API endpoints for training, deployment, and inference

## 🏗️ Architecture / Development

### Project Lifecycle

#### 1. Define labels
Identify categories for classification (e.g., "Action", "Adventure", "Strategy").

#### 2. Tag data
Label text documents with corresponding categories.

- **Single-label**: One category per document
- **Multi-label**: Multiple categories per document

#### 3. Split datasets

- **Training**: ~80%
- **Testing**: ~20%
- **Options**: Automatic or manual split

#### 4. Train model
Submit training request via API:

```json
POST <YOUR-ENDPOINT>/language/analyze-text/projects/<PROJECT-NAME>/:train?api-version=<API-VERSION>

Body:
{
  "modelLabel": "<MODEL-NAME>",
  "trainingConfigVersion": "<CONFIG-VERSION>",
  "evaluationOptions": {
    "kind": "percentage",
    "trainingSplitPercentage": 80,
    "testingSplitPercentage": 20
  }
}
```

#### 5. Monitor training status

```json
GET <ENDPOINT>/language/analyze-text/projects/<PROJECT-NAME>/train/jobs/<JOB-ID>?api-version=<API-VERSION>
```

#### 6. Evaluate & improve model

- Check metrics: Precision, Recall, F1 Score
- Add more varied & quality labeled data where performance is weak

#### 7. Deploy model

- Multiple deployments allowed (max 10 per project)
- Deployment name used for inference

### Deployment Example

```json
"tasks": [
  {
    "kind": "CustomSingleLabelClassification",
    "taskName": "MyTaskName",
    "parameters": {
      "projectName": "MyProject",
      "deploymentName": "MyDeployment"
    }
  }
]
```

#### 8. Submit documents for classification

```json
POST <ENDPOINT>/language/analyze-text/jobs?api-version=<API-VERSION>

Body:
{
  "displayName": "Classifying documents",
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "<LANGUAGE-CODE>",
        "text": "Text1"
      }
    ]
  },
  "tasks": [
    {
      "kind": "CustomSingleLabelClassification",
      "taskName": "<TASK-NAME>",
      "parameters": {
        "projectName": "<PROJECT-NAME>",
        "deploymentName": "<DEPLOYMENT-NAME>"
      }
    }
  ]
}
```

#### 9. Retrieve classification results

```json
GET <ENDPOINT>/language/analyze-text/jobs/<JOB-ID>?api-version=<API-VERSION>
```

**Response example:**

```json
{
  "tasks": {
    "items": [
      {
        "results": {
          "documents": [
            {
              "id": "<DOC-ID>",
              "class": [
                {
                  "category": "Class_1",
                  "confidenceScore": 0.055
                }
              ]
            }
          ]
        }
      }
    ]
  }
}
```

## 🔧 Best Practice / Considerations

- Use high-quality, diverse labeled data for better model performance
- Ensure clear label distinctions to avoid ambiguity
- Monitor precision, recall, and F1 Score to guide model improvement
- Use automatic split for large datasets; manual split for small datasets to control class distribution
- Limit of 10 deployments per project
- REST API is asynchronous; always poll job status after submission

## ❓ Exam-like Sample Questions

### Question 1:
You need to create a model that allows a document to belong to more than one category. Which project type should you select?

A. customSingleLabelClassification  
B. customMultiLabelClassification

**✅ Answer: B**

### Question 2:
Which evaluation metric measures the ratio of true positives to all predicted positives?

A. Recall  
B. Precision  
C. F1 Score

**✅ Answer: B**

### Question 3:
When using a smaller dataset, which data split option is recommended?

A. Automatic split  
B. Manual split

**✅ Answer: B**

### Question 4:
What is the maximum number of deployments allowed per Azure AI Language project?

A. 5  
B. 10  
C. 20

**✅ Answer: B**

### Question 5:
What header must be included in each API request to Azure AI Language?

A. Authorization  
B. SubscriptionKey  
C. Ocp-Apim-Subscription-Key

**✅ Answer: C**