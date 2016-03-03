from django.contrib import admin

from cocktail.models import UserProfile, Cocktail, CocktailTastePalette, CocktailBase, BartenderRatesCocktail

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'full_name', 'avatar', 'workplace', 'fav_cocktail' )

class CocktailAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'name', 'image', 'base', 'ingredients', 'how_to_make_comment', 'bartender', 'taste_palette', 'views', 'slug', 
                     'five_stars', 'four_stars', 'three_stars', 'two_stars', 'one_star' )

class CocktailTastePaletteAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'name', )

class CocktailBaseAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'name', )
   
class BartenderRatesCocktailAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'bartender', 'cocktail' )


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CocktailTastePalette, CocktailTastePaletteAdmin)
admin.site.register(CocktailBase, CocktailBaseAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BartenderRatesCocktail, BartenderRatesCocktailAdmin)