import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from datetime import datetime

openai_api_key = os.environ.get("OPENAI_API_KEY")
slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

client = OpenAI(api_key=openai_api_key)

def get_news_from_rss():
    url = "https://www.artificialintelligence-news.com/feed/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")
    
    website_title = soup.find("title").text.strip()
    print(f"サイトタイトル: {website_title}")
    
    articles = []
    article_elements = soup.find_all("item")
    print(f"記事要素数: {len(article_elements)}")
    
    for article_element in article_elements:
        title = article_element.find("title").text.strip()
        link = article_element.find("link").text.strip()
        description = article_element.find("description").text.strip()
        pub_date_str = article_element.find("pubDate").text.strip()
        pub_date = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")
        articles.append({"title": title, "link": link, "description": description, "pub_date": pub_date})
    
    return website_title, articles

def summarize_article(article_description):
    prompt = f"あなたは記事要約のプロです。以下のニュース記事のhrefリンクを確認してFormatに従い要約してください。要約は要点を3〜5個に整理してください。文書は日本語で要約してください。:\n\n<Format>\n1. *要約見出し1*:要約ポイント1つ目。\n1. *要約見出し2*:要約ポイント2つ目。\n1. *要約見出し3*:要約ポイント3つ目。\n\n{article_description}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = response.choices[0].message.content.strip()
    return summary

def send_slack_notification(website_title, article_title, article_link, pub_date, summary):
    message = f"記事タイトル: {article_title}\nリンク: {article_link}\n発行日: {pub_date}\n要約: \n{summary}"
    payload = {
        "text": message
    }
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code != 200:
        print("Slackへの通知が失敗しました")

def news_summary(event,context):
    website_title, articles = get_news_from_rss()
    for article in articles:
        article_title = article["title"]
        article_link = article["link"]
        article_description = article["description"]
        article_pub_date = article["pub_date"]
        summary = summarize_article(article_description)
        send_slack_notification(website_title, article_title, article_link, article_pub_date, summary)
    
    return 'OK'