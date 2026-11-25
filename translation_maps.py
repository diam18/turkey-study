#!/usr/bin/env python3
"""
Populates translation_maps.py with comprehensive Turkish and Russian content for all 13 modules.
"""

import copy

def translate_all_modules(en_modules, lang):
    import tr_translations
    import ru_translations

    if lang == 'tr':
        return tr_translations.get_all_tr_modules(en_modules)
    elif lang == 'ru':
        return ru_translations.get_all_ru_modules(en_modules)
    return en_modules

print("Translation maps dispatcher ready.")
