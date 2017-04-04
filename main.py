from flask import Flask, render_template, request
from open_cv import *
import os

app = Flask(__name__)

UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + "/static/"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():

    UPLOAD_FOLDER = os.path.join(UPLOAD_DIR, 'original_images/')
    UPLOAD_FOLDER_ENC = os.path.join(UPLOAD_DIR, 'encrypted_images/')

    # Requesting image for comparison.
    img_o = request.files['image_original']
    img_e = request.files['image_encrypted']

    # Extracting file name for comparison.
    img_o_name = img_o.filename
    img_e_name = img_e.filename

    # Creating upload directory is not exist.
    if not os.path.isdir(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    if not os.path.isdir(UPLOAD_FOLDER_ENC):
        os.mkdir(UPLOAD_FOLDER_ENC)

    dest_o = "".join([UPLOAD_FOLDER, img_o_name])
    dest_e = "".join([UPLOAD_FOLDER_ENC, img_e_name])
    print("Original Image : {}".format(dest_o))
    print("Encrypted Image : {}".format(dest_e))

    img_o.save(dest_o)
    img_e.save(dest_e)

    image_data = opencv_pixel(dest_o, dest_e)
    total_pixel = len(image_data[0])
    enc_total_pixel = len(image_data[1])
    unmodified_pixel = total_pixel - enc_total_pixel

    original_pixel = image_data[0]
    encrypted_pixel = image_data[2]

    data_value = []
    for i in range(len(original_pixel)):
        data_value.append(i)

    data_value_enc = []
    for j in range(len(encrypted_pixel)):
        data_value_enc.append(j)

    return render_template("index.html", data_original = original_pixel, label_original = data_value, data_enc = encrypted_pixel, label_enc = data_value_enc, total_pixel = total_pixel, unmodified_pixel = unmodified_pixel, enc_total_pixel = enc_total_pixel)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
