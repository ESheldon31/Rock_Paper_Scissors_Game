import cv2
from keras.models import load_model
import numpy as np
import random
import time


class RockPaperScissors:
    def __init__(self):
        self.round_marker = 1
        self.options = ['rock', 'paper', 'scissors', 'nothing']
        self.player_points = 0
        self.computer_points = 0
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.started = False
        self.countdown_switch = False
        self.camera_error = False
        self.timestamp = time.time()
        self.time_elapsed = 0
        self.message_left = ''
        self.message_right = ''
        self.message_left_mid = ''
        self.message_left_low = ''
        self.message_left_low_low = ''
        pass
    
    def play_video(self):
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, self.frame = self.cap.read()
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        cv2.putText(self.frame, self.message_left, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(self.frame, self.message_right, (430, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(self.frame, self.message_left_mid, (10, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(self.frame, self.message_left_low, (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.putText(self.frame, self.message_left_low_low, (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.imshow('frame', self.frame)
    
    def intro(self):
        self.message_left = 'ROCK, PAPER, SCISSORS!'
        self.message_left_mid = 'Press \'s\' to start.'
        self.switch_on()
    
    def switch_on(self):
        if cv2.waitKey(33) & 0xFF == ord('s'):
            self.started = True
            self.countdown_switch = True

    def control_panel(self):
        if self.started == False:
            if self.round_marker == 1:
                self.intro()
            elif self.round_marker == 4:
                self.end_game()
            elif self.camera_error == True:
                self.message_left_mid = 'The camera can\'t detect you. Press \'s\' to try again.'
                self.switch_on()
            elif self.round_marker > 1:
                self.message_left_low = f'Press \'s\' to move onto round {self.round_marker}.'
                self.switch_on()
            

    def get_player_choices(self):
        if self.started == True:
            self.time_elapsed = (10 * self.round_marker) - (time.time() - self.timestamp)

            if self.countdown_switch:
                self.message_left_low = ''
                self.message_left_mid = f'Show your hand in {int(self.time_elapsed)} seconds.'
            
            if self.time_elapsed <=0:
                self.message_left_low = ''
                self.countdown_switch = False
                self.computer_choice = random.choice(self.options[:3])
                index = self.get_prediction()

                if index == 3:
                    self.camera_error = True                
                else:
                    self.player_choice = self.options[index]
                    self.message_left = f'You chose {self.player_choice}.'
                    self.message_right = f'Computer chose {self.computer_choice}.'
                    self.determine_round_winner()


    def get_prediction(self):
        prediction = self.model.predict(self.data)
        index = np.argmax(prediction[0])
        return index
    
    def determine_round_winner(self):
        self.round_marker += 1
        if self.round_marker == 4:
            self.started = False
        else:
            self.compare_inputs()
            self.started = False

    def compare_inputs(self):
        if self.player_choice == self.computer_choice:
            self.player_points += 1
            self.computer_points += 1
            self.message_left_mid = 'It\'s a draw!'
        elif (self.player_choice == 'scissors' and self.computer_choice == 'paper') \
            or (self.player_choice == 'paper' and self.computer_choice == 'rock') \
            or (self.player_choice == 'rock' and self.computer_choice == 'scissors'):
            self.player_points += 1
            self.message_left_mid = 'You win this round!'
        else: 
            self.computer_points += 1
            self.message_left_mid = 'Computer wins this round!'

    def end_game(self):
        self.compare_inputs()
        if self.player_points == self.computer_points:
            self.message_left_low = 'It\'s a draw! Good game.'
        elif self.player_points > self.computer_points:
            self.message_left_low = 'You won the game! Well done!'
        else: 
            self.message_left_low = 'You lost. Better luck next time!'
        self.message_left_low_low = 'Press q to close the game.'
        
    def close_window(self):
        self.cap.release()
        cv2.waitKey(1000)
        cv2.waitKey(1)
        cv2.waitKey(1000)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.waitKey(1)

    
def play_game():
    game = RockPaperScissors()
    while game.round_marker < 5:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        game.play_video()
        game.control_panel()
        game.get_player_choices()
    game.close_window()
    

if __name__ == '__main__':
    play_game()