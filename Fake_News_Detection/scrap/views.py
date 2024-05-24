from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import news
from .forms import newsForm
import requests
from django.template import loader
import os

API_KEY=os.getenv('API_KEY')
SEARCH_ENGINE_ID=os.getenv('SEARCH_ENGINE_ID')
URL=os.getenv('URL')


def getNews(params):
    news_items = []
    for page in range(1, 11):
        res = requests.get(URL,params=params)
        if res.status_code == 200:
            res = res.json()
            items = res['items']

            for item in items:
                site_name = item['pagemap']['metatags'][0]['og:site_name']
                title = item['title']
                snippet = item['snippet']
                link = item['link']
                news_items.append({
                    'site_name': site_name,
                    'title': title,
                    'snippet': snippet,
                    'link': link
                })

            params['start'] += 1
        else:
            break
    return news_items

def getScrap(request):
    if request.method == 'POST':  # Correcting the condition for POST method
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

            news_items = getNews(params)
            for item in news_items:
                news.objects.create(
                    site_name=item['site_name'],
                    title=item['title'],
                    snippet=item['snippet'],
                    link=item['link']
                )

            return redirect('showNews')
    else:
        form = newsForm()


    template = loader.get_template('checker.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def delete(request):
    news.objects.all().delete()
    return HttpResponse("Deleted Successfully")

def showNews(request):
    news_items = news.objects.all()
    news_text = "\n".join([f"{item.title} - {item.site_name}\n{item.snippet}\n{item.link}\n" for item in news_items])
    template = loader.get_template('checker.html')
    context = {'news_text': news_text}
    return HttpResponse(template.render(context, request))
