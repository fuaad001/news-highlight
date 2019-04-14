from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources, view_source, get_by_category, get_by_language, get_top_headlines

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to best News Website Online'

    sort_type = request.args.get('sortBy_query')

    news_sources = get_sources()
    top_headlines = get_top_headlines()

    Categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    NewCategories = []
    for Category in Categories:
        cat = get_by_category(Category)
        NewCategories.append(cat)

    Languages = ['en', 'ar', 'de', 'es', 'fr', 'he', 'it', 'nl', 'no', 'pt', 'ru', 'se', 'ud', 'zh']
    NewLanguages = []
    for Language in Languages:
        lan = get_by_language(Language)
        NewLanguages.append(lan)

    return render_template('index.html', sources = news_sources, title = title, Categories = NewCategories, Languages = NewLanguages, sort_type = sort_type, headlines = top_headlines)

@main.route('/source/<id>')
def source(id):
    news_articles = view_source(id)
    title = id

    return render_template('source.html', title = title, news = news_articles)
