// Carousel functionality
function carousel() {
return {
    currentSlide: 0,
    totalSlides: 3,
    autoplayInterval: null,
    init() {
    this.startAutoplay();
    },
    next() {
    this.currentSlide = (this.currentSlide + 1) % this.totalSlides;
    },
    prev() {
    this.currentSlide = (this.currentSlide - 1 + this.totalSlides) % this.totalSlides;
    },
    startAutoplay() {
    this.autoplayInterval = setInterval(() => {
        this.next();
    }, 5000);
    },
    stopAutoplay() {
    clearInterval(this.autoplayInterval);
    }
}
}

// Lazy loading images
document.addEventListener('DOMContentLoaded', function() {
var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));

if ("IntersectionObserver" in window) {
    let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
    entries.forEach(function(entry) {
        if (entry.isIntersecting) {
        let lazyImage = entry.target;
        lazyImage.src = lazyImage.dataset.src;
        lazyImage.classList.remove("lazy");
        lazyImageObserver.unobserve(lazyImage);
        }
    });
    });

    lazyImages.forEach(function(lazyImage) {
    lazyImageObserver.observe(lazyImage);
    });
} else {
    // Fallback for browsers without IntersectionObserver support
    let lazyLoadThrottleTimeout;
    function lazyLoad() {
    if(lazyLoadThrottleTimeout) {
        clearTimeout(lazyLoadThrottleTimeout);
    }

    lazyLoadThrottleTimeout = setTimeout(function() {
        let scrollTop = window.pageYOffset;
        lazyImages.forEach(function(img) {
        if(img.offsetTop < (window.innerHeight + scrollTop)) {
            img.src = img.dataset.src;
            img.classList.remove('lazy');
        }
        });
        if(lazyImages.length == 0) { 
        document.removeEventListener("scroll", lazyLoad);
        window.removeEventListener("resize", lazyLoad);
        window.removeEventListener("orientationChange", lazyLoad);
        }
    }, 20);
    }

    document.addEventListener("scroll", lazyLoad);
    window.addEventListener("resize", lazyLoad);
    window.addEventListener("orientationChange", lazyLoad);
}
});