import torch
from TTS.api import TTS

class TTSEngine:
    def __init__(self, model_name="tts_models/multilingual/multi-dataset/your_tts"):
        """Initialize TTS engine with specified model."""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = TTS(model_name)

    def generate_audio(self, text, speaker_wav, language="en", output_path="output.wav"):
        """
        Generate audio from text using the specified speaker voice.
        
        Args:
            text (str): The text to convert to speech
            speaker_wav (str): Path to the speaker voice sample
            language (str): Language code (default: "en")
            output_path (str): Path where the output audio will be saved
        """
        self.tts.tts_to_file(
            text=text,
            speaker_wav=speaker_wav,
            language=language,
            file_path=output_path
        )
        return output_path
