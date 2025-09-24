from django import forms

from .models import Post, MusicVenue

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class MusicVenueForm(forms.ModelForm):

    class Meta:
        model = MusicVenue
        fields = ('name', 'address', 'description')