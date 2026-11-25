#!/usr/bin/env python3
"""
Full Russian text content generator for Anatolia Academic.
Translates all 13 modules, section headings, paragraphs, and infographics into authentic academic Russian.
"""

import copy

def get_all_ru_modules(en_modules):
    import ru_modules_data
    return ru_modules_data.get_modules(en_modules)
