from flask import Flask, render_template, request
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

MODEL_PATH = "model/strawberry_disease_model.h5"
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load the model
model = tf.keras.models.load_model(MODEL_PATH)
classes = ["Healthy", "Leaf Spot", "Other Disease"]

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]
    
    return predicted_class

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            predicted_label = predict_disease(filepath)
            return render_template("result.html", file_path=filepath, label=predicted_label)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
