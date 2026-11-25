#!/usr/bin/env python3
"""
Full Turkish text content generator for Anatolia Academic.
Translates all 13 modules, section headings, paragraphs, and infographics into authentic academic Turkish.
"""

import copy

def get_all_tr_modules(en_modules):
    import tr_modules_data
    return tr_modules_data.get_modules(en_modules)
