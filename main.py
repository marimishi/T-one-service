from fastapi import FastAPI, UploadFile, File
import tempfile, shutil
from service import transcribe_audio
import os

app = FastAPI(title="T-one")

@app.post("/voice")
async def endpoint(audio: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=audio.filename) as tmp:
        shutil.copyfileobj(audio.file, tmp)
        tmp_path = tmp.name

    try:
        text = transcribe_audio(tmp_path)
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}
    finally: 
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)