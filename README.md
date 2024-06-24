# Handwritten Digit Recognizer
![image](https://github.com/UltraDeveloper7/Handwritten-Digit-Recognizer/assets/75303541/f3b4ee85-6c45-421b-a651-bdae759e53e2)

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

3. A window will appear where you can draw digits. Press the "Recognize" button to get the model's prediction and accuracy for the drawn digit. Press the "Clear" button to clear the canvas.

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
