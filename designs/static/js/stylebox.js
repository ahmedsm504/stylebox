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