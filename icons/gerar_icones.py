"""Gera o favicon e os ícones do app a partir de um único desenho.

Desenho: um avião azul subindo na diagonal, deixando uma rota tracejada,
sobre fundo azul-noite.
Rode na raiz do repositório:  python3 icons/gerar_icones.py
"""
import math
from PIL import Image, ImageDraw

FUNDO = "#0C1120"
AZUL = "#4A7BF5"
AZUL_CLARO = "#9FBFFF"
ROTA = "#2F63E8"

# avião apontando para cima, num grid 100x100, centro em (50, 50)
AVIAO = [
    (50, 10), (55, 17), (55, 40), (90, 60), (90, 67), (55, 56), (55, 75), (66, 83), (66, 89),
    (50, 84), (34, 89), (34, 83), (45, 75), (45, 56), (10, 67), (10, 60), (45, 40), (45, 17),
]


def girar(pts, graus, cx=50, cy=50):
    a = math.radians(graus)
    c, s = math.cos(a), math.sin(a)
    return [(cx + (x - cx) * c - (y - cy) * s, cy + (x - cx) * s + (y - cy) * c) for x, y in pts]


def formas(escala=1.0):
    """Lista de (cor, pontos) num grid 100x100. escala<1 encolhe para a área segura."""
    c = 50

    def s(pts):
        return [(c + (x - c) * escala, c + (y - c) * escala) for x, y in pts]

    out = []
    # rota tracejada saindo de baixo, à esquerda
    for a, b in (((13, 87), (19, 81)), ((23, 77), (29, 71))):
        d = 1.9
        out.append((ROTA, s([(a[0] - d, a[1] - d), (b[0] - d, b[1] - d), (b[0] + d, b[1] + d), (a[0] + d, a[1] + d)])))
    # avião menor, girado 45° para subir à direita
    aviao = [(50 + (x - 50) * 0.72 + 6, 50 + (y - 50) * 0.72 - 6) for x, y in AVIAO]
    out.append((AZUL, s(girar(aviao, 45, 56, 44))))
    # cabine clara no nariz
    nariz = [(50, 12), (54, 18), (54, 26), (46, 26), (46, 18)]
    nariz = [(50 + (x - 50) * 0.72 + 6, 50 + (y - 50) * 0.72 - 6) for x, y in nariz]
    out.append((AZUL_CLARO, s(girar(nariz, 45, 56, 44))))
    return out


def png(tamanho, caminho, escala=1.0, cantos=0):
    S = tamanho * 4
    u = S / 100
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if cantos:
        d.rounded_rectangle([0, 0, S, S], radius=cantos * u, fill=FUNDO)
    else:
        d.rectangle([0, 0, S, S], fill=FUNDO)
    for cor, pts in formas(escala):
        d.polygon([(x * u, y * u) for x, y in pts], fill=cor)
    im = im.resize((tamanho, tamanho), Image.LANCZOS)
    if not cantos:
        im = im.convert("RGB")      # iOS e Android não querem transparência no ícone do app
    im.save(caminho, optimize=True)
    return im


def svg(caminho):
    partes = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">',
        f'<rect width="100" height="100" rx="22" fill="{FUNDO}"/>',
    ]
    for cor, pts in formas(1.0):
        p = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        partes.append(f'<polygon points="{p}" fill="{cor}"/>')
    partes.append("</svg>")
    open(caminho, "w").write("".join(partes) + "\n")


if __name__ == "__main__":
    import os
    import tempfile
    svg("favicon.svg")
    # favicon clássico: fundo com cantos arredondados, como o SVG
    tmp = os.path.join(tempfile.gettempdir(), "favicon-256.png")
    base = png(256, tmp, cantos=22)
    base.save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    # app: quadrado cheio (o sistema arredonda os cantos)
    png(180, "icons/apple-touch-icon.png")
    png(192, "icons/icon-192.png")
    png(512, "icons/icon-512.png")
    # Android "maskable": desenho menor, dentro da área segura de 80%
    png(512, "icons/icon-maskable-512.png", escala=0.78)
    print("ícones gerados")
