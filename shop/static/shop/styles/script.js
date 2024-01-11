document.addEventListener("DOMContentLoaded", function () {
    // Fetch and display numbers
    fetchNumbers();

    // Add event listener to the clear button
    $("#clear-button").on("click", function () {
        clearScores();
    });
});

function fetchNumbers() {
    fetch('/fetch_numbers/')  // Replace with your Django URL
        .then(response => response.json())
        .then(data => {
            const numbers = data.numbers;
            displayNumbers(numbers);
        })
        .catch(error => console.error('Error fetching data:', error));
}

function displayNumbers(numbers) {
    const container = document.getElementById('numbers-container');
    container.innerHTML = ''; // Clear existing content

    numbers.forEach(number => {
        const box = document.createElement('div');
        box.className = 'score-box';
        box.textContent = number;
        container.appendChild(box);
    });
}

function clearScores() {
    // Add logic to clear scores on the server side (Django view)
    fetch('/clear_scores/')  // Replace with your Django URL for clearing scores
        .then(response => response.json())
        .then(data => {
            console.log('Scores cleared:', data.message);
            fetchNumbers(); // Fetch and display updated numbers after clearing
        })
        .catch(error => console.error('Error clearing scores:', error));
}
