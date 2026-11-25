# -*- coding: utf-8 -*-
"""
Russian Master Compiler for Anatolia Academic (Modules 1 to 13).
"""

import copy
import ru_modules_1_to_5
import ru_modules_6_to_13

def compile_ru(en_modules):
    ru_mods = copy.deepcopy(en_modules)
    ru_mods = ru_modules_1_to_5.enrich_1_to_5(ru_mods)
    ru_mods = ru_modules_6_to_13.enrich_6_to_13(ru_mods)
    return ru_mods

if __name__ == "__main__":
    import json
    with open("js/locales/data_en.js", "r", encoding="utf-8") as f:
        en_raw = f.read()
    pfx = "const ACADEMIC_DATA_EN = "
    start = en_raw.index(pfx) + len(pfx)
    end = en_raw.index(";\nif (typeof module")
    en_data = json.loads(en_raw[start:end].strip())
    
    ru_res = compile_ru(en_data["modules"])
    print(f"Compiled {len(ru_res)} Russian modules successfully!")
    for m in ru_res:
        print(f"Mod {m['number']}: {m['title']} | Secs: {len(m['sections'])} | Infos: {len(m['infographics'])}")
