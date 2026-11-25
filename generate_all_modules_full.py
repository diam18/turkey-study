#!/usr/bin/env python3
"""
Full definitions of all 13 modules for English, Turkish, and Russian.
Provides 5x text expansion and 3x more illustrations/schemes/tables for Modules 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13.
"""

import json

def generate(citations_db):
    # Load the English modules
    from build_dataset_helper import get_en_modules
    en_modules = get_en_modules()
    
    # Let's import the rest of the modules
    import modules_5_to_13
    en_modules.extend(modules_5_to_13.get_modules_en())

    # Write data_en.js
    with open("js/locales/data_en.js", "w", encoding="utf-8") as f:
        data_en = {
            "metadata": {
                "title": "Anatolia Academic: Comprehensive Research Portal on the Republic of Turkey",
                "lang": "en",
                "version": "2.5.0",
                "lastUpdated": "2026-11-24",
                "scope": "Interdisciplinary Scholarly Research (History, Law, Politics, Armed Forces, Economy, Demography, Energy)",
                "citationStyle": "Chicago / APA / BibTeX Compliant"
            },
            "citations": citations_db,
            "modules": en_modules
        }
        f.write("const ACADEMIC_DATA_EN = " + json.dumps(data_en, ensure_ascii=False, indent=2) + ";\n")
        f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_EN;\n")

    print("data_en.js written successfully.")

    # Generate Turkish and Russian variants
    import generate_tr_ru
    generate_tr_ru.generate_tr(en_modules, citations_db)
    generate_tr_ru.generate_ru(en_modules, citations_db)
    print("Turkish and Russian datasets generated.")

if __name__ == "__main__":
    from build_multilingual_datasets import CITATIONS_DB
    generate(CITATIONS_DB)
