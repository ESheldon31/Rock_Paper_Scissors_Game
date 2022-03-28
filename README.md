# Rock_Paper_Scissors_Game

A game of Rock Paper Scissors in which the user plays against the computer. The program accesses the webcam and uses a Keras model to detect whether the user is showing rock, paper or scissors to the camera. 

## Creating the model

The model is created using Teachable-Machine. Here, I created four classes, Rock, Paper, Scissors and Nothing. To train each class, I provided images of myself showing each option to the camera. 

<img width="1245" alt="Pasted Graphic" src="https://user-images.githubusercontent.com/91407498/160380923-96a0d9fd-bd9d-471c-a42d-3eb990abb6da.png">

While the webcam is active, the model calculates a prediction of what the user is showing to the camera. This prediction will be the user input for the game. 

<img width="614" alt="Pasted Graphic 1" src="https://user-images.githubusercontent.com/91407498/160381798-2bb85654-e3cc-4745-a31a-fe9fef1f1c11.png">

The model was tested for accuracy and retrained with more images as required. 

<img width="357" alt="Pasted Graphic 2" src="https://user-images.githubusercontent.com/91407498/160381993-4d1db6fd-c4ad-4125-8b8f-b12bf9405ce6.png">

## Setting up the environment

Tensorflow, Opencv-python and ipykernel are required for this game. I set up a new conda virtual environment, using python 3.8 to avoid known issues between Tensorflow and the latest version of python. 

## Writing the code

The play_game function is simple. 

![image](https://user-images.githubusercontent.com/91407498/160385780-d80de149-ff80-47d8-ae47-2eee708dc373.png)

It initiates an instance of the RockPaperScissors class and enters the while loop. The webcam captures and shows the video on the screen and the game plays until the user presses 'q' at the end of three rounds. 

The flowchart below shows the logic inside the while loop. 

![image](https://user-images.githubusercontent.com/91407498/160477543-a11a0aa0-4adb-4e91-8782-35debccac915.png)
 
The model provides its prediction in a nested list, e.g. [[1.0838162e-07 2.2813882e-13 1.3565130e-09 9.9999988e-01]], with the highest value being the class (rock, paper, scissors or nothing) it thinks the user is showing. The get_prediction method extracts the highest value from the list using the Numpy method, argmax.

![image](https://user-images.githubusercontent.com/91407498/160477341-8ede303a-fd6a-4af6-99b1-182e0e8e1c93.png)

## Additional features

After coding the basic logic of the game, I added a few extra features to improve the user experience:
1. using the cv2.putText() method so the messages were printed onto the video frame, not in the terminal. 
2. adding a countdown to make it clearer when the user has to show their hand.

## Further possible improvements

Further improvements that could be made are:
1. further retraining of the model with different users and backgrounds to improve accuracy of model's predictions.
2. adding images to visually represent the computer choice on the screen. 
3. instead of just giving the option to close the window at the end of 3 rounds, the user could press a different key to play again. 
