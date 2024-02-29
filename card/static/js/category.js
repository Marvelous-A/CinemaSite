document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll("#fiter-form input[type='checkbox']");
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            document.getElementById("fiter-form").submit();
        });
    });
});

document.getElementById("search_filter").onclick = function(){
    document.getElementById('search_fieldset').classList.remove('hidden')
    // document.getElementById('search_fieldset').item.classList.add('check_place_on')

};
