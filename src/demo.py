import argparse
import wave
import struct
import pvkoala

def enhance_input_audio():
    parser = argparse.ArgumentParser(description="Removing noise from audio files using Koala")
    parser.add_argument("--access_key", required=True, help="AccessKey to use Koala features")
    parser.add_argument("--input_path", required=True, help="Path to the .wav input audio file")
    parser.add_argument("--output_path", required=True, help="Path to the .wav output audio file to save the enhanced input audio")
    
    args = parser.parse_args()
    koala = pvkoala.create(access_key=args.access_key)
    
    with wave.open(args.input_path, 'rb') as input_audio:
        assert input_audio.getsampwidth() == 2 
        assert input_audio.getnchannels() == 1 
        assert input_audio.getframerate() == koala.sample_rate
        
        with wave.open(args.output_path, 'wb') as output_audio:
            output_audio.setnchannels(1)
            output_audio.setsampwidth(2)
            output_audio.setframerate(koala.sample_rate)

            input_num_frames = input_audio.getnframes()
            current_sample = 0

            # Continue looping until all the input audio is processed, must account for the delay introduced by Koala SDK processing
            while current_sample < input_num_frames + koala.delay_sample:
                # Get a frame of audio with the size of Koala's frame length
                frame_data = input_audio.readframes(koala.frame_length)
                # Pad the frame with zeros so the last frame can still be processed if it is smaller than Koala's frame byte length (16-bit so 2 bytes)
                if len(frame_data) < koala.frame_length * 2:  
                    frame_data += b'\x00' * (koala.frame_length * 2 - len(frame_data))

                # Unpack the frame in bytes into samples so it can be enhanced by Koala
                converted_frame = struct.unpack('%dh' % koala.frame_length, frame_data)
                output_frame = koala.process(converted_frame)
                
                # Sample point must be past the delay to ensure that each frame gets fully processed, then pack the samples into bytes again, so it can be 
                # stored in an output .wav file
                if current_sample >= koala.delay_sample:
                    output_audio.writeframes(struct.pack('%dh' % len(output_frame), *output_frame))

                current_sample += koala.frame_length

    print("Enhanced audio has been written to %s." % (args.output_path))
    koala.delete()

if __name__ == '__main__':
    enhance_input_audio()
