#!/usr/bin/env python3
"""
Full Trilingual Translator for Anatolia Academic.
Translates all 13 modules, paragraphs, headers, and infographic items into:
- js/locales/data_tr.js (100% Turkish)
- js/locales/data_ru.js (100% Russian)
"""

import json
import re

def build_full_localized_files():
    # Load English dataset
    with open("js/locales/data_en.js", "r", encoding="utf-8") as f:
        content = f.read()
    
    prefix = "const ACADEMIC_DATA_EN = "
    start = content.index(prefix) + len(prefix)
    end = content.index(";\nif (typeof module")
    en_data = json.loads(content[start:end].strip())

    import build_tr_content
    import build_ru_content
    tr_citations = build_tr_content.get_turkish_citations()
    ru_citations = build_ru_content.get_russian_citations()

    # Load dictionaries of translations
    import translation_maps
    tr_modules = translation_maps.translate_all_modules(en_data["modules"], 'tr')
    ru_modules = translation_maps.translate_all_modules(en_data["modules"], 'ru')

    # Write data_tr.js
    data_tr = {
        "metadata": {
            "title": "Anatolia Academic: Türkiye Cumhuriyeti Kapsamlı Araştırma Portalı",
            "lang": "tr",
            "version": "2.5.0",
            "lastUpdated": "2026-11-24",
            "scope": "Disiplinlerarası Akademik Araştırma Portalı (Tarih, Hukuk, Siyaset, TSK, Ekonomi, Demografi, Enerji)",
            "citationStyle": "Chicago / APA / BibTeX Uyumlu"
        },
        "citations": tr_citations,
        "modules": tr_modules
    }

    with open("js/locales/data_tr.js", "w", encoding="utf-8") as f:
        f.write("const ACADEMIC_DATA_TR = " + json.dumps(data_tr, ensure_ascii=False, indent=2) + ";\n")
        f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_TR;\n")

    print("data_tr.js successfully generated (100% Turkish)!")

    # Write data_ru.js
    data_ru = {
        "metadata": {
            "title": "Anatolia Academic: Академический исследовательский портал о Турецкой Республике",
            "lang": "ru",
            "version": "2.5.0",
            "lastUpdated": "2026-11-24",
            "scope": "Междисциплинарный исследовательский портал (История, Право, Политика, Армия, Экономика, Демография, Энергетика)",
            "citationStyle": "Совместимо с Chicago / APA / BibTeX"
        },
        "citations": ru_citations,
        "modules": ru_modules
    }

    with open("js/locales/data_ru.js", "w", encoding="utf-8") as f:
        f.write("const ACADEMIC_DATA_RU = " + json.dumps(data_ru, ensure_ascii=False, indent=2) + ";\n")
        f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_RU;\n")

    print("data_ru.js successfully generated (100% Russian)!")

if __name__ == "__main__":
    build_full_localized_files()
