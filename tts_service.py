import edge_tts
import asyncio
import tempfile
import os


DEFAULT_VOICE = "en-US-JennyNeural"


async def _generate_audio(text: str, voice: str, output_path: str):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)


def text_to_speech(text: str, voice: str = DEFAULT_VOICE) -> str:
    """
    Text ko audio file mein convert karta hai.
    Returns: temp audio file ka path
    """
    # Unique temp file banao
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp.close()
    
    try:
        asyncio.run(_generate_audio(text, voice, tmp.name))
        return tmp.name
    except Exception as e:
        if os.path.exists(tmp.name):
            os.remove(tmp.name)
        raise ValueError(f"TTS fail: {str(e)}")


def cleanup_audio(path: str):
    """Temp audio file delete karo."""
    try:
        if path and os.path.exists(path):
            os.remove(path)
    except Exception:
        pass