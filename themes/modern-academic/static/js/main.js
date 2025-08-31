// Enhanced navbar functionality with scroll effects and active page detection

document.addEventListener('DOMContentLoaded', function() {
    // Get navbar element
    const navbar = document.querySelector('.navbar');
    
    // Scroll effect for navbar
    let lastScrollTop = 0;
    const scrollThreshold = 50; // Pixels to scroll before navbar changes
    
    function handleScroll() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > scrollThreshold) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScrollTop = scrollTop;
    }
    
    // Throttle scroll events for better performance
    let ticking = false;
    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(function() {
                handleScroll();
                ticking = false;
            });
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', requestTick);
    
    // Active page detection
    function setActiveNavLink() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
        
        // Remove active class from all links
        navLinks.forEach(link => {
            link.classList.remove('active');
        });
        
        // Add active class to current page link
        navLinks.forEach(link => {
            const linkHref = link.getAttribute('href');
            const navItem = link.getAttribute('data-nav-item');
            
            // Handle different URL patterns
            if (currentPath === '/' && (linkHref === '/' || linkHref === '/index.html' || navItem === 'home')) {
                link.classList.add('active');
            } else if (currentPath.includes('/pages/publications') && navItem === 'publications') {
                link.classList.add('active');
            } else if (currentPath.includes('/pages/research') && navItem === 'research') {
                link.classList.add('active');
            } else if (linkHref === currentPath) {
                link.classList.add('active');
            }
        });
    }
    
    // Set active link on page load
    setActiveNavLink();
    
    // Update active link when clicking nav links (for SPA-like behavior)
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Remove active from all
            navLinks.forEach(l => l.classList.remove('active'));
            // Add active to clicked link
            this.classList.add('active');
        });
    });
    
    // Enhanced responsive navbar handling
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    // Responsive breakpoints
    const breakpoints = {
        xs: 575,
        sm: 576,
        md: 768,
        lg: 992,
        xl: 1200,
        xxl: 1400
    };
    
    // Get current screen size
    function getCurrentBreakpoint() {
        const width = window.innerWidth;
        if (width <= breakpoints.xs) return 'xs';
        if (width <= breakpoints.md) return 'sm';
        if (width <= breakpoints.lg) return 'md';
        if (width <= breakpoints.xl) return 'lg';
        if (width <= breakpoints.xxl) return 'xl';
        return 'xxl';
    }
    
    // Responsive navbar behavior
    function handleResponsiveNavbar() {
        const currentBreakpoint = getCurrentBreakpoint();
        
        // Adjust navbar behavior based on screen size
        if (currentBreakpoint === 'xs' || currentBreakpoint === 'sm') {
            // Mobile: ensure proper mobile menu behavior
            if (navbarCollapse) {
                navbarCollapse.classList.add('mobile-nav');
            }
        } else {
            // Desktop: remove mobile styles
            if (navbarCollapse) {
                navbarCollapse.classList.remove('mobile-nav', 'show');
            }
        }
    }
    
    // Bootstrap navbar collapse for mobile
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });
        
        // Close mobile menu when clicking nav links
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                const currentBreakpoint = getCurrentBreakpoint();
                if (currentBreakpoint === 'xs' || currentBreakpoint === 'sm') {
                    navbarCollapse.classList.remove('show');
                }
            });
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navbar.contains(event.target);
            const currentBreakpoint = getCurrentBreakpoint();
            
            if (!isClickInsideNav && navbarCollapse.classList.contains('show') && 
                (currentBreakpoint === 'xs' || currentBreakpoint === 'sm')) {
                navbarCollapse.classList.remove('show');
            }
        });
    }
    
    // Handle window resize
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            handleResponsiveNavbar();
            
            // Re-calculate scroll position for different screen sizes
            handleScroll();
        }, 100);
    });
    
    // Initialize responsive behavior
    handleResponsiveNavbar();
    
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                e.preventDefault();
                const offsetTop = targetElement.offsetTop - navbar.offsetHeight - 20;
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Initialize on page load
    handleScroll();
    
    // News toggle functionality
    initializeNewsToggle();
});

// News section functionality
function initializeNewsToggle() {
    const newsContent = document.getElementById('newsContent');
    const toggleBtn = document.getElementById('toggleNewsBtn');
    const toggleText = document.getElementById('toggleNewsText');
    const toggleIcon = document.getElementById('toggleNewsIcon');
    
    if (!newsContent || !toggleBtn) return;
    
    // Find all news items (li elements)
    const newsItems = newsContent.querySelectorAll('ul li');
    
    if (newsItems.length === 0) return;
    
    let isExpanded = false;
    const itemsToShow = 10;
    
    // Initially hide items beyond the first 10
    function updateNewsDisplay() {
        newsItems.forEach((item, index) => {
            if (index >= itemsToShow && !isExpanded) {
                item.style.display = 'none';
            } else {
                item.style.display = 'list-item';
            }
        });
        
        // Update button text and icon
        if (isExpanded) {
            toggleText.textContent = 'Show Less';
            toggleIcon.className = 'bi bi-chevron-up ms-1';
        } else {
            toggleText.textContent = 'Show All';
            toggleIcon.className = 'bi bi-chevron-down ms-1';
        }
        
        // Hide button if there are 10 or fewer items
        if (newsItems.length <= itemsToShow) {
            toggleBtn.style.display = 'none';
        }
    }
    
    // Add click event to toggle button
    toggleBtn.addEventListener('click', function(e) {
        e.preventDefault();
        isExpanded = !isExpanded;
        updateNewsDisplay();
        
        // Smooth scroll to news section when expanding
        if (isExpanded) {
            setTimeout(() => {
                newsContent.scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'start' 
                });
            }, 100);
        }
    });
    
    // Initialize display
    updateNewsDisplay();
}

// Additional utility functions for enhanced UX
function addLoadingSpinner() {
    // Add subtle loading indicators for better UX
    const style = document.createElement('style');
    style.textContent = `
        .loading {
            opacity: 0.7;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }
        
        .loading::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            margin: -10px 0 0 -10px;
            border: 2px solid #f3f3f3;
            border-top: 2px solid var(--custom-primary, #0d6efd);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    `;
    document.head.appendChild(style);
}

// Call utility functions
addLoadingSpinner();

// Enhanced accessibility
document.addEventListener('keydown', function(e) {
    // Skip to main content with Alt+M
    if (e.altKey && e.key === 'm') {
        const mainContent = document.querySelector('main');
        if (mainContent) {
            mainContent.focus();
            mainContent.scrollIntoView({ behavior: 'smooth' });
        }
    }
    
    // Focus navbar with Alt+N
    if (e.altKey && e.key === 'n') {
        const firstNavLink = document.querySelector('.navbar-nav .nav-link');
        if (firstNavLink) {
            firstNavLink.focus();
        }
    }
});