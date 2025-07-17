// دالة نسخ النص إلى الحافظة
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert("✅ تم نسخ الكود بنجاح");
  }).catch(() => {
    alert("❌ لم يتم النسخ");
  });
}

// إدراج CSS في عناصر المعاينة بعد تحميل الصفحة
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('.css-injector').forEach(el => {
    const cssCode = el.dataset.cssCode;
    const targetId = el.dataset.cssTarget;
    const targetEl = document.getElementById(targetId);

    if (cssCode && targetEl) {
      const style = document.createElement("style");
      style.innerHTML = cssCode;
      targetEl.appendChild(style);
    }
  });
});

/////////////fillter and cards



// Add stagger animation to cards on page load
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.design-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
});

// Add active class to current filter button
document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const currentType = urlParams.get('type');
    
    // Remove active class from all buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Add active class to current button
    if (currentType) {
        const activeButton = document.querySelector(`[href="?type=${currentType}"]`);
        if (activeButton) {
            activeButton.classList.add('active');
        }
    } else {
        // If no type parameter, "الكل" should be active
        document.querySelector('[href="?"]').classList.add('active');
    }
});





document.addEventListener('DOMContentLoaded', function() {
    const navbarToggle = document.getElementById('navbar-toggle');
    const navbarMobile = document.getElementById('navbar-mobile');
    const navbar = document.getElementById('navbar');

    // Mobile menu toggle
    navbarToggle.addEventListener('click', function() {
        navbarToggle.classList.toggle('active');
        navbarMobile.classList.toggle('active');
    });

    // Scroll effect for navbar
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!navbar.contains(event.target)) {
            navbarToggle.classList.remove('active');
            navbarMobile.classList.remove('active');
        }
    });
    });


    // Add loading state to button on form submission
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            const submitBtn = document.getElementById('submitBtn');
            submitBtn.classList.add('loading');
            submitBtn.textContent = 'جاري تسجيل الدخول...';
        });



          // Function to detect content type and apply appropriate class
        function detectContentType(htmlCode, cssCode) {
            const html = htmlCode.toLowerCase();
            const css = cssCode.toLowerCase();
            
            // Check for different content types
            if (html.includes('button') || css.includes('button') || 
                html.includes('btn') || css.includes('btn')) {
                return 'button-content';
            }
            
            if (html.includes('form') || css.includes('form') || 
                html.includes('input') || css.includes('input')) {
                return 'form-content';
            }
            
            if (html.includes('nav') || css.includes('nav') || 
                html.includes('navbar') || css.includes('navbar')) {
                return 'navigation-content';
            }
            
            if (html.includes('table') || css.includes('table') || 
                html.includes('td') || css.includes('td')) {
                return 'table-content';
            }
            
            if (html.includes('modal') || css.includes('modal') || 
                html.includes('dialog') || css.includes('dialog')) {
                return 'modal-content';
            }
            
            if (html.includes('img') || css.includes('img') || 
                html.includes('image') || css.includes('image')) {
                return 'image-content';
            }
            
            if (html.includes('card') || css.includes('card') || 
                html.includes('panel') || css.includes('panel')) {
                return 'card-content';
            }
            
            // Default to text content
            return 'text-content';
        }

        // Function to apply dynamic sizing to Django template cards
        function applyDynamicSizing() {
            const designCards = document.querySelectorAll('.design-card');
            
            designCards.forEach(card => {
                const iframe = card.querySelector('.preview-iframe');
                if (iframe) {
                    // Wait for iframe to load
                    iframe.addEventListener('load', function() {
                        try {
                            const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
                            const htmlContent = iframeDoc.documentElement.innerHTML;
                            
                            // Extract CSS from style tags
                            const styleElements = iframeDoc.querySelectorAll('style');
                            let cssContent = '';
                            styleElements.forEach(style => {
                                cssContent += style.textContent;
                            });
                            
                            // Detect content type
                            const contentType = detectContentType(htmlContent, cssContent);
                            
                            // Apply the appropriate class
                            card.className = `design-card ${contentType}`;
                            
                            // Add content type badge
                            let badge = card.querySelector('.content-type-badge');
                            if (!badge) {
                                badge = document.createElement('div');
                                badge.className = 'content-type-badge';
                                card.appendChild(badge);
                            }
                            badge.textContent = contentType.replace('-content', '').toUpperCase();
                            
                        } catch (error) {
                            console.warn('Could not analyze iframe content:', error);
                            // Fallback to default sizing
                            card.className = 'design-card text-content';
                        }
                    });
                }
            });
        }

        // Apply dynamic sizing when page loads
        document.addEventListener('DOMContentLoaded', applyDynamicSizing);