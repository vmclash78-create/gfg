#!/usr/bin/env python3
"""Search an optional local JSON reference catalog; does not download third-party artwork."""
import argparse,json
from pathlib import Path
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("query",nargs="?",default=""); p.add_argument("--catalog",type=Path,default=Path("assets/library/catalog.json")); p.add_argument("--industry"); p.add_argument("--technique"); p.add_argument("--format",choices=("summary","json"),default="summary"); a=p.parse_args()
    if not a.catalog.exists(): print("No catalog found. Add authorized records with name, industry, mark_type, technique, mood, notes, source and license."); return 0
    data=json.loads(a.catalog.read_text(encoding="utf-8")); items=data if isinstance(data,list) else data.get("items",[]); out=[]; q=a.query.casefold()
    for x in items:
        blob=" ".join(str(x.get(k,"")) for k in ("name","industry","mark_type","technique","mood","notes","source")).casefold()
        if q and q not in blob: continue
        if a.industry and a.industry.casefold() not in str(x.get("industry","")).casefold(): continue
        if a.technique and a.technique.casefold() not in str(x.get("technique","")).casefold(): continue
        out.append(x)
    if a.format=="json": print(json.dumps(out,indent=2,ensure_ascii=False))
    else:
        print(f"{len(out)} match(es)")
        for x in out: print(f"- {x.get('name','Untitled')} | {x.get('industry','unspecified')} | {x.get('mark_type','unspecified')} | {x.get('technique','unspecified')}\\n  {x.get('notes','')}")
if __name__=="__main__": main()
