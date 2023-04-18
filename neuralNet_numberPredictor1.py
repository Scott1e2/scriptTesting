import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

# Generate sample data
np.random.seed(0)
X = np.random.randint(1, 100, size=(1000, 10))
y = np.array([1 if np.sum(x) >= 500 else 0 for x in X])

# Split the data into training and testing sets
X_train, X_test = X[:800], X[800:]
y_train, y_test = y[:800], y[800:]

# Build the model
model = Sequential()
model.add(Dense(16, input_dim=10, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
score = model.evaluate(X_test, y_test, batch_size=32)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


#needs review and iteration