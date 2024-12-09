from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://127.0.0.1:5500/*", "http://localhost:5500/*"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve the HTML file
@app.route("/")
def index():
    return jsonify({
        "message": "Hello, World!"
    })

@app.route("/upload_audio", methods=["POST"])
def upload_audio():
    print(request.files)
    if "audio" not in request.files:
        print("No audio file uploaded")
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["audio"]
    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    print(f"Saved audio chunk: {file_path}")
    return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

if __name__ == "__main__":
    app.run(debug=True)
