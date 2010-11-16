from __future__ import absolute_import
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from .models import *
from .forms import *
from .utils import *
from ncfmusic.apps.heroshots.models import *

def home(request):
    listen = Listen.objects.order_by('-insert_date')[:3]
    watch = Watch.objects.order_by('-insert_date')[:1]
    learn = Tutorial.objects.order_by('-insert_date')[:2]
    
    heroshots = Category.objects.filter(slug='homepage')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
            
    else:
        form = ContactForm()
    
    context = RequestContext(request, {
        'listen': listen,
        'watch': watch,
        'learn': learn,
        'form': form,
        'heroshots': heroshots
    })
    
    return render_to_response('homepage.html', context)
    
def about(request):
    page = get_object_or_404(Page, slug__exact='about')
    church = get_object_or_404(Church, name='New City Fellowship Glenwood')
    #   Maybe it would be easier to hard code this into the template?
    contact = get_object_or_404(Contact, church=church, first_name='James', last_name='Ward')
    
    context = RequestContext(request, {
        'page': page,
        'contact': contact
    })
    
def listen(request):
    page = get_object_or_404(Page, slug__exact='listen')
    listen_list = Listen.objects.order_by('-insert_date')
    
    paginator = Paginator(listen_list, 5)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        listens = paginator.page(page)
    except (EmptyPage, InvalidPage):
        listens = paginator.page(paginator.num_pages)
        
    context = RequestContext(request, {
        'page': page,
        'listens': listens
    })
    
    return render_to_response('about.html', context)
    
def watch(request):
    page = get_object_or_404(Page, slug__exact='watch')
    watch_list = Watch.objects.order_by('-insert_date')
    
    paginator = Paginator(watch_list, 5)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        watchs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        watchs = paginator.page(paginator.num_pages)
        
    context = RequestContext(request, {
        'page': page,
        'watchs': watchs
    })
    
    return render_to_response('watch.html', context)
    
def tutorials(requset):
    page = get_object_or_404(Page, slug__exact='tutorials')
    tutorial_list = Tutorial.objects.order_by('-insert_date')
    
    paginator = Paginator(tutorial_list, 3)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        tutorials = paginator.page(page)
    except (EmptyPage, InvalidPage):
        tutorials = paginator.page(paginator.num_pages)
        
    context = RequestContext(request, {
        'page': page,
        'tutorials': tutorials,
        'tutorial_list': tutorial_list[:5], #   For the sidebar
    })
    
    return render_to_response('tutorials.html', context)
    
def tutorial(request, slug):
    page = get_object_or_404(Page, slug__exact='tutorials')
    tutorial = get_object_or_404(Tutorial, slug__exact=slug)
    
    context = RequestContext(request, {
        'page': page,
        'tutorial': tutorial,
    })
    
    return render_to_response('tutorial.html', context)
    
def talks(request):
    page = get_object_or_404(Page, slug__exact='talks')
    talk_list = Talk.objects.order_by('-insert_date')
    
    paginator = Paginator(talk_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        talks = paginator.page(page)
    except (EmptyPage, InvalidPage):
        talks = paginator.page(paginator.num_pages)
        
    context = RequestContext(request, {
        'page': page,
        'talks': talks,
        'talk_list': talk_list[:5], #   For the sidebar
    })
    
    return render_to_response('talks.html', context)
    
def articles(request):
    page = get_object_or_404(Page, slug__exact='articles')
    article_list = Article.objects.order_by('-insert_date')
    
    paginator = Paginator(article_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        articles = paginator.page(page)
    except (EmptyPage, InvalidPage):
        articles = paginator.page(paginator.num_pages)
        
    context = RequestContext(request, {
        'page': page,
        'articles': articles,
        'article_list': article_list[:5], #   For the sidebar
    })
    
    return render_to_response('articles.html', context)
    
def article(request, slug):
    page = get_object_or_404(Page, slug__exact='articles')
    article = get_object_or_404(Article, slug__exact=slug)
    
    context = RequestContext(request, {
        'page': page,
        'article': article,
    })
    
    return render_to_response('article.html', context)
    
def songs(request, start_letter=None):
    page = get_object_or_404(Page, slug__exact='songs')
    
    song_list = Song.objects.order_by('title')
    
    #   I'm sure there's a better way to do this, but it's late and my brain's tired, so this will work
    sections = {}
    for letter in map(chr, range(65, 91)):
        sections[letter] = song_list.filter(title__startswith=letter)
    
    if start_letter:
        song_list = sections[start_letter]
        
    paginator = Paginator(song_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        songs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        songs = paginator.page(paginator.num_pages)

    context = RequestContext(request, {
        'page': page,
        'songs': songs,
        'sections': sections,
        'start_letter': start_letter
    })
    
    return render_to_response('songs.html', context)
    
def events(request, month=None, year=None):
    import datetime
    
    page = get_object_or_404(Page, slug__exact='events')
    
    events_list = Event.objects.order_by('start_date')
    
    #   I'm sure there's a better way to do this, but it's late and my brain's tired, so this will work
    months = {}
    first = events_list.order_by('start_date')[0]
    last = events_list.order_by('-start_date')[0]
    
    thisdate = datetime.date(first.year, first.month, 1)
    while thisdate <= last:
        months[thisdate] = events_list.filter(start_date__month=thisdate.month, start_date__year=thisdate.year)
        if thisdate.month == 12:
            thisdate = datetime.date(thisdate.year+1, 1, 1)
        else:
            thisdate = datetime.date(thisdate.year, thisdate.month+1, 1)
    
    if month and year:
        events_list = months[datetime.date(year,month,1)]
        
    paginator = Paginator(events_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        events = paginator.page(page)
    except (EmptyPage, InvalidPage):
        events = paginator.page(paginator.num_pages)

    context = RequestContext(request, {
        'page': page,
        'events': events,
        'months': months,
        'month': month,
        'year': year,
    })
    
    return render_to_response('events.html', context)
    
def event(request, slug):
    page = get_object_or_404(Page, slug__exact='events')
    event = get_object_or_404(Event, slug__exact=slug)
    
    context = RequestContext(request, {
        'page': page,
        'event': event,
    })
    
    return render_to_response('event.html', context)
    
def churches(request):
    page = get_object_or_404(Page, slug__exact='contributors')
    
    church_list = Church.objects.order_by('name')
    
    context = RequestContext(request, {
        'page': page,
        'church_list': church_list,
    })
    
    return render_to_response('churches.html', context)
    
def musicians(request):
    page = get_object_or_404(Page, slug__exact='contributors')
    
    musician_list = Contributors.objects.order_by('name')
    
    context = RequestContext(request, {
        'page': page,
        'musician_list': musician_list,
    })
    
    return render_to_response('musicians.html', context)
    
    