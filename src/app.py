from flask import Flask, request, send_from_directory, render_template
from src.demo import enhance_input_audio
import os

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
upload_folder = os.path.join(base_dir,f"files/input")
output_folder = os.path.join(base_dir,f"files/output")
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['OUTPUT_FOLDER'] = output_folder

@app.route('/', methods=['GET', 'POST'])
def upload_and_process_audio_files():
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

    if request.method == 'POST':
        file = request.files['file']
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], file.filename)
        
        file.save(input_path) 
        
        enhance_input_audio("ACCESS_KEY", input_path, output_path) 
        
        return send_from_directory(app.config['OUTPUT_FOLDER'], file.filename, as_attachment=True)

    return render_template('process_files.html')

if __name__ == '__main__':
    app.run(debug=True)
