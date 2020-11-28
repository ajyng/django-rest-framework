from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'is_public']

form = Postform(request.POST)
if form.is_valid():
    form.save(commit=False)