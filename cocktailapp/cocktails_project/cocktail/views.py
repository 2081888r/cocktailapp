from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from cocktail.forms import UserForm, UserProfileForm, CocktailForm, CocktailSearch
from django.contrib.auth.models import User
from cocktail.models import UserProfile, Cocktail, BartenderRatesCocktail

#Extra/helper functions here!

def getUserCocktails(request, username):
    user = User.objects.get(username = username)
    cocktails = Cocktail.objects.filter(bartender = user.id)    #get the cocktails for the profile we visit
    return cocktails

def getMostRecentUsers(request):
    users = User.objects.all().order_by('-id')[:3]
    profiles = UserProfile.objects.all().order_by('-user_id')[:3]
    return zip(users, profiles)

def getMostViewedCocktails(request):
    return Cocktail.objects.all().order_by('-views')[:3]

def isCocktailRatedByBartender(cocktail, bartender):
    try:
        liked = BartenderRatesCocktail.objects.get(bartender = bartender, cocktail = cocktail)
        if liked is not None:
            print str(bartender.username) + ' has rated ' + str(cocktail.name) 
            return True
    except BartenderRatesCocktail.DoesNotExist as u:
        print str(bartender.username) + ' has not rated ' + str(cocktail.name)
        return False
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        

def bartenderRatedCocktail(cocktail, bartender):
    if isCocktailRatedByBartender(cocktail, bartender):
        print "No need to add " + str(bartender.username) + " to database for " + str(cocktail.name)
    else:
        print "here..."
        liked = BartenderRatesCocktail.objects.get_or_create(bartender = bartender, cocktail = cocktail)
        print str(bartender.username) + " has been added to the database as he/she rated " + str(cocktail.name)
        
def getCocktailTotalVotes(cocktail):
    return (int(cocktail.five_stars) + int(cocktail.four_stars) + int(cocktail.three_stars) 
                + int(cocktail.two_stars) + int(cocktail.one_star)) 

def getCocktailAvgRating(cocktail):
    total_votes = getCocktailTotalVotes(cocktail)
    if total_votes > 0:
        print "hey"
        return (cocktail.one_star + cocktail.two_stars * 2 + cocktail.three_stars * 3 + cocktail.four_stars * 4 + cocktail.five_stars * 5) / total_votes
    return 0

def updateCocktailViews(cocktail):
    views = cocktail.views  #increment cocktail views
    views += 1
    cocktail.views = views
    cocktail.save()    
    

@login_required
def updateCocktailRating(request):
    if request.method == 'POST':
        print 'Start updating cocktail rating...'
        cocktail = Cocktail.objects.get(slug = request.POST.get('cocktail'))
        rating = int(request.POST.get('rating'))
        user = User.objects.get(id = request.POST.get('user'))
        
        if isCocktailRatedByBartender(cocktail, user):
            print str(user.username) + " has already rated " + str(cocktail)
            message = str(user.username) + " has already rated " + str(cocktail)
        else:
            if rating == 5:
                cocktail.five_stars += 1
            elif rating == 4:
                cocktail.five_stars += 1
            elif rating == 3:
                cocktail.three_stars += 1
            elif rating == 2:
                cocktail.two_stars += 1
            else:
                cocktail.one_star += 1
                
            cocktail.save()
            bartenderRatedCocktail(cocktail, user)
            print "The user " + str(user.username) + " gave rating " + str(rating) + " to " + str(cocktail.name)
            message = "The user " + str(user.username) + " gave rating " + str(rating) + " to " + str(cocktail.name)
    return HttpResponse(message)


# Create your views here.

def index(request):
    return render(request,'cocktails/index.html', {'bartenders': getMostRecentUsers(request), 'cocktails': getMostViewedCocktails(request)})

def cocktails(request):
    if request.method == 'POST':
        form = CocktailSearch(request.POST)
        if form.is_valid():
            qName = form.cleaned_data['name']
            qBase = form.cleaned_data['base']
            qTaste = form.cleaned_data['taste_palette']
            
            if qTaste is not None and qName is not None and qBase is not None:
                print "Search by All"
                cocktails = Cocktail.objects.all().filter(name__contains = qName, base = qBase, taste_palette = qTaste)
            elif qName is not None and qBase is not None:
                cocktails = Cocktail.objects.all().filter(name__contains = qName, base = qBase)
            elif qName is not None and qTaste is not None:
                cocktails = Cocktail.objects.all().filter(name__contains = qName, taste_palette = qTaste)
            elif qBase is not None and qTaste is not None:
                cocktails = Cocktail.objects.all().filter(base = qBase, taste_palette = qTaste)
            elif qName is not None and qTaste is None and qBase is None:
                cocktails = Cocktail.objects.all().filter(name__contains = qName)
            else:   #if they give all the fields as None
                cocktails = Cocktail.objects.all()
                
            cocktails.order_by('name')  #sort the cocktails based on their name
            
        else:
            print form.errors
        
    else:
        form = CocktailSearch()
        cocktails = Cocktail.objects.all().order_by('name')
        
    return render(request,'cocktails/cocktails.html', {'cocktails': cocktails, 'form': form})

