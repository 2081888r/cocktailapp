import os
import datetime
from random import randint
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocktails_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from cocktail.models import Cocktail, UserProfile, CocktailTastePalette, CocktailBase
                     
                                   
def addCocktailBase(name):
    base = CocktailBase.objects.get_or_create(name = name)[0]
    return base

def addCocktailTastePalette(name):
   p =  CocktailTastePalette.objects.get_or_create(name=name)[0]
   return p

  
def addCocktail(name, image, base, ingredients, how_to_make_comment, bartender, taste_palette, views, slug, 
                five_stars, four_stars, three_stars, two_stars, one_star):
    Cocktail.objects.get_or_create(name=name, image=image, base=base, ingredients=ingredients,
                                   how_to_make_comment=how_to_make_comment, 
                                   bartender=bartender, 
                                   taste_palette=taste_palette, views=views, slug=slug, 
                                   five_stars=five_stars, four_stars=four_stars, 
                                   three_stars=three_stars, two_stars=two_stars, 
                                   one_star=one_star)[0]
                                   
                                   

def addUser(name, pw, email, is_staff, is_superuser, is_active): 
    user = User.objects.get_or_create(username = name,
                                      password =pw,
                                      email = email,
                                      is_staff = is_staff,
                                      is_superuser = is_superuser,
                                      is_active = is_active,)[0]
    return user


def addUserProfile(user, full_name, workplace, fav_cocktail, avatar):
    UserProfile.objects.get_or_create(user=user, 
                                      full_name=full_name,
                                      workplace=workplace,
                                      fav_cocktail=fav_cocktail,
                                      avatar=avatar)[0]
    


