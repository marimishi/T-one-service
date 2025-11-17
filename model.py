from tone import StreamingCTCPipeline

class Model:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.pipeline = StreamingCTCPipeline.from_hugging_face()
        return cls._instance

    def transcribe_offline(self, audio):
        return self.pipeline.forward_offline(audio)
