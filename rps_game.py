import cv2
from keras.models import load_model
import numpy as np
import random
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Rock_paper_scissors:
    def __init__(self): 
        self.round_marker = 1
        self.options = ['rock', 'paper', 'scissors', 'nothing']
        self.player_points = 0
        self.computer_points = 0
        print('Get ready!')
        pass

    def compare_input(self, player_choice, computer_choice):
        time.sleep(2)
        if player_choice == computer_choice:
            self.player_points += 1
            self.computer_points += 1
            self.round_marker += 1
            print('It\'s a draw!')
        elif (player_choice == 'scissors' and computer_choice == 'paper') \
            or (player_choice == 'paper' and computer_choice == 'rock') \
            or (player_choice == 'rock' and computer_choice == 'paper'):
            self.player_points += 1
            self.round_marker += 1
            print('You won this round!')
        else: 
            self.computer_points += 1
            self.round_marker += 1
            print('You lost this round!')
        if self.round_marker <4:
            time.sleep(1)
            print(f'Get ready for round {self.round_marker}.')

    def get_prediction(self):
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #return None
        index = np.argmax(prediction[0])
        return index

    def get_input(self):
        while True:
            start_key = input('Press enter to start.')
            if start_key == '':
                computer_choice = random.choice(self.options[:3])
                while True: 
                    time.sleep(1)
                    index = self.get_prediction()
                    if index == 3:
                        print('The camera can\'t see you. Try again')
                    else:
                        player_choice = self.options[index]
                        print(f'You chose {player_choice}.')
                        print('The computer chose...')
                        time.sleep(2)
                        print(computer_choice)
                        self.compare_input(player_choice, computer_choice)
                        break 
            break

    def close_window(self):
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        self.cv2.destroyAllWindows()

def play_game():
    game = Rock_paper_scissors()
    while True:
        game.get_input()
        if game.round_marker == 4:
            time.sleep(2)
            if game.player_points == game.computer_points:
                print('It\'s a draw! Good game.')
                break
            elif game.player_points > game.computer_points:
                print('You won the game! Well done!')
                break
            else: print('You lost. Better luck next time!')
            game.close_window()
            break
        
            
if __name__ == '__main__':
    play_game()
