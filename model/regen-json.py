import sys, json, importlib.util
src, out = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('data', src)
data = importlib.util.module_from_spec(spec); spec.loader.exec_module(data)
open(out,'w',encoding='utf-8').write(json.dumps(data.MODEL, ensure_ascii=False, indent=2)+'\n')
