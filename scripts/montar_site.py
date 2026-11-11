"""Monta os dados da trilha e embute no index.html.

Fontes:
  dados/trilha.json          etapas (título, nível, resumo, grupos com os ids das aulas),
                             glossário, regras de ouro, mapa do ecossistema e "sobre"
  dados/etapas/etapa-N.json  aulas da etapa N, com vídeos e parecer do auditor

O resultado substitui a linha `const SITE = ...;` do index.html, para o site
continuar sem build no navegador e sem fetch (abre até direto do disco).

Uso:  python3 scripts/montar_site.py
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as f:
        return json.load(f)


def main():
    site = ler("dados/trilha.json")
    aulas = {}
    for arq in sorted(glob.glob(os.path.join(RAIZ, "dados/etapas/etapa-*.json"))):
        for a in json.load(open(arq, encoding="utf-8"))["aulas"]:
            a.pop("descartados", None)          # fica só na pesquisa, não vai para o site
            aulas[a["id"]] = a

    faltando, sem_video = [], []
    for etapa in site["etapas"]:
        for grupo in etapa["grupos"]:
            cheias = []
            for item in grupo["aulas"]:
                aid = item["id"] if isinstance(item, dict) else item
                base = aulas.get(aid)
                if not base:
                    faltando.append(f"etapa {etapa['modulo']}: {aid}")
                    continue
                aula = {**base, **(item if isinstance(item, dict) else {})}
                if not aula.get("videos"):
                    sem_video.append(f"etapa {etapa['modulo']}: {aid}")
                cheias.append(aula)
            grupo["aulas"] = cheias

    linha = "const SITE = " + json.dumps(site, ensure_ascii=False, separators=(",", ":")) + ";"
    caminho = os.path.join(RAIZ, "index.html")
    html = open(caminho, encoding="utf-8").read()
    html, n = re.subn(r"^const SITE = .*;$", lambda _: linha, html, count=1, flags=re.M)
    if n != 1:
        sys.exit("não achei a linha `const SITE = ...;` no index.html")
    open(caminho, "w", encoding="utf-8").write(html)

    total = sum(len(g["aulas"]) for e in site["etapas"] for g in e["grupos"])
    videos = sum(len(a.get("videos") or []) for e in site["etapas"] for g in e["grupos"] for a in g["aulas"])
    print(f"{len(site['etapas'])} etapas, {total} aulas, {videos} vídeos, {len(site.get('glossario', []))} termos")
    for x in faltando:
        print("  aula sem dados:", x)
    for x in sem_video:
        print("  aula sem vídeo:", x)


if __name__ == "__main__":
    main()
