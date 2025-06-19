# Azure AI Speech Service Implementation Guide

## 🧩 Problem
You need to implement an application that can recognize spoken commands and respond with synthesized speech output.

## 💡 Solution with Azure
Use Azure AI Speech service:
- Speech-to-Text API for recognizing speech
- Text-to-Speech API for generating speech output

## 🛠️ Components required
- Azure AI Speech resource (created via Azure Portal)
- Visual Studio Code
- Language SDK:
  - Microsoft.CognitiveServices.Speech NuGet package (C#)
  - azure-cognitiveservices-speech pip package (Python)
- (Optional) Audio input/output libraries:
  - System.Media.SoundPlayer (C#)
  - playsound (Python)
- Microphone (or use audio file as alternative)

GitHub repository: https://github.com/MicrosoftLearning/mslearn-ai-language

## 🏗️ Architecture / Development

### 1. 🔧 Provision Azure AI Speech resource
Azure Portal → Azure AI Services → Create Speech Service

Required settings: Subscription, Resource group, Region, Name, Pricing tier

After deployment: Get Key and Region from Keys and Endpoint

### 2. 🧑‍💻 Set up development environment
- Clone repo: mslearn-ai-language
- Open in VS Code → trust project if prompted
- Use Labfiles/07-speech → choose CSharp or Python → speaking-clock folder

### 3. 📦 Install SDK

**C#**
```bash
dotnet add package Microsoft.CognitiveServices.Speech --version 1.30.0
```

**Python**
```bash
pip install azure-cognitiveservices-speech==1.30.0
```

### 4. ⚙️ Configure app
Edit configuration file:
- C#: appsettings.json
- Python: .env

Add key and region

### 5. 🧠 Initialize SDK

**C#:**
```csharp
using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Audio;
speechConfig = SpeechConfig.FromSubscription(aiSvcKey, aiSvcRegion);
speechConfig.SpeechSynthesisVoiceName = "en-US-AriaNeural";
```

**Python:**
```python
import azure.cognitiveservices.speech as speech_sdk
speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"
```

### 6. 🎤 Recognize speech input

**Microphone**

**C#:**
```csharp
using AudioConfig audioConfig = AudioConfig.FromDefaultMicrophoneInput();
using SpeechRecognizer speechRecognizer = new SpeechRecognizer(speechConfig, audioConfig);
```

**Python:**
```python
audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
```

**Or from audio file**

Install playback:

**C#:**
```bash
dotnet add package System.Windows.Extensions --version 4.6.0
```

**Python:**
```bash
pip install playsound==1.2.2
```

Add code:

**C#:**
```csharp
string audioFile = "time.wav";
SoundPlayer wavPlayer = new SoundPlayer(audioFile);
wavPlayer.Play();
using AudioConfig audioConfig = AudioConfig.FromWavFileInput(audioFile);
```

**Python:**
```python
from playsound import playsound
audioFile = os.getcwd() + '\\time.wav'
playsound(audioFile)
audio_config = speech_sdk.AudioConfig(filename=audioFile)
```

### 7. 📜 Transcribe speech

**C#:**
```csharp
SpeechRecognitionResult speech = await speechRecognizer.RecognizeOnceAsync();
if (speech.Reason == ResultReason.RecognizedSpeech) {
    command = speech.Text;
    Console.WriteLine(command);
}
```

**Python:**
```python
speech = speech_recognizer.recognize_once_async().get()
if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
    command = speech.text
    print(command)
```

### 8. 🗣️ Synthesize speech

**C#:**
```csharp
using SpeechSynthesizer speechSynthesizer = new SpeechSynthesizer(speechConfig);
SpeechSynthesisResult speak = await speechSynthesizer.SpeakTextAsync(responseText);
```

**Python:**
```python
speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
speak = speech_synthesizer.speak_text_async(response_text).get()
```

### 9. 🔊 Use alternative voice

**C#:**
```csharp
speechConfig.SpeechSynthesisVoiceName = "en-GB-LibbyNeural";
```

**Python:**
```python
speech_config.speech_synthesis_voice_name = 'en-GB-LibbyNeural'
```

### 10. 📝 Use SSML

**C#:**
```csharp
string responseSsml = $@"
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>
  <voice name='en-GB-LibbyNeural'>
    {responseText}
    <break strength='weak'/>
    Time to end this lab!
  </voice>
</speak>";
SpeechSynthesisResult speak = await speechSynthesizer.SpeakSsmlAsync(responseSsml);
```

**Python:**
```python
responseSsml = " \
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
  <voice name='en-GB-LibbyNeural'> \
    {} \
    <break strength='weak'/> \
    Time to end this lab! \
  </voice> \
</speak>".format(response_text)
speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
```

## 🧠 Best practice / Considerations
- Ensure correct region and key in configuration
- Use neural voices for more natural synthesis
- Use SSML to control prosody, pauses, and emphasis
- Provide fallback for missing microphone by using audio file
- Handle recognition result errors (No match, Cancelled)
- Use await/.get() as appropriate for async methods

## ❓ Exam-style questions

**Q1. How do you configure speech recognition using the default microphone in Python?**
- 🅐 speech_sdk.SpeechRecognizer(audio_input="mic")
- 🅑 speech_sdk.AudioConfig(use_default_microphone=True) ✅
- 🅒 AudioConfig.FromWavFileInput("mic.wav")
- 🅓 SpeechSynthesizer(speech_config, audio=True)

**Q2. What must you do to synthesize speech with a custom voice in Azure AI Speech?**
- 🅐 Change your subscription tier
- 🅑 Use SSML
- 🅒 Set SpeechSynthesisVoiceName in the config ✅
- 🅓 Install a separate neural voice package

**Q3. Where do you find the key and region for your Azure AI Speech resource?**
- 🅐 Azure AI Studio
- 🅑 Speech Studio → Deployment tab
- 🅒 Keys and Endpoint page in the Azure Portal ✅
- 🅓 Billing page in Azure