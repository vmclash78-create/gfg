import importlib.util, tempfile, unittest, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/(name+'.py')); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
class ToolTests(unittest.TestCase):
 def test_audit_valid_svg(self):
  mod=load('svg_audit')
  with tempfile.TemporaryDirectory() as d:
   f=Path(d)/'ok.svg'; f.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="#111111"/></svg>'); r=mod.audit(f); self.assertEqual(r['errors'],[]); self.assertGreater(r['score'],0)
 def test_audit_invalid_svg(self):
  mod=load('svg_audit')
  with tempfile.TemporaryDirectory() as d:
   f=Path(d)/'bad.svg'; f.write_text('<svg>'); r=mod.audit(f); self.assertEqual(r['score'],0); self.assertTrue(r['errors'])
 def test_export_recolors_fill(self):
  mod=load('export_variants'); self.assertIn('#ffffff',mod.recolor('<svg><path fill="#000"/></svg>','#ffffff'))
 def test_catalog_json_parses(self): json.loads((ROOT/'assets/library/catalog.json').read_text())
if __name__=='__main__': unittest.main()
