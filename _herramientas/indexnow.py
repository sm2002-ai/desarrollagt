#!/usr/bin/env python3
"""
Avisa a Bing (y a los buscadores que usan IndexNow) que las páginas del sitio cambiaron.

Bing alimenta a Microsoft Copilot y es una de las fuentes que usa la búsqueda de ChatGPT,
así que conviene correr esto cada vez que se publique un cambio en GitHub Pages.

Uso (desde la carpeta del repositorio, después de que GitHub Pages termine de publicar):
    python _herramientas/indexnow.py

Solo usa la biblioteca estándar de Python. Lee las URLs de sitemap.xml.
Esta carpeta empieza con "_", por eso GitHub Pages no la publica.
"""
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SITIO = "https://sm2002-ai.github.io/desarrollagt/"   # cambiar si se conecta un dominio propio
CLAVE = "8f505853f4db0f550df4f5b6fd1491f1"           # debe coincidir con el archivo <CLAVE>.txt en la raíz


def main() -> int:
    sitemap = (RAIZ / "sitemap.xml").read_text(encoding="utf-8")
    urls = re.findall(r"<loc>(.*?)</loc>", sitemap)
    if not urls:
        print("No encontré URLs en sitemap.xml")
        return 1
    if not (RAIZ / f"{CLAVE}.txt").exists():
        print(f"Falta el archivo de clave {CLAVE}.txt en la raíz del repositorio")
        return 1

    host = re.sub(r"^https?://", "", SITIO).split("/")[0]
    cuerpo = {
        "host": host,
        "key": CLAVE,
        "keyLocation": f"{SITIO}{CLAVE}.txt",
        "urlList": urls,
    }
    solicitud = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(cuerpo).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(solicitud, timeout=30) as r:
            print(f"IndexNow respondió {r.status}: {len(urls)} URLs enviadas")
            return 0
    except urllib.error.HTTPError as e:
        # 200/202 = recibido. 403 = la clave no se encontró en el sitio (¿ya se publicó?). 422 = URLs fuera del host.
        print(f"IndexNow respondió {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}")
        return 1
    except urllib.error.URLError as e:
        print(f"No se pudo conectar con IndexNow: {e.reason}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
