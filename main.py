import argparse
from file_handlers import process_file
from tts_engine import TTSEngine

def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='Text-to-Speech from file')
    parser.add_argument('input_file', help='Path to input file (supports .txt, .pdf, .epub)')
    parser.add_argument('--speaker', default='audio/Harry.wav', help='Path to speaker voice sample')
    parser.add_argument('--language', default='en', help='Language code (default: en)')
    parser.add_argument('--output', default='output.wav', help='Output audio file path')
    
    args = parser.parse_args()

    try:
        # Extract text from input file
        text = process_file(args.input_file)
        
        # Initialize TTS engine
        tts_engine = TTSEngine()
        
        # Generate audio
        output_path = tts_engine.generate_audio(
            text=text,
            speaker_wav=args.speaker,
            language=args.language,
            output_path=args.output
        )
        
        print(f"Audio generated successfully: {output_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
