from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
            """
            Connection terminated.
            I'm sorry to interrupt you, Elizabeth. If you still even remember that name.
            But I'm afraid you've been misinformed.
            """)
