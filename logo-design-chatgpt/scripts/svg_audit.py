#!/usr/bin/env python3
"""Dependency-free first-pass SVG logo audit. Reports checks, warnings and a heuristic score."""
import argparse, re, sys, xml.etree.ElementTree as ET
from pathlib import Path
NUM = re.compile(r'[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?')
COLOR = re.compile(r'(?i)(?:fill|stroke|stop-color|color)\s*=\s*["\'](#[0-9a-f]{3,8}\b|[a-z]+|rgba?\([^)]*\)|hsla?\([^)]*\))')
def local(tag): return tag.rsplit("}", 1)[-1]
def audit(path):
    errors=[]; warnings=[]; info=[]
    try:
        raw=path.read_text(encoding="utf-8"); root=ET.fromstring(raw)
    except Exception as e:
        return {"path":str(path),"score":0,"errors":[f"Invalid or unreadable SVG: {e}"],"warnings":[],"info":[]}
    if local(root.tag)!="svg": errors.append("Root element is not svg.")
    vb=root.attrib.get("viewBox")
    if not vb: warnings.append("Missing viewBox.")
    else:
        vals=[float(x) for x in NUM.findall(vb)]
        if len(vals)!=4 or vals[2]<=0 or vals[3]<=0: errors.append("viewBox needs four values and positive dimensions.")
        else: info.append(f"viewBox {vb}; aspect ratio {vals[2]/vals[3]:.3f}.")
    if re.search(r'<script\b|\bon\w+\s*=|javascript:',raw,re.I): warnings.append("Active script/event-handler content detected.")
    if re.search(r'<image\b|href\s*=\s*["\']https?://',raw,re.I): warnings.append("Raster or external resource detected.")
    if re.search(r'filter\s*=|<filter\b|<foreignObject\b',raw,re.I): warnings.append("Filter/foreignObject may reduce portability.")
    elements=list(root.iter()); paths=[e for e in elements if local(e.tag)=="path"]
    commands=sum(len(re.findall(r'[MmLlHhVvCcSsQqTtAa]',e.attrib.get("d",""))) for e in paths)
    colors={m.group(1).lower() for m in COLOR.finditer(raw)}-{"none","currentcolor","inherit","transparent","black","white"}
    info += [f"{len(elements)} elements; {len(paths)} paths; approximately {commands} path commands.",f"{len(colors)} explicit non-neutral color values."]
    if len(elements)>300: warnings.append("High element count; inspect complexity.")
    if commands>450: warnings.append("High path-command count; simplify if details do not earn their place.")
    if len(colors)>5: warnings.append("Many colors; verify palette is intentional.")
    if re.search(r'font-family\s*=|<text\b',raw): warnings.append("Text/font dependency detected; verify font licensing and production needs.")
    return {"path":str(path),"score":0 if errors else max(0,100-12*len(warnings)),"errors":errors,"warnings":warnings,"info":info}
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("files",nargs="+",type=Path); p.add_argument("--json",action="store_true"); a=p.parse_args()
    results=[audit(f) for f in a.files]
    if a.json:
        import json; print(json.dumps(results,indent=2,ensure_ascii=False))
    else:
        for r in results:
            print(f"\n=== {r['path']} ===\nheuristic score: {r['score']}/100")
            for key,label in (("errors","ERROR"),("warnings","WARN"),("info","INFO")):
                for msg in r[key]: print(f"[{label}] {msg}")
    return 1 if any(r["errors"] for r in results) else 0
if __name__=="__main__": sys.exit(main())
