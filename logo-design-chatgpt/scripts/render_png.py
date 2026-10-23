#!/usr/bin/env python3
"""Render SVG to PNG using CairoSVG or Inkscape when installed."""
import argparse, shutil, subprocess, sys
from pathlib import Path
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("svg",type=Path); p.add_argument("-o","--output",type=Path); p.add_argument("--size",type=int,default=512); a=p.parse_args()
    if not a.svg.is_file(): p.error("SVG not found: "+str(a.svg))
    if not 1<=a.size<=8192: p.error("--size must be between 1 and 8192")
    out=a.output or a.svg.with_suffix(".png")
    try:
        import cairosvg; cairosvg.svg2png(url=str(a.svg),write_to=str(out),output_width=a.size,output_height=a.size)
    except ImportError:
        exe=shutil.which("inkscape")
        if not exe: print("Install CairoSVG or Inkscape to render PNG.",file=sys.stderr); return 2
        subprocess.run([exe,str(a.svg),"--export-type=png",f"--export-filename={out}",f"--export-width={a.size}"],check=True)
    print("Wrote",out.resolve()); return 0
if __name__=="__main__": sys.exit(main())
