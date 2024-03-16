# Koala-Noise-Suppression-Demo

## Requirements

- Need Python 3.7 or higher to use Koala SDK

## Installation

```console
pip3 install -r requirements.txt
```

## AccessKey

Obtain `AccessKey` key to initialize Koala and run the demo file/Flask app by signing up or logging into the Picovoice Console
at (https://console.picovoice.ai/). There are placeholders inserted into the source code in this repository that must be swapped with your personal `AccessKey` to test the source code.

## Demo File

To test the demo audio file, we can run the following command in the terminal:

```console
python3 demo.py --access_key ${ACCESS_KEY} --input_path ${WAV_INPUT_PATH} --output_path ${WAV_OUTPUT_PATH}
```

Replace `${ACCESS_KEY}` with your personal `AccessKey`, `${WAV_INPUT_PATH}` with a path to the `.wav` file you are looking to enhance, which meets the requirements outlined in the Picovoice Docs, and `${WAV_OUTPUT_PATH}` with a path to a `.wav` file that you would like to store the enhanced audio in. 

## Flask App (Meeting/Lecture Transcription Assistant)

To test the Flask application, navigate to the directory where app.py is stored and enter the following commands into the terminal:

```console
export FLASK_APP=app.py
flask run
```
Now open the development server to view the UI page and interact with the application.

## Side Notes

The source code found in this repository displays the functionality of Koala for suppressing noise in audio files, for simplicity purposes. To suppress noise in real-time audio, refer to Picovoice repositories where a demo is provided to transform real-time audio making use of Picovoice's `pvrecorder` package. 
This source code only handles .wav files that meet the requirements outlined in Picovoice repositories. To convert different audio file formats such as .mp3, we would have to first convert it over to the PCM format that Koala can process.