def populate():

    #populate cocktail taste palettes
    print "Adding taste palettes..."
    sweet = addCocktailTastePalette('Sweet')
    sour = addCocktailTastePalette('Sour')
    perfect = addCocktailTastePalette('Perfect')
    other = addCocktailTastePalette('Other')
    print "Done adding taste palettes!"
    print 
    print
    
    
    #populate cocktail bases
    print "Adding cocktail bases..."
    whiskey = addCocktailBase("Whiskey")
    bourbon = addCocktailBase("Bourbon")
    liquor = addCocktailBase("Liquor")
    vodka = addCocktailBase("Vodka")
    rum = addCocktailBase("Rum")
    gin = addCocktailBase("Gin")
    tequila = addCocktailBase("Tequila")
    other = addCocktailBase("Other")
    print "Done adding cocktail bases!"
    print 
    print
    
    
    #populate users
    print "Adding users..."
    admin = User.objects.get(username = "2021259K")
    test = addUser("test", "test", "test@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    marianbeke = addUser("marianbeke", "marianbeke123", "marianbeke@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    monicaberg = addUser("monicaberg", "monicaberg123", "monicaberg@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    simonecaporale = addUser("simonecaporale", "simonecaporale123", "simonecaporale@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    ryanc = addUser("ryanc", "ryanc123", "ryanc@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    mariokappes = addUser("mariokappes", "mariokappes123", "mariokappes@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    zdenekkastanek = addUser("zdenekkastanek", "zdenekkastanek123", "zdenekkastanek@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    timphilips = addUser("timphilips", "timphilips123", "timphilips@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    hidetsuguueno = addUser("hidetsuguueno", "hidetsuguueno123", "hidetsuguueno@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    tomwalker = addUser("tomwalker", "tomwalker123", "tomwalker@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    theospyropoulos = addUser("theospyropoulos", "theospyropoulos123", "theospyropoulos@cocktailapp.2021259K.gla.ac.uk", False, False, True)
    print "Done adding users!"
    print 
    print
    
    
    #populate userprofiles
    print "Adding user profiles..."
    addUserProfile(admin, "Georgios Kampanos", "Unemployed", "Whiskey Sour", "bartender_images/georgios.jpg")
    addUserProfile(test, "Test User", "Unemployed", "No Fav", "bartender_images/test.png")
    addUserProfile(marianbeke, "Marian Beke", "Nightjar, London", "Unknown", "bartender_images/marianbeke.gif")
    addUserProfile(monicaberg, "Monica Berg", "Pollen Street Social, London", "Uknown", "bartender_images/monicaberg.gif")
    addUserProfile(simonecaporale, "Simone Caporale", "Artesian Bar, London", "Unknown", "bartender_images/simonecaporale.gif")
    addUserProfile(ryanc, "Ryan Chetiyawardana", "White Lyan, London", "Unknown", "bartender_images/ryanc.gif")
    addUserProfile(mariokappes, "Mario Kappes", "Le Lion Bar de Paris, Hamburg", "Unknown", "bartender_images/mariokappes.gif")
    addUserProfile(zdenekkastanek, "Zdenek Kastanek", "28 HongKong Street, Singapore", "Unknown", "bartender_images/zdenekkastanek.gif")
    addUserProfile(timphilips, "Tim Philips", "Bulletin Place, Sydney", "Unknown", "bartender_images/timphilips.gif")
    addUserProfile(hidetsuguueno, "Hidetsugu Ueno", "Bar High Five, Tokyo", "Unknown", "bartender_images/hidetsuguueno.gif")
    addUserProfile(tomwalker, "Tom Walker", "The American Bar at The Savoy, London", "Unknown", "bartender_images/tomwalker.gif")
    addUserProfile(theospyropoulos, "Theo Spyropoulos", "A for Athens, Athens", "Unknown", "bartender_images/theo.jpg")
    print "Done adding user profiles!"
    print 
    print
    
    
    #populate cocktails
    
    print "Adding cocktails..."
    #add all users in one array to randomly select them
    users_array = [marianbeke,monicaberg,simonecaporale,ryanc,mariokappes,mariokappes,zdenekkastanek,timphilips,hidetsuguueno,tomwalker,theospyropoulos]

    addCocktail("Mojito", "cocktail_images/mojito.jpg", rum, "2-3 oz Light rum, Juice of 1 Lime (1 oz), 2 tsp Sugar, 2-4 Mint sprigs, Soda water", "Lightly muddle the mint and sugar with a splash of soda water in a mixing glass until the sugar dissolve and you smell the mint. Squeeze the lime into the glass, add rum and shake with ice. Strain over cracked ice in a highball glass. Top with soda water, garnish with mint sprig and serve.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Jello shots", "cocktail_images/jelloshots.jpg", vodka, "2 cups Vodka, 3 packages Jello with sugar, 3 cups Water", "Boil 3 cups of water then add jello. Mix jello and water until jello is completely disolved. Add the two cups of vodka and mix together. Pour mixture into plastic shot glasses and chill until firm. Then, eat away...", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Long Island Iced Tea", "cocktail_images/longislandicedtea.jpg", gin, "1 part Vodka, 1 part Tequila, 1 part Rum, 1 part Gin, 1 part Triple sec, 1 1/2 part Sour mix, 1 splash Coca-Cola", "Mix ingredients together over ice in a glass. Pour into shaker and give ONE brisk shake. Pour back into glass and make sure there is a touch of fizz at the top. Garnish with lemon.", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Cosmopolitan", "cocktail_images/cosmo.jpg", vodka, "1 oz Vodka, 1/2 oz Triple sec, 1/2 oz Rose's sweetened lime juice, 1/2 oz Cranberry juice, Lime wedge", "Shake liquid ingredients like hell in a shaker with ice. Place lime wedge on the rim of a Martini glass. Pour mix into the glass, up. Enjoy!", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("1-900-FUK-MEUP", "cocktail_images/fukmeup.jpg", tequila, "1/2 oz Absolut Kurant, 1/4 oz Grand Marnier, 1/4 oz Chambord raspberry liqueur, 1/4 oz Midori melon liqueur, 1/4 oz Malibu rum, 1/4 oz Amaretto, 1/2 oz Cranberry juice, 1/4 oz Pineapple juice", "Shake ingredients in a mixing tin filled with ice cubes. Strain into a rocks glass.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Margarita", "cocktail_images/margarita.jpg", whiskey, "1 1/2 oz Tequila, 1/2 oz Triple sec, 1 oz Lime juice, Salt", "Rub rim of cocktail glass with lime juice, dip rim in salt. Shake all ingredients with ice, strain into the salt-rimmed glass, and serve.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("A Piece of Ass", "cocktail_images/apieceofass.jpg", bourbon, "1 shot Amaretto, 1 shot Southern Comfort, Ice cubes, Top off with Sour mix", "Pour liquors over ice in a glass. Fill with sour mix and serve.", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Sangria", "cocktail_images/sangria.jpg", liquor, "1 1/2 L Red wine (Cabernet Sauvignon), 1 cup Sugar, 1 large Lemon, sliced, 1 large Orange, sliced, 1 large Apple, cut into thin sections, 3-4 oz plain Brandy, Soda water", "Mix wine, sugar and fruit, and let sit in the fridge for 18-24 hours. The mixture will have a somewhat syrupy consistency. Before serving stir in brandy and cut the mixture with soda water until it have a thinner, more wine like consistency. Serve from a pitcher in wine glasses.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Amaretto Sour", "cocktail_images/amarettosour.jpg", bourbon, "1 1/2 oz Amaretto, 3 oz Sour mix", "Shake and strain. Garnish with a cherry and an orange slice.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Apple Martini", "cocktail_images/applemartini.jpg", vodka, "1 part Vodka (Absolut), 1 part Sour Apple schnapps (Pucker), 1 part Apple juice", "Poor all ingredients into a shaker. Shake well and strain into a Martini glass.", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("A.M.F.", "cocktail_images/amf.jpg", vodka, "1/2 oz Vodka, 1/2 oz Rum, 1/2 oz Tequila, 1/2 oz Gin, 1/2 oz Blue Curacao, 2 oz Sour mix, 2 oz 7-Up", "Pour all ingredients except the 7-Up into a chilled glass filled with ice cubes. Top with 7-Up and stir gently.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Mai Tai", "cocktail_images/maitai.jpg", rum, "1 oz Light rum, 1/2 oz Orgeat syrup, 1/2 oz Triple sec, 1 1/2 oz Sweet and sour, 1 Cherry", "Shake all ingredients (except cherry) with ice and strain into a collins glass over several ice cubes. Top with the cherry and serve.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Sex on the Beach", "cocktail_images/sexonthebeach.jpg", vodka, "1 oz Vodka, 3/4 oz Peach schnapps Cranberry juice, Grapefruit juice", "Half fill with cranberry juice and grapefruit juice, stir in highball glass.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("White Russian", "cocktail_images/whiterussian.jpg", vodka, "2 oz Vodka, 1 oz Coffee liqueur, Light cream", "Pour vodka and coffee liqueur over ice cubes in an old-fashioned glass. Fill with light cream and serve.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Alabama Slammer", "cocktail_images/alabamaslammer.jpg", gin, "1 oz Southern Comfort, 1 oz Amaretto, 1/2 oz Sloe gin, 1 dash Lemon juice", "Pour all ingredients (except for lemon juice) over ice in a highball glass. Stir, add a dash of lemon juice, and serve.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("B-52", "cocktail_images/b52.jpg", liquor, "1/3 shot Kahlua, 1/3 shot Amaretto, 1/3 shot Bailey's irish cream", "Layer the Kahlua, Amaretto, and Irish Cream into a shot glass in that order. After drinking, notice the Vapor Trails.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Tequila Sunrise", "cocktail_images/tequilasunrise.jpg", tequila, "2 measures Tequila, Orange juice, 2 dashes Grenadine", "Pour tequila in a highball glass with ice, and top with orange juice. Stir. Add grenadine by tilting glass and pouring grenadine down side by flipping the bottle vertically very quickly. The grenadine should go straight to the bottom and then rise up slowly through the drink. Garnish stirrer, straw and cherry-orange.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Blow Job", "cocktail_images/blowjob.jpg", bourbon, "1.5 oz Amaretto Whipping cream", "Pour Amaretto into shot glass, top with whip cream. Drink with hands behind back in one smooth motion", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Screwdriver", "cocktail_images/screwdriver.jpg", vodka, "2 oz Vodka, Orange juice", "Comment", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Martini ", "cocktail_images/martini.jpg", gin, "2 1/2 oz Gin, 1 1/2 tsp Dry Vermouth, 1 twist of Lemon peel", "In a mixing glass half-filled with ice cubes, combine the gin and vermouth. Stir well. Strain into a cocktail glass. Garnish with the lemon twist or an olive.", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Bald P*ssy", "cocktail_images/baldpussy.jpg", vodka, "1 1/2 shot Melon liqueur, 1 shot Lime vodka, 1 shot Absolut Vodka, 1 shot Triple sec, 1 1/2 shot Blueberry schnapps, 1 splash Lime juice, 1 splash 7-Up", "Start at the top and venture your way to the bottom. Pour over ice and shake it on home! Pour in a highball glass and give 2 or 3 big gulps.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Manhattan", "cocktail_images/manhattan.jpg", bourbon, "3/4 oz Sweet Vermouth, 2 1/2 oz Blended Bourbon, dash Angostura bitters, 2 or 3 Ice cubes, 1 Maraschino cherry, 1 twist of Orange peel", "Combine the vermouth, whiskey, bitters and ice in a mixing glass. Stir gently, don't bruise the spirits and cloud the drink. Place the cherry in a chilled cocktail glass and strain the whiskey mixture over the cherry. Rub the cut edge of the orange peel over the rim of the glass and twist it over the drink to release the oils but don't drop it in.", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("After sex", "cocktail_images/aftersex.jpg", vodka, "2 cl Vodka, 1 cl Creme de Banane, Orange juice", "Comment", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Screaming Orgasm", "cocktail_images/screamingorgasm.jpg", vodka, "1 oz Vodka, 1 1/2 oz Bailey's irish cream, 1/2 oz Kahlua", "Pour first vodka, then Bailey's, then Kahlua into a cocktail glass over crushed ice. Stir. Caution: use only high quality vodka. Cheap vodka can cause the Bailey's to curdle. Test your brand of vodka by mixing 1 Tsp each of vodka and Bailey's first.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Absolut Sex", "cocktail_images/absolutsex.jpg", vodka, "3/4 oz Absolut Kurant, 3/4 oz Midori melon liqueur, 1 oz Cranberry juice, 1 splash Sprite or 7-up", "Shake Absolut Kurant, Midori, and Cranberry juice in shaker with ice: Strain into rocks glass: Splash of seven on top.Absolut Sex.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Bloody Mary", "cocktail_images/bloodymary.jpg", vodka, "1 1/2 oz Vodka, 3 oz Tomato juice, 1 dash Lemon juice, 1/2 tsp Worcestershire sauce, 2-3 drops Tabasco sauce, 1 wedge Lime", "Shake all ingredients (except lime wedge) with ice and strain into an old-fashioned glass over ice cubes. Add salt and pepper to taste. Add the wedge of lime and serve.", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Red Headed Slut", "cocktail_images/redheadedslut.jpg", liquor, "1 1/2 oz Jagermeister, 1 1/2 oz Peach schnapps, Fill with Cranberry juice", "This drink has a bit of a kick to it, and the ole' familiar Jagermeister after taste. However, it is a fun drink and after two or three of these you will be good to go. So kick back, enjoy, and remember -- Please don't drink and drive.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Tom Collins", "cocktail_images/tomcollins.jpg", gin, "2 oz Gin, 1 oz Lemon juice, 1 tsp superfine Sugar, 3 oz Club soda, 1 Maraschino cherry, 1 Orange slice", "In a shaker half-filled with ice cubes, combine the gin, lemon juice, and sugar. Shake well. Strain into a collins glass alomst filled with ice cubes. Add the club soda. Stir and garnish with the cherry and the orange slice.", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Chocolate Martini", "cocktail_images/chocolatemartini.jpg", vodka, "2 oz Vodka, 1/2 oz Creme de Cacao", "Pour ingredients into shaker filled with ice then pour into martini glass", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Black Russian", "cocktail_images/blackrussian.jpg", vodka, "3/4 oz Coffee liqueur, 1 1/2 oz Vodka", "Pour ingredients over ice cubes in an old-fashioned glass and serve.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Old Fashioned", "cocktail_images/oldfashioned.jpg", bourbon, "2 ounces bourbon or rye whiskey, 1 teaspoon superfine sugar (or 1 sugar cube), 2-3 dashes of bitters", "Place the sugar in an Old Fashioned glass and douse with the bitters, add a few drops of water, and stir until the sugar is dissolved. Add the whiskey and give a few good stirs to further dissolve the sugar, then add a couple of large ice cubes. Stir a few times to chill, garnish, if you like, with a slice of orange and a cherry, though it is perfectly fine to skip this step. If you are accustomed to topping the drink with soda, at least give it a chance once without, your father brought you up to be open-minded.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Martinez", "cocktail_images/martinez.jpg", whiskey, "1 1/2 ounce Old Tom gin, 1 1/2 ounce sweet vermouth, 1 teaspoon maraschino liqueur, 2 dashes orange bitters, Lemon twist, for garnish", "Comment", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("The Brooklyn", "cocktail_images/thebrooklyn.jpg", whiskey, "2 ounces rye or other whiskey, 1 ounce dry vermouth, 1/4 ounce maraschino liqueur, 1/4 ounce Amer Picon, or a few dashes Angostura or orange bitters", "Combine ingredients with ice and stir until well-chilled. Strain into a chilled cocktail glass.", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Daiquiri", "cocktail_images/daiquiri.jpg", rum, "2 ounces light rum (you can also use gold rum, but dark rum can be too heavy), 3/4 ounce fresh-squeezed lime juice (about 1/2 of a lime), 1 teaspoon sugar", "Pour sugar and lime juice into a cocktail shaker and stir until sugar is dissolved. Add the rum and fill shaker with ice; shake well for 10 seconds and strain into a chilled cocktail glass. Garnish with a wedge of lime.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("French 75", "cocktail_images/french75.jpg", whiskey, "2 ounces gin, 1 ounce freshly squeezed lemon juice, 2 teaspoons sugar, Champagne or sparkling wine, Garnish: long thin lemon spiral and cocktail cherry", "Fill cocktail shaker with ice. Shake gin, lemon juice, and sugar in a cocktail shaker until well chilled, about 15 seconds. Strain into a champagne flute. Top with Champagne. Stir gently, garnish with a long, thin lemon spiral and a cocktail cherry.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Jack Rose", "cocktail_images/jackrose.jpg", liquor, "2 ounces Laird's Applejack, 3/4 ounce grenadine, preferably homemade, 3/4 ounces fresh squeezed juice from 1 lemon, 1 dash Peychaud's bitters, Ice, Lemon twist", "Combine applejack, grenadine, lemon juice, and bitters in a cocktail shaker. Fill shaker with ice and shake vigorously until well chilled, about 15 seconds. Strain into a chilled coupe or martini glass. Squeeze lemon twist over surface of drink, skin-side-out to release fragrant oils. Rub rim of glass with skin side of lemon twist and discard twist. Serve immediately.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Negroni", "cocktail_images/negron.jpg", gin, "1 ounce dry gin, 1 ounce Campari, 1 ounce sweet vermouth", "Combine the ingredients in an old-fashioned glass filled with ice; stir to combine, twist a thin piece of orange peel over the drink for aromatics and use the twist as garnish.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Boulevardier", "cocktail_images/boulevardier.jpg", bourbon, "1 ounce bourbon or rye whiskey, 1 ounce Campari, 1 ounce sweet vermouth, Garnish: orange twist or cherry", "Pour ingredients into a mixing glass and fill with cracked ice. Stir well for 20 seconds and strain into a chilled cocktail glass. Garnish with a cherry or a twist of orange peel.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Mint Julep", "cocktail_images/mintjulep.jpg", bourbon, "2 to 3 ounces bourbon, 1 teaspoon sugar, to taste, dissolved in 1 teaspoon water (or use 2 tsp. simple syrup), 8 to 10 leaves fresh mint, Mint sprigs, for garnish, Crushed ice", "Place the sugar and water at the bottom of a julep cup or tall glass and stir until sugar is dissolved (or speed the process by using simple syrup). Add the mint leaves and gently bruise with a wooden muddler or a wooden spoon. Take care not to overwork the mint,", users_array[randint(0, len(users_array) - 1)], perfect, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Whiskey Sour", "cocktail_images/whiskeysour.jpg", whiskey, "2 ounces whiskey, 1 ounce fresh-squeezed lemon juice, 1 teaspoon sugar, 1 egg white ", "Pour ingredients into a cocktail shaker, fill with ice and shake for 10 seconds (if using the egg white, give it a little extra muscle and a little extra time). Strain into a chilled cocktail glass, or into an ice-filled Old Fashioned glass. Garnish with a cherry, a slice of orange, or everything or nothing at all.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Planter's Punch", "cocktail_images/planterspunch.jpg", rum, "3 ounces Coruba dark Jamaican rum, 1 ounce simple syrup, 3/4 ounce fresh lime juice, 3 dashes Angostura bitters", "Combine ingredients in a tall glass and fill with crushed ice. Swizzle with a bar spoon until a frost forms on the outside of the glass. The ice will settle as you do this; add more crushed ice to fill, garnish with a mint sprig.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Pegu Club", "cocktail_images/peguclub.jpg", gin, "2 ounces gin, 3/4 ounce lime juice, 3/4 ounce curacao, 1 dash Angostura bitters, 1 dash orange bitters", "Combine ingredients in a cocktail shaker, and fill with ice. Shake well, and strain into a chilled cocktail glass.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Corpse Reviser", "cocktail_images/corpsereviser.jpg", gin, "1 ounce gin, 1 ounce Lillet, 1 ounce fresh lemon juice, 1 ounce Cointreau, 1 drop absinthe or pastis", "Add all ingredients to a cocktail shaker; fill with ice and shake well. Strain into a chilled cocktail glass. Garnish with a cherry.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Improved", "cocktail_images/improved.jpg", gin, "2 ounces genever, 1/2 teaspoon simple syrup (see note above), 1 teaspoon Cointreau (or maraschino liqueur), 2 dashes Angostura bitters, Lemon peel", "Combine genever, simple syrup, Cointreau (or maraschino), and bitters in a mixing glass and fill with ice. Stir well to chill, about 15 seconds. Strain into a chilled cocktail glass. Twist a piece of lemon peel over the drink and rub around the rim of the glass.", users_array[randint(0, len(users_array) - 1)], sweet, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Caipirinha", "cocktail_images/caipirinha.jpg", rum, "2 ounces cachaca, 1/2 of a fresh lime, cut into quarters, 1 to 2 teaspoon superfine sugar, to taste", "Place the lime pieces and sugar in the cocktail shaker and crush with the muddler. Add cachaca and a handful of ice; shake well and pour, unstrained, into a rocks or old fashioned glass.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    addCocktail("Zombie", "cocktail_images/zombie.jpg", rum, "1 oz. apricot brandy, 1 oz. light rum, 1 oz. dark or Jamaican rum, 1 oz. lime juice, 2 dashes grenadine, Orange juice, 1 oz. Bacardi 151 rum", "Mix light and dark rum and brandy in a cocktail shaker, add lime juice and grenadine. Shake well and strain into a higball glass filled with cracked ice. Fill glass with orange juice but leave enough room to float the 151 on top. Garnish with a cherry and orange slice.", users_array[randint(0, len(users_array) - 1)], sour, randint(0, 1000), "", randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
    print "Done adding cocktails!"
    print 
    print



if __name__ == '__main__':
    print "Starting Cocktail population script..."
    populate()
