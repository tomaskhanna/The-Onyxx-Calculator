let currentInput = '';

function appendNumber(number) {
  currentInput += number; // Add the number or operator to the current input
  document.getElementById('result').value = currentInput; // Display the current input in the result field
}

function clearResult() {
  currentInput = ''; // Clear the current input when C is pressed
  document.getElementById('result').value = ''; // Clear the result field
}

function calculateResult() {
  try {
    currentInput = eval(currentInput); // Evaluate the expression entered by the user
    document.getElementById('result').value = currentInput; // Show the result
  } catch (error) {
    document.getElementById('result').value = 'Error'; // If there's an error in the expression, show 'Error'
    currentInput = ''; // Clear the input after showing error
  }
}
