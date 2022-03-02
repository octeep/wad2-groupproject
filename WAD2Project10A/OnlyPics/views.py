from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from OnlyPics.models import UserInfo, Picture
from OnlyPics.hcaptcha import verify_hcaptcha_request

#to be used in the template
def get_comments_according_to_picture(picture):
    comments = Comment.objects.filter(picture=picture)
    return comments

def index(request):
    # top_five_most_liked_pictures = Picture.objects.order_by('-likes')[:5]
    # context_dic = {}
    # context_dic['pics'] = top_five_most_liked_pictures
    # return render(request, 'onlypics/index.html', context=context_dic)
    return HttpResponse(
            """
            Connection terminated.
            I'm sorry to interrupt you, Elizabeth. If you still even remember that name.
            But I'm afraid you've been misinformed.
            """)

def explore(request):
    picture_list = Picture.objects.order_by('-likes')
    categories = Category.objects.all()


    context_dic = {}
    context_dic['pictures'] = picture_list
    context_dic['categories'] = categories

@login_required
def post_for_sale(request):
    return HttpResponse("Not yet implemented!")
    #form = PostForSaleForm()
    #if request.method == 'POST':
        #form = PostForSaleForm(request.POST)
        #if form.is_valid():
            #form.save(commit=True)
            #return redirect('/onlypics/')
        #else
            #print(form.errors)

     #return render(request, 'onlypics/post_for_sale.html', {'form':form}

@login_required
def profile(request):
    user = request.user
    pictures = Picture.objects.filter(user = user)

@login_required
def add_tokens(request):
    return HttpResponse("Not yet implemented!")

def whoami(request):
    if not request.user.is_authenticated:
        return HttpResponse(f"You are not logged in")
    user = request.user
    try:
        user_info = UserInfo.objects.get_or_create(user=user, tokens=50)[0]
        return HttpResponse(f"You are {user_info.nickname}")
    except UserInfo.DoesNotExist:
        return HttpResponse("You are logged in but there's no profile of you")


# hCaptcha testing
def vbucks(request):
    if request.method == 'POST':
        verify_hcaptcha_request(request)
        return HttpResponse("let it out")
    else:
        return render(request, 'onlypics/vbucks.html')

@login_required
def edit_profile(request):
    return HttpResponse("Joke")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("You have logged out.")
    else:
        return HttpResponse("You have already logged out.")