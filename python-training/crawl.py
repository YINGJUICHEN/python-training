import requests
from bs4 import BeautifulSoup

def crawl_ptt_movie(url):
    # 設定 User-Agent，避免被伺服器擋下
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    # 發送 GET 請求
    response = requests.get(url, headers=headers)
    
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找出文章標題和連結
    articles = soup.find_all('div', class_='title')
    for article in articles:
        # 抓取文章標題
        title = article.text.strip()
        # 抓取文章連結
        link = 'https://www.ptt.cc' + article.a['href']
        print(title)
        print(link)
        print()

if __name__ == "__main__":
    # PTT 電影版的 URL
    url = "https://www.ptt.cc/bbs/movie/index.html"
    crawl_ptt_movie(url)
