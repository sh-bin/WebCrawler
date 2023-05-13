from django.shortcuts import render
from . import forms
import requests
from bs4 import BeautifulSoup
import re


regex_expression = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'


def main(request):
    form = forms.UrlForm(request.GET)

    if form.is_valid() and re.match(regex_expression, form.cleaned_data['url']):
        urls = []
        html_page = requests.get(form.cleaned_data['url'])
        html_page_string = BeautifulSoup(html_page.text, 'html.parser')
        for i in html_page_string.find_all('a'):
            if re.match(regex_expression, str(i.get('href'))):
                urls.append(i.get('href'))

    else:
        urls = []

    context = {
        'form': form,
        'urls': urls,
    }
    return render(request, 'MainApp/WebCrawler.html', context=context)
