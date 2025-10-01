import requests
from bs4 import BeautifulSoup


# --- Parte 1: Análise HTML (Web Scraping) ---

def baixar_conteudo(url):
    """Faz a requisição HTTP e retorna o conteúdo HTML."""
    try:
        print(f"Baixando conteúdo de: {url}")
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"ERRO ao acessar a URL: {e}")
        return None


def analisar_html(html_content):
    """Analisa o HTML e extrai títulos e links principais."""
    if not html_content:
        return

    # Cria o objeto Beautiful Soup (árvore de análise)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Objetivo 1: Encontrar o Título Principal da Página
    # O título principal (tag <h1>) neste site de teste é o nome do site
    titulo_principal = soup.find('h1')
    if titulo_principal:
        print(f"✅ Título da Página: {titulo_principal.text.strip()}")
    else:
        print("❌ Título <h1> não encontrado.")

    print("\n--- Todos os Links na Página ---")

    # OBJETIVO 2: EXTRAÇÃO MELHORADA
    # Encontra e Extrai TODOS os links (tags <a>) da página
    links_encontrados = 0

    for link_tag in soup.find_all('a'):
        href = link_tag.get('href')  # Pega o atributo de destino
        texto = link_tag.text.strip()  # Pega o texto visível

        # Filtra links que têm um destino e algum texto visível
        if href and texto and not href.startswith('#'):
            # Imprime formatado (texto com 30 espaços, link com 60)
            print(f"-> {texto[:30]:<30} | {href[:60]}")
            links_encontrados += 1

    print(f"\nTotal de links válidos extraídos: {links_encontrados}")


# --- Parte 2: Demonstração XML (Bônus, já estava funcionando) ---

def analisar_xml(xml_content):
    """Demonstra a análise de um trecho de XML."""
    print("\n--- Demonstração XML (Busca por Livros) ---")

    # O parser 'xml' está funcionando após a instalação do lxml
    soup_xml = BeautifulSoup(xml_content, 'xml')

    livros = soup_xml.find_all('book')

    if livros:
        for livro in livros:
            titulo = livro.find('title').text
            autor = livro.find('author').text
            ano = livro.get('year')

            print(f"Livro: {titulo} | Autor: {autor} | Ano: {ano}")
    else:
        print("Nenhum elemento <book> encontrado.")


# ------------------------------------
# EXECUÇÃO PRINCIPAL
# ------------------------------------

if __name__ == "__main__":
    # NOVA URL de teste: site de scraping com estrutura mais clara
    URL_ALVO = "http://quotes.toscrape.com/"

    html_principal = baixar_conteudo(URL_ALVO)
    analisar_html(html_principal)

    # Trecho de XML para demonstração
    xml_dados = """
    <catalog>
      <book year="2005">
        <title>Python for Devs</title>
        <author>Guido van Rossum</author>
      </book>
      <book year="2018">
        <title>Data Science with Pandas</title>
        <author>Analyst X</author>
      </book>
    </catalog>
    """
    analisar_xml(xml_dados)