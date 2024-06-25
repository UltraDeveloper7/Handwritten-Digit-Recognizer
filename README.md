# Handwritten Digit Recognizer
![image](https://github.com/UltraDeveloper7/Handwritten-Digit-Recognizer/assets/75303541/2ca7f1e8-424c-404d-bca6-fbe29a7cacee)


## Overview
This repository contains the source code for a Handwritten Digit Recognizer using the MNIST dataset. The application allows users to train a model to recognize handwritten digits and provides a graphical user interface (GUI) to draw digits and get predictions.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
    - [Clone from GitHub](#clone-from-github)
    - [Download as ZIP](#download-as-zip)
5. [Usage](#usage)
6. [Running the Application](#running-the-application)
7. [Directory Structure](#directory-structure)
8. [Scripts](#scripts)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)
12. [Acknowledgements](#acknowledgements)

## Features
- Train a Convolutional Neural Network (CNN) on the MNIST dataset
- Save and load the trained model
- GUI for drawing digits and getting predictions
- Real-time digit recognition with accuracy display

## Technologies Used
- Python
- Keras
- TensorFlow
- CustomTkinter
- Pillow
- NumPy
- PyWin32

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or later installed

## Installation
You can install the application by either cloning it from GitHub or downloading it as a ZIP file.

### Clone from GitHub
1. Clone the repository:
    ```bash
    git clone https://github.com/UltraDeveloper7/Handwritten-Digit-Recognizer.git
    cd Handwritten-Digit-Recognizer
    ```

### Download as ZIP
1. Download the ZIP file from GitHub:
    - Go to the [repository page](https://github.com/UltraDeveloper7/Handwritten-Digit-Recognizer).
    - Click on the "Code" button and select "Download ZIP".
    - Extract the downloaded ZIP file.
    - Navigate to the extracted directory:
    ```bash
    cd Handwritten-Digit-Recognizer
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the Handwritten Digit Recognizer, follow the instructions in the "Running the Application" section to start the server, then navigate to the application in your web browser. You can draw digits and get real-time predictions with accuracy.

## Running the Application
1. The model is being trained by using the `train_digit_recognizer.py`:

2. Run the GUI using `Gui.py`:
    ```bash
    python Gui.py
    ```

## Instructions 
Instructions:
Open the Application:

Launch the Handwritten Digit Recognizer application.
Draw a Digit:

Using your mouse, draw a digit inside the white canvas area labeled "Draw..".
Recognize the Digit:

Press the "Recognize" button located below the canvas to get the model's prediction.
The application will display the recognized digit and the accuracy percentage just above the canvas.Based on the provided image and your previous instructions, here's the complete step-by-step guide for using the Handwritten Digit Recognizer application:

## Instructions:

1. **Open the Application**:
   - Launch the Handwritten Digit Recognizer application.

2. **Draw a Digit**:
   - Using your mouse, draw a digit inside the white canvas area labeled "Draw..".

3. **Recognize the Digit**:
   - Press the "Recognize" button located below the canvas to get the model's prediction.
   - The application will display the recognized digit and the accuracy percentage just above the canvas.

4. **Clear the Canvas**:
   - To draw a new digit, press the "Clear" button to clear the canvas area.

5. **Save the Drawing**:
   - Press the "Save" button to save the current drawing. The application will save the drawing with a unique filename based on the current timestamp.

6. **Load a Drawing**:
   - Press the "Load" button to open a file dialog where you can navigate to and select a previously saved drawing to load it into the canvas.

7. **Undo/Redo Actions**:
   - Use the "Undo" and "Redo" buttons to undo or redo the last drawing action.

8. **Show Recognition History**:
   - Press the "Show History" button to open a new window displaying the history of recognized digits along with their confidence scores.

## Directory Structure
```
handwritten-digit-recognizer/
├── README.md
├── requirements.txt
├── train_digit_recognizer.py
├── Gui.py
├── mnist.h5
```

## Scripts
- `train_digit_recognizer.py`: Script to train the CNN model on the MNIST dataset
- `Gui.py`: Script to run the GUI for digit recognition

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or issues, please contact [konstantinostoutounas@gmail.com](mailto:konstantinostoutounas@gmail.com).

## Acknowledgements
- Special thanks to the contributors and open-source libraries that made this project possible.

---

Thank you for using the Handwritten Digit Recognizer! Happy digitizing!
