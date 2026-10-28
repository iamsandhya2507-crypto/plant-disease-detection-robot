from pathlib import Path
from uuid import uuid4
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def simulated_robot_decision():
    # Simulation only. This function is not connected to physical hardware.
    return "SIMULATION: refer the plant for human inspection; no spraying performed."

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        image = request.files.get("leaf_image")
        if not image or image.filename == "":
            message = "Please choose a leaf image."
        elif not allowed_file(image.filename):
            message = "Upload a PNG, JPG, JPEG, or WEBP image."
        else:
            safe_name = secure_filename(image.filename)
            image.save(UPLOAD_DIR / f"{uuid4().hex}_{safe_name}")
            message = ("Image received. No trained disease-classification model is connected, "
                       "so this demo cannot identify a disease.")
    return render_template("index.html", message=message, robot_message=simulated_robot_decision())

@app.errorhandler(413)
def too_large(_error):
    return "Image is too large. Maximum upload size is 5 MB.", 413

if __name__ == "__main__":
    app.run(debug=True)
