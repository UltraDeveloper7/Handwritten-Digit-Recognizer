import keras
from keras.datasets import mnist # type: ignore
from keras.models import Sequential # type: ignore
from keras.layers import Dense, Dropout, Flatten # type: ignore
from keras.layers import Conv2D, MaxPooling2D # type: ignore
from keras import backend as K

class MNISTModel:
    def __init__(self):
        # Load and preprocess the data
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        self.x_train = self.x_train.reshape(self.x_train.shape[0], 28, 28, 1)
        self.x_test = self.x_test.reshape(self.x_test.shape[0], 28, 28, 1)
        self.input_shape = (28, 28, 1)

        self.y_train = keras.utils.to_categorical(self.y_train, 10)
        self.y_test = keras.utils.to_categorical(self.y_test, 10)

        self.x_train = self.x_train.astype('float32')
        self.x_test = self.x_test.astype('float32')
        self.x_train /= 255
        self.x_test /= 255

        self.batch_size = 128
        self.num_classes = 10
        self.epochs = 10

        self.model = None

    def build_model(self):
        self.model = Sequential()
        self.model.add(Conv2D(32, kernel_size=(5, 5), activation='relu', input_shape=self.input_shape))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.3))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(self.num_classes, activation='softmax'))

        self.model.compile(loss=keras.losses.categorical_crossentropy,
                           optimizer=keras.optimizers.Adadelta(),
                           metrics=['accuracy'])

    def train_model(self):
        if self.model is None:
            self.build_model()

        self.hist = self.model.fit(self.x_train, self.y_train,
                                   batch_size=self.batch_size,
                                   epochs=self.epochs,
                                   verbose=1,
                                   validation_data=(self.x_test, self.y_test))
        print("The model has successfully trained")

    def evaluate_model(self):
        if self.model is None:
            raise ValueError("Model has not been trained yet!")

        score = self.model.evaluate(self.x_test, self.y_test, verbose=0)
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])

    def save_model(self, file_name='mnist.h5'):
        if self.model is None:
            raise ValueError("Model has not been trained yet!")

        self.model.save(file_name)
        print(f"Saving the model as {file_name}")
        
    def run(self):
        self.train_model()
        self.evaluate_model()
        self.save_model()


