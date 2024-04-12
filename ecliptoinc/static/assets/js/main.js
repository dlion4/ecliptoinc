(function ($) {
    ("use strict");
    // Page loading
    $(window).on("load", function () {
        $("#preloader-active").fadeOut("slow");
    });
    /*-----------------
        Menu Stick
    -----------------*/
    var header = $(".sticky-bar");
    var win = $(window);
    win.on("scroll", function () {
        var scroll = win.scrollTop();
        if (scroll < 200) {
            header.removeClass("stick");
            $(".header-style-2 .categories-dropdown-active-large").removeClass("open");
            $(".header-style-2 .categories-button-active").removeClass("open");
        } else {
            header.addClass("stick");
        }
    });
    /*------ ScrollUp -------- */
    $.scrollUp({
        scrollText: '<svg width="20" height="25" viewBox="0 0 20 25" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M10.5998 24.2694C10.7522 24.1169 10.8485 23.9083 10.8485 23.6676L10.8503 1.20328C10.8504 0.737952 10.4653 0.35288 9.99997 0.352917C9.53464 0.352955 9.14951 0.738087 9.14947 1.20342L9.14766 23.6678C9.14762 24.1331 9.53269 24.5182 9.99802 24.5181C10.2387 24.5181 10.4473 24.4218 10.5998 24.2694Z" fill="#C5FF55"/><path d="M18.8405 10.0441C19.1695 9.71509 19.1695 9.16953 18.8406 8.84061L10.6017 0.601675C10.2728 0.272759 9.7272 0.272803 9.39823 0.601772L1.15796 8.84204C0.828992 9.17101 0.828948 9.71657 1.15786 10.0455C1.48678 10.3744 2.03234 10.3744 2.36131 10.0454L9.99981 2.40689L17.6371 10.0442C17.966 10.3731 18.5115 10.373 18.8405 10.0441Z" fill=""/></svg>',
        easingType: "linear",
        scrollSpeed: 900,
        animation: "fade"
    });
    //sidebar sticky
    if ($(".sticky-sidebar").length) {
        $(".sticky-sidebar").theiaStickySidebar();
    }
    //Header search form
    $(document).on('click', function(event) {
        var menu_text = $(".menu-texts");
        var btnOpen = $(".btn-search");
        var formSearch = $(".form-search");
        if (!menu_text.is(event.target) && menu_text.has(event.target).length === 0) {
            menu_text.addClass("menu-close");
            menu_text.css("style", "");
        }
        if (!formSearch.is(event.target) && formSearch.has(event.target).length === 0 && !btnOpen.is(event.target) && btnOpen.has(event.target).length === 0) {
            $(".form-search").slideUp();
        }
    });

    // btn search
    $(".btn-search").on('click', function(e){
        e.preventDefault();
        var _form_search = $(".form-search");
        if (_form_search.css('display') == 'none') {
            _form_search.slideDown();
        } else {
            _form_search.slideUp();
        }
    });
    /*----------------------------
        Category toggle function
    ------------------------------*/
    if ($(".categories-button-active").length) {
        var searchToggle = $(".categories-button-active");
        searchToggle.on("click", function (e) {
            e.preventDefault();
            if ($(this).hasClass("open")) {
                $(this).removeClass("open");
                $(this).siblings(".categories-dropdown-active-large").removeClass("open");
            } else {
                $(this).addClass("open");
                $(this).siblings(".categories-dropdown-active-large").addClass("open");
            }
        });
    }
    /*------ Wow Active ----*/
    new WOW().init();
    /*---------------------
        Select active
    --------------------- */
    if ($(".select-active").length) {
        $(".select-active").select2();
    }
    /*---- CounterUp ----*/
    if ($(".count").length) {
        $(".count").counterUp({
            delay: 10,
            time: 1000
        });
    }
    // Isotope active
    if ($(".grid").length) {
        $(".grid").imagesLoaded(function () {
            // init Isotope
            var $grid = $(".grid").isotope({
                itemSelector: ".grid-item",
                percentPosition: true,
                layoutMode: "masonry",
                masonry: {
                    // use outer width of grid-sizer for columnWidth
                    columnWidth: ".grid-item"
                }
            });
        });
    }
    /*====== SidebarSearch ======*/
    function sidebarSearch() {
        var searchTrigger = $(".search-active"),
            endTriggersearch = $(".search-close"),
            container = $(".main-search-active");
        searchTrigger.on("click", function (e) {
            e.preventDefault();
            container.addClass("search-visible");
        });
        endTriggersearch.on("click", function () {
            container.removeClass("search-visible");
        });
    }
    sidebarSearch();
    /*====== Sidebar menu Active ======*/
    function mobileHeaderActive() {
        var navbarTrigger = $(".burger-icon"),
            endTrigger = $(".mobile-menu-close"),
            container = $(".mobile-header-active"),
            wrapper4 = $("body");
        wrapper4.prepend('<div class="body-overlay-1"></div>');
        navbarTrigger.on("click", function (e) {
            navbarTrigger.toggleClass("burger-close");
            e.preventDefault();
            container.toggleClass("sidebar-visible");
            wrapper4.toggleClass("mobile-menu-active");
        });
        endTrigger.on("click", function () {
            container.removeClass("sidebar-visible");
            wrapper4.removeClass("mobile-menu-active");
        });
        $(".body-overlay-1").on("click", function () {
            container.removeClass("sidebar-visible");
            wrapper4.removeClass("mobile-menu-active");
            navbarTrigger.removeClass("burger-close");
        });
    }
    mobileHeaderActive();
    /*---------------------
        Mobile menu active
    ------------------------ */
    var $offCanvasNav = $(".mobile-menu"),
        $offCanvasNavSubMenu = $offCanvasNav.find(".sub-menu");
    /*Add Toggle Button With Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i class="fi-rr-angle-small-down"></i></span>');
    /*Close Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.slideUp();
    /*Category Sub Menu Toggle*/
    $offCanvasNav.on("click", "li a, li .menu-expand", function (e) {
        var $this = $(this);
        if (
            $this
                .parent()
                .attr("class")
                .match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/) &&
            ($this.attr("href") === "#" || $this.hasClass("menu-expand"))
        ) {
            e.preventDefault();
            if ($this.siblings("ul:visible").length) {
                $this.parent("li").removeClass("active");
                $this.siblings("ul").slideUp();
            } else {
                $this.parent("li").addClass("active");
                $this.closest("li").siblings("li").removeClass("active").find("li").removeClass("active");
                $this.closest("li").siblings("li").find("ul:visible").slideUp();
                $this.siblings("ul").slideDown();
            }
        }
    });
    /*--- language currency active ----*/
    $(".mobile-language-active").on("click", function (e) {
        e.preventDefault();
        $(".lang-dropdown-active").slideToggle(900);
    });
    /*--- categories-button-active-2 ----*/
    $(".categories-button-active-2").on("click", function (e) {
        e.preventDefault();
        $(".categori-dropdown-active-small").slideToggle(900);
    });
    /*--- Mobile demo active ----*/
    var demo = $(".tm-demo-options-wrapper");
    $(".view-demo-btn-active").on("click", function (e) {
        e.preventDefault();
        demo.toggleClass("demo-open");
    });
    /*-----More Menu Open----*/
    $(".more_slide_open").slideUp();
    $(".more_categories").on("click", function () {
        $(this).toggleClass("show");
        $(".more_slide_open").slideToggle();
    });
    /* --- SwiperJS --- */
    $(".swiper-group-6").each(function () {
        var swiper_6_items = new Swiper(this, {
            spaceBetween: 30,
            slidesPerView: 6,
            spaceBetween: 30,
            slidesPerGroup: 2,
            loop: true,
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev"
            },
            autoplay: {
                delay: 10000
            },
            breakpoints: {
                1199: {
                    slidesPerView: 6
                },
                800: {
                    slidesPerView: 4
                },
                400: {
                    slidesPerView: 2
                },
                350: {
                    slidesPerView: 2,
                    slidesPerGroup: 1,
                    spaceBetween: 15
                }
            }
        });
    });

    $(".swiper-group-4").each(function () {
        var swiper_4_items = new Swiper(this, {
            spaceBetween: 30,
            slidesPerView: 4,
            spaceBetween: 30,
            slidesPerGroup: 2,
            loop: true,
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev"
            },
            autoplay: {
                delay: 10000
            },
            breakpoints: {
                1199: {
                    slidesPerView: 4
                },
                800: {
                    slidesPerView: 3
                },
                500: {
                    slidesPerView: 2
                },
                350: {
                    slidesPerView: 1
                },
                250: {
                    slidesPerView: 1
                }
            },
            on: {
                afterInit: function () {
                    // set padding left slide fleet
                    var leftTitle = 0;
                    var titleFleet = $(".container");
                    if (titleFleet.length > 0) {
                        leftTitle = titleFleet.offset().left;
                    }
                    if ($(".box-swiper-padding").length > 0) {
                        $(".box-swiper-padding").css("padding-left", leftTitle + "px");
                    }
                }
            }
        });
    });

    $(".swiper-group-3").each(function () {
        var swiper_3_items = new Swiper(this, {
            spaceBetween: 30,
            slidesPerView: 3,
            spaceBetween: 30,
            slidesPerGroup: 1,
            loop: true,
            navigation: {
                nextEl: ".swiper-button-next-3",
                prevEl: ".swiper-button-prev-3"
            },
            autoplay: {
                delay: 10000
            },
            breakpoints: {
                1199: {
                    slidesPerView: 3
                },
                800: {
                    slidesPerView: 2
                },
                400: {
                    slidesPerView: 1
                },
                250: {
                    slidesPerView: 1
                }
            }
        });
    });

    $(".swiper-group-1").each(function () {
        var swiper_1_item = new Swiper(this, {
            spaceBetween: 30,
            slidesPerView: 1,
            spaceBetween: 30,
            slidesPerGroup: 1,
            loop: true,
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev"
            },
            autoplay: {
                delay: 10000
            }
        });
    });

    $(".swiper-group-testimonials").each(function () {
        var swiper_items_testimonials = new Swiper(this, {
            spaceBetween: 30,
            slidesPerView: 2,
            spaceBetween: 30,
            slidesPerGroup: 1,
            loop: true,
            navigation: {
                nextEl: ".swiper-button-next-testimonials",
                prevEl: ".swiper-button-prev-testimonials"
            },
            autoplay: {
                delay: 10000
            },
            breakpoints: {
                1199: {
                    slidesPerView: 2
                },
                1000: {
                    slidesPerView: 1
                },
                400: {
                    slidesPerView: 1
                },
                350: {
                    slidesPerView: 1
                }
            },
            on: {
                afterInit: function () {
                    // set padding left slide fleet
                    var leftTitle = 0;
                    var titleFleet = $(".container");
                    if (titleFleet.length > 0) {
                        leftTitle = titleFleet.offset().left;
                    }
                    if ($(".box-swiper-padding").length > 0) {
                        $(".box-swiper-padding").css("padding-left", leftTitle + "px");
                    }
                }
            }
        });
    });
    var swiper_animate_items = null;
    $(".swiper-group-animate").each(function () {
        swiper_animate_items = new Swiper(this, {
            spaceBetween: 30,
            slidesPerView: "auto",
            spaceBetween: 30,
            slidesPerGroup: 1,
            loop: true,
            speed: 5000,
            navigation: {
                nextEl: ".swiper-button-next-animate",
                prevEl: ".swiper-button-prev-animate"
            },
            autoplay: {
                enabled: 1,
                delay: 1,
                waitForTransition: 1,
                disableOnInteraction: 1,
                stopOnLastSlide: 1,
                reverseDirection: 1
            },
            // autoplay: {
            //     delay: 10000
            // },
            breakpoints: {
                1199: {
                    slidesPerView: "auto"
                },
                800: {
                    slidesPerView: "auto"
                },
                400: {
                    slidesPerView: 1
                },
                350: {
                    slidesPerView: 1
                }
            }
        });
    });

    $(".swiper-group-animate").mouseenter(function () {
        swiper_animate_items.autoplay.stop();
    });

    $(".swiper-group-animate").mouseleave(function () {
        swiper_animate_items.autoplay.start();
    });
    var swiper_animate_items_2 = null;
    $(".swiper-group-animate-2").each(function () {
        swiper_animate_items_2 = new Swiper(this, {
            spaceBetween: 30,
            slidesPerView: "auto",
            spaceBetween: 30,
            slidesPerGroup: 1,
            loop: true,
            speed: 5000,
            navigation: {
                nextEl: ".swiper-button-next-animate",
                prevEl: ".swiper-button-prev-animate"
            },
            autoplay: {
                enabled: 1,
                delay: 1,
                waitForTransition: 1,
                disableOnInteraction: 1,
                stopOnLastSlide: 1,
                reverseDirection: 0
            },
            // autoplay: {
            //     delay: 10000
            // },
            breakpoints: {
                1199: {
                    slidesPerView: "auto"
                },
                800: {
                    slidesPerView: "auto"
                },
                400: {
                    slidesPerView: 1
                },
                350: {
                    slidesPerView: 1
                }
            }
        });
    });
    $(".swiper-group-animate-2").mouseenter(function () {
        swiper_animate_items_2.autoplay.stop();
    });
    $(".swiper-group-animate-2").mouseleave(function () {
        swiper_animate_items_2.autoplay.start();
    });
    var swiper_animate_items_verticle = null;
    $(".swiper-group-animate-verticle").each(function () {
        $(this).slick({
            autoplay: true,
            arrows: false,
            dots: false,
            slidesToShow: 3,
            centerPadding: "10px",
            draggable: true,
            infinite: true,
            pauseOnHover: false,
            swipe: false,
            touchMove: false,
            vertical: true,
            speed: 3000,
            autoplaySpeed: 10,
            useTransform: true,
            cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
            adaptiveHeight: true
        });
    });

    $(".swiper-group-animate-verticle-2").each(function () {
        $(this).slick({
            autoplay: true,
            arrows: false,
            dots: false,
            slidesToShow: 3,
            centerPadding: "10px",
            draggable: true,
            infinite: true,
            pauseOnHover: false,
            swipe: false,
            touchMove: true,
            vertical: true,
            speed: 2000,
            direction: 1,
            // rtl: true,
            autoplaySpeed: 10,
            useTransform: true,
            cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
            adaptiveHeight: false
        });
    });

    $("#slide-top").each(function () {
        $(this).carouselTicker({
            mode: "vertical",
            direction: "prev"
        });
    });

    $("#slide-top-award").each(function () {
        $(this).carouselTicker({
            mode: "vertical",
            direction: "prev"
        });
    });

    $("#slide-top-award-2").each(function () {
        $(this).carouselTicker({
            mode: "vertical",
            direction: "prev"
        });
    });

    $("#slide-bottom-award").each(function () {
        $(this).carouselTicker({
            mode: "vertical",
            direction: "next"
        });
    });

    $("#slide-bottom").each(function () {
        $(this).carouselTicker({
            mode: "vertical",
            direction: "next"
        });
    });
    $("#slide-partners").each(function () {
        $(this).carouselTicker({
            direction: "prev"
        });
    });

    $("#slide-logos").each(function () {
        $(this).carouselTicker({
            direction: "prev"
        });
    });

    $("#slide-grow-1").each(function () {
        $(this).carouselTicker({
            direction: "prev",
            speed: 1,
            delay: 30
        });
    });

    $("#slide-grow-2").each(function () {
        $(this).carouselTicker({
            direction: "next",
            speed: 1,
            delay: 30
        });
    });

    //Dropdown selected item
    $(".dropdown-menu li a").on("click", function (e) {
        e.preventDefault();
        $(this)
            .parents(".dropdown")
            .find(".btn span")
            .html($(this).text() + ' <span class="caret"></span>');
        $(this).parents(".dropdown").find(".btn").val($(this).data("value"));
    });
    $(".list-tags-job .remove-tags-job").on("click", function (e) {
        e.preventDefault();
        $(this).closest(".job-tag").remove();
    });
    // Video popup
    if ($(".popup-youtube").length) {
        $(".popup-youtube").magnificPopup({
            type: "iframe",
            mainClass: "mfp-fade",
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
    }

    $(".cb-plan").on("click", function () {
        var _parents = $(this).parents("li");
        $(".list-choose-plan li").removeClass("active");
        _parents.addClass("active");
        var val = this.value;
        switchBilledType2(val);
    });
    if ($(".box-pricing-2").length > 0 || $(".box-pricing").length > 0) {
        switchBilled();
    }
    if ($(".box-choose-plan").length > 0) {
        switchBilledType2(1);
    }

    $(window)
        .resize(function () {
            var _pd_left = $(".padding-left-auto");
            var _pd_right = $(".padding-right-auto");
            var _container = $(".container");
            var _offset_left = _container.offset().left;
            _pd_left.css("padding-left", "" + _offset_left + "px");
            _pd_right.css("padding-right", "" + _offset_left + "px");
            $(".box-comming-soon-banner").css("padding-left", "" + _offset_left + "px");
        })
        .resize();
    var msnry = null;
    if ($("#masonry").length > 0) {
        msnry = new Masonry("#masonry", {
            itemSelector: ".col-lg-4",
            percentPosition: true
        });
    }
    $(".box-button-filters a.btn").on("click", function (e) {
        e.preventDefault();
        var _filter = $(this).attr("data-filter");
        $(".box-button-filters a.btn").removeClass("active");
        $(this).addClass("active");
        if (_filter == "all") {
            $(".item-filter").show();
        } else {
            $(".item-filter").hide();
            $("." + _filter).show();
        }
        msnry.layout();
    });

    /*------ Timer Countdown ----*/
    $("[data-countdown]").each(function () {
        var $this = $(this),
            finalDate = $(this).data("countdown");
        $this.countdown(finalDate, function (event) {
            $(this).html(event.strftime("" + '<span class="countdown-section"><span class="countdown-amount font-sm-bold lh-16">%D</span><span class="countdown-period lh-14 font-xs"> days </span></span>' + '<span class="countdown-section"><span class="countdown-amount font-sm-bold lh-16">%H</span><span class="countdown-period font-xs lh-14"> hours </span></span>' + '<span class="countdown-section"><span class="countdown-amount font-sm-bold lh-16">%M</span><span class="countdown-period font-xs lh-14"> mins </span></span>' + '<span class="countdown-section"><span class="countdown-amount font-sm-bold lh-16">%S</span><span class="countdown-period font-xs lh-14"> secs </span></span>'));
        });
    });
})(jQuery);
// Check billed
function switchBilled() {
    var checkBox = $("#cb_billed_type");
    var forMonth = $(".for-month");
    var forYear = $(".for-year");
    var billMonth = $(".text-billed-month");
    var billYear = $(".text-billed-year");
    for (var i = 0; i < forMonth.length; i++) {
        if (checkBox.is(":checked")) {
            forYear.eq(i).addClass("display-year");
            billYear.addClass("active");
            billMonth.removeClass("active");
            forMonth.eq(i).removeClass("display-month");
        } else {
            forYear.eq(i).removeClass("display-year");
            billMonth.addClass("active");
            billYear.removeClass("active");
            forMonth.eq(i).addClass("display-month");
        }
    }
}
function switchBilledType2(val) {
    var forMonth = $(".for-month");
    var forYear = $(".for-year");
    var billMonth = $(".text-billed-month");
    var billYear = $(".text-billed-year");
    for (var i = 0; i < forMonth.length; i++) {
        if (val == 1) {
            forYear.eq(i).addClass("display-year");
            billYear.addClass("active");
            billMonth.removeClass("active");
            forMonth.eq(i).removeClass("display-month");
        } else {
            forYear.eq(i).removeClass("display-year");
            billMonth.addClass("active");
            billYear.removeClass("active");
            forMonth.eq(i).addClass("display-month");
        }
    }
}
//Perfect Scrollbar
const ps = new PerfectScrollbar(".mobile-header-wrapper-inner");
