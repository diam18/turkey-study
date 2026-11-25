#!/usr/bin/env python3
"""
Full Trilingual Knowledge Base Generator for Anatolia Academic.
Translates all 13 modules, paragraphs, and infographics into authentic, deep Turkish and Russian.
"""

import json
import os
import copy

def generate():
    # 1. Load English source
    with open("js/locales/data_en.js", "r", encoding="utf-8") as f:
        en_raw = f.read()
    pfx = "const ACADEMIC_DATA_EN = "
    start = en_raw.index(pfx) + len(pfx)
    end = en_raw.index(";\nif (typeof module")
    en_data = json.loads(en_raw[start:end].strip())
    en_modules = en_data["modules"]

    # 2. Build Turkish Modules
    print("Compiling Turkish modules (1 to 13)...")
    import tr_master_compiler
    tr_modules = tr_master_compiler.compile_tr(en_modules)

    # 3. Build Russian Modules
    print("Compiling Russian modules (1 to 13)...")
    import ru_master_compiler
    ru_modules = ru_master_compiler.compile_ru(en_modules)

    # 4. Write data_tr.js
    from build_tr_content import get_turkish_citations
    data_tr = {
        "metadata": {
            "title": "Anatolia Academic: Türkiye Cumhuriyeti Kapsamlı Araştırma Portalı",
            "lang": "tr",
            "version": "2.5.0",
            "lastUpdated": "2026-11-24",
            "scope": "Disiplinlerarası Akademik Araştırma Portalı (Tarih, Hukuk, Siyaset, TSK, Ekonomi, Demografi, Enerji)",
            "citationStyle": "Chicago / APA / BibTeX Uyumlu"
        },
        "citations": get_turkish_citations(),
        "modules": tr_modules
    }
    with open("js/locales/data_tr.js", "w", encoding="utf-8") as f:
        f.write("const ACADEMIC_DATA_TR = " + json.dumps(data_tr, ensure_ascii=False, indent=2) + ";\n")
        f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_TR;\n")
    print("data_tr.js written successfully.")

    # 5. Write data_ru.js
    from build_ru_content import get_russian_citations
    data_ru = {
        "metadata": {
            "title": "Anatolia Academic: Академический исследовательский портал о Турецкой Республике",
            "lang": "ru",
            "version": "2.5.0",
            "lastUpdated": "2026-11-24",
            "scope": "Междисциплинарный исследовательский портал (История, Право, Политика, Армия, Экономика, Демография, Энергетика)",
            "citationStyle": "Совместимо с Chicago / APA / BibTeX"
        },
        "citations": get_russian_citations(),
        "modules": ru_modules
    }
    with open("js/locales/data_ru.js", "w", encoding="utf-8") as f:
        f.write("const ACADEMIC_DATA_RU = " + json.dumps(data_ru, ensure_ascii=False, indent=2) + ";\n")
        f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_RU;\n")
    print("data_ru.js written successfully.")

if __name__ == "__main__":
    generate()
