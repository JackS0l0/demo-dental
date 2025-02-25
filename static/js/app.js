window.addEventListener("scroll", function () {
    let navbar = document.querySelector(".navbarBlock");
    let logoImgTop = document.querySelector(".logoImgTop");
    if (window.scrollY > 10) {
        navbar.style.padding = "1.5vw 3.5vw";
        navbar.style.position = "fixed";
        navbar.style.top = "0";
        navbar.style.width = "100%";
        logoImgTop.style.width = "12.5vw";
    } else {
        navbar.style.padding = "";
        navbar.style.position = "";
        navbar.style.width = "";
        navbar.style.top = "";
        logoImgTop.style.width = "";
    }
});
let mybutton = document.getElementById("myBtn");
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}