document.getElementById('copy-button').addEventListener('click', function () {
    var userLinkInput = document.getElementById('user-link');

    // Create a temporary input element
    var tempInput = document.createElement('input');
    tempInput.value = userLinkInput.value;
    document.body.appendChild(tempInput);

    // Select the text
    tempInput.select();

    // Execute the copy command
    document.execCommand('copy');

    // Remove the temporary input
    document.body.removeChild(tempInput);

    // Show the toast
    var toast = new bootstrap.Toast(document.getElementById('copy-toast'));
    toast.show();
});





