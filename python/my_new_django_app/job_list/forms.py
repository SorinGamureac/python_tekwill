from django.forms import ModelForm
from job_list.models import JobPost


class JobPostForm(ModelForm):

    def clean_title(self):
        if 'web' in self.cleaned_data['title'].lower():
            raise ValidationError('Web article')

    class Meta:
        model = JobPost
        fields = ('title', 'content', 'author')