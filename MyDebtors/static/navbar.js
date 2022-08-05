const harmburger = document.getElementById('harmburger');
const mobileMenu = document.getElementById('mobile-menu');


harmburger.addEventListener('click', dropdownMenu);

function dropdownMenu() {
    if(mobileMenu.style.right === '0px') {
        mobileMenu.style.right = '-380px';
    } else {
        mobileMenu.style.right = '0px';
    }
}