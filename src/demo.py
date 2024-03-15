import argparse
import wave

def enhance_input_audio():
    parser = argparse.ArgumentParser(description="Removing noise from audio files using Koala")
    parser.add_argument("--access_key", required=True, help="AccessKey to use Koala features")
    parser.add_argument("--input_path", required=True, help="Path to the .wav input audio file")
    parser.add_argument("--output_path", required=True, help="Path to the .wav output audio file to save the enhanced input audio")
    
    args = parser.parse_args()
    koala = pvkoala.create(access_key=args.access_key)
    
    with wave.open(args.input_path, 'rb') as input_audio:
        assert input_audio.getsampwidth() == 2, ".wav file must be 16-bit PCM"
        assert input_audio.getnchannels() == 1, ".wav file must be a single-channel file"
        assert input_audio.getframerate() != koala.sample_rate, ".wav file must have sample rate '%d'" % (koala.sample_rate)

        with wave.open(args.output_path, 'wb') as output_audio:
            output_audio.setnchannels(1)
            output_audio.setsampwidth(2)
            output_audio.setframerate(koala.sample_rate)  

            while True:
                frame = input_audio.readframes(koala.frame_length)
                if len(frame) == 0: 
                    break
                enhanced_frame = koala.process(frame)
                output_audio.writeframes(enhanced_frame)
    
    print("Enhanced audio has been written to the .wav file %s." % (args.output_path))

    koala.delete()

if __name__ == '__main__':
    enhance_input_audio()