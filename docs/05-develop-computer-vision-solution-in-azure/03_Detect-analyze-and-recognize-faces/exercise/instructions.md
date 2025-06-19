# [Detect and Analyze Faces](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Labs/03-face-service.html)

The ability to detect and analyze human faces is a core AI capability. In this exercise, you’ll explore the Azure AI Vision service and the Face service to work with faces in images.

This exercise takes approximately 30 minutes.

**Note:** Capabilities of Azure AI services that return personally identifiable information are restricted to customers who have been granted limited access. This exercise does not include facial recognition tasks and can be completed without requesting any additional access to restricted features.

---

## Provision an Azure AI Face API Resource

If you don’t already have one in your subscription, you’ll need to provision an Azure AI Face API resource.

1. Open the Azure portal at [https://portal.azure.com](https://portal.azure.com) and sign in using your Azure credentials.
2. Select **Create a resource**.
3. In the search bar, search for **Face**, select **Face**, and create the resource with the following settings:
    - **Subscription:** Your Azure subscription
    - **Resource group:** Create or select a resource group
    - **Region:** Choose any available region
    - **Name:** A valid name for your Face resource
    - **Pricing tier:** Free F0
4. Create the resource and wait for deployment to complete, then view the deployment details.
5. When the resource has been deployed, go to it and under the **Resource management** node in the navigation pane, view its **Keys and Endpoint** page. You will need the endpoint and one of the keys from this page in the next procedure.

---

## Develop a Facial Analysis App with the Face SDK

In this exercise, you’ll complete a partially implemented client application that uses the Azure Face SDK to detect and analyze human faces in images.

**Note:** You can choose to use the SDK for Python.

### Prepare the Application Configuration

1. Clone the GitHub repo containing the code files for this exercise:

    ```bash
    rm -r mslearn-ai-vision -f
    git clone https://github.com/MicrosoftLearning/mslearn-ai-vision
    ```

2. Navigate to the language-specific folder containing the application code files:

    ```bash
    cd mslearn-ai-vision/Labfiles/face/python/face-api
    ls -a -l
    ```

    The folder contains application configuration and code files for your app. It also contains an `/images` subfolder, which contains some image files for your app to analyze.

3. Install the Azure AI Vision SDK package and other required packages:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt azure-ai-vision-face==1.0.0b2
    ```

4. Edit the configuration file for your app:

    ```bash
    code .env
    ```

    In the code file, update the configuration values it contains to reflect the endpoint and an authentication key for your Computer Vision resource (copied from its **Keys and Endpoint** page in the Azure portal).

5. Save your changes and close the code editor.

---

### Add Code to Create a Face API Client

1. Open the code file for the client application:

    ```bash
    code analyze-faces.py
    ```

2. Find the comment `# Import namespaces` and add the following code to import the namespaces you will need to use the Azure AI Vision SDK:

    ```python
    # Import namespaces
    from azure.ai.vision.face import FaceClient
    from azure.ai.vision.face.models import FaceDetectionModel, FaceRecognitionModel, FaceAttributeTypeDetection01
    from azure.core.credentials import AzureKeyCredential
    ```

3. In the `Main` function, find the comment `# Authenticate Face client` and add the following code to create and authenticate a `FaceClient` object:

    ```python
    # Authenticate Face client
    face_client = FaceClient(
         endpoint=cog_endpoint,
         credential=AzureKeyCredential(cog_key))
    ```

---

### Add Code to Detect and Analyze Faces

1. In the `Main` function, find the comment `# Specify facial features to be retrieved` and add the following code:

    ```python
    # Specify facial features to be retrieved
    features = [FaceAttributeTypeDetection01.HEAD_POSE,
                FaceAttributeTypeDetection01.OCCLUSION,
                FaceAttributeTypeDetection01.ACCESSORIES]
    ```

2. Under the code you just added, find the comment `# Get faces` and add the following code to print the facial feature information and call a function that annotates the image with the bounding box for each detected face:

    ```python
    # Get faces
    with open(image_file, mode="rb") as image_data:
         detected_faces = face_client.detect(
             image_content=image_data.read(),
             detection_model=FaceDetectionModel.DETECTION01,
             recognition_model=FaceRecognitionModel.RECOGNITION01,
             return_face_id=False,
             return_face_attributes=features,
         )

    face_count = 0
    if len(detected_faces) > 0:
         print(len(detected_faces), 'faces detected.')
         for face in detected_faces:

             # Get face properties
             face_count += 1
             print('\nFace number {}'.format(face_count))
             print(' - Head Pose (Yaw): {}'.format(face.face_attributes.head_pose.yaw))
             print(' - Head Pose (Pitch): {}'.format(face.face_attributes.head_pose.pitch))
             print(' - Head Pose (Roll): {}'.format(face.face_attributes.head_pose.roll))
             print(' - Forehead occluded?: {}'.format(face.face_attributes.occlusion["foreheadOccluded"]))
             print(' - Eye occluded?: {}'.format(face.face_attributes.occlusion["eyeOccluded"]))
             print(' - Mouth occluded?: {}'.format(face.face_attributes.occlusion["mouthOccluded"]))
             print(' - Accessories:')
             for accessory in face.face_attributes.accessories:
                 print('   - {}'.format(accessory.type))
             # Annotate faces in the image
             annotate_faces(image_file, detected_faces)
    ```

3. Save your changes.

---

### Run the Program

1. Run the program with the argument `images/face1.jpg`:

    ```bash
    python analyze-faces.py images/face1.jpg
    ```

    Observe the output, which should include the attributes of each face detected.

2. Run the program again, this time specifying the parameter `images/face2.jpg`:

    ```bash
    python analyze-faces.py images/face2.jpg
    ```

3. Run the program one more time, this time specifying the parameter `images/faces.jpg`:

    ```bash
    python analyze-faces.py images/faces.jpg
    ```

---

### Clean Up Resources

If you’ve finished exploring Azure AI Vision, you should delete the resources you have created in this exercise to avoid incurring unnecessary Azure costs:

1. Open the Azure portal at [https://portal.azure.com](https://portal.azure.com).
2. In the top search bar, search for the resources you created in this lab.
3. On the resource page, select **Delete** and follow the instructions to delete the resource. Alternatively, you can delete the entire resource group to clean up all resources at the same time.
