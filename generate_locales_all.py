#!/usr/bin/env python3
"""
Master generator for Anatolia Academic trilingual datasets:
- js/locales/data_en.js
- js/locales/data_tr.js
- js/locales/data_ru.js
"""

import json
import os
import sys

def main():
    print("Beginning generation of comprehensive trilingual datasets...")
    # Import base citations
    from build_multilingual_datasets import CITATIONS_DB

    # Let's read the detailed generator data
    import generate_all_modules_full
    generate_all_modules_full.generate(CITATIONS_DB)
    print("All three locale datasets generated successfully!")

if __name__ == "__main__":
    main()
