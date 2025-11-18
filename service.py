from tone import StreamingCTCPipeline, read_audio
from model import Model

def transcribe_audio(file_path: str) -> str:
    try:
        audio = read_audio(file_path)
        model = Model()
        result = model.transcribe_offline(audio)
        return " ".join([x.text for x in result])
    except Exception as e:
        return f"Ошибка транскрибации: {str(e)}"