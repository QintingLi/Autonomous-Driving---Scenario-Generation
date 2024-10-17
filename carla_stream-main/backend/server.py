import cv2
from mss import mss
from fastapi import FastAPI, Form, HTTPException, Query, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='.*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/webcam')
def webcam_display():

    def webcam():
        camera = cv2.VideoCapture(0)

        while True:
            success, frame = camera.read()
            if success:

                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            else:
                camera.release()

    return StreamingResponse(webcam(), media_type='multipart/x-mixed-replace; boundary=frame')


@app.get('/desktop')
def desktop_display():
    bounding_box = {'top': 0, 'left': 0, 'width': 800, 'height': 600}
    sct = mss()

    def desktop():
        while True:
            img = np.array(sct.grab(bounding_box))
            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return StreamingResponse(desktop(), media_type='multipart/x-mixed-replace; boundary=frame')
