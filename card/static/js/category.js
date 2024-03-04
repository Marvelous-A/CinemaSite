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

let inp = document.getElementById("search-input");
inp.oninput = function() {
    alert(inp.value)
}