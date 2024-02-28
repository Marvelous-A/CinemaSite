document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll("#fiter-form input[type='checkbox']");
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            document.getElementById("fiter-form").submit();
        });
    });
});