// Initialize AOS animations
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        once: true
    });
    
    // Hide loader when page is loaded
    const loaderWrapper = document.querySelector('.loader-wrapper');
    setTimeout(function() {
        loaderWrapper.style.opacity = '0';
        loaderWrapper.style.visibility = 'hidden';
    }, 800);
    
    // Change header on scroll
    const header = document.querySelector('header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    
    // Custom cursor
    const cursor = document.querySelector('.cursor');
    const cursorFollower = document.querySelector('.cursor-follower');
    
    document.addEventListener('mousemove', function(e) {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
        cursor.style.opacity = '1';
        
        cursorFollower.style.left = e.clientX + 'px';
        cursorFollower.style.top = e.clientY + 'px';
        cursorFollower.style.opacity = '1';
    });
    
    document.addEventListener('mouseout', function() {
        cursor.style.opacity = '0';
        cursorFollower.style.opacity = '0';
    });
    
    // Hover effect on links
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('mouseover', function() {
            cursor.style.transform = 'translate(-50%, -50%) scale(1.5)';
            cursor.style.borderColor = 'var(--primary)';
            cursorFollower.style.backgroundColor = 'var(--primary)';
        });
        
        link.addEventListener('mouseout', function() {
            cursor.style.transform = 'translate(-50%, -50%) scale(1)';
            cursor.style.borderColor = 'var(--primary)';
            cursorFollower.style.backgroundColor = 'var(--primary)';
        });
    });
    
    // Check for mobile devices
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        // Hide custom cursor on mobile
        cursor.style.display = 'none';
        cursorFollower.style.display = 'none';
    }
});
window.addEventListener('load', function () {
    const loaderWrapper = document.querySelector('.loader-wrapper');
    loaderWrapper.style.opacity = '0';
    // After a short delay, remove it from the layout so it doesn't capture clicks
    setTimeout(() => {
      loaderWrapper.style.display = 'none';
    }, 500);
  });
  