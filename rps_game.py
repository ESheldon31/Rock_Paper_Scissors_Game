import cv2
from keras.models import load_model
import numpy as np
import random
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

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

    def get_input(self, prediction):
        self.computer_choice = random.choice(self.options[:2])
        max = np.argmax(prediction[0])
        




# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()