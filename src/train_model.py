from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def build_model(input_dim):

    model = Sequential()

    model.add(Dense(16, activation='relu', input_dim=input_dim))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model