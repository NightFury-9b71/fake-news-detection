from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import news
from .forms import newsForm
import requests
from django.template import loader

# Create your views here.

API_KEY = "AIzaSyBUSVTIaVVuyU8TYl289PVZxM1lcRpstZo"
SEARCH_ENGINE_ID = "1393ff14496044d63"


def getNews(query: str,params: dict) -> list:
    news_items = []
    for page in range(1, 11):
        res = requests.get(query, params=params)
        if res.status_code == 200:
            res = res.json()
            items = res.get('items', [])

            for item in items:
                site_name = item['pagemap']['metatags'][0].get('og:site_name', 'N/A')
                title = item['title']
                snippet = item['snippet']
                link = item['link']
                news_items.append({
                    'site_name': site_name,
                    'title': title,
                    'snippet': snippet,
                    'link': link
                })

            params['start'] += 10  # Increment by 10 for the next page
        else:
            break
    return news_items



def getScrap(request):
    if requests.models == 'POST':
        form = newsForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']

            params = {
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID,
                'q': query,
                'num': 10,
                'start': 1
            }

            news_items = getNews(query,params)
            for item in news_items:
                news.objects.create(
                    site_name=item['site_name'],
                    title=item['title'],
                    snippet=item['snippet'],
                    link=item['link']
                )
            return redirect('news_success')
    else:
        form = newsForm()
        
    
    template = loader.get_template('checker.html')
    context = { 'form': form}
    return HttpResponse(template.render(context,request))

def news_success(request):
    return HttpResponse("News items have been successfully fetched and stored in the database.")
