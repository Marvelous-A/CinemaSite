document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll("#fiter-form_category input[type='checkbox']");
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            document.getElementById("fiter-form_category").submit();
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll("#fiter-form_director input[type='checkbox']");
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            document.getElementById("fiter-form_director").submit();
        });
    });
});