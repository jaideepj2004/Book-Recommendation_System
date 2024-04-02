document.getElementById("recommendationForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var genre = document.getElementById("genre").value;
    getRecommendations(genre);
});

function getRecommendations(genre) {
    // Make AJAX request to fetch recommendations from server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/recommendation", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var recommendations = JSON.parse(xhr.responseText);
            displayRecommendations(recommendations);
        }
    };
    xhr.send(JSON.stringify({genre: genre}));
}

function displayRecommendations(recommendations) {
    var recommendationsDiv = document.getElementById("recommendations");
    recommendationsDiv.innerHTML = "";
    recommendationsDiv.style.display = "block";
    recommendations.forEach(function(book, index) {
        var paragraph = document.createElement("p");
        paragraph.textContent = (index + 1) + ". " + book;
        recommendationsDiv.appendChild(paragraph);
    });
}
