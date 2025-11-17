import gradio as gr
from service import transcribe_audio

def transcribe_gradio(file):
    if file is None:
        return "Файл не загружен"
    return transcribe_audio(file)

with gr.Blocks(title="T-one Demo") as demo:
    
    audio = gr.Audio(
        sources=["microphone", "upload"],
        type="filepath", 
        label="Запишите с микрофона или загрузите файл"
    )
    
    out = gr.Textbox(label="Результат")
    audio.change(transcribe_gradio, inputs=audio, outputs=out)

if __name__ == "__main__":
    demo.launch()