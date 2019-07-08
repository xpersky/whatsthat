$(document).ready(function() {
        
    // Visual controll variables

    var hidden_about = true;
    var hidden_stats = true;
    var hidden_contact = true;

    var home_lock = false;
    var about_lock = false;
    var stats_lock = false;
    var contact_lock = false;
    

    $( window ).on( "load", function() { 
        if(history.state == 'home')
        {
            scrollToElement($('#home'), $('body,html'));       
        }
        else if(history.state == 'about')
        {
            scrollToElement($('#about'), $('body,html'));
        }
        else if(history.state == 'stats')
        {
            scrollToElement($('#stats'), $('body,html'));
        }
        else if(history.state == 'contact')
        {
            scrollToElement($('#contact'), $('body,html'));
        }
        else if(history.state == 'footer')
        {
            scrollToElement($('footer'), $('body,html'));
        }
    });

    // Scroll To function
    function scrollToElement(element, parent, duration) {
        $(parent)[0].scrollIntoView(true);
        $(parent).animate({
            scrollTop: $(parent).scrollTop() + $(element).offset().top - $(parent).offset().top
            }, {
            duration: duration,
            easing: 'linear'
        });
    }
    // Navigation
    $('.hm').on('click', function() {
        var paretq = $('body,html');
        var elemq = $('#home');
        scrollToElement(elemq, paretq, 600);
        history.replaceState('home', null, '/home');
        return false;
    })
    $('.ab').on('click', function() {
        var paretq = $('body,html');
        var elemq = $('#about');
        scrollToElement(elemq, paretq, 800);
        history.replaceState('about', null, '/about');
        return false;
    })
    $('.st').on('click', function() {
        var paretq = $('body,html');
        var elemq = $('#stats');
        scrollToElement(elemq, paretq, 1600);
        history.replaceState('stats', null, '/stats');
        return false;
    })
    $('.cn').on('click', function() {
        var paretq = $('body,html');
        var elemq = $('#contact');
        scrollToElement(elemq, paretq, 2400);
        history.replaceState('contact', null, '/contact');
        return false;
    })
    $('.back').on('click', function() {
        $('body,html').animate({
            scrollTop: 0
            }, {
            duration: 3000,
            easing: 'linear'
        });
        history.replaceState('home', null, '/home');
        return false;
    })
    $(window).scroll(function() {

    if ( $(this).scrollTop() >= ($(document).height() - $(this).height() - 50 )) {
        $('.back').fadeIn();
    } else {
        if( $('back').css('display') != 'none') $('.back').fadeOut();
    }

    if ( $(this).scrollTop() >= 0 &&  $(this).scrollTop() < $('.about_con').offset().top - 50 )
    {
        if(history.state != 'home') history.replaceState('home', null, '/home');
    }
    else if ( $(this).scrollTop() >= $('.about_con').offset().top - 50 && $(this).scrollTop() < $('.stats_con').offset().top - 50 )
    {
        if(history.state != 'about') history.replaceState('about', null, '/about');
        if(hidden_about)
        {
            $('.section_left').fadeIn();
            setTimeout(function(){ $('.ab_title_con').fadeIn(); },  250);
            setTimeout(function(){ $('.ab_text').fadeIn(); },   500);
            hidden_about = false;
        }
    }
    else if ( $(this).scrollTop() >= $('.stats_con').offset().top - 50 && $(this).scrollTop() < $('.contact_con').offset().top - 50 )
    {
        if(history.state != 'stats') history.replaceState('stats', null, '/stats');
        if(hidden_stats)
        {   
            var dataset = [];
            $.ajax({
                url: '/statistics',
                datatype: 'json',
                success: function(data) {
                    dataset = data;
                }
            });
            $('.st_title_con').fadeIn();
            setTimeout(function(){ $('.st_chart_con').fadeIn(); },  250);
            setTimeout(function(){
                var ctx = document.getElementById('usage').getContext('2d');
                var myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June','July','Aug','Sept','Oct','Nov','Dec'],
                        datasets: [{
                            label: 'total usage',
                            data: dataset,
                            backgroundColor: 'rgba(39, 60, 117,0.5)' , 
                            borderColor: 'rgba(25, 42, 86,1.0)' ,
                            borderWidth: 1
                        }]
                    },
                    options: {
                        legend: {
                            display: false
                            },
                        scales: {
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true
                                }
                            }]
                        }
                    }
                }); }, 250)
            hidden_stats = false;
        }
    }
    else if ( $(this).scrollTop() >= $('.contact_con').offset().top - 50 && $(this).scrollTop() < ($('footer').offset().top - $(this).height()))
    {
        if(history.state != 'contact') history.replaceState('contact', null, '/contact');
        if(hidden_contact)
        {
            $('.form_con').fadeIn();
            hidden_contact = false;
        }
    }
    else if ( $(this).scrollTop() >= ($('footer').offset().top - $(this).height()) )
    {
        if(history.state != 'footer') history.replaceState('footer', null, '/footer');
    }

    });
})