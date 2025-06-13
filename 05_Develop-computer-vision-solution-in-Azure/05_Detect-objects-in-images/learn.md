# Azure AI Custom Vision - Object Detection

## Problem
You need to automatically identify and locate specific objects in an image—for example, detecting different items on a grocery store checkout belt.

## Solution with Azure
Use **Azure AI Custom Vision** to build, train, and deploy an **object detection model** that identifies classes of objects and their positions in an image.

## Componenti richiesti
- **Azure AI Custom Vision Training resource** - To upload, label, and train custom object detection models.
- **Azure AI Custom Vision Prediction resource** - To generate object detection predictions using the trained model.
- **Custom Vision portal** - A graphical web interface for project creation, labeling, training, and model management.
- **Custom Vision SDK or REST API** - To programmatically interact with training and prediction services.

## Architettura/Sviluppo

### Training Workflow
1. **Create a Custom Vision project** via portal or SDK.
2. **Upload training images**.
3. **Label each image** with tags and bounding boxes (either manually, via smart labeler, or external tools).
4. **Train the model** and publish it to a prediction resource.
5. **Evaluate model performance** using provided evaluation tools in the portal.

### Labeling Details
- Tags are associated with specific **bounding boxes**, not entire images.
- Bounding boxes are defined with four values:
  - `left`, `top`, `width`, `height` (proportional to the image dimensions).

### Prediction Workflow
Using Python SDK:

```python
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

credentials = ApiKeyCredentials(in_headers={"Prediction-key": "<YOUR_PREDICTION_RESOURCE_KEY>"})
prediction_client = CustomVisionPredictionClient(endpoint="<YOUR_PREDICTION_RESOURCE_ENDPOINT>", credentials=credentials)

image_data = open("<PATH_TO_IMAGE_FILE>", "rb").read()
results = prediction_client.detect_image("<YOUR_PROJECT_ID>", "<YOUR_PUBLISHED_MODEL_NAME>", image_data)

for prediction in results.predictions:
    if prediction.probability > 0.5:
        print(f"{prediction.tag_name} ({prediction.probability})")
        print(f" Left:{prediction.bounding_box.left}, Top:{prediction.bounding_box.top}, Height:{prediction.bounding_box.height}, Width:{prediction.bounding_box.width}")
```

## Best practice / Considerazioni
- Separate training and prediction resources for **regional optimization** and **cost efficiency**.
- Use **smart labeler** after initial training to speed up further labeling.
- If using external labeling tools, ensure the format matches **Custom Vision API requirements** (normalized bounding box values).
- Use appropriate SDKs for your development language (e.g., `azure-cognitiveservices-vision-customvision` for Python).

## Domande simulate d'esame (basate solo sul contenuto fornito)

1. **What is required to use Azure AI Custom Vision for object detection?**
   - A training resource and a prediction resource in Azure.

2. **What distinguishes object detection from image classification in Custom Vision?**
   - Object detection uses **bounding boxes with tags**; image classification uses tags for the **entire image**.

3. **How are bounding boxes defined in Custom Vision labeling?**
   - By proportional values for left, top, width, and height relative to the image.

4. **What is the purpose of the Custom Vision portal?**
   - To create, label, train, publish, and evaluate object detection models.

5. **Which SDK package is used for object detection prediction in Python?**
   - `azure-cognitiveservices-vision-customvision`

6. **Can training and prediction resources be located in different regions?**
   - Yes, to support flexible deployment scenarios.