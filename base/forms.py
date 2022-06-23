from django import forms
from .models import Category, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # category = forms.ModelChoiceField(queryset=Category.objects.all(widget=forms.Select(attrs={'class':'form-control'})))
        # title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}))
        # slug = forms.SlugField(widget=forms.SlugField(attrs={'class':'form-control','placeholder':'Enter Title'}))
        fields = ('category_id', 'title','intro','body','image','status')
        # fields = '__all__'
        labels = {'category_id': 'Category','intro': 'Introduction',}
        