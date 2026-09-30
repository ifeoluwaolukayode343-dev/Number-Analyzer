
const numberInput = document.getElementById("numberInput");
const analyzeButton = document.getElementById("analyzeButton");
const message = document.getElementById("message");
const results = document.getElementById("results");

// Display a number without unnecessary decimal zeros
function formatNumber(number) {
    return Number(number.toFixed(10)).toString();
}

// Calculate the sum
function calculateSum(numbers) {
    return numbers.reduce((total, number) => total + number, 0);
}

// Calculate the average
function calculateAverage(numbers) {
    return calculateSum(numbers) / numbers.length;
}

// Find the largest number
function findLargest(numbers) {
    return Math.max(...numbers);
}

// Find the smallest number
function findSmallest(numbers) {
    return Math.min(...numbers);
}

// Get even numbers
function getEvenNumbers(numbers) {
    return numbers.filter(number => Number.isInteger(number) && number % 2 === 0);
}

// Get odd numbers
function getOddNumbers(numbers) {
    return numbers.filter(number => Number.isInteger(number) && number % 2 !== 0);
}

// Analyze the numbers when the button is clicked
analyzeButton.addEventListener("click", function () {
    const userInput = numberInput.value.trim();

    message.textContent = "";
    message.className = "";
    results.hidden = true;

    if (userInput === "") {
        message.textContent = "Please enter some numbers.";
        message.className = "error";
        return;
    }

    const values = userInput.split(",").map(value => value.trim());

    // Reject empty values and invalid numbers
    if (
        values.some(value => value === "" || !Number.isFinite(Number(value)))
    ) {
        message.textContent =
            "Invalid input. Please enter numbers separated by commas.";
        message.className = "error";
        return;
    }

    const numbers = values.map(Number);

    message.textContent = "Numbers analyzed successfully!";
    message.className = "success";

    // Display the original numbers
    document.getElementById("numbersDisplay").textContent =
        numbers.map(formatNumber).join(", ");

    // Calculate the results
    const total = calculateSum(numbers);
    const average = calculateAverage(numbers);
    const largest = findLargest(numbers);
    const smallest = findSmallest(numbers);
    const evenNumbers = getEvenNumbers(numbers);
    const oddNumbers = getOddNumbers(numbers);

    // Display the analysis
    document.getElementById("total").textContent = formatNumber(total);
    document.getElementById("average").textContent =
        formatNumber(average);
    document.getElementById("largest").textContent =
        formatNumber(largest);
    document.getElementById("smallest").textContent =
        formatNumber(smallest);
    document.getElementById("count").textContent = numbers.length;

    // Display even numbers
    document.getElementById("evenNumbers").textContent =
        evenNumbers.length
            ? evenNumbers.map(formatNumber).join(", ")
            : "No even numbers found.";

    // Display odd numbers
    document.getElementById("oddNumbers").textContent =
        oddNumbers.length
            ? oddNumbers.map(formatNumber).join(", ")
            : "No odd numbers found.";

    results.hidden = false;
});