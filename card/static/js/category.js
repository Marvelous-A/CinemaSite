document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll("#fiter-form input[type='checkbox']");
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            document.getElementById("fiter-form").submit();
        });
    });
});


let filter = document.getElementById("search_fieldset"); 
document.getElementById("search_filter").onclick = function(){ 
    if (filter.hasAttribute('hidden')){ 
        filter.removeAttribute('hidden');  
    }else{ 
        filter.setAttribute('hidden', ''); 
    } 
};

document.getElementById('search-input').addEventListener('input', function() {
    document.getElementById("search_bar").submit();
});


document.addEventListener('DOMContentLoaded', function() {
    var SearchInput = document.getElementById('search-input');
    var tempValue = SearchInput.value;
    SearchInput.value = '';
    document.getElementById('search-input').focus(); // Установить фокус на поле ввода поиска
    SearchInput.value = tempValue;
});



