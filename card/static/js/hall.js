let truePlaces = []
let foundValue = -1
let typePlace = document.querySelectorAll('.place')
let bronePlaces = document.getElementById('brone_places')
let priceBilets = document.getElementById('price_tickets')
let resaultPrice = document.getElementById('resault_price')
let pricePerTicket = document.getElementById('price_per_ticket').innerHTML

typePlace.forEach((item) => {
    let valu = item.getAttribute('data-id')
    if (valu != 'booking'){
        item.addEventListener('click', function(){
            if ((item.classList.value.at(-1) == "f") || (item.classList.value.at(-1) == "e")){
                item.classList.remove('check_place_off')
                item.classList.add('check_place_on')

                let foundValue = truePlaces.indexOf(valu);
                if (foundValue == -1) {
                    truePlaces.push(valu)
                }

            }else{
                item.classList.remove('check_place_on')
                item.classList.add('check_place_off')
                let foundValue = truePlaces.indexOf(valu);
                if (foundValue !== -1) {
                    truePlaces.splice(foundValue, 1)
                }
            }
            console.log(valu , item.classList.value, truePlaces, foundValue)
            console.log(truePlaces)
            bronePlaces.value = truePlaces
            resault_price.value = truePlaces.length*pricePerTicket
            priceBilets.innerHTML = "Цена: " + truePlaces.length*pricePerTicket + " руб"
        })
    }
})