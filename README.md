# OCR-Project

## Car License Plate Recognition Application on FastApi

### Introduction

In the project, the aim is creating an application that predicts car license plates by using OCR models on FastApi. The notebook includes all findings and results from the app.

The Swagger UI has three parameters which are model_selection(dropdown selection), steps viewing options(dropdown selection), and upload image parameter.

![first](https://user-images.githubusercontent.com/110412961/188324259-6626127f-8851-4d50-a2a5-47309a4928fd.PNG)

There are three model options which are Tesseract, EasyOcr, and KerasOcr. These models are applied by using Python, and they are open source models used for OCR (Optical Character Recognition) provides us with different ways to see an image and find and recognize the text in it. Moreover, preprocess is implemented on the image before predictions. All codes are available in the 'Preprocess and Prediction' file. 

![second](https://user-images.githubusercontent.com/110412961/188324329-58722a24-1274-4e43-bfd4-199a067e03fe.PNG)

If the 'steps' option is chosen as 'Yes,' the swagger UI gives all steps, and at the end, it gives the car license plate number in a string format. 
To do that, the user uploads an image by using the image parameter.

For example:<br>
Model = 'Tesseract', steps = 'Yes', Image = 'Car3'<br>

![third](https://user-images.githubusercontent.com/110412961/188324359-a9c9a3de-773d-46b1-9a4b-2848634639e5.png)

Output:

![step1](https://user-images.githubusercontent.com/110412961/188324386-5a907db8-1828-4f32-b33e-bf00641e21c9.png)
![step2](https://user-images.githubusercontent.com/110412961/188324391-c83bd29c-8b3d-48cb-9f1f-a8cad8437730.png)

![step3](https://user-images.githubusercontent.com/110412961/188324393-ea2a9287-7a9c-4d86-83a9-3e9e0d9196bd.png)

![step4](https://user-images.githubusercontent.com/110412961/188324394-ede4bdcd-6503-4715-bb03-16df7552a43f.png)

![step5](https://user-images.githubusercontent.com/110412961/188324395-c2a4e864-7d93-4e75-807d-b0649da219fa.png)

After the viewing of steps, swagger gives a response which is the prediction of the tesseract model for the plate.

![result1](https://user-images.githubusercontent.com/110412961/188324419-0b01b40b-f872-4878-b16d-e25a02c0acb9.png)

The response of the other model predictions without steps for the same plate:<br>

#### Easy Ocr:

![easyocrresult](https://user-images.githubusercontent.com/110412961/188324443-8fabce55-59dd-4d53-a54e-84f7adaaa72c.png)

#### Keras-Ocr:

![kerasocrresult](https://user-images.githubusercontent.com/110412961/188324467-f54e059a-6956-46be-943a-b8c438b0ce05.png)

### Car Plates Example with Different Shapes and Low Quality

![Cars150](https://user-images.githubusercontent.com/110412961/188324497-11083d4f-38d4-4568-8480-be4877a24563.png)

For the plate above, the response of models:

Tesseract: "DL8CX 4850\n"<br>
EasyOcr: [" DL8CX 4850"] <br>
KerasOcr: "4850"

### Conclusion 

The correctness of predictions is high for all models. However, when the shape and quality of the plate change, the correctness decrease for Keras-Ocr while Tesseract and Easy Ocr give correct results.






