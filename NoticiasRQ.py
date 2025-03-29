import requests
from bs4 import BeautifulSoup
import feedparser

def get_news(city=None):
    #Obtém 10 notícias: 7 gerais e pelo menos 3 sobre uma cidade específica (se fornecida).
    
    # URL para notícias gerais
    url_general = "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419"
    feed_general = feedparser.parse(url_general)
    news_list = [entry.title for entry in feed_general.entries[:7]]  # Pegamos 7 notícias gerais

    # Se uma cidade foi especificada, adicionamos 3 notícias sobre ela
    if city:
        url_city = f"https://news.google.com/rss/search?q={city.replace(' ', '+')}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
        feed_city = feedparser.parse(url_city)
        city_news = [entry.title for entry in feed_city.entries[:5]]  # Tentamos pegar até 5 notícias da cidade
        
        # Garante que tenha pelo menos 3 notícias sobre a cidade
        while len(city_news) < 3:
            city_news.append(f"Nenhuma notícia relevante encontrada sobre {city}")

        news_list.extend(city_news[:3])  # Adicionamos exatamente 3 notícias da cidade

    return print(news_list)  # Retorna todas as notícias

get_news("Cabo Frio")  # Obtém 7 gerais + 3 sobre a cidade selecionada