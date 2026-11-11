# MarkItDown Jesús

[microsoft/markitdown](https://github.com/microsoft/markitdown) es una utilidad en Python (licencia MIT)
que convierte documentos a **Markdown**, pensada sobre todo para alimentar LLMs y pipelines de análisis
de texto. Conserva la estructura importante (títulos, listas, tablas, enlaces), no la fidelidad visual.

## Formatos soportados
PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls), HTML, CSV, JSON, XML, EPUB, ZIP (recorre el contenido),
Outlook (.msg), notebooks Jupyter, imágenes (metadatos EXIF + OCR/descripción opcional con LLM),
audio (metadatos + transcripción) y URLs de YouTube.

## Instalación
```bash
pip install 'markitdown[all]'      # o solo lo que necesites: 'markitdown[pdf,docx,xlsx]'
```
Requiere Python ≥ 3.10.

## Uso rápido
```bash
markitdown archivo.pdf > archivo.md
markitdown archivo.pdf -o archivo.md
cat archivo.pdf | markitdown
```
```python
from markitdown import MarkItDown
md = MarkItDown()
print(md.convert("informe.docx").text_content)
```
Descripción de imágenes con un LLM (opcional):
```python
md = MarkItDown(llm_client=cliente, llm_model="...")
```
Extras: plugins de terceros (`--use-plugins`), Azure Document Intelligence (`-d -e <endpoint>`)
para PDFs escaneados, y un servidor MCP (`markitdown-mcp`) para usarlo desde Claude u otros clientes.

## Probado (v0.1.9)
| Entrada | Resultado |
| --- | --- |
| .docx con título, párrafo y tabla | `# Informe trimestral` + tabla Markdown (cabecera vacía si la tabla de Word no la marca) |
| .xlsx | Una sección `## <hoja>` por hoja con su tabla |
| .html | Títulos, enlaces y listas correctos |
| .pdf (texto) | Solo texto plano, sin estructura de títulos |

**Limitaciones observadas:** los PDF salen como texto plano y los escaneados necesitan OCR
(Document Intelligence o plugin). Los diseños complejos (columnas, maquetación) se pierden.

## Script de lotes
`convertir.py` convierte un archivo o una carpeta entera (recursiva) y conserva la estructura:
```bash
pip install -r requirements.txt
python convertir.py ./documentos ./salida_md     # documentos/a.pdf -> salida_md/a.pdf.md
```
