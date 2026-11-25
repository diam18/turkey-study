#!/usr/bin/env python3
"""
Turkish Master Compiler for Anatolia Academic (Modules 1 to 13).
"""

import copy

def compile_tr(en_modules):
    tr = copy.deepcopy(en_modules)

    # First load modules 1, 2, 3, 4, 5 from our previous work
    import tr_full_builder
    tr = tr_full_builder.build_turkish_modules(en_modules)

    # Now let's populate Modules 6 to 13 in Turkish
    import tr_modules_6_to_13
    tr = tr_modules_6_to_13.enrich(tr)

    return tr
