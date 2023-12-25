let phone = document.getElementById('phone_valid')
phone.oninput = function() {
    if (/^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/.test(phone.value) == false){
        console.log("ОШИБКА!!!")
        document.getElementById("phone_error").hidden = false;
    }else{
        document.getElementById("phone_error").hidden = true;
    }
}

let email = document.getElementById('email_valid')
email.oninput = function() {
    if (/[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]+/.test(email.value) == false){
        console.log("ОШИБКА!!!")
        document.getElementById("email_error").hidden = false;
    }else{
        document.getElementById("email_error").hidden = true;
    }
}

let age = document.getElementById('age_valid')
age.oninput = function() {
    if (/[a-zA-Zа-яА-Я]/.test(age.value)){
        console.log("ОШИБКА!!!")
        document.getElementById("age_error").hidden = false;
    }else{
        document.getElementById("age_error").hidden = true;
    }
}

let city = document.getElementById('city_valid')
city.oninput = function() {
    if (/[a-zA-Zа-яА-Я|a-zA-Zа-яА-Я-]/.test(city.value) == false){
        console.log("ОШИБКА!!!")
        document.getElementById("city_error").hidden = false;
    }else{
        document.getElementById("city_error").hidden = true;
    }
}