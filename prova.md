# Azure OpenAI - Guida Completa

## PROBLEMA
Hai bisogno di creare un'applicazione che sfrutti modelli LLM (Large Language Models) per generare testo, codice o immagini, oppure calcolare embeddings o trascrivere audio. Come puoi farlo usando Azure OpenAI?

## SOLUZIONE
Utilizza il servizio Azure OpenAI per accedere e gestire modelli come gpt-4, gpt-35-turbo, text-embedding-ada, dall-e, whisper, ecc.

## COMPONENTI NECESSARI

| Componente | Descrizione |
|------------|-------------|
| Azure OpenAI Resource | Risorsa principale da creare nel portale o via CLI |
| Azure CLI / Azure Portal | Per creare e gestire risorse e deployment dei modelli |
| API Key e Endpoint | Per autenticarsi e fare chiamate REST o tramite SDK |
| Modello da deployare | Es: gpt-35-turbo, text-embedding-ada, dall-e, whisper |
| Deployment Name | Alias del modello per l'applicazione |
| SDK (Python: openai) | Per integrare i modelli nel tuo codice (chat, completions, embeddings, ecc.) |

## PROCEDURA OPERATIVA

### 1. Creare la risorsa Azure OpenAI (CLI)
```bash
az cognitiveservices account create \
-n MyOpenAIResource \
-g OAIResourceGroup \
-l eastus \
--kind OpenAI \
--sku s0 \
--subscription subscriptionID
```

### 2. Deploy di un modello (es. GPT-35 Turbo)
```bash
az cognitiveservices account deployment create \
   -g OAIResourceGroup \
   -n MyOpenAIResource \
   --deployment-name MyModel \
   --model-name gpt-35-turbo \
   --model-version "0125"  \
   --model-format OpenAI \
   --sku-name "Standard" \
   --sku-capacity 1
```

### 3. Utilizzo tramite API (REST – esempio chat completions)
```bash
curl https://<ENDPOINT>.openai.azure.com/openai/deployments/<DEPLOYMENT_NAME>/chat/completions?api-version=2023-03-15-preview \
  -H "Content-Type: application/json" \
  -H "api-key: <API_KEY>" \
  -d '{
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is Azure OpenAI?"}
    ]
}'
```

### 4. Utilizzo tramite Python SDK
```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="<YOUR_ENDPOINT_NAME>",
    api_key="<YOUR_API_KEY>",
    api_version="2024-02-15-preview"
)

response = client.chat.completions.create(
    model="<YOUR_DEPLOYMENT_NAME>",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]
)
print(response.choices[0].message.content)
```

## TIPI DI MODELLI DISPONIBILI

| Categoria | Modello (esempio) | Descrizione |
|-----------|-------------------|-------------|
| LLM Chat | gpt-4, gpt-35-turbo | Generazione testo/conversazioni/chatbot |
| Codice | gpt-35-turbo | Code generation |
| Embedding | text-embedding-ada:002 | Trasforma testo in vettori numerici |
| Immagini | dall-e | Genera immagini da prompt (preview) |
| Speech-to-text | whisper | Trascrive audio in testo |
| Text-to-speech | text-to-speech | Genera voce da testo |

## PERMESSI NECESSARI

| Ruolo Azure | Permessi |
|-------------|----------|
| Cognitive Services OpenAI User | Visualizzazione risorsa, playground |
| Cognitive Services OpenAI Contributor | Creazione deployment |

## CASI D'USO COMUNI

| Obiettivo | Modello consigliato | Endpoint |
|-----------|-------------------|----------|
| Chatbot / Assistant | gpt-35-turbo | chat/completions |
| Motore di ricerca semantico | text-embedding-ada:002 | embeddings |
| Generazione codice | gpt-4 o gpt-35-turbo | completions |
| Analisi similitudini tra testi | text-similarity-* | embeddings |
| Generazione immagini | dall-e | images/generations |
| Trascrizione vocale | whisper | audio/transcriptions |

## DOMANDE D'ESAME SIMULATE

1. **Hai bisogno di un chatbot aziendale su sito web. Quale modello Azure OpenAI useresti e come lo configureresti?**

2. **Devi implementare una ricerca semantica per confrontare descrizioni prodotto. Che modello usi?**

3. **Vuoi generare automaticamente codice Python a partire da prompt naturali. Quale modello e endpoint?**

4. **Vuoi integrare l'AI nel tuo codice Python: quali parametri sono necessari per connetterti?**

5. **Quali ruoli RBAC sono richiesti per creare un deployment di un modello GPT in azienda?**