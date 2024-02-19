categorys = []

document.querySelectorAll('.category_checkbox').forEach((element) => {
    element.onclick = orderFunction;
});

function orderFunction() {
    let thriller = document.querySelector('.category_checkbox[value="thriller"')
    let horror = document.querySelector('.category_checkbox[value="horror"')
    let drama = document.querySelector('.category_checkbox[value="drama"')
    
    if (this.value == 'thriller' && categorys.includes('thriller') == false){
        categorys.push('thriller')
    }
    else if (this.value == 'thriller' && categorys.includes('thriller') == true){
        delete categorys[categorys.indexOf('thriller')]
    }

    if (this.value == 'horror' && categorys.includes('horror') == false){
        categorys.push('horror')
    }
    else if (this.value == 'horror' && categorys.includes('horror') == true){
        delete categorys[categorys.indexOf('horror')]
    }

    if (this.value == 'drama' && categorys.includes('drama') == false){
        categorys.push('drama')
    }
    else if (this.value == 'drama' && categorys.includes('drama') == true){
        delete categorys[categorys.indexOf('drama')]
    }
    console.log(categorys)
}