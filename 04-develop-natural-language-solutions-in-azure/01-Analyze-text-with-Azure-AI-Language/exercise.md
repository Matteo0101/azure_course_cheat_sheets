✅ Analyze-text-with-Azure-AI-Language

🧩 Problem
You need to analyze text documents (e.g., reviews) to automatically extract insights such as the language, sentiment, key topics, entities, and linked entities to improve decision-making or content understanding.

💡 Solution with Azure
Use the Text Analytics capabilities in Azure AI Language to analyze documents. It enables language detection, sentiment analysis, key phrase extraction, named entity recognition, and detection of linked entities via SDK or REST API.

🧱 Required Components
Azure AI Language resource

Endpoint and subscription key (from Azure Portal)

Text Analytics SDK for C# or Python (azure-ai-textanalytics==5.3.0)

(Optional) .env or appsettings.json for secure key configuration

Cloud Shell + GitHub repo: https://github.com/microsoftlearning/mslearn-ai-language

🏗️ Architecture / Development
1. Provision Azure AI Language Resource
In Azure Portal → Create resource → Search "Language Service"

Use Pricing tier F0 (free) if available

Once deployed, go to Keys and Endpoint to retrieve connection details

2. Clone Code Repository in Azure Cloud Shell
bash
Copia
Modifica
rm -r mslearn-ai-language -f
git clone https://github.com/microsoftlearning/mslearn-ai-language
cd mslearn-ai-language/Labfiles/01-analyze-text
3. Install SDK & Configure App
Navigate to:

cd Python/text-analysis or cd C-Sharp/text-analysis

Python:

bash
Copia
Modifica
python -m venv labenv
./labenv/bin/Activate.ps1
pip install -r requirements.txt azure-ai-textanalytics==5.3.0
C#:

bash
Copia
Modifica
dotnet add package Azure.AI.TextAnalytics --version 5.3.0
4. Update Config File with Azure Credentials
Python: edit .env

C#: edit appsettings.json

Add ai_key and ai_endpoint

💬 Text Analysis Functionalities
a. Language Detection
Detects the language of a text sample.

Python:

python
Copia
Modifica
detectedLanguage = ai_client.detect_language(documents=[text])[0]
print("Language:", detectedLanguage.primary_language.name)
C#:

csharp
Copia
Modifica
DetectedLanguage detectedLanguage = aiClient.DetectLanguage(text);
Console.WriteLine($"Language: {detectedLanguage.Name}");
b. Sentiment Analysis
Classifies the sentiment as positive, negative, neutral, or mixed.

Python:

python
Copia
Modifica
sentimentAnalysis = ai_client.analyze_sentiment(documents=[text])[0]
print("Sentiment:", sentimentAnalysis.sentiment)
C#:

csharp
Copia
Modifica
DocumentSentiment sentimentAnalysis = aiClient.AnalyzeSentiment(text);
Console.WriteLine($"Sentiment: {sentimentAnalysis.Sentiment}");
c. Key Phrase Extraction
Extracts main concepts or ideas from the text.

Python:

python
Copia
Modifica
phrases = ai_client.extract_key_phrases(documents=[text])[0].key_phrases
for phrase in phrases:
    print(phrase)
C#:

csharp
Copia
Modifica
KeyPhraseCollection phrases = aiClient.ExtractKeyPhrases(text);
foreach (string phrase in phrases)
    Console.WriteLine(phrase);
d. Named Entity Recognition (NER)
Identifies named entities like locations, people, organizations.

Python:

python
Copia
Modifica
entities = ai_client.recognize_entities(documents=[text])[0].entities
for entity in entities:
    print(f"{entity.text} ({entity.category})")
C#:

csharp
Copia
Modifica
CategorizedEntityCollection entities = aiClient.RecognizeEntities(text);
foreach (var entity in entities)
    Console.WriteLine($"{entity.Text} ({entity.Category})");
e. Linked Entity Recognition
Finds entities with external links (e.g., Wikipedia).

Python:

python
Copia
Modifica
entities = ai_client.recognize_linked_entities(documents=[text])[0].entities
for entity in entities:
    print(f"{entity.name} ({entity.url})")
C#:

csharp
Copia
Modifica
LinkedEntityCollection linkedEntities = aiClient.RecognizeLinkedEntities(text);
foreach (var linkedEntity in linkedEntities)
    Console.WriteLine($"{linkedEntity.Name} ({linkedEntity.Url})");
✅ Best Practices / Considerations
Use Cloud Shell for quick development/testing

Use .env/appsettings.json to secure sensitive info

Batch process documents to reduce API calls

Analyze sentiment trends over time in reviews or feedback

Detect named and linked entities for deeper contextual understanding

Consider rate limits and pricing tier when analyzing large text volumes

