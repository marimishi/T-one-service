import soundfile as sf
import numpy as np
import resampy
from model import Model

TARGET_SR = 16000

def read_audio_file(file_path: str):
    try:
        audio, sr = sf.read(file_path, dtype="float32", always_2d=False)

        if audio.ndim == 2:
            audio = np.mean(audio, axis=1)

        if sr != TARGET_SR:
            audio = resampy.resample(audio, sr, TARGET_SR)

        return audio
    except Exception as e:
        raise ValueError(f"Error reading file: {str(e)}")

def transcribe_audio(file_path: str) -> str:
    audio = read_audio_file(file_path)
    model = Model()
    result = model.transcribe_offline(audio)
    return " ".join([x.text for x in result])
