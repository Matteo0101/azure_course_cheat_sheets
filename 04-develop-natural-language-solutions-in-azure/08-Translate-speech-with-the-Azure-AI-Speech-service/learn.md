# Azure AI Speech Translation Guide

## 🎯 Problem
You need to implement a real-time **speech-to-text translation** solution, possibly with **speech output** in the target language(s).

## ✅ Solution with Azure
Use **Azure AI Speech Translation** service via the **Speech SDK**, which enables real-time **speech recognition, translation, and synthesis** into one or more target languages.

## 🧩 Componenti richiesti
* ✅ Azure AI Speech resource (or Azure AI Services resource)
* ✅ Azure AI Speech SDK (supports C#, Python, etc.)
* ✅ `SpeechTranslationConfig` object
* ✅ `TranslationRecognizer` object
* ✅ Optional: `SpeechSynthesizer` (for audio output)
* ✅ Optional: `AudioConfig` (for specifying input/output source)

## 🛠️ Architettura / Sviluppo

### 🔹 Provision Azure Speech Resource
* Create a Speech resource in Azure
* Retrieve:
   * **Location** (e.g., `eastus`)
   * **Key** (from Keys and Endpoint section in Azure Portal)

### 🔹 Speech-to-Text Translation
**Flow using SDK:**
1. Create `SpeechTranslationConfig` using your Azure key + region
2. Specify:
   * Source (speech recognition) language
   * One or more target languages
3. (Optional) Use `AudioConfig` for custom audio input
4. Create a `TranslationRecognizer` with the above
5. Call `RecognizeOnceAsync()` to:
   * Transcribe spoken input
   * Translate it into target language(s)
6. Use result properties:
   * `Text`: original transcription
   * `Translations`: dictionary of target language translations
   * `Reason`: check if translation is successful (e.g., `RecognizedSpeech`)

### 🔹 Synthesize Translations (Speech-to-Speech)

#### 🟣 Event-Based Synthesis
* Use only for **1:1** translation
* In `TranslationConfig`, set the voice for target speech
* Add handler for `Synthesizing` event on `TranslationRecognizer`
* In handler: call `.GetAudio()` to get translated audio stream

#### 🟢 Manual Synthesis
* Use for **1:n** translations (multiple targets)
* Steps:
   1. Use `TranslationRecognizer` → get `Translations` dictionary
   2. For each translation:
      * Create a `SpeechSynthesizer`
      * Call `SpeakTextAsync()` for each translated string

## 🧠 Best Practice / Considerazioni
* 🔐 Always secure and store resource **keys and endpoints** properly
* 🌐 Use **standard ISO language codes** (e.g., `en`, `fr`)
* 🧪 **Test voice compatibility** when using neural voices in synthesis
* ⚡ **Event-based synthesis** better for low-latency 1:1 flows
* 🔄 Use **manual synthesis** for multi-language or post-processed translations

## ❓ Domande simulate d'esame

### 1.
**Q:** What configuration object is required to define the source and target languages for speech translation in Azure AI Speech SDK?  
**A:** `SpeechTranslationConfig`

### 2.
**Q:** What object in the Azure Speech SDK is used to retrieve translated audio via an event handler?  
**A:** `TranslationRecognizer` with a `Synthesizing` event handler

### 3.
**Q:** Which result property contains the translated text for each target language?  
**A:** `Translations` (dictionary in the result object)

### 4.
**Q:** How can you perform speech-to-speech translation for multiple target languages without handling events?  
**A:** Use **manual synthesis**: iterate through `Translations` and call `SpeakTextAsync()` for each.