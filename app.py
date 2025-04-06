from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import os
import cv2

app = Flask(__name__)
model = YOLO(r"C:\Users\balak\PalmTreeDet\runs\detect\train6\weights\best.pt")

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            
            # Run detection
            results = model(filepath)
            result_img = results[0].plot()
            result_path = os.path.join(RESULT_FOLDER, filename)
            cv2.imwrite(result_path, result_img)
            
            return render_template('result.html', 
                                 original=filepath, 
                                 result=result_path,
                                 count=len(results[0].boxes))
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)