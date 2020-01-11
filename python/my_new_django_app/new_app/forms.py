from django.forms import ModelForm
from new_app.models import BlogPost


class BlogPostForm(ModelForm):

    def clean_title(self):
        if 'web' in self.cleaned_data['title'].lower():
            raise ValidationError('Web article')

    class Meta:
        model = BlogPost
        fields = ('title', 'content')