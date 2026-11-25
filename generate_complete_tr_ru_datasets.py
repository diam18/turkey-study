#!/usr/bin/env python3
"""
Full-fidelity Trilingual Generator for Anatolia Academic.
Directly generates:
- js/locales/data_tr.js (100% Scholarly Turkish)
- js/locales/data_ru.js (100% Scholarly Russian)
With 5x expanded text content and 3x more infographics/schemes on Modules 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13.
"""

import json
import os

from build_tr_content import get_turkish_citations
from build_ru_content import get_russian_citations

# Load English baseline
with open("js/locales/data_en.js", "r", encoding="utf-8") as f:
    en_raw = f.read()

pfx = "const ACADEMIC_DATA_EN = "
start = en_raw.index(pfx) + len(pfx)
end = en_raw.index(";\nif (typeof module")
en_data = json.loads(en_raw[start:end].strip())

print("English modules loaded. Compiling comprehensive Turkish dataset...")

import tr_full_builder
import ru_full_builder

tr_modules = tr_full_builder.build_turkish_modules(en_data["modules"])
ru_modules = ru_full_builder.build_russian_modules(en_data["modules"])

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
    "citations": get_turkish_citations(),
    "modules": tr_modules
}

with open("js/locales/data_tr.js", "w", encoding="utf-8") as f:
    f.write("const ACADEMIC_DATA_TR = " + json.dumps(data_tr, ensure_ascii=False, indent=2) + ";\n")
    f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_TR;\n")

print("data_tr.js successfully generated!")

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
    "citations": get_russian_citations(),
    "modules": ru_modules
}

with open("js/locales/data_ru.js", "w", encoding="utf-8") as f:
    f.write("const ACADEMIC_DATA_RU = " + json.dumps(data_ru, ensure_ascii=False, indent=2) + ";\n")
    f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_RU;\n")

print("data_ru.js successfully generated!")
