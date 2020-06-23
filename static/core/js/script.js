window.onscroll = function() {
    shrinkHeader()
};

function shrinkHeader() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById("branding").style.fontSize = "1.5rem";
        document.getElementById("branding").style.marginBottom = "0";
    } else {
        document.getElementById("branding").style.fontSize = "4rem";
        document.getElementById("branding").style.marginBottom = "0.25rem";
    }
}
