from keras.models import load_model # type: ignore
from tkinter import *
import customtkinter as ctk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
from train_digit_recognizer import MNISTModel

model = load_model('mnist.h5')

def predict_digit(img):
    #resize image to 28x28 pixels
    img = img.resize((28,28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img/255.0
    #predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Handwritten Digit Recognizer")
        self.geometry("400x500")
        self.resizable(False, False)

        self.x = self.y = 0

        # Creating main frame to center content
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True)

        # Creating elements
        self.label = ctk.CTkLabel(self.main_frame, text="Draw..", font=("Helvetica", 24))
        self.label.pack(pady=10)

        self.canvas = ctk.CTkCanvas(self.main_frame, width=300, height=300, bg="white", cursor="cross")
        self.canvas.pack(pady=10)

        self.classify_btn = ctk.CTkButton(self.main_frame, text="Recognise", command=self.classify_handwriting)
        self.classify_btn.pack(side='left', padx=10, pady=10)

        self.button_clear = ctk.CTkButton(self.main_frame, text="Clear", command=self.clear_all)
        self.button_clear.pack(side='right', padx=10, pady=10)

        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")

    def classify_handwriting(self):
        HWND = self.canvas.winfo_id()  # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas
        a, b, c, d = rect
        rect = (a + 4, b + 4, c - 4, d - 4)
        im = ImageGrab.grab(rect)

        digit, acc = predict_digit(im)
        self.label.configure(text=str(digit) + ', ' + str(int(acc * 100)) + '%')

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 8
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='black')


if __name__ == "__main__":
    mnist_model = MNISTModel()
    mnist_model.run()

    app = App()
    app.mainloop()
