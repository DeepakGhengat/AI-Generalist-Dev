#!/usr/bin/env python3
"""
Ultra Simple Voice to Prompt - Absolute minimum!
Just speak → get markdown. That's it!
"""

import os, sys, wave, pyaudio, openai, threading
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def record(sec=30):
    print(f"🎤 Recording (max {sec}s)... SPEAK! Press ENTER to stop.")
    p, s = pyaudio.PyAudio(), []
    st = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

    stop_flag = {'stop': False}
    def wait_for_enter():
        input()
        stop_flag['stop'] = True

    threading.Thread(target=wait_for_enter, daemon=True).start()

    for i in range(int(16000/1024*sec)):
        if stop_flag['stop']:
            break
        s.append(st.read(1024))

    st.stop_stream(); st.close(); p.terminate()
    f = "temp.wav"
    w = wave.open(f, 'wb')
    w.setnchannels(1); w.setsampwidth(p.get_sample_size(pyaudio.paInt16)); w.setframerate(16000); w.writeframes(b''.join(s))
    w.close()
    print("⏹️  Recording stopped!")
    return f

def transcribe(f):
    print("📝 Transcribing...")
    return openai.Audio.transcribe(model="whisper-1", file=open(f, 'rb')).text

def format_text(t):
    print("✨ Formatting...")
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Convert this dictation into a clean, well-formatted markdown PROMPT only. Do NOT provide solutions, answers, or code. Just format the request clearly:\n\n{t}"}],
        max_tokens=2000
    ).choices[0].message.content

print("="*50)
audio = record()
text = transcribe(audio)
print(f"\n📋 You: {text}\n")
markdown = format_text(text)
file = f"prompt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
open(file, 'w').write(markdown)
print(f"💾 Saved: {file}\n\n{markdown}\n{'='*50}")
os.remove(audio)