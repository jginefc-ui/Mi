---
name: markitdown-jesus
description: Convierte documentos (PDF, Word .docx, PowerPoint .pptx, Excel .xlsx/.xls, HTML, CSV, JSON, XML, EPUB, ZIP, correos .msg) a Markdown con la librería MarkItDown de Microsoft. Úsala cuando el usuario pida pasar, convertir o extraer un documento a Markdown o a texto, o quiera leer el contenido de un Excel, PowerPoint o similar.
---

# MarkItDown Jesús

Convierte a Markdown los archivos que suba el usuario.

## Pasos

1. Instala la librería (solo la primera vez en la conversación):
   ```bash
   pip install 'markitdown[all]' 2>/dev/null || pip install --break-system-packages 'markitdown[all]'
   ```
   Si la instalación falla por falta de red, díselo al usuario: debe permitir la instalación de
   paquetes en los ajustes de ejecución de código de Claude.

2. Convierte:
   - Un archivo: `markitdown RUTA_DEL_ARCHIVO -o SALIDA.md`
   - Varios archivos o una carpeta: `python scripts/convertir.py ENTRADA CARPETA_SALIDA`
     (el script está en la carpeta de esta skill; genera `nombre.ext.md` por archivo).

3. Entrega el resultado:
   - Muestra el Markdown en la respuesta si es corto.
   - Si es largo o son varios archivos, guárdalos como archivos descargables y resume el contenido.

## Avisos
- Los PDF salen como texto plano, sin títulos. Los PDF escaneados (imagen) no tienen texto:
  avisa al usuario de que hace falta OCR.
- Las tablas de Word sin fila de cabecera salen con una cabecera vacía.
