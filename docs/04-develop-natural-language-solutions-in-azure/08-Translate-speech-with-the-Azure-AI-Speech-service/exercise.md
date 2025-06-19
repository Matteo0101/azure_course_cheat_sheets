# Azure AI Speech Translation Setup Guide

## ✅ 1. Provision Azure AI Speech Resource

1. Go to https://portal.azure.com
2. Search "Azure AI services" > Click Create under Speech service
3. Fill in:
   - **Subscription**: Your Azure sub
   - **Resource Group**: Create or choose
   - **Region**: Any available
   - **Name**: Unique
   - **Pricing**: Select F0 (Free) or S (Standard)
4. Agree to Responsible AI
5. Click Review + create > Create

After deployment, open the Keys and Endpoint page. You'll use the key and region in your code.

## ✅ 2. Prepare Development Environment

### Option A: Already cloned?
Just open mslearn-ai-language in VS Code.

### Option B: Clone the repo
1. Open VS Code
2. Press Ctrl+Shift+P → type Git: Clone → enter:
   ```bash
   https://github.com/MicrosoftLearning/mslearn-ai-language
   ```
3. Open the cloned folder in VS Code.
4. If prompted, trust the authors.
5. Don't add required assets if prompted.

## ✅ 3. Install Azure Speech SDK

Open terminal in:
```bash
Labfiles/08-speech-translation/<CSharp or Python>/translator
```

Run:

**For C#:**
```bash
dotnet add package Microsoft.CognitiveServices.Speech --version 1.30.0
```

**For Python:**
```bash
pip install azure-cognitiveservices-speech==1.30.0
```

## ✅ 4. Configure API Key and Region

- **C#**: Edit appsettings.json
- **Python**: Edit .env

Add your key and region from Azure (not the endpoint!).

## ✅ 5. Modify Code for Translation

Open:
- **C#**: Program.cs
- **Python**: translator.py

### Import namespaces

**C#:**
```csharp
using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Audio;
using Microsoft.CognitiveServices.Speech.Translation;
```

**Python:**
```python
import azure.cognitiveservices.speech as speech_sdk
```

### Configure Translation & Speech

**C#:**
```csharp
translationConfig = SpeechTranslationConfig.FromSubscription(aiSvcKey, aiSvcRegion);
translationConfig.SpeechRecognitionLanguage = "en-US";
translationConfig.AddTargetLanguage("fr");
translationConfig.AddTargetLanguage("es");
translationConfig.AddTargetLanguage("hi");

speechConfig = SpeechConfig.FromSubscription(aiSvcKey, aiSvcRegion);
```

**Python:**
```python
translation_config = speech_sdk.translation.SpeechTranslationConfig(ai_key, ai_region)
translation_config.speech_recognition_language = 'en-US'
translation_config.add_target_language('fr')
translation_config.add_target_language('es')
translation_config.add_target_language('hi')

speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
```

## ✅ 6. Translate Speech

### 🎤 Option A: Microphone Input

Add inside Translate function:

**C#:**
```csharp
using AudioConfig audioConfig = AudioConfig.FromDefaultMicrophoneInput();
using TranslationRecognizer translator = new TranslationRecognizer(translationConfig, audioConfig);
Console.WriteLine("Speak now...");
TranslationRecognitionResult result = await translator.RecognizeOnceAsync();
translation = result.Translations[targetLanguage];
Console.WriteLine(translation);
```

**Python:**
```python
audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config=audio_config)
print("Speak now...")
result = translator.recognize_once_async().get()
translation = result.translations[targetLanguage]
print(translation)
```

### 🔊 Option B: Use Audio File

Install sound library:

**C#:**
```bash
dotnet add package System.Windows.Extensions --version 4.6.0
```

**Python:**
```bash
pip install playsound==1.3.0
```

Then, add:

**C#:**
```csharp
using System.Media;

string audioFile = "station.wav";
SoundPlayer wavPlayer = new SoundPlayer(audioFile);
wavPlayer.Play();
using AudioConfig audioConfig = AudioConfig.FromWavFileInput(audioFile);
using TranslationRecognizer translator = new TranslationRecognizer(translationConfig, audioConfig);
TranslationRecognitionResult result = await translator.RecognizeOnceAsync();
translation = result.Translations[targetLanguage];
Console.WriteLine(translation);
```

**Python:**
```python
from playsound import playsound

audioFile = 'station.wav'
playsound(audioFile)
audio_config = speech_sdk.AudioConfig(filename=audioFile)
translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config=audio_config)
result = translator.recognize_once_async().get()
translation = result.translations[targetLanguage]
print(translation)
```

## ✅ 7. Add Speech Synthesis

Add under Synthesize translation comment:

**C#:**
```csharp
var voices = new Dictionary<string, string>
{
    ["fr"] = "fr-FR-HenriNeural",
    ["es"] = "es-ES-ElviraNeural",
    ["hi"] = "hi-IN-MadhurNeural"
};
speechConfig.SpeechSynthesisVoiceName = voices[targetLanguage];
using SpeechSynthesizer speechSynthesizer = new SpeechSynthesizer(speechConfig);
SpeechSynthesisResult speak = await speechSynthesizer.SpeakTextAsync(translation);
```

**Python:**
```python
voices = {
    "fr": "fr-FR-HenriNeural",
    "es": "es-ES-ElviraNeural",
    "hi": "hi-IN-MadhurNeural"
}
speech_config.speech_synthesis_voice_name = voices.get(targetLanguage)
speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
speak = speech_synthesizer.speak_text_async(translation).get()
```

## ✅ 8. Run the Program

From the terminal in the translator folder:

**C#:**
```bash
dotnet run
```

**Python:**
```bash
python translator.py
```

Follow the prompts, enter one of: fr, es, or hi, and speak or play your audio file.

## 📝 Notes

- You can retrieve all translations from result.translations.
- The Hindi output may not render properly in some consoles due to encoding.
- Azure allows both mic and file input; you can choose dynamically.