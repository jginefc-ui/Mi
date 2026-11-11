---
name: markitdown-jesus
description: Convierte documentos (PDF, Word .docx, PowerPoint .pptx, Excel .xlsx/.xls, HTML, CSV, JSON, XML, EPUB, ZIP, correos .msg) a Markdown con la librería MarkItDown de Microsoft para gastar menos tokens. Úsala siempre que el usuario suba o mencione un documento de esos formatos y quiera consultarlo, analizarlo, resumirlo o convertirlo, y cuando pida ahorrar tokens.
---

# MarkItDown Jesús

Objetivo: que trabajar con documentos gaste **los menos tokens posibles**. Convierte el documento a
Markdown una sola vez y trabaja después sobre ese `.md`, leyendo solo las partes necesarias.

## Reglas para ahorrar tokens
- No abras ni recorras el archivo original con código si ya lo puedes convertir.
- Ejecuta todo en silencio: no muestres salidas de instalación ni logs.
- **Nunca** imprimas el Markdown completo en la conversación ni hagas `cat` del archivo entero.
- Para responder preguntas, busca solo lo necesario en el `.md` (`grep -n -i`, `head`, `sed -n 'X,Yp'`).
- Respuestas breves: da el dato pedido, no repitas el contenido del documento.

## Pasos
1. Instala la librería en silencio (solo la primera vez en la conversación):
   ```bash
   pip install -q 'markitdown[all]' >/dev/null 2>&1 || pip install -q --break-system-packages 'markitdown[all]' >/dev/null 2>&1
   ```
   Si falla por falta de red, díselo al usuario en una frase: debe permitir la instalación de
   paquetes en Ajustes → Capacidades.

2. Convierte sin mostrar el resultado:
   - Un archivo: `markitdown RUTA_DEL_ARCHIVO -o SALIDA.md`
   - Varios o una carpeta: `python scripts/convertir.py ENTRADA CARPETA_SALIDA`
     (el script está en la carpeta de esta skill; genera `nombre.ext.md` por archivo).
   Después mira solo el tamaño y la estructura: `wc -c SALIDA.md` y `grep -n '^#' SALIDA.md | head -40`.

3. Responde:
   - Si el usuario pidió el Markdown, entrégalo como **archivo descargable** (no pegado en el chat) y
     recomiéndale reutilizar ese `.md` en próximos chats o en el conocimiento de un Proyecto en lugar
     del original: así ahorra tokens cada vez.
   - Si hizo una pregunta sobre el documento, búscala en el `.md` y contesta solo eso.

## Avisos
- Los PDF salen como texto plano, sin títulos. Los PDF escaneados (imagen) no tienen texto:
  avisa de que hace falta OCR.
- Las tablas de Word sin fila de cabecera salen con una cabecera vacía.
