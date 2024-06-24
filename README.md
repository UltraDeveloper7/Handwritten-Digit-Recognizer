# Handwritten-Digit-Recognizer

This repository contains a Handwritten Digit Recognizer using the MNIST dataset. The project is divided into two main components:

1. `train_digit_recognizer.py`: This script is used to train a Convolutional Neural Network (CNN) on the MNIST dataset to recognize handwritten digits.
2. `gui.py`: This script provides a graphical user interface (GUI) for users to draw digits and get predictions from the trained model.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/handwritten-digit-recognizer.git
    cd handwritten-digit-recognizer
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Training the Model

1. To train the model, run the `train_digit_recognizer.py` script. This will train the CNN on the MNIST dataset and save the trained model as `mnist.h5`.

    ```bash
    python train_digit_recognizer.py
    ```

2. The script will output the training progress and final evaluation metrics on the test dataset.

## Running the GUI

1. After training the model, you can start the GUI to recognize handwritten digits. Run the `gui.py` script:

    ```bash
    python gui.py
    ```

2. A window will appear where you can draw digits. Press the "Recognize" button to get the model's prediction and accuracy for the drawn digit. Press the "Clear" button to clear the canvas.

## Files

- **train_digit_recognizer.py**: Contains the `MNISTModel` class to build, train, and evaluate the CNN model.
- **gui.py**: Provides the GUI to draw digits and recognize them using the trained model.


## Usage

1. Ensure you have the required packages installed.
2. Train the model using `train_digit_recognizer.py`.
3. Run the GUI using `gui.py` to draw and recognize digits.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or find any bugs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
