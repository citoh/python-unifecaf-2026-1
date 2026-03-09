# INSTALANDO A APLICAÇÃO:
# python3 -m venv venv
# source venv/bin/activate
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# CLASSES -----------------------------------------------
class Noticia:
    def __init__(self, titulo, link):
        self.titulo = titulo
        self.link = link

    def __str__(self):
        return f"{self.titulo}\n{self.link}"


# FUNÇÕES E VARIÁVEIS ------------------------------------
def getNoticias(busca=None):
    url = "https://www.r7.com/"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return []

    html = BeautifulSoup(response.text, "html.parser")
    noticias = []
    vistos = set()

    for a_tag in html.find_all("a", href=True):
        titulo = a_tag.get_text(strip=True)
        link = urljoin(url, a_tag["href"])

        if not titulo:
            continue

        if busca is None or busca.lower() in titulo.lower():
            chave = (titulo, link)
            if chave not in vistos:
                vistos.add(chave)
                noticias.append(Noticia(titulo, link))

    return noticias


# PROGRAMA PRINCIPAL ------------------------------------
noticias = getNoticias("brasil")

print("Títulos encontrados:\n")

if noticias:
    for i, noticia in enumerate(noticias, 1):
        print(f"{i:02d}. {noticia.titulo}")
        print(f"{noticia.link}\n")
else:
    print("Nenhuma notícia encontrada.")