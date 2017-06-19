

var ranString = function(amt) {
    var string = '';
    for(var i = 0; i < amt; i++) {
        string += dictionary[Math.floor(Math.random() * dictionary.length)];
    }
    return string;
}

var name_animation = function() {
    dictionary = "0123456789qwertyuiopasdfghjklzxcvbnm!?><`~+*=@#$%".split('');
    var str = 'Dionýz Lazar'
    var el = document.getElementById('name');
    if (el) {
        el.innerHTML = '';
        var count = str.length;
        el.className = '';
        var delay = 50;

        var gen = setInterval(function() {
            el.setAttribute('data-before', ranString(count/2-1));
            el.setAttribute('data-after', ranString(count/2-1));
            if(delay > 0) {
                delay--;
            }
            else {
                if(count < str.length) {
                    el.innerHTML += str[str.length - count-1];
                }
                count--;
                if(count === -1) {
                    clearInterval(gen);
                }
            }
        }, 40);
    }
}

$( document ).ready( function() {
    var header = $('header');
    var close = $('#mobile-menu-close');
    $('#mobile-menu-open').on('click', function() {
         header.addClass("active");
    });

    // Close mobile menu
    close.on('click', function() {
        header.removeClass('active');
    });

    $('#menu a').on('click', function(){
        close.click();
    });

    name_animation();
});