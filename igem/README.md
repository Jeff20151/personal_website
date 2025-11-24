# igem_website

Static bilingual landing page for the STEAMxDREAM iGEM training program.

## How to view locally

```bash
cd /Users/jeff/Desktop/igem_website
python3 -m http.server 4000
```

Then open http://localhost:4000 in your browser and load `index.html`.

## Brochure PDF

- Source copy: `docs/igem-training-brochure.html`
- Generator script: `python3 docs/generate_pdf.py`
- Output: `docs/igem-training-brochure.pdf`

Font note: the PDF uses a local symlink to the system font `Arial Unicode.ttf` at `docs/fonts_ArialUnicode.ttf` (ignored by git). If that symlink is missing, point it to a Unicode TTF or swap in an open-source CJK font before running the script.
