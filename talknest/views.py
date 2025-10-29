from django.shortcuts import render,redirect
from .models import Topic, Post,UserProfile
from django.db.models import Q
from .forms import AvatarUploadForm


def home(request):
    topics = Topic.objects.all()
    return render(request, "home.html",{'topics': topics})

def search(request):
    keyword = request.GET.get('keyword', '')
    user = request.GET.get('user', '')
    topic_id = request.GET.get('topic', '')
    before = request.GET.get('before', '')
    after = request.GET.get('after', '')

    posts = None  # mặc định chưa tìm

    # chỉ thực hiện tìm kiếm nếu có ít nhất 1 tham số GET
    if any([keyword, user, topic_id not in [None, '', 'all'], before, after]):
        posts = Post.objects.all()

    if keyword:
        posts = posts.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))

    if user:
        posts = posts.filter(author__username__icontains=user)

    if topic_id and topic_id != 'all':
        posts = posts.filter(topic_id=topic_id)

    if before:
        posts = posts.filter(created_at__lte=before)

    if after:
        posts = posts.filter(created_at__gte=after)

    topics = Topic.objects.all()

    return render(request, 'search.html', {
        'posts': posts,
        'topics': topics,
        'keyword': keyword,
        'user': user,
        'before': before,
        'after': after,
        'topic_id': topic_id,
    })

def register(request):
    return render(request, "register.html")
def login(request):
    return render(request, "login.html")
def profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # ✅ Lưu avatar mới
            return redirect('profile')  # Reload lại trang để hiển thị ảnh
    else:
        form = AvatarUploadForm(instance=profile)

    user_posts = user.posts.all() if hasattr(user, 'posts') else []

    return render(request, 'profile.html', {
        'user': user,
        'form': form,
        'user_posts': user_posts
    })