// Handle form submission
document.getElementById("colorForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent form from reloading the page

  const hexInput = document.getElementById("hexInput").value.trim();

  // Validate the input
  if (!/^#[0-9A-Fa-f]{6}$/.test(hexInput)) {
    document.getElementById("result").innerText = "Invalid HEX color code. Use the format #FFFFFF.";
    return;
  }

  // Remove the "#" from the hex code
  const hexColor = hexInput.substring(1);

  // Backend URL
  const backendUrl = "https://colorserver.onrender.com/predict/";

//   document.getElementById("result").innerText = "Color Works";

  // Fetch the prediction from the backend
  fetch(`${backendUrl}${hexColor}`)
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to get color prediction.");
      }
      return response.text();
    })
    .then(predictedColor => {
      // Display the result
      document.getElementById("result").innerText = `Predicted Color: ${predictedColor}`;
    })
    .catch(error => {
      // Display error message
      console.error(error);
      document.getElementById("result").innerText = "Error: Unable to predict the color. Please try again later.";
    });
});
