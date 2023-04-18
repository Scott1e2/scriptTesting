// uses tensorflow in order to try and predict the behaviors of the stock market

const tf = require('@tensorflow/tfjs');
const csv = require('csv-parser');
const fs = require('fs');

// Load the data from a CSV file
let data = [];
fs.createReadStream('stock_data.csv')
  .pipe(csv())
  .on('data', (row) => {
    data.push(row);
  })
  .on('end', () => {
    // Split the data into training and testing sets
    const trainData = data.slice(0, data.length * 0.8);
    const testData = data.slice(data.length * 0.8);

    // Define the model
    const model = tf.sequential();
    model.add(tf.layers.dense({units: 64, inputShape: [4], activation: 'relu'}));
    model.add(tf.layers.dense({units: 1, activation: 'linear'}));
    model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});

    // Convert the data to tensors
    const xs = tf.tensor2d(trainData.map(row => [row.Open, row.High, row.Low, row.Close]));
    const ys = tf.tensor1d(trainData.map(row => row.AdjClose));

    // Train the model
    model.fit(xs, ys, {epochs: 100}).then(() => {
      // Make predictions on the test data
      const xsTest = tf.tensor2d(testData.map(row => [row.Open, row.High, row.Low, row.Close]));
      const ysTest = tf.tensor1d(testData.map(row => row.AdjClose));
      const predictions = model.predict(xsTest);

      // Compare the predictions to the actual prices
      for (let i = 0; i < predictions.length; i++) {
        if (predictions[i] > ysTest[i]) {
          // If the prediction is higher, buy the stock
          console.log(`Buy stock at: ${ysTest[i]}`);
        } else if (predictions[i] < ysTest[i]) {
          // If the prediction is lower, sell the stock
          console.log(`Sell stock at: ${ysTest[i]}`);
        } else {
          console.log('Hold stock');
        }
      }
    });
  });

  //not sure where to implement yet