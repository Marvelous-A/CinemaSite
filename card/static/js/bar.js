let bar = document.getElementById("bar");
let bar_click = document.getElementById("bar_click");

bar_click.onclick = function(){ 
    if (bar.hasAttribute('hidden')){ 
        bar.removeAttribute('hidden');
    }else{ 
        bar.setAttribute('hidden', ''); 
    } 
};