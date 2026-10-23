#!/usr/bin/env python3
"""Generate a standalone HTML visual test sheet for SVG files."""
import argparse, html
from pathlib import Path
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("files",nargs="+",type=Path); p.add_argument("-o","--output",type=Path,default=Path("logo-preview.html")); p.add_argument("--title",default="Logo stress-test sheet"); a=p.parse_args(); cards=[]
    for f in a.files:
        if not f.is_file(): p.error(f"File not found: {f}")
        src=html.escape(f.resolve().as_uri(),quote=True); name=html.escape(f.stem)
        cards.append(f'<article><h2>{name}</h2><div class="sample"><img src="{src}" alt="{name}"></div><div class="tests"><section><b>16 px</b><img class="tiny" src="{src}"></section><section><b>32 px</b><img class="small" src="{src}"></section><section class="mono"><b>One colour</b><img src="{src}"></section><section class="dark"><b>Reversed</b><img src="{src}"></section><section class="squint"><b>Squint</b><img src="{src}"></section><section class="mirror"><b>Mirror check</b><img src="{src}"></section></div><p>Review silhouette, legibility, optical balance, contrast and similarity risk.</p></article>')
    doc='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>'+html.escape(a.title)+'</title><style>body{font:16px/1.5 system-ui;background:#f3f4f6;color:#171717;padding:24px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:20px}article{background:white;border:1px solid #ddd;border-radius:16px;padding:18px}.sample{height:180px;display:grid;place-items:center;border:1px solid #ddd}img{max-width:90%;max-height:140px;object-fit:contain}.tests{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-top:12px}section{min-height:95px;border:1px solid #ddd;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:6px;overflow:hidden}section img{max-height:56px}.tiny{width:16px!important;height:16px!important}.small{width:32px!important;height:32px!important}.mono img{filter:grayscale(1) contrast(3)}.dark{background:#151515;color:white}.dark img{filter:brightness(0) invert(1)}.squint img{filter:blur(1.5px);opacity:.85}.mirror img{transform:scaleX(-1)}@media print{article{break-inside:avoid}}</style><h1>'+html.escape(a.title)+'</h1><p>Browser-based approximate checks; inspect the actual artwork at intended sizes.</p><main>'+''.join(cards)+'</main></html>'
    a.output.write_text(doc,encoding="utf-8"); print("Wrote",a.output.resolve())
if __name__=="__main__": main()
