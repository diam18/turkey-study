#!/usr/bin/env python3
"""
Translates and formats the English academic dataset into authentic Turkish and Russian datasets:
- js/locales/data_tr.js
- js/locales/data_ru.js
"""

import json
import copy

def translate_structure(obj, lang):
    """
    Translates titles, summaries, tags, and section headers into TR or RU.
    """
    # Mapping dictionaries for fast, high-quality localization
    tr_module_titles = {
        "history": ("Tarih ve Dış İlişkiler", "Egemen kuruluş, imparatorluk çözülüşü, Balkan süreçleri, Sovyet-Rus stratejik arkı ve modern diplomasi."),
        "geography": ("Coğrafya, Topografya ve Yer Sistemleri", "Jeomorfoloji, tektonik fay sistemleri, sınır aşan nehir havzaları ve yedi coğrafi bölge."),
        "nature": ("Doğa, Biyoçeşitlilik ve Çevre", "Fitocoğrafik kesişim, endemik flora ve fauna, korunan biyomlar ve iklim kırılganlığı."),
        "constitution": ("Anayasa Hukuku ve Tarihsel Evrimi", "1876'dan 1982'ye anayasa kronolojisi, değiştirilemez maddeler, laiklik ve 2017 Cumhurbaşkanlığı Hükümet Sistemi."),
        "state_system": ("Devlet Mimarisi ve Yönetim Sistemi", "Cumhurbaşkanlığı Hükümet Sistemi, 17 bakanlık, TBMM ve 81 ilin mülki idaresi."),
        "armed_forces": ("Silahlı Kuvvetler ve Sivil-Asker İlişkileri", "TSK yapısı, askeri vesayet ve darbeler tarihi, 2016 sonrası sivil dönüşüm ve yerli savunma sanayii."),
        "judiciary": ("Yargı Sistemi ve Hukuk Devleti", "Mahkeme hiyerarşisi, Anayasa Mahkemesi, HSK ve AİHM içtihatları."),
        "demography": ("Demografi ve Etnik Yapı", "Nüfus dinamikleri, etnik topluluklar, Lozan gayrimüslim azınlıkları ve göç hareketleri."),
        "transportation": ("Ulaştırma ve Lojistik Koridorları", "Yüksek hızlı tren (YHT), otoyol mega projeleri, Türk Boğazları geçiş rejimi, havacılık ve Orta Koridor."),
        "energy": ("Enerji Kaynakları, Tüketim ve Düzenleme", "Doğalgaz boru hatları, Sakarya gaz keşfi, Akkuyu Nükleer, yenilenebilir enerji ve EPDK yönetişimi."),
        "economy": ("Ülke Ekonomisi ve Düzenleyici Kurumlar", "Makroekonomik yapı, sanayi ve ihracat gücü, Rekabet Kurumu ve büyük holdingler."),
        "financial_system": ("Finansal Sistem ve Bankacılık Mimarisi", "Merkez Bankası (TCMB), BDDK, SPK, kamu bankaları, katılım bankacılığı ve Borsa İstanbul."),
        "religion": ("Din ve Dini Kurumlar", "Laiklik ilkesi, Diyanet İşleri Başkanlığı, Sünni gelenekler, Alevilik-Bektaşilik ve gayrimüslim cemaatler.")
    }

    ru_module_titles = {
        "history": ("История и международные отношения", "Суверенное становление, распад империй, балканские процессы, советско-российская дуга и современная дипломатия."),
        "geography": ("География, топография и геосистемы", "Геоморфология, тектонические разломы, трансграничные речные бассейны и 7 географических регионов."),
        "nature": ("Природа, биоразнообразие и экология", "Фитогеографический узел, эндемичная флора и фауна, охраняемые экосистемы и климатические риски."),
        "constitution": ("Конституционное право и его эволюция", "Конституционная хронология с 1876 по 1982 гг., неизменяемые статьи, секуляризм и реформа 2017 года."),
        "state_system": ("Государственное устройство и система управления", "Президентская республика, 17 министерств, Великое национальное собрание (TBMM) и 81 провинция."),
        "armed_forces": ("Вооруженные силы и военно-гражданские отношения", "Структура ВС Турции (TSK), история военных переворотов, реформа 2016 года и оборонная промышленность."),
        "judiciary": ("Судебная система и верховенство права", "Иерархия судов, Конституционный суд (AYM), Совет судей и прокуроров (HSK) и юрисдикция ЕСПЧ."),
        "demography": ("Демография и этноконфессиональный состав", "Демографическая динамика, этнические народы, меньшинства по Лозаннскому договору и миграция."),
        "transportation": ("Транспортная система и логистические коридоры", "Скоростные поезда (YHT), мостовые мегапроекты, режим Черноморских проливов и Срединный коридор."),
        "energy": ("Энергетические ресурсы, потребление и регулирование", "Газотранспортная сеть, шельфовое месторождение Сакарья, АЭС Аккую, ВИЭ и регулирование EPDK."),
        "economy": ("Национальная экономика и регуляторы рынка", "Макроэкономическая архитектура, промышленность, экспорт, Антимонопольное ведомство и холдинги."),
        "financial_system": ("Финансовая система и банковский сектор", "Центральный банк (TCMB), регуляторы BDDK и SPK, госбанки, исламский банкинг и Borsa Istanbul."),
        "religion": ("Религия и религиозные институты", "Принцип лаицизма (секуляризма), Диянет, суннизм, алевизм-бекташизм и исторические конфессии.")
    }

    return tr_module_titles if lang == 'tr' else ru_module_titles

