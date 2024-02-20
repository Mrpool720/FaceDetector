# FaceDetector
👉 OpenCV for Face Detection in Images <br>
👉 Import the OpenCV Package <br>
👉 Read the Image <br>
👉 Convert the Image to Grayscale <br>
👉 Load the Classifier :- The pre-trained Haar Cascade classifier that is built into OpenCV <br>
👉 Perform the Face Detection <br>
👉 Drawing a Bounding Box <br>
👉 Displaying the Image <br>
<br>
Intro to Haar Cascade Classifiers<br><br>
This method was first introduced in the paper Rapid Object Detection Using a Boosted Cascade of Simple Features, written by Paul Viola and Michael Jones.<br>

The idea behind this technique involves using a cascade of classifiers to detect different features in an image. These classifiers are then combined into one strong classifier that can accurately distinguish between samples that contain a human face from those that don’t.<br>

The Haar Cascade classifier that is built into OpenCV has already been trained on a large dataset of human faces, so no further training is required. We just need to load the classifier from the library and use it to perform face detection on an input image.
