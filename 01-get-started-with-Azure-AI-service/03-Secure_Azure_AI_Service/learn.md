# Azure AI Services Security Guide

## 🔐 Problem
You need to secure access to Azure AI services. How do you authenticate users/applications and manage network security to protect your resources from unauthorized access?

## 💡 Solution with Azure
Use a combination of authentication methods (keys, Microsoft Entra ID, managed identities) and network access controls (IP restrictions, virtual networks, private endpoints) to protect Azure AI services. Additionally, use Azure Key Vault to manage secrets securely.

## 🧩 Required Components
- Azure AI Services
- Microsoft Entra ID (formerly Azure AD)
- Azure Key Vault
- Azure Virtual Network (VNet)
- Private Endpoints
- Firewall/IP Access Rules
- Azure CLI / PowerShell
- Managed Identity (System/User-assigned)
- Role-based Access Control (RBAC)

## 🏗️ Architecture / Development

### 🔑 Authentication via Subscription Keys
- Default authentication method for many Azure AI services
- Two keys provided per service to allow rotation without downtime
- Regenerate keys regularly using:
  - Azure Portal
  - `az cognitiveservices account keys regenerate` (CLI)

**Key rotation steps:**
1. Use only one key in production
2. Regenerate the unused key
3. Switch apps to use new key
4. Regenerate the original key

### 🔐 Storing Keys in Azure Key Vault
- Use Key Vault to securely store AI service keys
- Access controlled via managed identities
- Avoid hardcoding secrets in applications

### 🔁 Token-Based Authentication
- Some REST APIs require token-based auth
- Subscription key exchanged for short-lived token (10 minutes)
- SDKs handle token retrieval/usage automatically

### 👤 Microsoft Entra ID Authentication
Used for AI Foundry and other services.

**Authenticate via:**

**Service Principals**
- Register application
- Create service principal via `New-AzADServicePrincipal`
- Assign role: "Cognitive Services User"

**Managed Identities**
- System-assigned (one resource)
- User-assigned (reusable across resources)

Example (system-assigned):
```bash
az vm identity assign -g <group> -n <vm>
```
Then assign role: "Cognitive Services Contributor"

## 🌐 Network Security Configuration

### 🔄 Default Behavior
Azure AI services are publicly accessible by default.

### 🧱 Restrict Access with Network Settings
**Options:**
- All networks (default)
- Selected Networks and Private Endpoints
- Disabled (most restrictive)

### 🔄 Changing Default Action
Changing from "All networks" → "Selected" or "Disabled" will block all access unless exceptions are added.

### 🌍 Virtual Networks & IP Access
Configure in Azure Portal → Networking:
1. Select Virtual Network
2. Add subnet
3. Enable Service Endpoint: Microsoft.CognitiveServices
4. Optionally add IP address/ranges under Firewall

### 🔒 Private Endpoint Access
Create Private Endpoint connection:
1. Resource → Networking → Private endpoint connections
2. Follow wizard (Subscription, Region, Subnet, DNS)
3. Once connected, change access to "Disabled" for strict control

### 🛡️ Trusted Azure Services Exceptions
Allow access to trusted Azure services:
- Azure AI Services
- Azure Machine Learning / AI Foundry
- Azure AI Search

Enable exception in Networking panel:
- Option: Allow Azure services on the trusted services list

## ✅ Best Practices / Considerations
- 🔁 Rotate keys regularly and automate via scripts or pipelines
- 🔐 Use Key Vault + Managed Identity for all secrets
- 👤 Use Microsoft Entra ID wherever possible for role-based access
- 🌐 Limit network exposure using VNets or private endpoints
- ❌ Disable all networks and allow only necessary trusted paths
- 🔄 Test access after each configuration change
- 📚 SDKs handle auth/token logic—prefer SDK usage in apps

## 🧪 Sample Exam Questions

### 🔐 You're using a subscription key to access Azure AI services. How do you rotate it without downtime?
A. Use both keys in rotation and regenerate one at a time ✔️  
B. Regenerate both keys simultaneously  
C. Delete and re-create the service  
D. Restart all dependent services after key change  

### 🔒 You want to prevent hardcoding keys in your application. What should you use?
A. Application config file  
B. Azure Key Vault with managed identity ✔️  
C. Store key in plain text in Azure Blob  
D. Hardcode into source code  

### 🌐 How do you restrict access to an AI service to a specific subnet?
A. Use service endpoint in selected virtual network ✔️  
B. Change key value  
C. Use application gateway  
D. Disable Azure Firewall  

### 👤 You need to assign access to a VM to consume Azure AI services. What do you configure?
A. User-assigned identity  
B. System-assigned managed identity ✔️  
C. Anonymous access  
D. Public endpoint  

### 🔁 What does token-based auth require?
A. Sending a long-lived key on each request  
B. Getting a short-lived token using a subscription key ✔️  
C. Using SSH keys  
D. Enabling HTTP only mode