from django import forms
from django.contrib.auth.models import User
from cocktail.models import UserProfile, Cocktail, CocktailTastePalette, CocktailBase
from django.db.models.fields.files import ImageField
from django.db import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required = False)
    full_name = forms.CharField(required = False)
    fav_cocktail = forms.CharField(required = False)
    workplace = forms.CharField(required = False)
    class Meta:
        model = UserProfile
        fields = ('full_name', 'avatar', 'fav_cocktail', 'workplace')
        
        
class CocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ('name', 'image', 'base', 'ingredients', 'how_to_make_comment', 'taste_palette')
        
class CocktailSearch(forms.ModelForm):
    name = forms.CharField(required = False)
    class Meta:
        model = Cocktail
        fields = ('name', 'base', 'taste_palette')