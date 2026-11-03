import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://www.comichron.com/monthlycomicssales/"
headers = {"User-Agent": "trabalho-faculdade-comics/1.0"}


def textoParaNum(texto):
    if not texto:
        return None
    limpo = texto.replace("$", "").replace(",", "").strip()
    try:
        return float(limpo)
    except ValueError:
        return None


def extrair_mes(ano, mes):
    url = f"{base_url}{ano}/{ano}-{mes:02d}.html"
    try:
        r = requests.get(url, headers=headers, timeout=20)
    except Exception:
        return None
    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    registros = []

    for tabela in soup.find_all("table"):
        linhas = tabela.find_all("tr")

        idx_header = None
        cols = None
        for i, tr in enumerate(linhas[:5]):
            txt = [c.get_text(strip=True).lower() for c in tr.find_all(["th", "td"])]
            if any("title" in t for t in txt):
                idx_header = i
                cols = txt
                break
        if cols is None:
            continue

        i_tit = None
        for i, c in enumerate(cols):
            if "comic-book title" in c or "title" in c:
                i_tit = i
                break

        i_issue = None
        for i, c in enumerate(cols):
            if "issue" in c:
                i_issue = i
                break

        i_preco = None
        for i, c in enumerate(cols):
            if "price" in c or "cover price" in c:
                i_preco = i
                break

        i_ed = None
        for i, c in enumerate(cols):
            if "publisher" in c or "published" in c:
                i_ed = i
                break

        if i_tit is None or i_ed is None or i_issue is None:
            continue

        rank = 0
        for tr in linhas[idx_header + 1:]:
            tds = tr.find_all("td")
            if len(tds) < 3:
                continue
            v = [td.get_text(strip=True) for td in tds]

            titulo = v[i_tit] if i_tit < len(v) else None
            editora = v[i_ed] if i_ed < len(v) else None
            if not titulo or not editora:
                continue

            edicao = v[i_issue] if i_issue < len(v) else None
            preco = v[i_preco] if i_preco is not None and i_preco < len(v) else None

            rank += 1
            registros.append({
                "Ano": ano,
                "Mes": mes,
                "Rank": rank,
                "Titulo": titulo,
                "Edicao": edicao,
                "Preco": textoParaNum(preco),
                "Editora": editora,
            })

    return pd.DataFrame(registros) if registros else None