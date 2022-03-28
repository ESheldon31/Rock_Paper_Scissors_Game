# Rock_Paper_Scissors_Game
A game of Rock Paper Scissors in which the user plays against the computer. The program accesses the webcam and uses a Keras model to detect whether the user is showing rock, paper or scissors to the camera. 

**Creating the model**
The model is created using Teachable-Machine. Here, I created four classes, Rock, Paper, Scissors and Nothing. To train each class, I provided images of myself showing each option to the camera. 

<img width="1245" alt="Pasted Graphic" src="https://user-images.githubusercontent.com/91407498/160380923-96a0d9fd-bd9d-471c-a42d-3eb990abb6da.png">

While the webcam is active, the model calculates a prediction of what the user is showing to the camera. This prediction is the user input for the game. 

<img width="614" alt="Pasted Graphic 1" src="https://user-images.githubusercontent.com/91407498/160381798-2bb85654-e3cc-4745-a31a-fe9fef1f1c11.png">

The model was tested for accuracy and retrained with more images as required. 

<img width="357" alt="Pasted Graphic 2" src="https://user-images.githubusercontent.com/91407498/160381993-4d1db6fd-c4ad-4125-8b8f-b12bf9405ce6.png">

**Setting up the environment**
Tensorflow, Opencv-python and ipykernel are required for this game. I set up a new conda virtual environment, using python 3.8 to avoid known issues between Tensorflow and the latest version of python. 

**Writing the code**
