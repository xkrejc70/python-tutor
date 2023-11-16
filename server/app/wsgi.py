from flask import Flask, jsonify, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import socket
import os


UPLOAD_FOLDER = 'server/app/uploads'
ALLOWED_EXTENSIONS = {'py'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# api
@app.route("/api", methods=['GET'])
def return_home():
    return jsonify({"host": "Hostname: " + socket.gethostname()})

# uploads
@app.route("/api/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            app.logger.debug('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            app.logger.debug('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            app.logger.debug('it is py')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            app.logger.debug('not .py')


    return jsonify({"host": "Hostname"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)