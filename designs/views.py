from django.shortcuts import render, redirect
from .forms import DesignForm
from django.contrib.auth.decorators import login_required

# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DesignForm

@login_required
def create_design(request):
    if not request.user.profile.is_approved:
        return render(request, 'designs/waiting_approval.html')  # ⬅️ الحساب تحت المراجعة

    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            design = form.save(commit=False)
            design.creator = request.user
            design.save()

            action = request.POST.get('action')  # ⬅️ تحديد نوع الزر المضغوط
            if action == 'save_home':
                return redirect('design_list')  # 🔁 الرجوع للصفحة الرئيسية
            elif action == 'save_new':
                return redirect('create_design')  # 🔁 فتح صفحة إنشاء تصميم جديد
    else:
        form = DesignForm()

    return render(request, 'designs/design_create.html', {'form': form})


from django.shortcuts import render
from .models import Design

def design_list(request):
    design_type = request.GET.get('type')
    if design_type:
        designs = Design.objects.filter(design_type=design_type).order_by('-created_at')
    else:
        designs = Design.objects.all().order_by('-created_at')
    return render(request, 'designs/design_list.html', {
        'designs': designs,
        'current_type': design_type  # علشان نتحكم في الـ active button
    })


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل الدخول مباشرة بعد التسجيل
            return redirect('design_list')
    else:
        form = UserCreationForm()
    return render(request, 'designs/register.html', {'form': form})


from django.shortcuts import get_object_or_404

def design_detail(request, pk):
    design = get_object_or_404(Design, pk=pk)
    return render(request, 'designs/design_detail.html', {'design': design})


from django.contrib.auth.models import User

def designer_profile(request, username):
    user = get_object_or_404(User, username=username)
    designs = Design.objects.filter(creator=user).order_by('-created_at')
    return render(request, 'designs/designer_profile.html', {
        'designer': user,
        'designs': designs
    })


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Design
from .forms import DesignForm

@login_required
def edit_design(request, pk):
    design = get_object_or_404(Design, pk=pk, creator=request.user)
    
    if request.method == 'POST':
        form = DesignForm(request.POST, instance=design)
        if form.is_valid():
            form.save()
            return redirect('design_detail', pk=design.pk)
    else:
        form = DesignForm(instance=design)
    
    return render(request, 'designs/edit_design.html', {'form': form, 'design': design})


# designs/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile_view(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    return render(request, 'designs/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# designs/views.py
from django.contrib.auth import logout

@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        return redirect('design_list')
    return render(request, 'designs/delete_account.html')


# views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# views.py
from django.http import JsonResponse
from .models import Design, DesignLike
from django.contrib.auth.decorators import login_required


@login_required
def like_design(request, design_id):
    design = get_object_or_404(Design, id=design_id)
    user = request.user

    # check if user already liked this design
    like, created = DesignLike.objects.get_or_create(design=design, user=user)
    if not created:
        # already liked → remove it
        like.delete()
        liked = False
    else:
        liked = True

    # new like count
    like_count = DesignLike.objects.filter(design=design).count()

    return JsonResponse({'liked': liked, 'like_count': like_count})


from django.db.models import Count

def best_designs(request):
    designs = Design.objects.annotate(
        like_count=Count('designlike')
    ).filter(like_count__gte=10).order_by('-like_count', '-created_at')
    return render(request, 'designs/best_designs.html', {'designs': designs})