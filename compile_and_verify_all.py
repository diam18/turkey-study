#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master compiler and validator for Anatolia Academic trilingual knowledge base.
"""

import json
import os
import copy
from build_tr_content import get_turkish_citations
from build_ru_content import get_russian_citations
import tr_master_compiler
import ru_master_compiler

def main():
    # 1. Load English source
    with open("js/locales/data_en.js", "r", encoding="utf-8") as f:
        en_raw = f.read()
    pfx = "const ACADEMIC_DATA_EN = "
    start = en_raw.index(pfx) + len(pfx)
    end = en_raw.index(";\nif (typeof module")
    en_data = json.loads(en_raw[start:end].strip())
    en_modules = en_data["modules"]
    print(f"Loaded {len(en_modules)} EN modules from data_en.js")

    # 2. Compile Turkish modules
    tr_modules = tr_master_compiler.compile_tr(en_modules)
    # Apply full infographics enrichment for Turkish
    # Mod 4 Info 2 (timeline)
    tr_modules[3]['infographics'][2] = {
        'type': 'timeline',
        'title': 'Anayasa Tarihinde Dönüm Noktaları Kronolojisi',
        'items': [
            {'year': '1808', 'event': 'Sened-i İttifak: Padişahın mutlak yetkilerini yerel ayanlar karşısında sınırlandıran ilk anayasal belge.'},
            {'year': '1876', 'event': 'I. Meşrutiyet & Kanûn-ı Esâsî: İlk yazılı Türk anayasası ilan edildi; Heyet-i Âyân ve Meclis-i Meb\'ûsân kuruldu.'},
            {'year': '1909', 'event': '1909 Anayasa Değişiklikleri: II. Meşrutiyet sonrası padişahın meclisi fesih yetkisi sınırlandırıldı, meclis üstünlüğü sağlandı.'},
            {'year': '1921', 'event': '1921 Teşkilât-ı Esâsîye Kanunu: Kurtuluş Savaşı şartlarında meclis hükümeti sistemi ve "Egemenlik kayıtsız şartsız milletindir" ilkesi kabul edildi.'},
            {'year': '1924', 'event': '1924 Cumhuriyet Anayasası: Hilafetin ilgası sonrası kabul edildi; meclis hükümeti ile parlamenter sistem karması kuruldu.'},
            {'year': '1937', 'event': 'Laiklik İlkesinin Kabulü: Atatürk ilkeleri (Laiklik dahil) 2. maddeye eklenerek anayasal kural haline getirildi.'},
            {'year': '1961', 'event': '1961 Anayasası: 27 Mayıs sonrası Anayasa Mahkemesi, Cumhuriyet Senatosu ve geniş temel haklar güvencesi ihdas edildi.'},
            {'year': '1982', 'event': '1982 Anayasası: 12 Eylül sonrası yürütmeyi güçlendiren, tek meclisli ve %10 seçim barajlı anayasa kabul edildi.'},
            {'year': '2017', 'event': 'Cumhurbaşkanlığı Hükümet Sistemi: 16 Nisan referandumuyla başbakanlık kaldırıldı, yürütme yetkisi doğrudan Cumhurbaşkanına verildi.'}
        ]
    }
    # Mod 5 Info 0 (organogram)
    tr_modules[4]['infographics'][0] = {
        'type': 'organogram',
        'title': 'Türkiye Yürütme ve Devlet İdaresi Kurumsal Şeması',
        'nodes': [
            {'id': 'pres', 'title': 'Cumhurbaşkanı', 'type': 'head', 'sub': 'Devletin Başı, Yürütmenin Tek Yetkilisi, Başkomutan'},
            {'id': 'cab', 'title': 'Cumhurbaşkanlığı Kabinesi (17 Bakanlık)', 'parent': 'pres', 'type': 'exec', 'sub': 'İçişleri, Dışişleri, Milli Savunma, Hazine ve Maliye, Adalet vb.'},
            {'id': 'politika', 'title': '9 Politika Kurulu & Ofisler', 'parent': 'pres', 'type': 'coord', 'sub': 'Ekonomi, Güvenlik, Hukuk, Dijital Dönüşüm, Finans Ofisi'},
            {'id': 'sbb_mit', 'title': 'Bağlı Stratejik Başkanlıklar', 'parent': 'pres', 'type': 'coord', 'sub': 'MİT, SBB, Savunma Sanayii Bşk. (SSB), Diyanet, İletişim Bşk.'},
            {'id': 'tbmm', 'title': 'Türkiye Büyük Millet Meclisi (TBMM)', 'parent': 'pres', 'type': 'super', 'sub': '600 Milletvekili, Yasama Yetkisi ve Bütçe Denetimi'},
            {'id': 'tasra', 'title': 'Mülki Taşra İdaresi (81 İl Valiliği)', 'parent': 'cab', 'type': 'field', 'sub': 'Valilikler, 973 Kaymakamlık ve İl Müdürlükleri Ağı'},
            {'id': 'yerel', 'title': 'Yerel Yönetimler (30 Büyükşehir)', 'parent': 'tasra', 'type': 'field', 'sub': 'Büyükşehir ve İlçe Belediyeleri, İl Genel Meclisleri'}
        ]
    }
    # Mod 6 Info 1 (organogram)
    tr_modules[5]['infographics'][1] = {
        'type': 'organogram',
        'title': 'Sivil-Asker Komuta Hiyerarşisi ve Savunma Sanayii Teşkilat Şeması',
        'nodes': [
            {'id': 'pres', 'title': 'Cumhurbaşkanı', 'type': 'head', 'sub': 'TSK Başkomutanı ve Yürütmenin Başı'},
            {'id': 'msb', 'title': 'Milli Savunma Bakanlığı (MSB)', 'parent': 'pres', 'type': 'exec', 'sub': 'Sivil Bakanlık Hiyerarşik Komuta Zinciri'},
            {'id': 'genelkurmay', 'title': 'Genelkurmay Başkanlığı', 'parent': 'msb', 'type': 'coord', 'sub': 'Kuvvetlerin Harekât ve İstihbarat Eşgüdümü'},
            {'id': 'kuvvetler', 'title': 'Kuvvet Komutanlıkları', 'parent': 'genelkurmay', 'type': 'high', 'sub': 'Kara Kuvvetleri, Deniz Kuvvetleri (Mavi Vatan), Hava Kuvvetleri'},
            {'id': 'ssb', 'title': 'Savunma Sanayii Başkanlığı (SSB)', 'parent': 'pres', 'type': 'coord', 'sub': 'Savunma Tedarik ve Yerli Sanayi Ekosistem Koordinasyonu'},
            {'id': 'sanayi', 'title': 'Milli Savunma Sanayii Şirketleri', 'parent': 'ssb', 'type': 'sub', 'sub': 'Aselsan, Baykar, TUSAŞ/TAI, Roketsan, STM, Havelsan'}
        ]
    }
    # Mod 7 Info 0 (organogram)
    tr_modules[6]['infographics'][0] = {
        'type': 'organogram',
        'title': 'Türk Yargı Teşkilatı Hiyerarşi ve İstinaf Şeması',
        'nodes': [
            {'id': 'aym', 'title': 'Anayasa Mahkemesi (AYM)', 'type': 'apex', 'sub': '15 Üye: Norm Denetimi ve Bireysel Başvuru Yetkisi'},
            {'id': 'yargitay', 'title': 'Yargıtay (Adli Yargı Temyiz)', 'parent': 'aym', 'type': 'high', 'sub': 'Hukuk ve Ceza Genel Kurulları, Son Derece Temyiz Mahkemesi'},
            {'id': 'danistay', 'title': 'Danıştay (İdari Yargı Temyiz)', 'parent': 'aym', 'type': 'high', 'sub': 'İdari Dava Daireleri, İdari Eylem ve İşlemlerin Temyiz Mercii'},
            {'id': 'bam', 'title': 'Bölge Adliye Mahkemeleri (BAM)', 'parent': 'yargitay', 'type': 'appellate', 'sub': 'Adli Yargı 2. Derece İstinaf Mahkemeleri'},
            {'id': 'bim', 'title': 'Bölge İdare Mahkemeleri (BİM)', 'parent': 'danistay', 'type': 'appellate', 'sub': 'İdari Yargı 2. Derece İstinaf Mahkemeleri'},
            {'id': 'ilk', 'title': 'İlk Derece Mahkemeleri', 'parent': 'bam', 'type': 'base', 'sub': 'Asliye Hukuk/Ceza, Ağır Ceza, İdare ve Vergi Mahkemeleri'}
        ]
    }
    # Mod 8 Info 2 (timeline)
    tr_modules[7]['infographics'][2] = {
        'type': 'timeline',
        'title': 'Türkiye\'de Tarihsel Göç ve Nüfus Hareketleri Kronolojisi',
        'items': [
            {'year': '1923-1924', 'event': 'Türk-Yunan Nüfus Mübadelesi: Lozan Antlaşması uyarınca ~1,2 milyon Rum Yunanistan\'a, ~500 bin Müslüman Türk Anadolu\'ya göç etti.'},
            {'year': '1950-1970', 'event': 'Köyden Kente İç Göç Dalgası: Tarımda makineleşme ve karayolu hamlesiyle kırsaldan İstanbul, Ankara ve İzmir\'e kitlesel kentsel göç yaşandı.'},
            {'year': '1961-1973', 'event': 'Batı Avrupa\'ya İşgücü Göçü: Almanya, Avusturya, Belçika ve Fransa ile imzalanan anlaşmalarla 800 bini aşkın işçi Avrupa\'ya gitti.'},
            {'year': '1989', 'event': 'Bulgaristan\'dan "Büyük Göç": Jivkov rejiminin asimilasyon baskısı sonucu 360 bini aşkın Bulgaristan Türkü Türkiye\'ye sığındı.'},
            {'year': '1991', 'event': 'Körfez Savaşı Sığınmacı Dalgası: Irak\'ın kuzeyindeki çatışmalardan kaçan 450 bin sivil Türkiye sınırına ulaştı, insani koridor açıldı.'},
            {'year': '2011-2024', 'event': 'Suriye İnsani Krizi ve Geçici Koruma: İç savaştan kaçan 3,7 milyonu aşkın sığınmacıya açık kapı politikası ve geçici koruma statüsü tanındı.'}
        ]
    }
    # Mod 9 Info 2 (timeline)
    tr_modules[8]['infographics'][2] = {
        'type': 'timeline',
        'title': 'Türkiye Ulaştırma ve Lojistik Altyapı Kronolojisi',
        'items': [
            {'year': '1973', 'event': 'Boğaziçi Köprüsü (15 Temmuz Şehitler): Asya ve Avrupa kıtalarını bağlayan ilk sabit asma köprü hizmete açıldı.'},
            {'year': '2009', 'event': 'Ankara-Eskişehir İlk Yüksek Hızlı Tren (YHT): Türkiye yüksek hızlı demiryolu teknolojisiyle tanışarak dünyada 8., Avrupa\'da 6. ülke oldu.'},
            {'year': '2013', 'event': 'Marmaray Boğaz Tüp Geçişi: Asya ve Avrupa demiryolu şebekelerini deniz tabanının altından bağlayan asrın projesi tamamlandı.'},
            {'year': '2016', 'event': 'Yavuz Sultan Selim ve Osmangazi Köprüleri: Kuzey Marmara Otoyolu ve İzmit Körfezi asma köprü projeleriyle transit omurga güçlendirildi.'},
            {'year': '2018', 'event': 'İstanbul Havalimanı (IGA) 1. Etap Açılışı: Yıllık 90 milyon yolcu kapasiteli küresel transit aktarma merkezi faaliyete başladı.'},
            {'year': '2022', 'event': '1915 Çanakkale Köprüsü: 2.023 metre orta açıklığıyla dünyanın en uzun asma köprüsü unvanını alarak Çanakkale Boğazı\'nı birleştirdi.'}
        ]
    }
    # Mod 10 Info 2 (timeline)
    tr_modules[9]['infographics'][2] = {
        'type': 'timeline',
        'title': 'Enerji ve Hidrokarbon Mega Projeleri Kronolojisi',
        'items': [
            {'year': '1977', 'event': 'Kerkük-Yumurtalık Ham Petrol Boru Hattı: Türkiye ile Irak arasındaki ilk büyük uluslararası enerji arteri devreye girdi.'},
            {'year': '2003', 'event': 'Mavi Akım Doğalgaz Boru Hattı: Rusya\'dan Karadeniz tabanından Samsun\'a uzanan derin deniz boru hattı gaz akışına başladı.'},
            {'year': '2006', 'event': 'Bakü-Tiflis-Ceyhan (BTC) Ham Petrol Hattı: Hazar petrollerini Akdeniz\'e taşıyan Doğu-Batı enerji koridoru resmen açıldı.'},
            {'year': '2018', 'event': 'TANAP Trans-Anadolu Doğalgaz Boru Hattı: Şah Deniz 2 gazını Türkiye ve Güney Gaz Koridoru üzerinden Avrupa\'ya ulaştıran hat açıldı.'},
            {'year': '2020', 'event': 'Karadeniz Sakarya Gaz Keşfi: Fatih sondaj gemisi 710 milyar m³ rezerve sahip Türkiye tarihinin en büyük doğalgaz sahasını keşfetti.'},
            {'year': '2023', 'event': 'Akkuyu Nükleer Santrali İlk Yakıt Getirilişi: 4.800 MW\'lık VVER-1200 reaktörlerine nükleer yakıt teslim edilerek santral sahası nükleer tesis statüsü kazandı.'}
        ]
    }
    # Mod 11 Info 2 (timeline)
    tr_modules[10]['infographics'][2] = {
        'type': 'timeline',
        'title': 'Modern Türkiye Ekonomi Politikası Dönüm Noktaları',
        'items': [
            {'year': '1923', 'event': 'İzmir İktisat Kongresi: Yeni devletin ekonomik bağımsızlık ilkeleri ve yerli özel teşebbüsü destekleme kararı alındı.'},
            {'year': '1934', 'event': 'I. Beş Yıllık Sanayi Planı: Devletçilik ilkesi doğrultusunda Sümerbank, Etibank ve temel sanayi tesisleri kuruldu.'},
            {'year': '1980', 'event': '24 Ocak Kararları: İthal ikameci modelden ihracata dayalı dışa açık piyasa ekonomisine ve serbest kambiyo rejimine geçildi.'},
            {'year': '1996', 'event': 'AB ile Gümrük Birliği\'nin Yürürlüğe Girmesi: Sanayi mallarında tarife engelleri kaldırılarak Türkiye sanayisi Avrupa standartlarına entegre oldu.'},
            {'year': '2001', 'event': 'Güçlü Ekonomiye Geçiş Programı: 2001 krizi sonrası bağımsız BDDK, bağımsız TCMB enflasyon hedeflemesi ve bütçe disiplini reformları yapıldı.'},
            {'year': '2023', 'event': 'Ortodoks Para Politikasına Dönüş: Enflasyonla mücadele amacıyla rasyonel zemine dönülerek politika faizi %50 seviyesine yükseltildi.'}
        ]
    }
    # Mod 12 Info 2 (timeline)
    tr_modules[11]['infographics'][2] = {
        'type': 'timeline',
        'title': 'Türk Finans ve Bankacılık Sistemi Kronolojisi',
        'items': [
            {'year': '1863', 'event': 'Memleket Sandıkları & Ziraat Bankası Kökleri: Mithat Paşa öncülüğünde Türk bankacılık tarihinin ilk yerli tarımsal kredi sandığı kuruldu.'},
            {'year': '1924', 'event': 'Türkiye İş Bankası\'nın Kuruluşu: Cumhuriyetin ilk ulusal ticari bankası Atatürk\'ün talimatıyla kuruldu.'},
            {'year': '1930', 'event': 'Türkiye Cumhuriyet Merkez Bankası (TCMB) Kanunu: Para basma imtiyazı Osmanlı Bankası\'ndan alınarak bağımsız ulusal merkez bankasına verildi.'},
            {'year': '1985', 'event': 'Katılım Bankacılığının Başlaması: Faizsiz bankacılık prensiplerine dayalı ilk özel finans kuruluşları faaliyete geçti.'},
            {'year': '2000', 'event': 'Bankacılık Düzenleme ve Denetleme Kurumu (BDDK) Faaliyete Geçti: Bankacılık sektörünün tek elden ihtiyati denetimi bağımsız üst kurula devredildi.'},
            {'year': '2016', 'event': 'Türkiye Varlık Fonu\'nun (TVF) İhdası: Stratejik kamu varlıklarını yönetmek üzere ulusal varlık fonu ihdas edildi.'}
        ]
    }
    # Mod 13 Info 2 (timeline)
    tr_modules[12]['infographics'][2] = {
        'type': 'timeline',
        'title': 'Türkiye\'de Laiklik ve Dini Kurumlar Kronolojisi',
        'items': [
            {'year': '1924', 'event': 'Diyanet İşleri Başkanlığı\'nın Kuruluşu ve Tevhid-i Tedrisat: Şeriye ve Evkaf Vekaleti lağvedilerek Diyanet ihdas edildi, eğitim birliği sağlandı.'},
            {'year': '1925', 'event': 'Tekke, Zaviye ve Türbelerin Kapatılması: 677 sayılı Kanun ile tarikat faaliyetleri, dervişlik ve şeyhlik unvanları yasaklandı.'},
            {'year': '1928', 'event': '"Devletin dini İslam\'dır" İbaresinin Kaldırılması: Anayasa metnindeki dini hükümler ayıklanarak sekülerleşme adımı atıldı.'},
            {'year': '1937', 'event': 'Laiklik İlkesinin Anayasa\'ya Girmesi: Türkiye Cumhuriyeti Anayasası\'nın 2. maddesine laiklik ilkesi açıkça dahil edildi.'},
            {'year': '1982', 'event': 'Din Kültürü ve Ahlak Bilgisi Dersinin Zorunlu Kılınması: 1982 Anayasası\'nın 24. maddesiyle okullarda din eğitimi anayasal kural haline geldi.'},
            {'year': '2022', 'event': 'Alevi-Bektaşi Kültür ve Cemevi Başkanlığı İhdası: Cemevlerinin bakım, aydınlatma ve kültürel faaliyetleri kamu güvencesine alındı.'}
        ]
    }

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

    # 3. Compile Russian modules
    ru_modules = ru_master_compiler.compile_ru(en_modules)

    data_ru = {
        "metadata": {
            "title": "Anatolia Academic: Академический исследовательский портал о Турецкой Республике",
            "lang": "ru",
            "version": "2.5.0",
            "lastUpdated": "2026-11-24",
            "scope": "Междисциплинарный академический исследовательский портал (История, Конституционное право, Система власти, Вооруженные силы, Демография, Транспорт, Энергетика, Экономика, Финансы, Религия)",
            "citationStyle": "Совместимо с Chicago / APA / BibTeX"
        },
        "citations": get_russian_citations(),
        "modules": ru_modules
    }

    with open("js/locales/data_ru.js", "w", encoding="utf-8") as f:
        f.write("const ACADEMIC_DATA_RU = " + json.dumps(data_ru, ensure_ascii=False, indent=2) + ";\n")
        f.write("if (typeof module !== 'undefined' && module.exports) module.exports = ACADEMIC_DATA_RU;\n")
    print("data_ru.js written successfully.")

    print("\n--- VALIDATION CHECK ---")
    for lang, path, pfx in [('EN', 'js/locales/data_en.js', 'const ACADEMIC_DATA_EN = '),
                             ('TR', 'js/locales/data_tr.js', 'const ACADEMIC_DATA_TR = '),
                             ('RU', 'js/locales/data_ru.js', 'const ACADEMIC_DATA_RU = ')]:
        with open(path, 'r', encoding='utf-8') as f:
            raw = f.read()
        st = raw.index(pfx) + len(pfx)
        ed = raw.index(";\nif (typeof module")
        obj = json.loads(raw[st:ed].strip())
        print(f"[{lang}] Modules: {len(obj['modules'])}, Citations: {len(obj['citations'])}, Metadata Title: {obj['metadata']['title']}")
        for m in obj['modules']:
            assert len(m['sections']) >= 3, f"Module {m['number']} in {lang} has too few sections"
            assert len(m['infographics']) >= 1, f"Module {m['number']} in {lang} has no infographics"
        print(f"[{lang}] All integrity assertions passed!")

if __name__ == "__main__":
    main()
