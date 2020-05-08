//   all ------------------
function initBalkon() {
	//   loader ------------------
    $(".loader").fadeOut(500, function() {
        $("#main").animate({
            opacity: "1"
        }, 500);
    });
	//   Background image ------------------
    var a = $(".bg");
    a.each(function(a) {
        if ($(this).attr("data-bg")) $(this).css("background-image", "url(" + $(this).data("bg") + ")");
    });
 	//   css ------------------
    function d() {
        $(".alt").each(function() {
            $(this).css({
                "margin-top": -$(this).height() / 2 + "px"
            });
        });
        var a = $(".social-wrap li"), b = a.length, c = $(".social-wrap ul").width();
        a.css({
            width: c / b - .5
        });
        $(".height-emulator").css({
            height: $(".content-footer").outerHeight(true)
        });
    }
    d();
    $(window).on("resize", function() {
        d();
    });
		//   scrollToFixed------------------
    if ($(".fixed-bar").outerHeight(true) < $(".post-container").outerHeight(true)) {
        $(".fixed-bar").addClass("fixbar-action");
        $(".fixbar-action").scrollToFixed({
            minWidth: 1064,
            marginTop: function() {
                var a = $(window).height() - $(".fixed-bar").outerHeight(true) - 100;
                if (a >= 0) return 20;
                return a;
            },
            removeOffsets: true,
            limit: function() {
                var a = $(".limit-box").offset().top - $(".fixed-bar").outerHeight() - 70;
                return a;
            }
        });
    } else $(".fixed-bar").removeClass("fixbar-action");
    $(".fixed-filter").scrollToFixed({
        minWidth: 1224,
        zIndex: 12,
        marginTop: 110,
        limit: function() {
            var a = $(".limit-box").offset().top - $(".fixed-filter").outerHeight(true) - 10;
            return a;
        }
    });
    $(".sroll-nav-container").scrollToFixed({
        minWidth: 1064,
        zIndex: 12,
        marginTop: 110,
        removeOffsets: true,
        limit: function() {
            var a = $(".limit-box").offset().top - $(".sroll-nav-container").outerHeight(true) - 90;
            return a;
        }
    });
	//   Isotope------------------
    function e() {
        if ($(".gallery-items").length) {
            var a = $(".gallery-items").isotope({
                singleMode: true,
                columnWidth: ".grid-sizer, .grid-sizer-second, .grid-sizer-three",
                itemSelector: ".gallery-item, .gallery-item-second, .gallery-item-three",
                transformsEnabled: true,
                transitionDuration: "700ms",
                resizable: true
            });
            a.imagesLoaded(function() {
                a.isotope("layout");
            });
            $(".gallery-filters").on("click", "a.gallery-filter", function(b) {
                var c = $(this).attr("data-filter"), d = $(this).text();
                b.preventDefault();
                var c = $(this).attr("data-filter");
                a.isotope({
                    filter: c
                });
                $(".gallery-filters a.gallery-filter").removeClass("gallery-filter-active");
                $(this).addClass("gallery-filter-active");
                var e = window.navigator.userAgent;
                var f = e.indexOf("MSIE ");
                if (f > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./)) $(".filt-text").text(d); else $(".filt-text").text(d).shuffleLetters({});
            });
            a.isotope("on", "layoutComplete", function(a, b) {
                var c = a.length;
                $(".num-album").html(c);
            });
        }
    }
    var f = $(".gallery-item").length;
    $(".all-album , .num-album").html(f);
    e();
    $(window).on("load", function() {
        e();
    });
	//   Swiper------------------
    if ($(".slider-wrap").length > 0) var g = new Swiper(".slider-wrap .swiper-container", {
        scrollbar: ".swiper-scrollbar",
        scrollbarHide: true,
        slidesPerView: "auto",
        centeredSlides: false,
        spaceBetween: 20,
        grabCursor: true,
        freeMode: true,
        scrollbarHide: false,
        nextButton: ".swiper-button-next",
        prevButton: ".swiper-button-prev"
    });
    if ($(".fs-gallery-wrap").length > 0) {
        var h = $(".fs-gallery-wrap").data("autoplayslider"), i = $(".fs-gallery-wrap").data("slidereffect");
        var j = new Swiper(".fs-gallery-wrap .swiper-container", {
            autoplay: h,
            autoplayDisableOnInteraction: false,
            pagination: ".swiper-pagination",
            paginationClickable: true,
            paginationBulletRender: function(a, b, c) {
                return '<span class="' + c + '">' + (b + 1) + "</span>";
            },
            effect: i,
            speed: 1e3,
            grabCursor: true,
            nextButton: ".swiper-button-next",
            prevButton: ".swiper-button-prev",
            loop: true
        });
        k();
        j.on("onSlideChangeStart", function() {
            l();
        });
        j.on("onSlideChangeEnd", function() {
            k();
        });
        function k() {
            $(".slide-progress").css({
                width: "100%",
                transition: "width 5000ms"
            });
        }
        function l() {
            $(".slide-progress").css({
                width: 0,
                transition: "width 0s"
            });
        }
    }
    var m = new Swiper(".single-slider .swiper-container", {
        pagination: ".swiper-pagination",
        paginationType: "fraction",
        effect: $(".single-slider").data("effects"),
        loop: true,
        grabCursor: true,
        autoHeight: true,
        nextButton: ".swiper-button-next",
        prevButton: ".swiper-button-prev"
    });
    var n = $(".partcile-dec").data("parcount");
    $(".partcile-dec").jParticle({
        background: "rgba(255,255,255,0.01)",
        color: "#ccc",
        particlesNumber: n,
        particle: {
            speed: 20
        }
    });
	//   lightGallery------------------
    $(".image-popup").lightGallery({
        selector: "this",
        cssEasing: "cubic-bezier(0.25, 0, 0.25, 1)",
        download: false,
        counter: false
    });
    var o = $(".lightgallery"), p = o.data("looped");
    o.lightGallery({
        selector: ".lightgallery a.popup-image , .lightgallery  a.popgal",
        cssEasing: "cubic-bezier(0.25, 0, 0.25, 1)",
        download: false,
        loop: false
    });
    o.on("onBeforeNextSlide.lg", function(a) {
        g.slideNext();
        return false;
    });
    o.on("onBeforePrevSlide.lg", function(a) {
        g.slidePrev();
        return false;
    });
    $(".filter-button").on("click", function() {
        $(".hid-filter").slideToggle(500);
    });
    $(".show-exfilter").on("click", function(a) {
        a.preventDefault();
        $(".product-mainfilter").slideToggle(500);
    });
	//   appear------------------ 
    $(".stats").appear(function() {
        $(".num").countTo();
    });
    $(".piechart-holder").appear(function() {
        $(this).find(".chart").each(function() {
            $(".chart").easyPieChart({
                barColor: "#292929",
                trackColor: "#eee",
                scaleColor: "#eee",
                size: "150",
                lineWidth: "40",
                lineCap: "butt",
                onStep: function(a, b, c) {
                    $(this.el).find(".percent").text(Math.round(c));
                }
            });
        });
    });
	//   share------------------
    var r = $(".share-wrapper");
    function s() {
        A();
        r.animate({
            right: 0
        }, 500);
        r.removeClass("isShare");
    }
    function t() {
        r.animate({
            right: "-130px"
        }, 500);
        r.addClass("isShare");
    }
    $(".show-share").on("click", function() {
        if (r.hasClass("isShare")) s(); else t();
    });
    var u = $(".share-container");
    u.share({
        networks: [ "facebook", "pinterest", "googleplus", "twitter", "linkedin" ]
    });
	//   tabs------------------
    $(".tabs-menu a").on("click", function(a) {
        a.preventDefault();
        $(this).parent().addClass("current");
        $(this).parent().siblings().removeClass("current");
        var b = $(this).attr("href");
        $(".tab-content").not(b).css("display", "none");
        $(b).fadeIn();
    });
	//   scroll to------------------
    $(".custom-scroll-link").on("click", function() {
        var a = 70;
        if (location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") || location.hostname == this.hostname) {
            var b = $(this.hash);
            b = b.length ? b : $("[name=" + this.hash.slice(1) + "]");
            if (b.length) {
                $("html,body").animate({
                    scrollTop: b.offset().top - a
                }, {
                    queue: false,
                    duration: 1200,
                    easing: "easeInOutExpo"
                });
                return false;
            }
        }
    });
	//   to top------------------
    $(".to-top").on("click", function(a) {
        a.preventDefault();
        $("html, body").animate({
            scrollTop: 0
        }, 800);
        return false;
    });
	//   show hide------------------
    $(".show-cart").on("click", function() {
        $(".cart-overlay").fadeIn(400);
        $(".cart-modal").animate({
            right: 0
        }, 400);
        return false;
    });
    $(".cart-overlay , .close-cart").on("click", function() {
        $(".cart-overlay").fadeOut(400);
        $(".cart-modal").animate({
            right: "-350px"
        }, 400);
        return false;
    });
	//   Contact form------------------
    $("#contactform").submit(function() {
        var a = $(this).attr("action");
        $("#message").slideUp(750, function() {
            $("#message").hide();
            $("#submit").attr("disabled", "disabled");
            $.post(a, {
                name: $("#name").val(),
                email: $("#email").val(),
                phone: $("#phone").val(),
                comments: $("#comments").val(),
                verify: $('#verify').val()
            }, function(a) {
                document.getElementById("message").innerHTML = a;
                $("#message").slideDown("slow");
                $("#submit").removeAttr("disabled");
                if (null != a.match("success")) $("#contactform").slideDown("slow");
            });
        });
        return false;
    });
    $("#contactform input, #contactform textarea").keyup(function() {
        $("#message").slideUp(1500);
    });
	//   mailchimp------------------
    $("#subscribe").ajaxChimp({
        language: "eng",
        url: "http://kwst.us9.list-manage1.com/subscribe/post?u=992ebe1f14864e841317ca145&id=163340d9c8"
    });
    $.ajaxChimp.translations.eng = {
        submit: "Submitting...",
        0: '<i class="fa fa-check"></i> We will be in touch soon!',
        1: '<i class="fa fa-warning"></i> You must enter a valid e-mail address.',
        2: '<i class="fa fa-warning"></i> E-mail address is not valid.',
        3: '<i class="fa fa-warning"></i> E-mail address is not valid.',
        4: '<i class="fa fa-warning"></i> E-mail address is not valid.',
        5: '<i class="fa fa-warning"></i> E-mail address is not valid.'
    };
	//   Video------------------
    var v = $(".background-youtube").data("vid");
    var f = $(".background-youtube").data("mv");
    $(".background-youtube").YTPlayer({
        fitToBackground: true,
        videoId: v,
        pauseOnScroll: true,
        mute: f,
        callback: function() {
            var a = $(".background-video").data("ytPlayer").player;
        }
    });
    var w = $(".background-vimeo").data("vim");
    $(".background-vimeo").append('<iframe src="//player.vimeo.com/video/' + w + '?background=1"  frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen ></iframe>');
    $(".video-holder").height($(".media-container").height());
    if ($(window).width() > 1024) {
        if ($(".video-holder").size() > 0) if ($(".media-container").height() / 9 * 16 > $(".media-container").width()) {
            $(".background-vimeo iframe ").height($(".media-container").height()).width($(".media-container").height() / 9 * 16);
            $(".background-vimeo iframe ").css({
                "margin-left": -1 * $("iframe").width() / 2 + "px",
                top: "-75px",
                "margin-top": "0px"
            });
        } else {
            $(".background-vimeo iframe ").width($(window).width()).height($(window).width() / 16 * 9);
            $(".background-vimeo iframe ").css({
                "margin-left": -1 * $("iframe").width() / 2 + "px",
                "margin-top": -1 * $("iframe").height() / 2 + "px",
                top: "50%"
            });
        }
    } else if ($(window).width() < 760) {
        $(".video-holder").height($(".media-container").height());
        $(".background-vimeo iframe ").height($(".media-container").height());
    } else {
        $(".video-holder").height($(".media-container").height());
        $(".background-vimeo iframe ").height($(".media-container").height());
    }
    $(".video-container").css("width", $(window).width() + "px");
    $(".video-container ").css("height", parseInt(720 / 1280 * $(window).width()) + "px");
    if ($(".video-container").height() < $(window).height()) {
        $(".video-container ").css("height", $(window).height() + "px");
        $(".video-container").css("width", parseInt(1280 / 720 * $(window).height()) + "px");
    }
	//   show hede------------------
    $(".menubutton").on("click", function() {
        $(".top-bar-menu").slideToggle(300);
    });
    $(".cat-button").on("click", function() {
        $(".category-nav-inner ul").slideToggle(300);
    });
    $(".product-cat-mains").matchHeight();
    $(".searchform input").on("keypress change", function(a) {
        var b = $(this).val();
        $(".dublicated-text").text(b);
    });
    var x = $(".show-fixed-search"), y = $(".fixed-search");
    function z() {
        x.removeClass("vissearch");
        y.fadeIn(300);
        t();
    }
    function A() {
        x.addClass("vissearch");
        y.fadeOut(300);
    }
    x.on("click", function() {
        if ($(this).hasClass("vissearch")) z(); else A();
    });
    $(".search-form-bg").on("click", function() {
        A();
    });
    $(".blog-btn").on("click", function() {
        $(this).parent(".blog-btn-filter").find("ul").slideToggle(500);
        return false;
    });
    $(".scroll-nav").addClass("black-bg");
	//   Window scroll------------------
    $(window).bind("scroll", function() {
        $("section").each(function() {
            var a = $(this);
			var sn = $(".scroll-nav");
            var b = a.position().top - $(window).scrollTop();
            if (b <= 0) {
                $("section").removeClass("current2");
                a.addClass("current2");
            } else {
                a.removeClass("current2");
                sn.removeClass("black-bg");
            }
            if ($(".current2").hasClass("parallax-section"))sn.addClass("black-bg"); else sn.removeClass("black-bg");
        });
    });
    $(".scroll-init  ul ").singlePageNav({
        filter: ":not(.external)",
        updateHash: false,
        offset: 70,
        threshold: 120,
        speed: 1200,
        currentClass: "act-scrlink"
    });
	$(".scroll-init ul.menu a").on("click", function() {
      setTimeout(function() {
       C();
       }, 1500);
    });
	//   Sidebar menu------------------
    var sbo = $(".sb-overlay "),
		sbm = $(".sidebar-menu"),
		sbmb = $(".sb-menu-button");
    function B() {
        sbo.fadeIn(300);
        sbm.animate({
            right: 0
        });
        sbmb.removeClass("vis-m");
    }
    $("#hid-men2").menu();
    function C() {
        sbm.animate({
            right: "-470px"
        });
        sbo.fadeOut(300);
        sbmb.addClass("vis-m");
    }
    sbo.on("click", function() {
        C();
    });
    sbmb.on("click", function() {
        if ($(this).hasClass("vis-m")) B(); else C();
    });
    $(".nav-button-wrap").on("click", function() {
        $(".nav-holder").slideToggle(500);
    });
    var D = function() {
        $(".box-item").on("touchstart", function() {
            $(this).trigger("hover");
        }).on("touchend", function() {
            $(this).trigger("hover");
        });
    };
    D();
	// team  ------------------
    $(".team-box").on({
		mouseenter: function () {
        $(this).find("ul.team-social").fadeIn();
        $(this).find(".team-social a").each(function(a) {
            var b = $(this);
            setTimeout(function() {
                b.animate({
                    opacity: 1,
                    top: "0"
                }, 400);
            }, 150 * a);
        });
    },
	 mouseleave: function () {
        $(this).find(".team-social a").each(function(a) {
            var b = $(this);
            setTimeout(function() {
                b.animate({
                    opacity: 0,
                    top: "50px"
                }, 400);
            }, 150 * a);
        });
        setTimeout(function() {
            $(this).find("ul.team-social").fadeOut();
        }, 150);
		  }
    });
	
     if ($(window).width() < 1064) {
 		 $(".nav-holder nav li").on("click", function() {
 			 $(this).find("ul").toggleClass("visul");			
   		 });
		 $(".nav-holder nav li ul").parent("li").addClass("lidec")
      } 
	
	
}

function initparallax() {
    var a = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return a.Android() || a.BlackBerry() || a.iOS() || a.Opera() || a.Windows();
        }
    };
    trueMobile = a.any();
    if (null == trueMobile) {
        var b = new Scrollax();
        b.reload();
        b.init();
    }
    if (trueMobile) $(".background-video").remove();
}
if(navigator.userAgent.match(/Trident\/7\./)) { // if IE
        $('body').on("mousewheel", function () {
            // remove default behavior
            event.preventDefault();

            //scroll without smoothing
            var wheelDelta = event.wheelDelta;
            var currentScrollPosition = window.pageYOffset;
            window.scrollTo(0, currentScrollPosition - wheelDelta);
        });
}
$(function() {
    initBalkon();
    initparallax();
});