window.onload = function () {
    calculateCart();
}



function calculateCart() {


    var cprice = document.getElementsByClassName('course-price')
    var ctotal = 0
    for (var i = 0; i < cprice.length; i++) {
        var thisprice = parseFloat(cprice[i].innerText);
        ctotal = ctotal + thisprice;
    }

    var bprice = document.getElementsByClassName('book-price')
    var btotal = 0
    for (var i = 0; i < bprice.length; i++) {
        var thisprice = parseFloat(bprice[i].innerText);
        btotal = btotal + thisprice;
    }

    var qprice = document.getElementsByClassName('quiz-price')
    var qtotal = 0
    for (var i = 0; i < qprice.length; i++) {
        var thisprice = parseFloat(qprice[i].innerText);
        qtotal = qtotal + thisprice;
    }


    const totalPrice = ctotal + btotal + qtotal;



    document.getElementById('totalPrice').innerText = totalPrice;

    document.getElementById('amount').value = totalPrice;
    document.getElementById('totalPrice1').innerText = totalPrice;


}

function applyCoupon() {
    totalPrice = document.getElementById('totalPrice').innerText;
    coupon = document.getElementById('coupon').value;
    if (coupon == 'PORALEKHA') {
        if (totalPrice >= 1000) {
            totalPrice = totalPrice - 50;
        }

    }

    document.getElementById('totalPrice1').innerText = totalPrice;


}

function cartValueChange(number, isIncrease, cart1, cart2) {




    const cartValueCount = document.getElementById(number);
    const cartCount = parseInt(cartValueCount.value);

    let cartNewCount = cartCount;
    if (isIncrease == true) {
        cartNewCount = cartCount + 1;
    }

    else if (isIncrease == false && cartCount > 1) {
        cartNewCount = cartCount - 1;
    }
    cartValueCount.value = cartNewCount;

    //total

    const cartOldPrice = document.getElementById(cart1 + '-total');
    const cartPrice = cartOldPrice.innerText;
    const cartNewPrice = parseInt(cartPrice);
    let cartTotal = cartNewCount * cartNewPrice;

    // console.log(cartTotal)
    // console.log(cartNewCount)

    document.getElementById(cart2 + '-total').innerText = cartTotal;

    calculateCart()
}


