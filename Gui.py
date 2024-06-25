from keras.models import load_model # type: ignore
from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import win32gui
from PIL import ImageGrab, Image, ImageTk
import numpy as np
from train_digit_recognizer import MNISTModel
import os
import json
from datetime import datetime

mnist_model = MNISTModel()
mnist_model.run()

model = load_model('mnist.h5')

def predict_digit(img):
    # Resize image to 28x28 pixels
    img = img.resize((28,28))
    # Convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    # Reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img.astype('float32')
    img = img / 255.0
    # Predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res), res

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Handwritten Digit Recognizer")
        self.geometry("400x600")
        self.resizable(False, False)

        self.x = self.y = 0
        self.history = []
        self.undo_stack = []
        self.redo_stack = []

        # Creating main frame to center content
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True)

        # Creating elements
        self.label = ctk.CTkLabel(self.main_frame, text="Draw..", font=("Helvetica", 24))
        self.label.pack(pady=10)

        self.canvas = ctk.CTkCanvas(self.main_frame, width=300, height=300, bg="white", cursor="cross")
        self.canvas.pack(pady=10)

        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(pady=10)

        self.classify_btn = ctk.CTkButton(button_frame, text="Recognise", command=self.classify_handwriting)
        self.classify_btn.pack(side='left', padx=10)

        self.button_clear = ctk.CTkButton(button_frame, text="Clear", command=self.clear_all)
        self.button_clear.pack(side='right', padx=10)

        save_load_frame = ctk.CTkFrame(self.main_frame)
        save_load_frame.pack(pady=10)

        self.save_btn = ctk.CTkButton(save_load_frame, text="Save", command=self.save_drawing)
        self.save_btn.pack(side='left', padx=10)

        self.load_btn = ctk.CTkButton(save_load_frame, text="Load", command=self.load_drawing)
        self.load_btn.pack(side='right', padx=10)

        undo_redo_frame = ctk.CTkFrame(self.main_frame)
        undo_redo_frame.pack(pady=10)

        self.undo_btn = ctk.CTkButton(undo_redo_frame, text="Undo", command=self.undo)
        self.undo_btn.pack(side='left', padx=10)

        self.redo_btn = ctk.CTkButton(undo_redo_frame, text="Redo", command=self.redo)
        self.redo_btn.pack(side='right', padx=10)

        self.history_btn = ctk.CTkButton(self.main_frame, text="Show History", command=self.show_history)
        self.history_btn.pack(pady=10)

        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def clear_all(self):
        self.canvas.delete("all")
        self.undo_stack = []
        self.redo_stack = []

    def classify_handwriting(self):
        self.save_state_to_undo_stack()
        HWND = self.canvas.winfo_id()  # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas
        a, b, c, d = rect
        rect = (a + 4, b + 4, c - 4, d - 4)
        im = ImageGrab.grab(rect)

        digit, acc, scores = predict_digit(im)
        if acc < 0.5:  # Adjust the threshold as needed
            self.label.configure(text="Failed to recognize the digit")
        else:
            self.label.configure(text=f"{digit}, {int(acc * 100)}%")
            self.history.append((int(digit), float(acc), scores.tolist()))

    def save_drawing(self):
        self.save_state_to_undo_stack()
        HWND = self.canvas.winfo_id()
        rect = win32gui.GetWindowRect(HWND)
        a, b, c, d = rect
        rect = (a + 4, b + 4, c - 4, d - 4)
        im = ImageGrab.grab(rect)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"drawing_{timestamp}.png"
        im.save(file_name)
        with open("history.json", "w") as f:
            json.dump(self.history, f)
        self.label.configure(text=f"Drawing saved as {file_name}")

    def load_drawing(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if file_path:
            self.save_state_to_undo_stack()
            loaded_image = Image.open(file_path)
            self.tkimage = ImageTk.PhotoImage(loaded_image)
            self.canvas.create_image(0, 0, anchor='nw', image=self.tkimage)
            if os.path.exists("history.json"):
                with open("history.json", "r") as f:
                    self.history = json.load(f)
            self.label.configure(text=f"Loaded {file_path}")

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.get_current_canvas_state())
            last_state = self.undo_stack.pop()
            self.restore_canvas_state(last_state)

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.get_current_canvas_state())
            next_state = self.redo_stack.pop()
            self.restore_canvas_state(next_state)

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 8
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='black')

    def start_draw(self, event):
        self.redo_stack = []

    def end_draw(self, event):
        self.save_state_to_undo_stack()

    def save_state_to_undo_stack(self):
        self.undo_stack.append(self.get_current_canvas_state())
        self.redo_stack = []

    def get_current_canvas_state(self):
        HWND = self.canvas.winfo_id()  # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas
        a, b, c, d = rect
        rect = (a + 4, b + 4, c - 4, d - 4)
        im = ImageGrab.grab(rect)
        return im

    def restore_canvas_state(self, image):
        self.clear_all()
        self.tkimage = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.tkimage)

    def show_history(self):
        history_window = Toplevel(self)
        history_window.title("Recognition History")
        history_window.geometry("400x400")
        history_text = Text(history_window, wrap=WORD)
        history_text.pack(expand=True, fill=BOTH)
        for h in self.history:
            history_text.insert(END, f"Digit: {h[0]}, Confidence: {int(h[1] * 100)}%\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()
