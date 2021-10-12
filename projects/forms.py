from django.forms import ModelForm, widgets
from django import forms
from django.db.models.functions import Cast
from django.db.models import CharField
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        #self.fields['title'].widget.attrs.update({'class':'input'})


class ReviewForm(ModelForm):
    # value = forms.ModelChoiceField(
    #     label="",
    #     # queryset=Review.objects.values_list('value', flat=True).distinct(),
    #     queryset = Review.VOTE_TYPE.all(),
    #     empty_label="Place your vote"
    #     )
    class Meta:
        model =  Review
        fields =  ['value', 'body']
        labels = {
            'body':'',
            'value':''
        }
        widgets = {
            'body':forms.Textarea(attrs={'placeholder': 'Add a comment'})
        }
        

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['value'].empty_label = 'lorem'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})