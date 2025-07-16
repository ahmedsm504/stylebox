# StyleBox 🎨

منصة Django بسيطة لعرض ومشاركة تصاميم HTML وCSS.

## 💡 المميزات
- تسجيل ودخول المصممين
- رفع تصاميم HTML + CSS
- تصفية التصاميم حسب النوع (زر، كارد، ناف بار...)
- صفحة تفاصيل للتصميم
- نسخ الكود بزر واحد
- صفحة لكل مصمم مع بياناته وتصاميمه
- تعديل الملف الشخصي، تغيير كلمة المرور، حذف الحساب

## ⚙️ التقنيات المستخدمة
- Python 3.13
- Django 5.1.6
- Tailwind CSS
- SQLite

## 🚀 بدء المشروع محليًا

```bash
git clone https://github.com/ahmedsm504/stylebox.git
cd stylebox
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