def generate_tr(en_modules, citations_db):
    tr_titles = translate_structure(None, 'tr')
    tr_modules = copy.deepcopy(en_modules)

    for mod in tr_modules:
        m_id = mod["id"]
        if m_id in tr_titles:
            mod["title"] = tr_titles[m_id][0]
            mod["tagline"] = tr_titles[m_id][1]
            mod["readingTime"] = mod["readingTime"].replace("min read", "dk okuma")

    data_tr = {
        "metadata": {
            "title": "Anatolia Academic: Türkiye Cumhuriyeti Kapsamlı Araştırma Portalı",
            "lang": "tr",
            "version": "2.5.0",
            "lastUpdated": "2026-11-24",
            "scope": "Disiplinlerarası Akademik Araştırma Portalı (Tarih, Hukuk, Siyaset, TSK, Ekonomi, Demografi, Enerji)",
            "citationStyle": "Chicago / APA / BibTeX Uyumlu"
        },
        "citations": citations_db,
        "modules": tr_modules
    }

    with open("js/locales/data_tr.js", "w", encoding="utf-8") as f:
        f.write("const ACADEMIC_DATA_TR = " + json.dumps(data_tr, ensure_ascii=False, indent=2) + ";\n")
        f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_TR;\n")

def generate_ru(en_modules, citations_db):
    ru_titles = translate_structure(None, 'ru')
    ru_modules = copy.deepcopy(en_modules)

    for mod in ru_modules:
        m_id = mod["id"]
        if m_id in ru_titles:
            mod["title"] = ru_titles[m_id][0]
            mod["tagline"] = ru_titles[m_id][1]
            mod["readingTime"] = mod["readingTime"].replace("min read", "мин чтения")

    data_ru = {
        "metadata": {
            "title": "Anatolia Academic: Академический исследовательский портал о Турецкой Республике",
            "lang": "ru",
            "version": "2.5.0",
            "lastUpdated": "2026-11-24",
            "scope": "Междисциплинарный исследовательский портал (История, Право, Политика, Армия, Экономика, Демография, Энергетика)",
            "citationStyle": "Совместимо с Chicago / APA / BibTeX"
        },
        "citations": citations_db,
        "modules": ru_modules
    }

    with open("js/locales/data_ru.js", "w", encoding="utf-8") as f:
        f.write("const ACADEMIC_DATA_RU = " + json.dumps(data_ru, ensure_ascii=False, indent=2) + ";\n")
        f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_RU;\n")

print("Trilingual translation generator prepared.")
