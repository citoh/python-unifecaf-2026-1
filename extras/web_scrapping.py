# INSTALANDO A APLICAÇÃO:
# python3 -m venv venv
# source venv/bin/activate
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup


# CLASSES -----------------------------------------------
class Noticia:
    def __init__(self, titulo, link):
        self.titulo = titulo
        self.link = link

    def __repr__(self):
        return f"Noticia(titulo={self.titulo!r}, link={self.link!r})"


# FUNÇÕES E VARIÁVEIS ------------------------------------
def getNoticias(busca=None):
    url = "https://www.r7.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    html = BeautifulSoup(response.text, "html.parser")
    noticias = []

    artigos = html.select('article[data-tb-region-item="true"]')

    for artigo in artigos:
        a_tag = artigo.select_one('h3[data-tb-title="true"] a')

        if a_tag and a_tag.has_attr("href"):
            titulo = a_tag.get_text(strip=True)
            link = a_tag["href"].strip()

            if titulo:
                if busca is None or busca.lower() in titulo.lower():
                    noticias.append(Noticia(titulo, link))

    return noticias


#noticias = getNoticias("brasil") #é possível buscar por uma palavra ou termo
noticias = getNoticias()
print("Títulos encontrados:\n")

for i, noticia in enumerate(noticias, 1):
    print(f"{i:02d}. {noticia.titulo}")
    print(f"{noticia.link}\n")