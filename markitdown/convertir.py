#!/usr/bin/env python3
"""Convierte a Markdown todos los archivos de una carpeta usando MarkItDown.

Uso:
    python convertir.py ENTRADA [SALIDA]

- ENTRADA: archivo o carpeta (se recorre recursivamente).
- SALIDA: carpeta destino (por defecto, ./salida_md). Se conserva la estructura.
"""
import sys
from pathlib import Path

from markitdown import MarkItDown

EXTENSIONES = {
    ".pdf", ".docx", ".pptx", ".xlsx", ".xls", ".csv", ".json", ".xml",
    ".html", ".htm", ".epub", ".zip", ".msg", ".ipynb", ".txt",
    ".jpg", ".jpeg", ".png", ".mp3", ".wav",
}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    entrada = Path(sys.argv[1])
    salida = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("salida_md")
    base = entrada if entrada.is_dir() else entrada.parent
    archivos = (
        [p for p in sorted(entrada.rglob("*")) if p.suffix.lower() in EXTENSIONES]
        if entrada.is_dir()
        else [entrada]
    )

    md = MarkItDown(enable_plugins=False)
    ok = errores = 0
    for archivo in archivos:
        rel = archivo.relative_to(base)
        destino = salida / rel.with_name(rel.name + ".md")  # demo.pdf -> demo.pdf.md
        try:
            texto = md.convert(str(archivo)).text_content
        except Exception as e:  # formato no soportado, archivo corrupto, etc.
            print(f"ERROR {archivo}: {e}")
            errores += 1
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(texto, encoding="utf-8")
        print(f"OK    {archivo} -> {destino}")
        ok += 1

    print(f"\n{ok} convertidos, {errores} con error")
    return 0 if errores == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
