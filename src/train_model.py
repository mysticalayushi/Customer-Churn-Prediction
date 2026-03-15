import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


def build_model(input_dim: int) -> tf.keras.Model:
    """
    Build and compile the churn prediction neural network.

    Architecture: 64 → Dropout(0.3) → 32 → Dropout(0.3) → 1 (sigmoid)
    Trained with binary crossentropy and Adam optimiser.
    Class weights should be passed to model.fit() to handle the ~80/20 imbalance.

    Args:
        input_dim: Number of input features after one-hot encoding.

    Returns:
        Compiled Keras Sequential model.
    """
    tf.keras.backend.clear_session()

    model = Sequential([
        Dense(64, activation='relu', input_dim=input_dim),
        Dropout(0.3),
        Dense(32, activation='relu'),
        Dropout(0.3),
        Dense(1,  activation='sigmoid')
    ])

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model


def train_model(model, X_train, y_train, epochs=50, batch_size=32, validation_split=0.2):
    """
    Train the model with class weights to handle class imbalance.

    Args:
        model:            Compiled Keras model from build_model().
        X_train:          Scaled training features (numpy array).
        y_train:          Training labels (0 = stayed, 1 = churned).
        epochs:           Number of training epochs (default 50).
        batch_size:       Batch size (default 32).
        validation_split: Fraction of training data used for validation.

    Returns:
        Keras History object containing training metrics per epoch.
    """
    # Compute class weight to counter the ~80/20 imbalance
    neg, pos          = np.bincount(y_train)
    class_weight_ratio = neg / pos   # upweight the minority (churn) class

    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=validation_split,
        class_weight={0: 1.0, 1: class_weight_ratio},
        verbose=1
    )

    return history
