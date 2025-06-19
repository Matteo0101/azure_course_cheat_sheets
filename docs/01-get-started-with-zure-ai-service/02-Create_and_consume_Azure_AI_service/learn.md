# Azure AI Services Guide

🧠 **Problem**
You need to build intelligent applications using prebuilt AI capabilities such as vision, language, speech, document understanding, or search. How do you provision and consume Azure AI services in a secure, manageable, and efficient way?

🔧 **Azure Solution**
Use **Azure AI services** to consume cloud-based AI capabilities via **REST APIs** or **SDKs**. Provision services either as a **multi-service** or **single-service** resource depending on usage, scalability, and management needs.

📦 **Required Components**
* Azure Subscription
* Azure AI resource (multi-service or single-service)
* Endpoint URI
* Subscription Key(s)
* Azure Region (Location)
* REST API or SDK for preferred language (C#, Python, JavaScript, Java, Go)

🏗️ **Architecture / Development**

🛠 Provisioning Options:
* **Multi-service Resource**:
   * One resource for multiple AI capabilities (Language, Vision, Speech, etc.)
   * Single billing, credentials, and endpoint
* **Single-service Resource**:
   * Separate resources per service
   * Per-region customization
   * Independent billing and access management
   * Free tier often available

🧠 Training vs Prediction:
* Some services (e.g., custom models) require **separate training and prediction** resources
* Allows cost separation between model training and inference

🔑 Consuming Services:
* **Endpoint URI**: HTTP address for service requests
* **Subscription Key**: Authenticates client application
* **Location**: Azure region for the resource
* Two keys are provided; both are valid and regenerable

🧪 Using REST APIs:
* Send data in **JSON** via **HTTP** (POST, PUT, GET depending on the function)
* Receive JSON responses
* Language-agnostic: works with cURL, Postman, or any programming language supporting HTTP

💻 Using SDKs:
* Easier abstraction over REST
* Available for major languages:
   * C# (.NET Core)
   * Python
   * JavaScript (Node.js)
   * Java
   * Go
* Include service-specific classes and methods

✅ **Best Practices / Considerations**
* Use **multi-service resource** for unified management in production
* Use **single-service resource** when:
   * You need service separation (e.g., region, security, cost)
   * You're testing via the free tier
* Regenerate keys regularly to enhance security
* Use SDKs for robust application development; use REST for quick tests or language-agnostic integration
* Always confirm service availability and SDK support per language and region in official documentation

❓**Sample Exam Questions**

1. 🔐 **You need to build an app that uses Azure AI Vision and Azure AI Speech. What provisioning option enables you to use a single set of credentials and billing?**
   A. Separate single-service resources
   B. Multi-service resource ✅
   C. Separate Azure subscriptions
   D. Cognitive Containers

2. 🌍 **Why might you choose to provision separate AI service resources for each service?**
   A. To get better REST API performance
   B. To reduce the number of access keys
   C. To use different geographical regions or separate billing ✅
   D. To increase SDK compatibility

3. 🧾 **Which information must be provided to a client application to consume an Azure AI service? (Choose all that apply)**
   ⬜ Username and password
   ✅ Endpoint URI
   ✅ Subscription Key
   ✅ Resource Location (for some SDKs)

4. 🧰 **Which method allows language-agnostic access to Azure AI services?**
   A. SDK
   B. Azure CLI
   C. REST API ✅
   D. PowerShell

5. 🧠 **You want to build a custom model and keep training and prediction costs separate. What should you do?**
   A. Use multi-service resource
   B. Use free-tier resources
   C. Use separate resources for training and prediction ✅
   D. Enable autoscaling