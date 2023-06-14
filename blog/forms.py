from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form for editing a blog post
    """
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'