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