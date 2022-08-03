/*Notification menu variables */
const notifi_Icon = document.getElementById('notifi-icon');
const notifications = document.getElementById('notifications');


/* Sidebar menu variables */
const harmburgerMenu = document.getElementById('harmburger');
const sideBar = document.getElementById('sidebar');
const contentArea = document.getElementById('content_area');



/*Event listeners */
harmburgerMenu.addEventListener('click', openSidebar);
notifi_Icon.addEventListener('click', openNotifications);

function openSidebar() {

    if(sideBar.style.left === '-300px') {
        sideBar.style.left = '0px';
        contentArea.classList.remove('reduce');
        contentArea.style.position = 'relative';
    } else {
        sideBar.style.left = '-300px';
        contentArea.classList.add('reduce');
        contentArea.style.position = 'absolute';
    }
}

function openNotifications() {
    if(notifications.style.display === 'block') {
        notifications.style.display = 'none';
    } else {
        notifications.style.display = 'block';
    }
}
