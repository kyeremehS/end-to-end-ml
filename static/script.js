document.getElementById('wine-form').addEventListener('submit', function() {
    let submitButton = document.querySelector('button[type="submit"]');
    submitButton.innerHTML = "Predicting... <i class='fas fa-spinner fa-spin'></i>";
    submitButton.disabled = true;
});
