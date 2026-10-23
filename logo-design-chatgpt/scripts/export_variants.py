#!/usr/bin/env python3
"""Create recoloured SVG variants and a web manifest scaffold."""
import argparse, json, re
from pathlib import Path
def recolor(src,color):
    return re.sub(r'(?i)\b(fill|stroke)\s*=\s*(["\'])(?!none\b|url\()(.*?)\2',lambda m:f'{m.group(1)}={m.group(2)}{color}{m.group(2)}',src)
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("svg",type=Path); p.add_argument("--mono",default="#111111"); p.add_argument("--reverse",default="#ffffff"); p.add_argument("--outdir",type=Path,default=Path("logo-exports")); p.add_argument("--web-icons",action="store_true"); a=p.parse_args()
    if not a.svg.is_file(): p.error("SVG not found: "+str(a.svg))
    a.outdir.mkdir(parents=True,exist_ok=True); src=a.svg.read_text(encoding="utf-8")
    for name,color in (("monochrome",a.mono),("reversed",a.reverse)):
        dest=a.outdir/(a.svg.stem+"-"+name+".svg"); dest.write_text(recolor(src,color),encoding="utf-8"); print(dest)
    if a.web_icons:
        manifest={"name":a.svg.stem,"short_name":a.svg.stem[:12],"icons":[{"src":f"/icons/icon-{n}.png","sizes":f"{n}x{n}","type":"image/png"} for n in (16,32,48,180,192,512)],"display":"standalone"}
        dest=a.outdir/"site.webmanifest"; dest.write_text(json.dumps(manifest,indent=2),encoding="utf-8"); print(dest)
        (a.outdir/"EXPORT-NOTES.md").write_text("Manifest scaffold only. Render and inspect every PNG size before deployment; this script does not create PNG/ICO files.\\n")
if __name__=="__main__": main()
