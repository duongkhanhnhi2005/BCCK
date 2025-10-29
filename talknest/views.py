from django.shortcuts import render
from .models import Community, Post
from django.db.models import Q
from .forms import CommunityForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404



def home(request):
    communities = Community.objects.all()
    return render(request, "home.html",{'communities': communities})

def search(request):
    keyword = request.GET.get('keyword', '')
    user = request.GET.get('user', '')
    community_id = request.GET.get('community', '')
    before = request.GET.get('before', '')
    after = request.GET.get('after', '')

    posts = None  # mặc định chưa tìm

    # chỉ thực hiện tìm kiếm nếu có ít nhất 1 tham số GET
    if any([keyword, user, community_id not in [None, '', 'all'], before, after]):
        posts = Post.objects.all()

    if keyword:
        posts = posts.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))

    if user:
        posts = posts.filter(author__username__icontains=user)

    if community_id and community_id != 'all':
        posts = posts.filter(community_id=community_id)

    if before:
        posts = posts.filter(created_at__lte=before)

    if after:
        posts = posts.filter(created_at__gte=after)

    communities = Community.objects.all()

    return render(request, 'search.html', {
        'posts': posts,
        'communities': communities,
        'keyword': keyword,
        'user': user,
        'before': before,
        'after': after,
        'community_id': community_id,
    })

def register(request):
    return render(request, "register.html")
def login(request):
    return render(request, "login.html")

@login_required
def create_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.created_by = request.user  # Gán người tạo
            community.save()
            community.members.add(request.user)  # Auto join sau khi tạo
            return redirect('community_detail', community_id=community.id)
    else:
        form = CommunityForm()

    return render(request, 'create_community.html', {'form': form})

@login_required
def community_detail(request, community_id):
    community = get_object_or_404(Community, community_id=community_id)
    posts = Post.objects.filter(community=community).order_by('-created_at')

    is_member = request.user in community.members.all()

    # Xử lý tham gia / rời cộng đồng
    if request.method == "POST":
        if is_member:
            community.members.remove(request.user)
        else:
            community.members.add(request.user)
        return redirect('community_detail', community_id=community.community_id)

    return render(request, 'community_detail.html', {
        'community': community,
        'posts': posts,
        'is_member': is_member
    })


def community_list(request):
    communities = Community.objects.all()
    return render(request, 'community_list.html', {'communities': communities})
