from gtts import gTTS
tts = gTTS(text="Hi", lang='tr')
tts.save("audio1.mp3")
