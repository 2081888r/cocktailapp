#Models for cocktail websites database, Ross Wilson & Georgios Kampanos

from django.db import models
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import default
from django.template.defaultfilters import slugify
from django.db.models.fields.related import ForeignKey

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    full_name = models.CharField(max_length = 64, default = "")
    workplace = models.CharField(max_length = 64, default = "")
    fav_cocktail = models.CharField(max_length = 64, default = "")
    avatar = models.ImageField(upload_to='bartender_images', blank=True)
    
    def save(self, *args, **kwargs):
       super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username
    
class CocktailTastePalette(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, default = "")

    def __unicode__(self):
        return self.name

class CocktailBase(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, default = "")

    def __unicode__(self):
        return self.name

class Cocktail(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, default = "")
    image = models.ImageField(upload_to='cocktail_images', blank=True)
    base = models.ForeignKey(CocktailBase, blank = True, null = True)
    ingredients = models.CharField(max_length = 512, default = "")
    how_to_make_comment = models.CharField(max_length=256, default = "")
    bartender = models.ForeignKey(User)
    taste_palette = models.ForeignKey(CocktailTastePalette, blank = True, null = True)
    views = models.IntegerField(default = 0)
    slug = models.SlugField(unique=True, default = "")
    five_stars = models.IntegerField(default = 0, null = True)
    four_stars = models.IntegerField(default = 0, null = True)
    three_stars = models.IntegerField(default = 0, null = True)
    two_stars = models.IntegerField(default = 0, null = True)
    one_star = models.IntegerField(default = 0, null = True)
    
    def ingredients_as_list(self):
        return self.ingredients.split(',')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cocktail, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
    
    
 
class BartenderRatesCocktail(models.Model):
    id = models.AutoField(primary_key = True)
    bartender = models.ForeignKey(User)
    cocktail = models.ForeignKey(Cocktail)
    
    def __unicode__(self):
        return self.id

