from annoying.decorators import render_to

@render_to('hero.html')
def home(request):
    return {}