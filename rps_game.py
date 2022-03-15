import cv2
from keras.models import load_model
import numpy as np
import random
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Rock_paper_scissors:
    def __init__(self, prediction, round_marker= 0):
        self.prediction = prediction
        self.round_marker = round_marker
        self.options = ['rock', 'paper', 'scissors', 'nothing']
        self.computer_choice = ''
        self.player_choice = ''
        self.player_points = 0
        self.computer_points = 0
        print('Get ready!')
        pass

    def compare_input(self):
        # While loop?
        if self.player_choice == self.computer_choice:
            self.player_points += 1
            self.computer_points += 1
            self.round_marker += 1
            print('It\'s a draw!')
        elif (self.player_choice == 'scissors' and self.computer_choice == 'paper') \
            or (self.player_choice == 'paper' and self.computer_choice == 'rock') \
            or (self.player_choice == 'rock' and self.computer_choice == 'paper'):
            self.player_points += 1
            self.round_marker += 1
            print('You won this round!')
        else: 
            self.computer_points += 1
            self.round_marker += 1
            print('You lost this round!')
        pass

    def get_input(self, prediction):
        while True:
            self.computer_choice = random.choice(self.options[:2])
            index = np.argmax(prediction[0])
            self.player_choice = self.options[index]
        # What about if player shows nothing?
            print(f'You chose {self.player_choice}.')
            print('The computer chose...')
        # Add delay?
            print(self.computer_choice)
            break 
        
        self.compare_input()
        pass

def play_game():
    game = Rock_paper_scissors(prediction, round_marker=0)
    while True:
        game.get_input(prediction)
        if game.round_marker == 3:
            if game.player_points == game.computer_points:
                print('It\'s a draw! Good game.')
                break
            elif game.player_points > game.computer_points:
                print('You won! Well done!')
                break
            else: print('You lost. Better luck next time!')
            break
        pass

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    play_game()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()