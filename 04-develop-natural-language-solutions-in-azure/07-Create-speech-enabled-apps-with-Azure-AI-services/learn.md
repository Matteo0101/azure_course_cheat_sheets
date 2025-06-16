# 🧠 Speech Recognition and Synthesis with Azure AI Speech

## ❓ Problem
You need to build an application that can recognize spoken input and/or generate spoken output. How can you use Azure AI Speech to implement speech recognition (speech to text) and synthesis (text to speech)?

## ✅ Solution with Azure
Use the Azure AI Speech service, which offers the following APIs:

- **Speech to Text** (real-time, batch, or custom)
- **Text to Speech** (interactive or batch)
- **Optional**: SSML for fine-grained control of speech output

Provision an Azure AI Speech or Azure AI Services resource to start using the SDKs or REST APIs.

## 🧩 Components Required

- Azure AI Speech resource (or AI Services resource)
- Speech SDK (language-specific: Python, C#, etc.)
- Keys and endpoint from Azure portal
- SpeechConfig for resource connection (location + key)
- AudioConfig for audio input/output (mic, speakers, file, or stream)
- SpeechRecognizer (for recognition)
- SpeechSynthesizer (for synthesis)
- Optional: SSML string for advanced control

## 🏗️ Architecture / Development

### 🗣️ Speech to Text

1. Create SpeechConfig with resource key and region.
2. Create optional AudioConfig (default mic or audio file).
3. Instantiate SpeechRecognizer using the configs.
4. Use `RecognizeOnceAsync()` to transcribe.
5. Inspect SpeechRecognitionResult for:
   - Text (recognized text)
   - Reason (RecognizedSpeech, NoMatch, Canceled)
   - Other metadata like Duration, OffsetInTicks, ResultId.

**✅ Supports:**
- Real-time transcription
- Batch transcription
- Custom models for domain accuracy

### 🔊 Text to Speech

1. Create SpeechConfig with resource key and region.
2. Create optional AudioConfig (default speaker, file, or stream).
3. Instantiate SpeechSynthesizer using the configs.
4. Use `SpeakTextAsync("your text")` for basic synthesis.
5. Inspect SpeechSynthesisResult for:
   - AudioData (output stream)
   - Reason (SynthesizingAudioCompleted)
   - ResultId, Properties

**✅ Supports:**
- Standard and neural voices
- Batch synthesis for large text
- Voice customization using SpeechSynthesisVoiceName

## ⚙️ Configure Audio Format and Voices

- Use `SetSpeechSynthesisOutputFormat()` to define:
  - Format (e.g., Riff24Khz16BitMonoPcm)
- Use SpeechSynthesisVoiceName to specify voice:
  - E.g., en-GB-George
  - Types: Standard and Neural

## 🧾 Speech Synthesis Markup Language (SSML)

XML-based markup for detailed speech control

**Allows:**
- Speaking styles (e.g., cheerful, angry)
- Pauses, phonemes
- Prosody (pitch, rate, volume)
- Say-as rules (e.g., dates, numbers)
- Multiple voices in dialog

Use `SpeakSsmlAsync(ssml_string)` to invoke

**Example SSML:**

```xml
<speak xmlns="http://www.w3.org/2001/10/synthesis" 
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US"> 
  <voice name="en-US-AriaNeural"> 
    <mstts:express-as style="cheerful"> I say tomato </mstts:express-as> 
  </voice> 
  <voice name="en-US-GuyNeural"> 
    I say <phoneme alphabet="sapi" ph="t ao m ae t ow"> tomato </phoneme>. 
    <break strength="weak"/>Lets call the whole thing off! 
  </voice> 
</speak>
```

## 🧠 Best Practice / Considerations

- Always secure and rotate keys from the Azure portal.
- Use neural voices for better realism.
- Choose the appropriate audio format and sampling rate based on your output use case (e.g., media, telephony).
- Use SSML for fine control in UX-heavy applications.
- For large-scale operations, prefer batch APIs to reduce latency and improve throughput.
- Handle API response Reason fields to detect and troubleshoot issues.

## 📝 Simulated Exam Questions

**Q: You need to convert text into speech and play it through a non-default speaker. Which components are necessary in the SDK?**
A: SpeechConfig, AudioConfig, SpeechSynthesizer

**Q: How do you change the speech output to a cheerful voice tone in Azure AI Speech?**
A: Use SSML with `<mstts:express-as style="cheerful">`

**Q: Which method would you use to transcribe a single utterance using the Speech SDK?**
A: `RecognizeOnceAsync()`

**Q: You need to process prerecorded audio in bulk. What should you use?**
A: Batch transcription via Speech to Text API

**Q: How can you specify a neural voice in your speech synthesis code?**
A: Set `SpeechConfig.SpeechSynthesisVoiceName = "en-US-AriaNeural"`

**Q: What does a NoMatch result from RecognizeOnceAsync() indicate?**
A: The audio was parsed, but no speech was recognized.

**Q: Which SDK method should you use to process SSML content?**
A: `SpeakSsmlAsync()`

**Q: You want a high-quality 24kHz, 16-bit mono output file. How do you configure this?**
A: `SetSpeechSynthesisOutputFormat(SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)`