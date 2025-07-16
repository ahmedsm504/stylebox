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