def cocktails_single(request, cocktail_slug):
    
    try: 
        cocktail = Cocktail.objects.get(slug = cocktail_slug)
        bartender = User.objects.get(username = cocktail.bartender)
        profile = UserProfile.objects.get(user_id = bartender.id)
        
        updateCocktailViews(cocktail)
        #variable that "locks" or unlocks the rating system for the logged in user
        if isCocktailRatedByBartender(cocktail, request.user): 
            readonly = "readonly" 
        else: readonly = ""
        
        return render(request, 'cocktails/cocktails_single.html', {'cocktail': cocktail, 'bartender': bartender, 
                                                                   'profile': profile, 
                                                                   'readonly': readonly,
                                                                   'rating': getCocktailAvgRating(cocktail), 
                                                                   'total_votes': getCocktailTotalVotes(cocktail)})
    except Cocktail.DoesNotExist as c:
        print '%s (%s)' % (c.message, type(c))
        return HttpResponseRedirect('/cocktail/404/')  #if cocktail doesn't exist
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return HttpResponseRedirect('/cocktail/404/')  #catch all the exceptions
        
    
    return render(request,'cocktails/cocktails_single.html', {})

@login_required
def cocktails_add(request):
    if request.method == 'POST':
        cocktail_form = CocktailForm(request.POST, request.FILES) #get the data and the files from the form
        
        if cocktail_form.is_valid():
            form = cocktail_form.save(commit=False)
            form.bartender = request.user     #get the user we want to update the profile
            form.save()  #save the profile
            return HttpResponseRedirect('/cocktail/profile/' + request.user.username)  #redirect to the homepage
        else:
            print cocktail_form.errors   
    else:
        cocktail_form = UserProfileForm()

    return render(request,'cocktails/cocktails_add.html', {'cocktail_form': cocktail_form})

@login_required
def cocktails_edit(request, cocktail_slug):
    cocktail = Cocktail.objects.get(slug = cocktail_slug)
    if request.method == 'POST':
        form = CocktailForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['image'] is not None: 
                cocktail.image = form.cleaned_data['image']
            cocktail.name = form.cleaned_data['name']
            cocktail.base = form.cleaned_data['base']
            cocktail.how_to_make_comment = form.cleaned_data['how_to_make_comment']
            cocktail.ingredients = form.cleaned_data['ingredients']
            cocktail.taste_palette = form.cleaned_data['taste_palette']
            cocktail.save()
            return HttpResponseRedirect('/cocktail/cocktails/' + cocktail.slug)
        else:
            print form.errors
    else:
        form = CocktailForm()
        
    return render(request, 'cocktails/cocktails_edit.html', {'cocktail': cocktail, 'form': form})

def bartenders(request):
    return render(request,'cocktails/bartenders.html', {'bartenders':zip(User.objects.all(), UserProfile.objects.all())})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/cocktail/')
            else:
                return HttpResponse("Your Cocktail account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'registration/login.html', {})
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/cocktail/')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request, 'registration/registration_form.html', {'user_form': user_form, 'registered': registered} )
    
@login_required
def register_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES) #get the data and the files from the form
        
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user     #get the user we want to update the profile
            profile.save()  #save the profile
            return HttpResponseRedirect('/cocktail/')  #redirect to the homepage
        else:
            print profile_form.errors   
    else:
        profile_form = UserProfileForm()
    
    return render(request,"profiles/profile_update.html", {'profile_form': profile_form, 'user_name': request.user})


def profile(request, username):
    try:
        user = User.objects.get(username = username)
        profile = UserProfile.objects.get(user_id = user.id)
        cocktails = getUserCocktails(request, username)
        return render(request,"profiles/profile.html", {'bartender': user, 'profile': profile, 'cocktails': cocktails})
    except User.DoesNotExist as u:
        print '%s (%s)' % (u.message, type(u))
        return HttpResponseRedirect('/cocktail/404/')  #if user doesn't exist
    except Exception as e:
        print '%s (%s)' % (e.message, type(e))
        return HttpResponseRedirect('/cocktail/404/')  #catch all the exceptions
    
@login_required
def profile_update(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = UserProfile.objects.get(user_id = request.user.id)
            profile_form_data = profile_form.cleaned_data
            profile_new_avatar = profile_form_data['avatar']
            profile_new_full_name = profile_form_data['full_name']
            profile_new_fav_cocktail = profile_form_data['fav_cocktail']
            profile_new_workplace = profile_form_data['workplace']
            if profile_new_avatar is not None: 
                profile.avatar = profile_new_avatar
            if len(profile_new_full_name) > 0: 
                profile.full_name = profile_new_full_name
                print profile_new_full_name
            if len(profile_new_fav_cocktail) > 0: 
                profile.fav_cocktail = profile_new_fav_cocktail
                print profile_new_fav_cocktail
            if len(profile_new_workplace) > 0: 
                profile.workplace = profile_new_workplace
                print profile_new_workplace
            profile.save()
            url = '/cocktail/profile/'+str(request.user.username)
            return HttpResponseRedirect(url)  #redirect to the profile
        else:
            print profile_form.errors
#             
    else:
        profile_form = UserProfileForm()
    
    return render(request,"profiles/profile_update.html", {'profile_form': profile_form, 'user_name': request.user})
    
    
def error_page(request):
    return render(request, 'cocktails/404.html')
