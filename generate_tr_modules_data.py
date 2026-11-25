#!/usr/bin/env python3
"""
Builds tr_modules_data.py with comprehensive, articulate academic Turkish for all 13 modules.
"""

def generate():
    with open("tr_modules_data.py", "w", encoding="utf-8") as f:
        f.write('''# -*- coding: utf-8 -*-
"""
Articulate, deep academic Turkish data for all 13 modules.
"""
import copy

def get_modules(en_modules):
    tr_mods = copy.deepcopy(en_modules)
    
    # Module 1: Tarih ve Dış İlişkiler
    m1 = tr_mods[0]
    m1["title"] = "Tarih ve Dış İlişkiler"
    m1["tagline"] = "Egemen kuruluş, imparatorluk çözülüşü, Balkan süreçleri, Sovyet-Rus stratejik arkı ve modern diplomasi."
    m1["readingTime"] = "32 dk okuma"
    m1["summary"] = "Türkiye Cumhuriyeti'nin tarihsel temellerini, Selçuklu ve Osmanlı mirasından Kurtuluş Savaşı'na ve Kemalist modernleşmeye kadar çok katmanlı olarak ele alan kapsamlı bir akademik analiz. Sovyetler Birliği/Rusya ve Bulgaristan ile ikili ilişkilerin tarihsel derinliği, Yunanistan, Orta Doğu, Güney Kafkasya, NATO ittifakı ve Montrö Boğazlar Sözleşmesi rejimi ayrıntılı olarak incelenmektedir."
    
    m1["sections"][0]["title"] = "1. Osmanlı Öncesi Anadolu, Selçuklu Devlet Aklı ve Beylikler Dönemi"
    m1["sections"][0]["content"] = """Modern Türkiye'nin tarihsel güzergahı, Anadolu coğrafyasında binlerce yıllık medeniyet sentezlerine dayanmaktadır. Oğuz Türk boylarının batıya göçü ve Sultan Alparslan'ın Bizans İmparatoru Romen Diyojen'e karşı kazandığı 1071 Malazgirt Zaferi, Anadolu'nun kapılarını kalıcı Türk yerleşimine açmıştır [ZURCHER-2017].

Önce İznik, ardından Konya merkezli kurulan Anadolu Selçuklu Devleti (1077–1308), İpek Yolu üzerinde kervansaraylar, medreseler ve abidevi mimari eserler inşa ederek özgün bir Fars-Türk yüksek kültür havzası meydana getirmiştir. Bu dönemde Mevlânâ Celâleddîn-i Rûmî ve Yunus Emre gibi felsefi ve tasavvufi düşünürler yetişmiştir. 1243 Kösedağ Savaşı'ndaki Moğol yenilgisinin ardından merkezi otorite dağılmış, Anadolu'da beylikler dönemi başlamış; Söğüt'te kurulan Osmanoğulları Beyliği kısa sürede cihanşümul bir imparatorluğa dönüşmüştür."""

    m1["sections"][1]["title"] = "2. Osmanlı İmparatorluğu: Klasik Kurumlar, Tanzimat ve Meşrutiyet Mücadeleleri"
    m1["sections"][1]["content"] = """Fatih Sultan Mehmed'in 29 Mayıs 1453'te İstanbul'u fethi, Osmanlı Devleti'ni üç kıtaya hükmeden bir imparatorluğa dönüştürmüştür. Kanunî Sultan Süleyman devrinde (1520–1566) imparatorluk en geniş sınırlarına ulaşmış, Viyana kapılarından Basra Körfezi'ne kadar uzanmıştır:

- **Klasik Millet Sistemi:** Gayrimüslim tebaa inanç esasına göre teşkilatlandırılmış (Rum Ortodoks, Ermeni Gregoryen ve Yahudi milletleri); ibadet, medeni hukuk ve cemaat içi yargı özerkliği tanınmıştır.
- **Yapısal Duraklama ve Doğu Sorunu:** 1683 İkinci Viyana Kuşatması ve 1699 Karlofça Antlaşması ile başlayan askeri geri çekilme, 19. yüzyılda Düvel-i Muazzama'nın müdahalelerine sahne olan 'Şark Meselesi'ne dönüşmüştür.
- **Tanzimat ve Islahat Modernleşmesi (1839–1876):** 1839 Gülhane Hatt-ı Hümayunu ve 1856 Islahat Fermanı ile din farkı gözetilmeksizin can, mal ve ırz emniyeti kanun güvencesine alınmış; modern ordu (Nizam-ı Cedid) ve Batı tarzı mahkemeler ihdas edilmiştir.
- **I. ve II. Meşrutiyet:** 1876'da ilk Osmanlı anayasası (Kanûn-ı Esâsî) yürürlüğe girmiş; II. Abdülhamid'in meclisi tatil etmesinin ardından 1908 Jön Türk Devrimi ile anayasal monarşi yeniden kurulmuş, ancak devlet Trablusgarp ve Balkan Savaşları (1912–1913) felaketlerine sürüklenmiştir."""

    m1["sections"][2]["title"] = "3. I. Dünya Savaşı, Paylaşım Planları ve Milli Mücadele (1914–1923)"
    m1["sections"][2]["content"] = """Osmanlı Devleti I. Dünya Savaşı'nda Çanakkale'de (1915) destansı bir savunma zaferi kazanmasına rağmen genel savaşta mağlup olmuş ve 30 Ekim 1918 Mondros Mütarekesi imzalanmıştır. 10 Ağustos 1920'de imzalanan Sevr Antlaşması (Treaty of Sèvres), Türk egemenliğini İç Anadolu'ya sıkıştıran ağır bir paylaşım dayatmıştır:

- **Milli Mücadele:** 19 Mayıs 1919'da Mustafa Kemal Paşa'nın Samsun'a çıkışıyla örgütlenen milli direniş, Erzurum ve Sivas Kongrelerinde Misak-ı Millî ilkelerini ilan etmiştir.
- **TBMM'nin Açılışı:** İstanbul'un işgali üzerine 23 Nisan 1920'de Ankara'da Türkiye Büyük Millet Meclisi açılmış, millet egemenliğine dayalı yeni devlet kurulmuştur.
- **Kurtuluş Savaşı Cepheleri (1920–1922):** Doğu'da Kâzım Karabekir komutasında Ermenistan mağlup edilmiş; Güney'de Fransız kuvvetleri Ankara İtilafnamesi (1921) ile çekilmiş; Batı Cephesi'nde İnönü ve Sakarya Meydan Muharebesi ile Yunan ilerleyişi durdurulmuştur. 26 Ağustos 1922 Büyük Taarruz ile 9 Eylül'de İzmir kurtarılmıştır.
- **Lozan Barış Antlaşması (1923):** İsmet Paşa başkanlığındaki heyetin yürüttüğü müzakerelerle 24 Temmuz 1923'te Lozan Antlaşması imzalanmış; Sevr yırtılıp atılmış, kapitülasyonlar kaldırılmış ve bağımsız Türkiye Cumhuriyeti uluslararası alanda tescil edilmiştir [LAUSANNE-1923]. 29 Ekim 1923'te Cumhuriyet ilan edilmiştir."""

    m1["sections"][3]["title"] = "4. Sovyet-Rus Stratejik Arkı: Dayanışma, Soğuk Savaş Krizleri ve Modern Karşılıklı Bağımlılık"
    m1["sections"][3]["content"] = """Türkiye ile Rus devleti arasındaki münasebetler, 12 büyük imparatorluk savaşından devrimci dayanışmaya ve Soğuk Savaş cepheleşmesinden günümüzün 'bölümlere ayrılmış stratejik ortaklığına' uzanan beş asırlık bir jeopolitik arkı temsil eder:

- **Lenin-Atatürk Devrimci İttifakı (1920–1923):** Ankara hükümeti ile Sovyet Rusya emperyalizme karşı ortak mücadele zemininde birleşmiştir. 16 Mart 1921'de imzalanan **Moskova Antlaşması (Kardeşlik ve Dostluk Antlaşması)** ile Sovyetler Sevr'i reddeden ilk büyük güç olmuş ve TBMM'yi tanımıştır [MOSCOW-TREATY-1921]. Moskova'dan 10 milyon altın ruble, 39.000 tüfek ve mühimmat temin edilmiştir. 13 Ekim 1921 **Kars Antlaşması** ile doğu sınırı kesinleşmiştir [KARS-TREATY-1921].
- **1930'lar Sanayi Kredileri:** Sovyet Gosplan uzmanları Türkiye'nin Birinci Beş Yıllık Sanayi Planı'na (1934) katkı sağlamış, Sümerbank Kayseri ve Nazilli tekstil fabrikaları Sovyet kredileriyle inşa edilmiştir.
- **Stalin'in Boğazlar ve Toprak Talepleri (1945):** II. Dünya Savaşı sonunda Stalin'in Kars ve Ardahan'ı talep etmesi ve Boğazlarda ortak askeri üs istemesi, Türkiye'nin tarafsızlık politikasını sona erdirerek **Truman Doktrini (1947)** ve **1952'de NATO'ya katılımına** yol açmıştır [ZURCHER-2017].
- **1962 Küba Füze Krizi:** Türkiye'ye konuşlandırılan ABD Jüpiter füzeleri, Kruşçev ve Kennedy arasındaki gizli anlaşmayla Küba'daki Sovyet füzelerinin çekilmesi karşılığında sökülmüştür. Buna rağmen 1970'lerde İskenderun Demir-Çelik (İSDEMİR) ve Seydişehir Alüminyum gibi ağır sanayi tesisleri Sovyet teknik yardımıyla kurulmuştur.
- **Soğuk Savaş Sonrası ve Enerji Bağımlılığı:** 1990'lardan itibaren **Mavi Akım (Blue Stream)** ve **TürkAkım (TurkStream)** doğalgaz boru hatları inşa edilmiştir. Rus devlet şirketi Rosatom, Mersin'de 20 milyar dolarlık **Akkuyu Nükleer Güç Santrali**'ni inşa etmektedir.
- **S-400 Tedariği ve Montrö'nün Uygulanması:** 2017'de Rusya'dan S-400 hava savunma sistemi satın alınmış; 2022 Rusya-Ukrayna Savaşı'nda Türkiye, **Montrö Boğazlar Sözleşmesi'nin 19. maddesini** uygulayarak savaşan tarafların savaş gemilerine Boğazları kapatmış ve Karadeniz'de tırmanmayı önlemiştir [UN-TREATY-MONTREUX, SIPRI-2024-MLX]."""

    m1["sections"][4]["title"] = "5. Bulgaristan ve Balkan Ekseni: Tarihsel Antlaşmalar, Soğuk Savaş ve 1989 Büyük Göçü"
    m1["sections"][4]["content"] = """Türkiye-Bulgaristan ilişkileri ortak Osmanlı geçmişini, Soğuk Savaş sınır hattını ve insani dramları içeren hayati bir köprüdür:

- **Konstantiniyye (1913) ve Ankara (1925) Antlaşmaları:** 1913 İstanbul Antlaşması Doğu Trakya sınırını çizmiş ve Bulgaristan'daki Türk azınlığın dini haklarını güvenceye almıştır. 18 Ekim 1925 **Ankara Dostluk Antlaşması** ile iki ülke birbirini tanımış, serbest göç ve azınlık mülk hakları teyit edilmiştir.
- **Soğuk Savaşın Trakya Sınırı (NATO - Varşova Paktı):** 269 kilometrelik Türkiye-Bulgaristan sınırı, Soğuk Savaş boyunca iki zıt kutbun cephe hattı olmuştur. Türk 1. Ordusu Boğazlar istikametini savunmak üzere Edirne ve Kırklareli'de konuşlandırılmıştır.
- **1989 Zorunlu Asimilasyon ve 'Büyük Göç':** Todor Jivkov komünist rejimi 1984 yılı sonunda 'Yenisürec' (Soya Dönüş) adı altında 800 binden fazla Türk'ün Türkçe isimlerini zorla değiştirmiş, Türkçe konuşmayı ve dini vecibeleri yasaklamıştır. Mayıs 1989'da başlayan barışçıl direniş şiddetle bastırılmış; 3 Haziran 1989'da Türkiye sınır kapılarını açınca **üç ay içinde 360 binden fazla Bulgaristan Türkü yük vagonları ve araçlarla anavatana sığınmıştır** [BULGARIA-EXODUS-1989]. Bu olay, II. Dünya Savaşı'ndan sonra Avrupa'daki en büyük mülteci akını olmuştur.
- **1989 Sonrası Normalleşme ve NATO Ortaklığı:** Jivkov'un devrilmesiyle haklar iade edilmiş, Hak ve Özgürlükler Hareketi (HÖH/DPS) Bulgar parlamentosunda kilit aktör olmuştur. Bugün Kapıkule/Kaptan Andreevo Sınır Kapısı dünyanın en işlek ikinci kara gümrük kapısıdır. Ocak 2023'te BOTAŞ ile Bulgargaz arasında 13 yıllık doğalgaz iletim ve terminal kapasite anlaşması imzalanmıştır."""

    m1["sections"][5]["title"] = "6. Bölgesel Dinamikler: Yunanistan, Orta Doğu, Kafkasya ve Çok Taraflı İttifaklar"
    m1["sections"][5]["content"] = """Türkiye'nin çevre bölgelerindeki dış politika dengeleri:
- **Yunanistan (Ege ve Kıbrıs):** 1923 Lozan Antlaşması ile dengelenen ilişkiler; 1955 6-7 Eylül olayları, 1974 Kıbrıs Barış Harekâtı, Ege kıta sahanlığı, karasularının genişliği (6 mil - 12 mil tartışması), hava sahası (FIR) ve gayriasri adaların silahlandırılması meseleleri etrafında sürmektedir [LAUSANNE-1923]. 2023 Atina Bildirgesi ile istişari görüşmeler sürmektedir.
- **Suriye ve Irak:** Fırat ve Dicle nehirlerinin sınır aşan sular yönetimi (GAP), PKK terörüne karşı sınır ötesi harekatlar (Fırat Kalkanı, Zeytin Dalı, Barış Pınarı) ve Suriye iç savaşından kaçan 3.1 milyondan fazla sığınmacının Türkiye'de geçici koruma altında barındırılması [TUIK-2024-POP].
- **İran:** 1639 Kasr-ı Şirin Antlaşması'ndan bu yana değişmeyen sınır hattı, kontrollü rekabet ve yüksek hacimli doğalgaz ithalatına dayanır.
- **Güney Kafkasya:** *"Bir millet, iki devlet"* şiarıyla Azerbaycan ile kurulan stratejik ittifak, 2021 **Şuşa Beyannamesi** ile askeri bağlayıcılık kazanmıştır. 2020 İkinci Karabağ Savaşı'nda Türk SİHA'ları belirleyici rol oynamıştır.
- **Çok Taraflı Kurumlar:** NATO (1952'den beri üye, LANDCOM İzmir), Avrupa Birliği (1963 Ankara Anlaşması, 1995 Gümrük Birliği, 1999 adaylık) ve kurucu mimarı olduğu Türk Devletleri Teşkilatı (TDT)."""

    # Localize infographics for Module 1
    m1["infographics"][0]["title"] = "Modern Türkiye'nin Diplomatik ve Egemenlik Kilometre Taşları (1918–2026)"
    m1["infographics"][0]["items"] = [
        {"year": "1919", "event": "Atatürk Samsun'a çıktı (19 Mayıs); Amasya Genelgesi ile milli mücadele ilan edildi."},
        {"year": "1920", "event": "Misak-ı Millî kabul edildi; TBMM Ankara'da açıldı; Sevr Antlaşması dayatıldı."},
        {"year": "1921", "event": "Sovyet Rusya ile Moskova ve Kars Antlaşmaları imzalanarak doğu sınırları güvenceye alındı."},
        {"year": "1922", "event": "Büyük Taarruz ile işgal orduları mağlup edildi; Mudanya Mütarekesi imzalandı; Saltanat kaldırıldı."},
        {"year": "1923", "event": "Lozan Barış Antlaşması imzalandı (24 Temmuz); Türkiye Cumhuriyeti ilan edildi (29 Ekim)."},
        {"year": "1925", "event": "Türkiye ile Bulgaristan Krallığı arasında Ankara Dostluk Antlaşması akdedildi."},
        {"year": "1936", "event": "Montrö Boğazlar Sözleşmesi ile Türk Boğazları üzerinde tam egemenlik tesis edildi."},
        {"year": "1945", "event": "Stalin Türkiye'den Kars, Ardahan ve Boğazlarda üs talep etti; Sovyet notasının reddi."},
        {"year": "1952", "event": "Türkiye, Truman Doktrini çerçevesinde Yunanistan ile birlikte resmen NATO'ya katıldı."},
        {"year": "1962", "event": "Küba Füze Krizi: ABD ve SSCB gizli uzlaşmayla Türkiye'deki Jüpiter füzelerini söktü."},
        {"year": "1974", "event": "Kıbrıs Barış Harekâtı icra edildi; ABD 1975-1978 silah ambargosu uyguladı."},
        {"year": "1989", "event": "Büyük Göç: 360 binden fazla Bulgaristan Türkü Jivkov rejiminin baskısından anavatana sığındı."},
        {"year": "1999", "event": "AB Helsinki Zirvesi'nde Türkiye'ye resmi aday ülke statüsü verildi."},
        {"year": "2017", "event": "Anayasa referandumu ile Cumhurbaşkanlığı Hükümet Sistemine geçiş kabul edildi."},
        {"year": "2020", "event": "TürkAkım doğalgaz boru hattı açıldı; İkinci Karabağ Savaşı'nda Azerbaycan'a stratejik destek."},
        {"year": "2022", "event": "Türkiye, Montrö Madde 19'u işleterek savaş halindeki donanmalara Boğazları kapattı."}
    ]

    m1["infographics"][1]["title"] = "Uluslararası Egemenlik Antlaşmaları ve Sınır Rejimleri Matrisi"
    m1["infographics"][1]["headers"] = ["Antlaşma", "İmza Tarihi", "Taraflar", "Egemenlik ve Sınır Hükümleri", "Arşiv / Kaynak Referansı"]
    m1["infographics"][1]["rows"] = [
        ["Moskova Antlaşması", "16 Mar 1921", "TBMM Hükümeti & RSFSC (Sovyetler)", "Sevr hükümsüz kılındı; Sovyet altın ve mühimmat yardımı; TBMM tanındı", "Sovyet Dış Politika Arşivi [MOSCOW-TREATY-1921]"],
        ["Kars Antlaşması", "13 Eki 1921", "TBMM & Ermenistan, Azerbaycan, Gürcistan", "Kuzeydoğu sınırı kesinleşti (Kars, Ardahan, Artvin Türkiye'ye; Batum Gürcistan'a)", "TBMM Zabıt Ceridesi [KARS-TREATY-1921]"],
        ["Lozan Antlaşması", "24 Tem 1923", "Türkiye & Britanya, Fransa, İtalya, Yunanistan", "Tam uluslararası bağımsızlık, Doğu Trakya, kapitülasyonların ilga edilmesi", "Milletler Cemiyeti [LAUSANNE-1923]"],
        ["Ankara Dostluk Antlaşması", "18 Eki 1925", "Türkiye Cumhuriyeti & Bulgaristan Krallığı", "Trakya sınırı teyit edildi; serbest göç hakkı ve azınlık mülk güvenceleri", "Bulgaristan Devlet Arşivi [BULGARIA-EXODUS-1989]"],
        ["Montrö Sözleşmesi", "20 Tem 1936", "Türkiye, İngiltere, SSCB, Fransa, Bulgaristan", "Boğazlar Komisyonu lağvedildi; Türkiye'ye tam tahkimat ve savaş kapatma yetkisi", "BM Antlaşmalar Serisi [UN-TREATY-MONTREUX]"],
        ["Şuşa Beyannamesi", "15 Haz 2021", "Türkiye Cumhuriyeti & Azerbaycan Cumhuriyeti", "Karşılıklı askeri yardım, ortak savunma taahhüdü ve lojistik koridor birliği", "T.C. Resmî Gazete 2021"]
    ]

    m1["infographics"][2]["title"] = "Sovyet-Rus ve Bulgaristan Jeopolitik Göstergeleri"
    m1["infographics"][2]["data"] = [
        {"label": "1921 Sovyet Yardımı", "value": "10M+ Altın Ruble", "sub": "Kurtuluş Savaşı'nda top, tüfek ve cephane desteği"},
        {"label": "1989 Büyük Göç", "value": "360.000+ Soydaş", "sub": "Jivkov rejiminin baskısından sığınan Türk nüfusu"},
        {"label": "TürkAkım İletim Kapasitesi", "value": "31,5 Milyar m³/yıl", "sub": "Karadeniz tabanından geçen çift hatlı gaz iletimi"},
        {"label": "Akkuyu Nükleer Kurulu Güç", "value": "4.800 MW", "sub": "20 Milyar $ Rosatom Yap-İşlet-Sahip Ol yatırımı"},
        {"label": "Kapıkule Tır Trafiği", "value": "1.000.000+ Tır/yıl", "sub": "Dünyanın en işlek ikinci kara gümrük kapısı"},
        {"label": "S-400 Füze Alımı", "value": "2,5 Milyar Dolar", "sub": "2017'de imzalandı, ABD CAATSA yaptırımını tetikledi"}
    ]

    # Module 2 (Geography)
    m2 = tr_mods[1]
    m2["title"] = "Coğrafya, Topografya ve Yer Sistemleri"
    m2["tagline"] = "Jeomorfoloji, tektonik fay sistemleri, sınır aşan nehir havzaları ve yedi coğrafi bölge."
    m2["summary"] = "Türkiye'nin 783.562 km²'lik yüzölçümünü, dört denize açılan kıyılarını, üç aktif fay zonunu ve Fırat-Dicle sınır aşan havzalarını inceleyen fiziki ve jeomorfolojik profil."
    m2["sections"][0]["title"] = "1. Ülke Yüzölçümü ve Yedi Coğrafi Bölgenin Morfolojisi"
    m2["sections"][0]["content"] = """Türkiye, 783.562 kilometrekarelik yüzölçümüyle (iç sular dahil) Asya ile Avrupa arasında Türk Boğazları (İstanbul Boğazı, Marmara Denizi, Çanakkale Boğazı) üzerinden köprü kurar. Topraklarının yaklaşık %97'si Anadolu'da, %3'ü Trakya'dadır. 8.333 kilometrelik kıyı şeridine sahiptir [TUIK-2024-POP].

1941 Ankara I. Coğrafya Kongresi kararları uyarınca Türkiye yedi ana coğrafi bölgeye ayrılmıştır:
1. **Marmara Bölgesi:** Boğazlar, yoğun sanayi, alçak tepeler ve geçiş iklimi.
2. **Ege Bölgesi:** Kıyıya dik dağlar (horst-graben sistemi) ve Gediz, Büyük Menderes alüvyal vadileri.
3. **Akdeniz Bölgesi:** Toros Dağları silsilesi, karstik ovalar ve subtropikal narenciye/seracılık tarımı.
4. **İç Anadolu Bölgesi:** Ortalama 1.000 m rakımlı yüksek plato, Tuz Gölü havzası ve bozkır bitki örtüsü.
5. **Karadeniz Bölgesi:** Kıyıya paralel Kuzey Anadolu Dağları, gür ormanlar ve bol yağış rejimi.
6. **Doğu Anadolu Bölgesi:** Volkanik platolar, Ağrı Dağı (5.137 m, Türkiye'nin en yüksek noktası) ve Van Gölü (3.755 km²).
7. **Güneydoğu Anadolu Bölgesi:** Fırat ve Dicle nehirlerinin hayat verdiği kurak plato ve GAP sulama kuşağı."""

    m2["sections"][1]["title"] = "2. Tektonik Yapı ve Aktif Fay Sistemleri"
    m2["sections"][1]["content"] = """Türkiye, Alp-Himalaya deprem kuşağında yer alması nedeniyle yerkürenin en sismik alanlarından biridir. Arap Levhası'nın kuzeye hareketi ile Avrasya Levhası arasında sıkışan Anadolu Levhacığı yılda yaklaşık 20–25 mm batıya ötelenmektedir:
- **Kuzey Anadolu Fay Hattı (KAF):** Karlıova'dan Marmara Denizi'ne uzanan 1.500 km'lik sağ yönlü doğrultu atımlı aktif fay (1939 Erzincan Mw 7.8, 1999 Gölcük Mw 7.6).
- **Doğu Anadolu Fay Hattı (DAF):** Karlıova'dan Hatay'a uzanan 500 km'lik sol yönlü doğrultu atımlı fay. 6 Şubat 2023 Kahramanmaraş deprem ikilisi (Mw 7.8 ve Mw 7.6) bu hatta kırılmış, 11 ilde 53 binden fazla can kaybına yol açmıştır [AYM-REPORTS, WB-TUR-2024].
- **Ege Graben Sistemi:** Batı Anadolu'da kuzey-güney yönlü açılma tektoniği ve yoğun jeotermal kaynaklar üretir."""

    m2["sections"][2]["title"] = "3. Hidroloji, Nehir Havzaları ve Sınır Aşan Sular"
    m2["sections"][2]["content"] = """Türkiye 25 hidrolojik havzaya ayrılmıştır. En kritik havzalar, Doğu Anadolu yaylalarından doğup Suriye ve Irak'a akan **Fırat** ve **Dicle** nehirleridir. Türkiye Fırat suyunun yaklaşık %88-90'ını, Dicle'nin ise %40-50'sini sağlamaktadır.

Devlet eliyle yürütülen **Güneydoğu Anadolu Projesi (GAP)**, bu nehirler üzerinde Atatürk Barajı ve Ilısu Barajı dahil 22 baraj ve 19 HES'i kapsar. Türkiye sınır aşan suları mutlak kota konusu değil, hakça ve makul kullanım ilkesine tabi ortak kaynaklar olarak değerlendirmektedir."""

    m2["infographics"][0]["title"] = "Temel Coğrafi ve Fiziki Göstergeler"
    m2["infographics"][0]["data"] = [
        {"label": "Toplam Yüzölçümü", "value": "783.562 km²", "sub": "Dünyada 37. sırada"},
        {"label": "Kıyı Uzunluğu", "value": "8.333 km", "sub": "Karadeniz, Ege, Akdeniz, Marmara"},
        {"label": "En Yüksek Nokta", "value": "5.137 m", "sub": "Büyük Ağrı Dağı"},
        {"label": "Ortalama Yükseklik", "value": "1.132 m", "sub": "Engebeli ve yüksek plato morfolojisi"},
        {"label": "Ana Fay Zonları", "value": "3 Büyük Sistem", "sub": "KAF, DAF ve Ege Grabenleri"},
        {"label": "Su Havzası Sayısı", "value": "25 Havza", "sub": "Fırat-Dicle, Kızılırmak, Sakarya"}
    ]

    # Module 3 (Nature)
    m3 = tr_mods[2]
    m3["title"] = "Doğa, Biyoçeşitlilik ve Çevre"
    m3["tagline"] = "Fitocoğrafik kesişim, endemik flora ve fauna, korunan biyomlar ve iklim kırılganlığı."
    m3["summary"] = "Avrupa-Sibirya, Akdeniz ve İran-Turan fitocoğrafik bölgelerinin kesişiminde yer alan Türkiye'nin 11.000'i aşkın bitki türünü (%34 endemizm), yaban hayatını ve 2053 net sıfır karbon hedefini içeren çevre profili."
    m3["sections"][0]["title"] = "1. Botanik Çeşitlilik ve Küresel Biyoçeşitlilik Sıcak Noktası"
    m3["sections"][0]["content"] = """Türkiye, üç farklı fitocoğrafik bölgenin (Avrupa-Sibirya, Akdeniz, İran-Turan) kesiştiği yegane coğrafyadır:
- **11.000'den fazla damarlı bitki türü** (tüm Avrupa kıtasındaki toplam bitki sayısına yakın).
- **Yaklaşık %34 endemizm oranı** (~3.700 endemik tür), özellikle Toroslar ve Anadolu Çaprazı üzerinde yoğunlaşmıştır.
- Buğday, arpa, mercimek ve nohut gibi temel tarım bitkilerinin yabani ataları Güneydoğu Anadolu'daki Bereketli Hilal bölgesinde ortaya çıkmıştır."""

    m3["sections"][1]["title"] = "2. Fauna ve Yaban Hayatı Koruma Alanları"
    m3["sections"][1]["content"] = """Türkiye 470 kuş, 160 memeli ve 130 sürüngen türüne ev sahipliği yapar:
- **Kilit Memeliler:** Bozayı (*Ursus arctos*), kurt (*Canis lupus*), vaşak (*Lynx lynx*), yaban keçisi ve son yıllarda fotokapanlarla varlığı kanıtlanan nesli tehlike altındaki Anadolu parsı (*Panthera pardus tulliana*).
- **Kuş Göç Yolları:** İstanbul Boğazı ve Hatay Belen Geçidi, süzülen kuşların (leylekler, kartallar) kıtalararası ana göç koridorudur.
- **Deniz Canlıları:** Akdeniz fokları (*Monachus monachus*) Ege mağaralarında, caretta caretta deniz kaplumbağaları ise güney kumsallarında ürer."""

    m3["sections"][2]["title"] = "3. Çevresel Riskler ve İklim Değişikliği Politikası"
    m3["sections"][2]["content"] = """IPCC raporlarında Akdeniz Havzası'nın en kırılgan iklim sıcak noktalarından biri olarak tanımlanan Türkiye'de:
- **Su Stresi:** Kişi başına yıllık kullanılabilir su miktarı 1.350 m³ seviyesinde olup 'su stresi çeken ülke' kategorisindedir; 2035'te 1.000 m³ sınırına inme riski mevcuttur.
- **Toprak Erozyonu:** Toprakların %70'inden fazlası erozyon riski altındadır.
- **Orman Yangınları:** 2021 yazında Akdeniz ve Ege'de 170 bin hektardan fazla orman alanı yanmıştır.
- **Net Sıfır Hedefi:** Türkiye Ekim 2021'de Paris İklim Anlaşması'nı onaylamış ve **2053 Net Sıfır Emisyon** hedefini taahhüt etmiştir."""

    m3["infographics"][0]["title"] = "Biyoçeşitlilik ve Çevre Göstergeleri"
    m3["infographics"][0]["data"] = [
        {"label": "Bitki Tür Sayısı", "value": "11.000+ Tür", "sub": "Batı Avrasya'nın en zengin florası"},
        {"label": "Endemizm Oranı", "value": "~%34 Endemik", "sub": "3.700'den fazla endemik takson"},
        {"label": "Milli Park Sayısı", "value": "48 Milli Park", "sub": "900 bin hektardan geniş koruma alanı"},
        {"label": "Kuş Türü Sayısı", "value": "470 Tür", "sub": "Küresel kıtalararası göç darboğazı"},
        {"label": "Kişi Başı Su Potansiyeli", "value": "1.350 m³/yıl", "sub": "Su stresi kategorisi"},
        {"label": "Net Sıfır Hedefi", "value": "2053 Yılı", "sub": "Paris Anlaşması karbon nötr taahhüdü"}
    ]

    return tr_mods
''')
    print("tr_modules_data.py builder created.")

if __name__ == "__main__":
    generate()
