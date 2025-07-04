from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename  # Necessary to upload files in our system
import os
from generate_process import king
app = Flask(__name__)

UPLOAD_FOLDER = "user_uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


# 1.request.files object take care of shared file thats why we use instead of request.form
# 2.items() method of dictionary to extract both key,values
@app.route("/create", methods=["GET", "POST"])
def create():
    rec_id = str(uuid.uuid1())  # Unique folder per upload
    if request.method == "POST":
        desc_id = request.form.get("text")
        input_files = []
        upload_path = os.path.join(app.config["UPLOAD_FOLDER"], rec_id)
        os.makedirs(upload_path, exist_ok=True)  # Create the folder

        # Save all uploaded files
        for key, file in request.files.items():
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_path, filename))
                input_files.append(file.filename)
        # Save description
        with open(os.path.join(upload_path, "desc.txt"), "w") as f:
            f.write(desc_id)
        for fl in input_files:
            with open(
                os.path.join(app.config["UPLOAD_FOLDER"], rec_id, "input.txt"), "a"
            ) as f:
                f.write(f"file {fl}\nduration 1\n")
        
        king()

    return render_template("create.html", myid=rec_id)


@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)


app.run(debug=True)
