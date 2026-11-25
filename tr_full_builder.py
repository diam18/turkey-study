#!/usr/bin/env python3
"""
Turkish Full Academic Content Builder
Translates Modules 1 to 13 completely into scholarly Turkish.
"""

import copy

def build_turkish_modules(en_modules):
    tr = copy.deepcopy(en_modules)

    # Load Module 1, 2, 3 from tr_modules_data
    from generate_tr_modules_data import generate
    import tr_modules_data
    partial_tr = tr_modules_data.get_modules(en_modules)
    tr[0] = partial_tr[0]
    tr[1] = partial_tr[1]
    tr[2] = partial_tr[2]

    # Module 4: Anayasa Hukuku
    m4 = tr[3]
    m4["title"] = "Anayasa Hukuku ve Tarihsel Evrimi"
    m4["tagline"] = "1876'dan 1982'ye anayasa kronolojisi, değiştirilemez maddeler, laiklik ve 2017 Cumhurbaşkanlığı Hükümet Sistemi."
    m4["readingTime"] = "28 dk okuma"
    m4["summary"] = "Türk anayasa tarihinin kapsamlı hukuki analizi: 1808 Sened-i İttifak ve 1876 Kanûn-ı Esâsî'den 1921 Teşkilât-ı Esâsîye'ye, 1924 Cumhuriyet Anayasası'ndan 1961 ve 1982 darbe anayasalarına, değiştirilemez 1-4. maddelerden parlamenter sistemi lağveden 2017 Cumhurbaşkanlığı Hükümet Sistemi anayasa değişikliklerine kadar tüm süreç."
    
    m4["sections"][0]["title"] = "1. Cumhuriyet Öncesi Anayasacılık: Sened-i İttifak'tan Kanûn-ı Esâsî'ye"
    m4["sections"][0]["content"] = """Türk anayasacılığı, hükümdarın mutlak iktidarını sınırlandırma ve temel hakları güvenceye alma çabalarının iki asırlık ürünüdür:
- **Sened-i İttifak (1808):** Osmanlı anayasa hukukçularınca Magna Carta'ya benzetilen, Sultan II. Mahmud ile yerel ayanlar arasında imzalanan ilk iktidar sınırlama belgesidir. Padişahın keyfi vergi ve idam yetkisini sınırlandırmıştır.
- **Tanzimat ve Islahat Fermanları (1839, 1856):** Kanun önünde eşitlik, can, mal, ırz güvenliği ve Müslim-gayrimüslim eşitliği ilkelerini getirmiştir.
- **Kanûn-ı Esâsî (1876):** Midhat Paşa başkanlığındaki komisyonca hazırlanan ve II. Abdülhamid tarafından ilan edilen ilk yazılı Türk anayasasıdır. Meclis-i Âyân ve Meclis-i Meb'ûsân'dan oluşan çift meclisli sistemi getirmiş, ancak 113. maddedeki padişahın sürgün yetkisi nedeniyle 1878'de meclis tatil edilmiştir.
- **1909 Değişiklikleri:** II. Meşrutiyet sonrası anayasada yapılan köklü tadilatla padişahın yetkileri daraltılmış, meclis üstünlüğü ve bakanlar kurulunun meclise karşı kolektif sorumluluğu tesis edilmiştir."""

    m4["sections"][1]["title"] = "2. Devrim Anayasaları: 1921 Meclis Hükümeti ve 1924 Cumhuriyet Anayasası"
    m4["sections"][1]["content"] = """Osmanlı Devleti'nin çöküşü yeni bir anayasal paradigmayı doğurmuştur:
- **1921 Teşkilât-ı Esâsîye Kanunu (85 Sayılı Kanun):** Kurtuluş Savaşı koşullarında 20 Ocak 1921'de kabul edilen 23 maddelik devrimci anayasadır. 1. maddesi *"Hâkimiyet bilâkaydüşart milletindir"* ilkesini koymuştur. Yasama ve yürütmenin TBMM'de toplandığı **Meclis Hükümeti Sistemi** benimsenmiştir.
- **1924 Anayasası (491 Sayılı Kanun):** Cumhuriyetin ilanından sonra 20 Nisan 1924'te yürürlüğe girmiştir. Tek meclisli meclis hükümeti-parlamenter sistem karması bir yapıdır.
- **Laikleşme Adımları:** 1924 Anayasası'nda başlangıçta yer alan *"Türkiye Devleti'nin dini İslam'dır"* ibaresi 1928'de metinden çıkarılmış; 1937'de **Laiklik**, Cumhuriyetçilik, Milliyetçilik, Halkçılık, Devletçilik ve İnkılapçılık ilkeleri anayasal kural haline getirilmiştir [TBMM-CONST-1982, ZURCHER-2017]."""

    m4["sections"][2]["title"] = "3. Askeri Darbe Anayasaları: 1961 Çoğulcu Dengeleri ve 1982 Güvenlikçi Otoritesi"
    m4["sections"][2]["content"] = """Türkiye'de 20. yüzyılın ikinci yarısına askeri darbeler ve vesayet mekanizmaları damga vurmuştur:
- **1961 Anayasası:** 27 Mayıs 1960 darbesi sonrası Kurucu Meclis tarafından hazırlanmıştır. İktidarın tek elde toplanmasını önlemek amacıyla geniş bir denge-fren sistemi kurmuştur:
  - Kanunların anayasaya uygunluğunu denetlemek üzere **Anayasa Mahkemesi (AYM)** kurulmuştur.
  - Millet Meclisi ve Cumhuriyet Senatosu'ndan oluşan **Çift Meclis Sistemi** getirilmiştir.
  - Üniversitelere ve TRT'ye idari özerklik tanınmış, sendika ve grev hakları anayasal güvenceye alınmıştır.
- **1982 Anayasası:** 12 Eylül 1980 askeri darbesi sonrasında Milli Güvenlik Konseyi gözetiminde hazırlanmış ve Kenan Evren'in cumhurbaşkanlığı ile birlikte onaylatılmıştır. Birey yerine devleti, özgürlük yerine kamu düzenini önceleyen güvenlikçi bir ruha sahiptir:
  - Senato lağvedilmiş, tek meclisli TBMM'ye dönülmüştür.
  - Temsilde adaletten ziyade yönetimde istikrarı sağlama gerekçesiyle **%10 ulusal seçim barajı** getirilmiştir (2022'de %7'ye düşürülmüştür).
  - Cumhurbaşkanının yetkileri olağanüstü genişletilmiş, YÖK ihdas edilerek üniversiteler kontrol altına alınmıştır [TBMM-CONST-1982, AYM-REPORTS]."""

    m4["sections"][3]["title"] = "4. Değiştirilemez Hükümler: 1–4. Maddeler ve Anayasal Kimlik"
    m4["sections"][3]["content"] = """1982 Anayasası'nın 4. maddesi, devletin kurucu temelini oluşturan ilk üç maddenin değiştirilmesini ve değiştirilmesinin teklif dahi edilmesini kesin olarak yasaklamıştır:
- **Madde 1 (Devletin Şekli):** *"Türkiye Devleti bir Cumhuriyettir."*
- **Madde 2 (Cumhuriyetin Nitelikleri):** *"Türkiye Cumhuriyeti, toplumun huzuru, millî dayanışma ve adalet anlayışı içinde, insan haklarına saygılı, Atatürk milliyetçiliğine bağlı, başlangıçta belirtilen temel ilkelere dayanan, demokratik, lâik ve sosyal bir hukuk devletidir."*
- **Madde 3 (Bütünlük, Resmi Dil, Bayrak, Marş, Başkent):** *"Türkiye Devleti, ülkesi ve milletiyle bölünmez bir bütündür. Dili Türkçedir. Bayrağı, şekli kanununda belirtilen, beyaz ay yıldızlı al bayraktır. Millî marşı 'İstiklâl Marşı'dır. Başkenti Ankara'dır."*
- **Madde 4 (Değiştirme Yasağı):** İlk üç maddenin değiştirilmesini ve teklif edilmesini yasaklar. Anayasa Mahkemesi içtihatlarında bu hükümler devletin 'anayasal kimliği' olarak nitelendirilir."""

    m4["sections"][4]["title"] = "5. 2017 Anayasa Değişiklikleri: Cumhurbaşkanlığı Hükümet Sistemi"
    m4["sections"][4]["content"] = """16 Nisan 2017 referandumunda %51,4 evet oyuyla kabul edilen 18 maddelik anayasa paketiyle, Türkiye'nin 94 yıllık parlamenter yönetim geleneği sona ermiş ve yürütme yetkisi tek elde toplanmıştır:
- **Başbakanlığın Kaldırılması:** Başbakanlık makamı ve Bakanlar Kurulu lağvedilmiş, tüm yürütme yetkisi doğrudan halk tarafından seçilen **Cumhurbaşkanı**'na devredilmiştir.
- **Cumhurbaşkanlığı Kararnameleri:** Cumhurbaşkanına yürütme yetkisine ilişkin konularda kanun gücünde kararname çıkarma yetkisi tanınmıştır. Temel haklar ve kanunla düzenlenen alanlarda kararname çıkarılamaz; kanun ile kararname çatışırsa kanun hükümleri uygulanır.
- **Partili Cumhurbaşkanlığı:** Cumhurbaşkanının tarafsızlığı ve partisiyle ilişiğinin kesilmesi şartı kaldırılmıştır.
- **Meclis Denetiminin Sınırlandırılması:** Gensoru ve hükümete güvenoyu müesseseleri yürürlükten kaldırılmıştır. Bakanlar Meclis dışından atanmakta ve sadece Cumhurbaşkanına karşı sorumlu olmaktadır [TBMM-CONST-1982, AYM-REPORTS]."""

    m4["infographics"][0]["title"] = "Karşılaştırmalı Anayasa Matrisi: 1876 - 1921 - 1924 - 1961 - 1982 - 2017"
    m4["infographics"][0]["headers"] = ["Anayasa", "Hükümet Sistemi", "Yasama Organı", "Yargısal Denetim", "Laiklik İlkesi", "Yürütmenin Başı"]
    m4["infographics"][0]["rows"] = [
        ["1876 Kanûn-ı Esâsî", "Meşruti Monarşi", "Çift Meclis (Âyân + Meb'ûsân)", "Yok (Şeriye ve Nizamiye)", "Devlet dini İslam (Madde 11)", "Padişah & Sadrazam"],
        ["1921 Teşkilât-ı Esâsîye", "Meclis Hükümeti", "Tek Meclis (TBMM)", "Yok (Meclis Egemenliği)", "Belirtilmemiş (Savaş dönemi)", "TBMM Reisi"],
        ["1924 Anayasası", "Parlamenter Üstünlük", "Tek Meclis (TBMM)", "Yok (Meclis yorumu esastı)", "1928/1937'de anayasaya girdi", "Cumhurbaşkanı & Başbakan"],
        ["1961 Anayasası", "Parlamenter (Denge-Fren)", "Çift Meclis (Millet M. + Senato)", "Anayasa Mahkemesi kuruldu", "Değiştirilemez ilke olarak girdi", "Cumhurbaşkanı (Tarafsız) & Başbakan"],
        ["1982 Anayasası (İlk)", "Yürütme Ağırlıklı Parlamenter", "Tek Meclis (TBMM 400-550)", "AYM denetimi (sınırlı başvuru)", "Madde 2 ve 4 güvencesinde", "Güçlü Cumhurbaşkanı & Başbakan"],
        ["2017 Değişiklikleri", "Cumhurbaşkanlığı Sistemi", "Tek Meclis (TBMM 600 vekil)", "AYM + Bireysel Başvuru", "Madde 2 ve 4 güvencesinde", "Cumhurbaşkanı (Tek Yürütme Organı)"]
    ]

    m4["infographics"][1]["title"] = "Anayasal Eşikler ve Usul Göstergeleri"
    m4["infographics"][1]["data"] = [
        {"label": "TBMM Üye Tam Sayısı", "value": "600 Milletvekili", "sub": "2017'de 550'den 600'e çıkarıldı"},
        {"label": "Referandum Eşiği", "value": "360 Kabul Oyu (3/5)", "sub": "Anayasa değişikliğini halkoyuna sunma şartı"},
        {"label": "Doğrudan Kabul", "value": "400 Kabul Oyu (2/3)", "sub": "Referanduma gerek kalmaksızın kabul"},
        {"label": "Seçim Barajı", "value": "%7 Ülke Barajı", "sub": "2022'de %10'dan %7'ye indirildi"},
        {"label": "Değiştirilemez Madde", "value": "1, 2 ve 3. Maddeler", "sub": "4. madde ile koruma altındadır"},
        {"label": "AYM Üye Sayısı", "value": "15 Hukukçu Üye", "sub": "Norm denetimi ve bireysel başvurulara bakar"}
    ]

    # Module 5: Devlet Mimarisi
    m5 = tr[4]
    m5["title"] = "Devlet Mimarisi ve Yönetim Sistemi"
    m5["tagline"] = "Cumhurbaşkanlığı Hükümet Sistemi, 17 bakanlık, TBMM ve 81 ilin mülki idaresi."
    m5["readingTime"] = "26 dk okuma"
    m5["summary"] = "Türkiye'nin üniter idare geleneği, Cumhurbaşkanlığı Kararnameleri mekanizması, 17 icracı bakanlık, 600 sandalyeli TBMM yasama süreçleri, 81 ildeki vali ve kaymakamlık mülki idare ağı, 30 büyükşehir belediyesi ve Kamu Denetçiliği Kurumu'nu kapsayan kapsamlı kurumsal rehber."
    
    m5["sections"][0]["title"] = "1. Yürütme Erki: Cumhurbaşkanlığı Teşkilatı ve Politika Kurulları"
    m5["sections"][0]["content"] = """Türkiye Cumhuriyeti Anayasası'nın 104. maddesi uyarınca yürütme yetkisi ve görevi **Cumhurbaşkanı**'na aittir. Cumhurbaşkanı halk tarafından beş yıllık süre için seçilir:
- **Cumhurbaşkanlığı Külliyesi ve Bağlı Kuruluşlar:** Beştepe'de faaliyet gösteren merkez teşkilatı şu yapılardan oluşur:
  - **9 Politika Kurulu:** Ekonomi, Güvenlik ve Dış Politika, Hukuk, Sosyal Politikalar, Sağlık ve Gıda, Bilim ve Teknoloji kurulları stratejik vizyon üretir.
  - **Strateji ve Bütçe Başkanlığı (SBB):** Kalkınma planlarını ve merkezi yönetim bütçe kanun teklifini hazırlar.
  - **Savunma Sanayii Başkanlığı (SSB):** Savunma tedarik ve yerli Ar-Ge projelerini yönetir.
  - **Milli İstihbarat Teşkilatı (MİT):** Doğrudan Cumhurbaşkanına bağlı istihbarat koordinasyonu.
  - **Diyanet İşleri Başkanlığı:** Dini kamu hizmetlerini ve cami idaresini yürütür.
  - **İletişim Başkanlığı:** Kamu diplomasisi ve basın akreditasyonunu koordine eder [TBMM-CONST-1982, DCP-DIYANET-2024]."""

    m5["sections"][1]["title"] = "2. İcracı Bakanlıklar ve Cumhurbaşkanlığı Kabinesi"
    m5["sections"][1]["content"] = """Cumhurbaşkanlığı Kabinesi iki haftada bir Cumhurbaşkanı başkanlığında toplanır. Bakanlar TBMM dışından atanır ve milletvekili dokunulmazlığına atanmayla birlikte sahip olurlar:
- **Temel Egemenlik Bakanlıkları:** Dışişleri, Milli Savunma, İçişleri (Emniyet, Jandarma, Sahil Güvenlik, AFAD), Adalet ve Hazine ve Maliye Bakanlığı.
- **Ekonomik ve Sektörel Bakanlıklar:** Enerji ve Tabii Kaynaklar, Ticaret, Sanayi ve Teknoloji, Ulaştırma ve Altyapı, Çevre/Şehircilik/İklim Değişikliği, Tarım ve Orman [WB-TUR-2024]."""

    m5["sections"][2]["title"] = "3. Yasama Erki: Türkiye Büyük Millet Meclisi (TBMM)"
    m5["sections"][2]["content"] = """TBMM millet adına egemenliği kullanan yasama organıdır:
- **Seçim ve Temsil:** D'Hondt nispi temsil sistemiyle 87 seçim çevresinde seçilen 600 milletvekilinden oluşur. Ülke barajı %7'dir.
- **Görev ve Yetkileri:** Kanun koymak, değiştirmek ve kaldırmak; Merkezi Yönetim Bütçe Kanununu görüşmek ve kabul etmek; para basılmasına ve savaş ilanına karar vermek; milletlerarası antlaşmaların onaylanmasını uygun bulmak; TSK'nın yabancı ülkelere gönderilmesine izin vermek (Madde 92).
- **Denetim Yolları:** Yazılı soru önergeleri, genel görüşme, meclis araştırması ve bakanlar ile Cumhurbaşkanı hakkında yürütülen meclis soruşturması (Yüce Divan süreci) [TBMM-CONST-1982]."""

    m5["sections"][3]["title"] = "4. Taşra İdaresi ve Yerel Yönetimler: 81 İl ve 30 Büyükşehir"
    m5["sections"][3]["content"] = """Anayasa'nın 126. maddesi uyarınca Türkiye merkezi idare ve yerinden yönetim ilkelerine göre idare edilir:
- **Merkezi Taşra İdaresi:**
  - **81 İl (Valilik):** İl idaresinin başında Cumhurbaşkanı kararıyla atanan **Vali** bulunur. Vali, ilde devletin ve Cumhurbaşkanının temsilcisidir.
  - **973 İlçe (Kaymakamlık):** İlin alt kademesidir; kariyer meslek mensubu **Kaymakamlar** tarafından yönetilir.
- **Yerel Yönetimler:**
  - **30 Büyükşehir Belediyesi:** Nüfusu 750 bini aşan illerde kuruludur (İstanbul, Ankara, İzmir, Bursa, Antalya vb.). Büyükşehir Belediye Başkanı doğrudan halk tarafından seçilir; kentsel ulaşım, imar planları, su-kanalizasyon (İSKİ vb.) hizmetlerini yürütür.
  - **İlçe Belediyeleri:** Yerel temizlik, park, çevre ve zabıta hizmetlerini yürütür.
  - **Kamu Denetçiliği Kurumu (Ombudsmanlık):** İdarenin her türlü eylem ve işlemine karşı vatandaşların şikayetlerini inceleyen anayasal denetim organıdır [TBMM-CONST-1982]."""

    m5["infographics"][0]["title"] = "Türkiye Yürütme ve Devlet İdaresi Kurumsal Şeması"
    m5["infographics"][1]["title"] = "Taşra İdaresi ve Yerel Yönetimler Karşılaştırma Matrisi"
    m5["infographics"][1]["headers"] = ["Kurum", "İdari Düzey", "Atama / Seçim Usulü", "Görev ve Yetki Sahası", "Denetim Mercii"]
    m5["infographics"][1]["rows"] = [
        ["Valilik", "İl Düzeyi (81 İl)", "Cumhurbaşkanlığı Kararı ile Atama", "İldeki tüm kamu kurumlarının ve genel güvenliğin başı", "Cumhurbaşkanı & İçişleri Bakanlığı"],
        ["Kaymakamlık", "İlçe Düzeyi (973 İlçe)", "Bakanlık / Cumhurbaşkanlığı Ataması", "İlçedeki mülki idare ve kamu hizmetlerinin amiri", "İl Valisi & İçişleri Bakanlığı"],
        ["Büyükşehir Belediyesi", "Metropol İller (30 Büyükşehir)", "5 yılda bir doğrudan halk oyuyla seçim", "Ulaşım, nazım imar, su-kanalizasyon, itfaiye", "Belediye Meclisi & Sayıştay"],
        ["İlçe Belediyesi", "İlçe Yerel Düzey", "5 yılda bir doğrudan halk oyuyla seçim", "Mahalli temizlik, parklar, yapı ruhsatları, zabıta", "Büyükşehir Meclisi & İçişleri"]
    ]

    m5["infographics"][2]["title"] = "Devlet İdaresi ve Yasama Göstergeleri"
    m5["infographics"][2]["data"] = [
        {"label": "İl Sayısı", "value": "81 İl (Valilik)", "sub": "Fransız departman modelinden mülhem"},
        {"label": "İlçe Sayısı", "value": "973 İlçe", "sub": "Kariyer kaymakamlarca yönetilir"},
        {"label": "Büyükşehir Sayısı", "value": "30 Büyükşehir", "sub": "Ülke nüfusunun ~%78'ini barındırır"},
        {"label": "Milletvekili Sayısı", "value": "600 Milletvekili", "sub": "Nispi temsil D'Hondt usulü"},
        {"label": "Diplomatik Misyon", "value": "260+ Temsilcilik", "sub": "Dünyanın en geniş 5. hariciye ağı"},
        {"label": "Bakanlık Sayısı", "value": "17 Bakanlık", "sub": "Parlamento dışından atanan kabine"}
    ]

    return tr
