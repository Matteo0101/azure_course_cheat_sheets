# 🎨 Image Classification Solution (Azure AI Custom Vision)

## 🔍 **Problem**

You need to build a computer vision solution that can classify images into categories (e.g., identify products in a grocery checkout, classify fruit images) using your own training data.

---

## ☁️ **Solution with Azure**

Use **Azure AI Custom Vision**, which enables:

-   **📊 Image classification**: Predict a single class (multiclass) or multiple classes (multilabel) for an image
-   **🎯 Object detection** (not detailed in this material)

You train your own model using labeled images, then publish the model for prediction.

---

## 🧩 **Components Required**

-   **🏋️ Azure AI Custom Vision training resource**
    Used to train custom models with your image data

-   **🔮 Azure AI Custom Vision prediction resource**
    Used to generate predictions from new images using your trained model

-   **🌐 Azure AI Custom Vision portal**
    Web interface at [https://www.customvision.ai](https://www.customvision.ai) for managing projects, uploading images, training, publishing, and testing models

-   **📱 SDK / REST API**

    -   Python: `azure-cognitiveservices-vision-customvision`
    -   .NET: `Microsoft.Azure.CognitiveServices.Vision.CustomVision.Training` and `...Prediction`

-   **🆔 Project ID + resource endpoints/keys**
    Required for training and prediction API calls

---

## 🏗️ **Architecture / Development**

### 🏋️ Training a model

-   Create an image classification project in the **Custom Vision portal**
-   Associate the project with a **training resource**
-   Upload images and assign class label tags
-   Train and evaluate the model in the portal
-   Publish the trained model to a **prediction resource**

> 💡 Both **multiclass** (single label per image) and **multilabel** (multiple labels per image) classification are supported.

### 🔮 Example: Classify images (Python SDK)

```python
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

# Authenticate a client for the prediction API
credentials = ApiKeyCredentials(in_headers={"Prediction-key": "<YOUR_PREDICTION_RESOURCE_KEY>"})
prediction_client = CustomVisionPredictionClient(
    endpoint="<YOUR_PREDICTION_RESOURCE_ENDPOINT>",
    credentials=credentials
)

# Get classification predictions for an image
image_data = open("<PATH_TO_IMAGE_FILE>", "rb").read()
results = prediction_client.classify_image(
    "<YOUR_PROJECT_ID>",
    "<YOUR_PUBLISHED_MODEL_NAME>",
    image_data
)

# Process predictions
for prediction in results.predictions:
    if prediction.probability > 0.5:
        print(image, ': {} ({:.0%})'.format(prediction.tag_name, prediction.probability))
```

---

## ⭐ **Best Practice / Considerations**

### 🔄 **Separate training and prediction resources**

Enables flexibility (e.g., train in one region, deploy prediction resources in multiple regions)

### 🚀 **DevOps integration**

Use SDKs / REST API to automate training and publishing as part of a CI/CD pipeline

### 🛠️ **Resource management**

-   Each resource has its own endpoint and authentication key
-   Each project has a unique project ID used by client applications

---

## 📝 **Sample Exam-Like Questions**

### 1️⃣ What is required to train and publish an image classification model with Azure AI Custom Vision?

**✅ Answer:** A **training resource** for model training and a **prediction resource** for generating predictions

---

### 2️⃣ How can you classify images using a trained Custom Vision model?

**✅ Answer:** Submit images to the **prediction resource** using the SDK, REST API, or Custom Vision portal

---

### 3️⃣ What type of image classification is supported by Azure AI Custom Vision?

**✅ Answer:** **Multiclass** (one label per image) and **multilabel** (multiple labels per image) classification

---

### 4️⃣ What advantage does separating training and prediction resources provide?

**✅ Answer:** Flexibility to train in one region and deploy prediction endpoints in others for performance or compliance reasons

---

### 5️⃣ Which tool allows you to visually upload images, tag them, train, and test models?

**✅ Answer:** The **Azure AI Custom Vision portal** at [https://www.customvision.ai](https://www.customvision.ai)
