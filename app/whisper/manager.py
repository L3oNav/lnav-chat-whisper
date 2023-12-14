from app.utils.manager import Manager
from app.whisper.models import Script
class WhisperManager(Manager):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key

    def process_audio(self, audio_file_path):
        try:
            # Load the Whisper model (assuming it's pre-loaded)
            model = whisper.load_model("base")

            # Load audio from the given file and pad/trim it
            audio = whisper.load_audio(audio_file_path)
            audio = whisper.pad_or_trim(audio)

            # Make a log-Mel spectrogram and move it to the model's device
            mel = whisper.log_mel_spectrogram(audio).to(model.device)

            # Detect the spoken language
            _, probs = model.detect_language(mel)
            detected_language = max(probs, key=probs.get)

            # Decode the audio
            options = whisper.DecodingOptions()
            result = whisper.decode(model, mel, options)

            # Process the recognized text or language as needed
            recognized_text = result.text

            # For demonstration, we print the detected language and recognized text
            print(f"Detected language: {detected_language}")
            print(f"Recognized text: {recognized_text}")

            # Implement further processing or storage of the recognized text
            return recognized_text
        except Exception as e:
            raise Exception(f"Error processing audio: {str(e)}")

    def new_script(self, script, language, message_id):
        try:
            script = Script(script=script, language=language, message_id=message_id)
            self.session.add(script)
            self.session.commit()
            return script
        except Exception as e:
            raise Exception(f"Error creating script: {str(e)}")

    def run_processing_loop(self):
        while not self.audio_queue.empty():
            audio_file_path = self.audio_queue.get()
            
            try:
                transcription = self.process_audio(audio_file_path)
                # Remove the processed audio file from the queue
                self.remove_processed_audio(audio_file_path)
                
            except Exception as e:
                # Handle errors and retries here
                print(f"Error processing audio file {audio_file_path}: {str(e)}")
