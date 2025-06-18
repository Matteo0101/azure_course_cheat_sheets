# Azure AI Services Containers Guide

## 🧩 **Problem**
You need to use Azure AI services in environments where:
* Sensitive data must remain on-premises.  
* Latency between services and local data must be minimized.
* Full control over hosting, networking, and authentication is required.

## 🚀 **Solution with Azure**
Use **Azure AI services containers** to run Azure Cognitive Services locally or in your own Azure infrastructure. This allows for secure, low-latency AI capabilities without sending data to the cloud.

## 🧱 **Required Components**

| Component | Description |
|-----------|-------------|
| **Azure AI Services Container Image** | Specific to the feature (e.g., sentiment analysis, speech-to-text). |
| **Container Host** | Where the container is deployed (e.g., Docker, ACI, AKS). |
| **Azure AI Services Resource** | Required in Azure to enable billing and usage tracking. |
| **API Key** | Used in container configuration for billing. |
| **Billing Endpoint** | URI of the Azure resource used for metering. |
| **EULA Acceptance** | Required to run the container (`Eula=accept`). |

## 🏗️ **Architecture / Development**

1. **Download Container Image**  
   Use `docker pull` to retrieve the relevant container from the Microsoft Container Registry (MCR).

2. **Deploy the Container**  
   On Docker, Azure Container Instances (ACI), or Azure Kubernetes Service (AKS).

3. **Configure the Container**  
   Set required parameters:
   * `ApiKey=<your_key>`
   * `Billing=<your_azure_endpoint>`
   * `Eula=accept`

4. **Consume the Service**
   * Applications send requests directly to the local container endpoint.
   * No subscription key needed for each request.
   * Use your own network and authentication policies.

5. **Billing**
   * Usage metrics are periodically sent to Azure for billing purposes.
   * Sensitive data stays local; only usage is reported.

## ✅ **Best Practices / Considerations**

* 🔒 **Security**: You can fully control authentication and access at the network level.
* 🗂️ **Granularity**: Each AI capability (e.g., key phrase extraction, sentiment analysis) is in a separate container image.
* 🕒 **Latency**: Local deployment reduces latency when accessing local data.
* 📦 **Portability**: Containers are portable across environments (Linux, Windows, on-prem, Azure).
* 📜 **Licensing**: You must accept the EULA to run containers.

## ❓ **Simulated Exam Questions**

1. **What are the three required parameters when configuring an Azure AI services container?**  
   👉 `ApiKey`, `Billing`, `Eula`

2. **Can you use Azure AI services containers without an Azure subscription?**  
   ❌ No. An Azure resource is required for billing and usage reporting.

3. **Why might you prefer to use containers for Azure AI services?**  
   ✅ To keep data on-premises, reduce latency, and have more control over security.

4. **Where can you deploy Azure AI services containers?**  
   👉 Docker server, Azure Container Instances (ACI), Azure Kubernetes Service (AKS)

5. **Are all AI features available in a single container?**  
   ❌ No. Each feature (e.g., language detection, sentiment analysis) has its own image.