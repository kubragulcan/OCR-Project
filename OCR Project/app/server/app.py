from fastapi import FastAPI, HTTPException, UploadFile, File 
from bson.objectid import ObjectId
from enum import Enum
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
import easyocr
import imutils
import keras_ocr



plt.style.use('dark_background')
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\kubra.gulcan\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'



class Models(str, Enum):
    Tesseract = 'Tesseract'
    EasyOcr = 'EasyOcr'
    KerasOcr = 'KerasOcr'

class YesNo(str, Enum):
    Yes = 'Yes'
    No = 'No'

app = FastAPI()


@app.post("/CarLicensePlateRecognition")
async def UploadImage( Model_selection: Models , Steps: YesNo, image: UploadFile = File(...)):
    img = cv2.imread(image.filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
    edged = cv2.Canny(bfilter, 30, 200) #Edge detection

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 15, True)
        if len(approx) == 4:
            location = approx
            break
    
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    (x,y) = np.where(mask==255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]


    if Steps == 'Yes':
        plt.figure(figsize=(6,5))
        plt.imshow(img, cmap='gray')
        plt.axis('off')
        plt.show()
        plt.imshow(gray, cmap='gray')
        plt.axis('off')
        plt.show()
        plt.imshow(edged, cmap='gray')
        plt.axis('off')
        plt.show()
        plt.imshow(new_image, cmap='gray')
        plt.axis('off')
        plt.show()
        plt.imshow(cropped_image, cmap='gray')
        plt.axis('off')
        plt.show()


    
    if Model_selection == 'Tesseract' :
        data = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 6')
        return data
        
    if Model_selection == 'EasyOcr':
        reader = easyocr.Reader(['en'])
        data = reader.readtext(cropped_image)
        final_text = ""
        for _, text, __ in data:
            final_text += " "
            final_text += text
        return {final_text}

    if Model_selection == 'KerasOcr' :
        pipeline = keras_ocr.pipeline.Pipeline()
        images = [new_image]
        prediction_groups = pipeline.recognize(images)
  
        predicted_image_1 = prediction_groups[0]
        for text, box in predicted_image_1:
                print(text)
        return text



    



