from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io

text = "Hi this is Adam!"
language = 'en'

tts = gTTS(text=text, lang=language)

# ✅ Correct way: write to memory buffer
mp3_fp = io.BytesIO()
tts.write_to_fp(mp3_fp)

# Move to beginning of buffer
mp3_fp.seek(0)

# Convert to AudioSegment
audio_segment = AudioSegment.from_file(mp3_fp, format="mp3")

# Play audio
play(audio_segment)
