from bs4 import BeautifulSoup
import json

with open('minjust.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
parties = []

section = soup.find('div', id='section-765')
if section:
    for li in section.find_all('li'):
        a_tag = li.find('a')
        if a_tag:
            name = a_tag.get_text(separator=' ', strip=True)
            name = ' '.join(name.split())
            
            doc_url = a_tag.get('href')
            if doc_url:
                if doc_url.startswith('/'):
                    doc_url = 'https://minjust.gov.ru' + doc_url
                if doc_url.startswith('http://'):
                    doc_url = doc_url.replace('http://', 'https://')
            parties.append({"name": name, "doc_url": doc_url})

with open('parties.json', 'w', encoding='utf-8') as json_file:
    json.dump(parties, json_file, ensure_ascii=False, indent=2)

print(json.dumps(parties, ensure_ascii=False, indent=2))
print("\nДанные сохранены в файл 'parties.json'")
