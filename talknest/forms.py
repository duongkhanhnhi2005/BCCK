from django import forms
from .models import Community
from .models import UserProfile



class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']
        labels = {
            'name': 'Tên cộng đồng',
            'description': 'Mô tả cộng đồng',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên cộng đồng...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Giới thiệu về cộng đồng của bạn...'}),
        }


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar_url']

