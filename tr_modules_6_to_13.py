#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deep Turkish academic texts for Modules 6 through 13.
"""

def enrich(tr):
    # Module 6: Silahlı Kuvvetler
    m6 = tr[5]
    m6["title"] = "Silahlı Kuvvetler ve Sivil-Asker İlişkileri"
    m6["tagline"] = "TSK yapısı, askeri vesayet ve darbeler tarihi, 2016 sonrası sivil dönüşüm ve yerli savunma sanayii."
    m6["readingTime"] = "30 dk okuma"
    m6["summary"] = "Türk Silahlı Kuvvetleri'nin (TSK) NATO içindeki konumu, Kara, Deniz (Mavi Vatan) ve Hava kuvvetleri doktrini; ordunun siyasetteki vesayet rolü ve askeri müdahaleler tarihi (1960, 1971, 1980, 1997, 2016); 15 Temmuz darbe girişimi sonrası sivil otoriteye bağlanması ve yerli savunma sanayi ekosistemi (SSB, Aselsan, Baykar, TUSAŞ)."
    
    m6["sections"][0]["title"] = "1. Askeri Teşkilat, Stratejik Doktrin ve NATO Görevleri"
    m6["sections"][0]["content"] = """Türk Silahlı Kuvvetleri (TSK), yaklaşık 425.000 muvazzaf personeliyle NATO'nun ABD'den sonraki en büyük ikinci ordusudur:
- **Kuvvet Komutanlıkları:**
  - **Kara Kuvvetleri Komutanlığı:** Dört orduya ayrılmıştır: 1. Ordu (İstanbul/Trakya), 2. Ordu (Malatya/Suriye-Irak sınırı), 3. Ordu (Erzincan/Kafkaslar) ve Ege Ordusu / 4. Ordu (İzmir).
  - **Deniz Kuvvetleri Komutanlığı:** **'Mavi Vatan'** deniz doktrini çerçevesinde Karadeniz, Ege ve Doğu Akdeniz'de 462.000 km²'lik deniz yetki alanlarını savunur. Envanterinde Milgem Ada sınıfı korvetler, havadan bağımsız tahrikli Reis sınıfı denizaltılar ve amfibi SİHA gemisi **TCG Anadolu (L-400)** bulunur.
  - **Hava Kuvvetleri Komutanlığı:** F-16 filoları, yerli Özgür modernizasyonu, havadan erken ihbar uçakları (HİK) ve gelişmiş insansız hava araçlarını yönetir.
- **NATO Entegrasyonu:** Türkiye 1952'den beri NATO üyesidir. İzmir'de NATO Müttefik Kara Komutanlığı (LANDCOM), Adana İncirlik Hava Üssü ve Malatya Kürecik balistik füze radar üssü bulunmaktadır [SIPRI-2024-MLX]."""

    m6["sections"][1]["title"] = "2. Siyasi Bir Güç Olarak Ordu: Vesayet Geleneği ve Darbeler Kronolojisi"
    m6["sections"][1]["content"] = """Cumhuriyet tarihi boyunca subay kadrosu kendisini devrimlerin ve laik cumhuriyetin nihai koruyucusu olarak görmüş ve sivil siyasete doğrudan müdahale etmiştir:
- **27 Mayıs 1960 Darbesi:** Milli Birlik Komitesi (MBK) Başbakan Adnan Menderes'in Demokrat Parti hükümetini devirmiş; Menderes, Fatin Rüştü Zorlu ve Hasan Polatkan Yassıada yargılamaları sonrası idam edilmiştir.
- **12 Mart 1971 Muhtırası:** Genelkurmay Başkanı Memduh Tağmaç ve kuvvet komutanlarının muhtırasıyla Başbakan Süleyman Demirel istifaya zorlanmıştır.
- **12 Eylül 1980 Askeri Darbesi:** Sokak çatışmaları ve siyasi kilitlenme gerekçesiyle Orgeneral Kenan Evren liderliğindeki cunta meclisi feshetmiş, partileri kapatmış, 650 bin kişiyi gözaltına almış ve 1982 Anayasasını yürürlüğe koymuştur.
- **28 Şubat 1997 Post-Modern Darbesi:** Milli Güvenlik Kurulu'nun (MGK) 18 maddelik kararlarıyla Necmettin Erbakan'ın Refahyol hükümeti istifaya zorlanmıştır.
- **27 Nisan 2007 E-Muhtırası:** Abdullah Gül'ün cumhurbaşkanlığı seçimine karşı Genelkurmay internet sitesinden yayımlanan bildiri sivil hükümet tarafından reddedilmiştir [ZURCHER-2017]."""

    m6["sections"][2]["title"] = "3. 15 Temmuz 2016 Darbe Girişimi ve TSK'nın Sivilleşme Reformları"
    m6["sections"][2]["content"] = """15 Temmuz 2016 gecesi ordu içindeki FETÖ cuntası tarafından kalkışılan kanlı darbe girişimi, halkın sokaklara çıkarak tanklara direnmesi ve sivil iradenin arkasında durmasıyla bastırılmış, 251 vatandaş şehit olmuştur. Ardından cumhuriyet tarihinin en köklü sivil-asker reformları yapılmıştır:
- **Genelkurmay'ın Bakanlığa Bağlanması:** Genelkurmay Başkanı ve Kara, Deniz, Hava kuvvet komutanları **doğrudan sivil Milli Savunma Bakanı'na (MSB)** bağlanmıştır.
- **Jandarma ve Sahil Güvenliğin Ayrılması:** Jandarma ve Sahil Güvenlik TSK yapısından tamamen çıkarılarak İçişleri Bakanlığı'na bağlanmıştır.
- **YAŞ'ın Sivilleşmesi:** Yüksek Askeri Şûra'da sivil bakanlar çoğunluğu ele geçirmiştir.
- **Milli Savunma Üniversitesi (MSÜ):** Askeri liseler kapatılmış, subay yetiştirme görevi sivil rektör yönetimindeki MSÜ'ye verilmiştir [TBMM-CONST-1982]."""

    m6["sections"][3]["title"] = "4. Yerli Savunma Sanayii Ekosistemi: SSB, Aselsan, Baykar ve TUSAŞ"
    m6["sections"][3]["content"] = """1974 Kıbrıs Barış Harekâtı sonrası uygulanan silah ambargoları yerli savunma hamlesini başlatmıştır. Savunma Sanayii Başkanlığı (SSB) koordinasyonunda:
- **Yerlilik Oranı:** 2000'lerin başında %20 seviyesinde olan yerlilik oranı **%80'in üzerine** çıkmıştır.
- **Öncü Şirketler:**
  - **ASELSAN:** Radar, elektronik harp (KORAL), elektro-optik ve askeri telsiz sistemleri.
  - **Baykar Teknoloji:** Dünyaca ünlü **Bayraktar TB2**, **Akıncı** TİHA ve insansız savaş uçağı **Bayraktar Kızılelma**.
  - **TUSAŞ (TAI):** 5. nesil milli muharip uçak **KAAN** (2024 ilk uçuş), Hürjet ve Atak-II helikopteri.
  - **ROKETSAN:** Tayfun balistik füzesi, Atmaca gemisavar füzesi ve Siper hava savunma sistemi.
- **İhracat Gücü:** Yıllık savunma ve havacılık ihracatı **5,5 milyar doları** aşarak 170'ten fazla ülkeye ulaşmıştır [SIPRI-2024-MLX]."""

    m6["infographics"][0]["title"] = "Türkiye'de Askeri Müdahaleler ve Siyasi Sonuçları Matrisi"
    m6["infographics"][0]["headers"] = ["Müdahale", "Tarih", "Yöneten Komuta", "Gerekçe", "Siyasi ve Hukuki Sonucu"]
    m6["infographics"][0]["rows"] = [
        ["1960 Askeri Darbesi", "27 May 1960", "Milli Birlik Komitesi (MBK)", "DP otoriterleşmesi ve kardeş kavgası", "Menderes idam edildi; 1961 Anayasası hazırlandı"],
        ["1971 Muhtırası", "12 Mar 1971", "Genelkurmay Başkanı & Kuvvet Komutanları", "Sokak çatışmaları ve anarşi", "Demirel istifa etti; teknokrat hükümetler kuruldu"],
        ["1980 Askeri Darbesi", "12 Eyl 1980", "Milli Güvenlik Konseyi (Kenan Evren)", "Siyasi kilitlenme ve terör", "Meclis feshedildi; 650 bin gözaltı; 1982 Anayasası kabul edildi"],
        ["1997 Post-Modern Darbe", "28 Şub 1997", "Milli Güvenlik Kurulu (MGK)", "İrtica tehdidi ve laiklik karşıtlığı", "Refahyol hükümeti devrildi; 8 yıllık kesintisiz eğitime geçildi"],
        ["2007 E-Muhtırası", "27 Nis 2007", "Genelkurmay Basın Açıklaması", "Gül'ün cumhurbaşkanlığı adaylığı", "Hükümet muhtırayı reddetti; erken seçimle iktidar pekişti"],
        ["2016 Darbe Girişimi", "15 Tem 2016", "Yurtta Sulh Konseyi (FETÖ Cuntası)", "Devlet yönetimini ele geçirme teşebbüsü", "Halk direnişiyle bastırıldı; TSK tamamen sivil bakanlığa bağlandı"]
    ]

    m6["infographics"][1]["title"] = "Sivil-Asker Komuta Hiyerarşisi ve Savunma Sanayii Teşkilat Şeması"
    m6["infographics"][2]["title"] = "Askeri Güç ve Savunma Sanayii Göstergeleri"
    m6["infographics"][2]["data"] = [
        {"label": "Muvazzaf Asker Sayısı", "value": "~425.000 Asker", "sub": "NATO'nun en büyük ikinci ordusu"},
        {"label": "Yerli Savunma Oranı", "value": ">%80 Yerlilik", "sub": "2002'deki %20 seviyesinden yükseldi"},
        {"label": "Yıllık Savunma İhracatı", "value": "5,5 Milyar $+ / yıl", "sub": "170'ten fazla ülkeye askeri ihracat"},
        {"label": "Bayraktar TB2 İhracatı", "value": "30+ Ülke", "sub": "Karabağ, Ukrayna ve Libya'da operasyonel"},
        {"label": "5. Nesil Savaş Uçağı", "value": "TUSAŞ KAAN", "sub": "2024'te ilk uçuşunu başarıyla tamamladı"},
        {"label": "Amfibi SİHA Gemisi", "value": "TCG Anadolu", "sub": "Dünyanın ilk SİHA taşıyıcı çıkarma gemisi"}
    ]

    # Module 7: Yargı Sistemi
    m7 = tr[6]
    m7["title"] = "Yargı Sistemi ve Hukuk Devleti"
    m7["tagline"] = "Mahkeme hiyerarşisi, Anayasa Mahkemesi, HSK ve AİHM içtihatları."
    m7["readingTime"] = "27 dk okuma"
    m7["summary"] = "Türk yargı mimarisinin ayrıntılı incelemesi: adli ve idari yargı ayrılığı, ilk derece, istinaf (BAM/BİM) ve temyiz (Yargıtay/Danıştay) kademeleri; Anayasa Mahkemesi'nin norm denetimi ve bireysel başvuru yetkisi; HSK'nın yapısı; UYAP bilişim ağı ve Anayasa 90. maddesi uyarınca AİHM kararlarının bağlayıcılığı."
    
    m7["sections"][0]["title"] = "1. Kıta Avrupası Hukuk Geleneği ve Çift Başlı Yargı Düzeni"
    m7["sections"][0]["content"] = """Türkiye Cumhuriyeti yargı düzeni, 1926 yılında İsviçre Medeni Kanunu ve İtalyan Ceza Kanunu'nun iktibasıyla Kıta Avrupası sivil hukuk sistemine (*Civil Law*) dahil olmuştur:
- **Çift Başlı Yargı Mimarisi:** Yargı erki iki ana dikey kolda teşkilatlanmıştır:
  - **Adli Yargı (Hukuk ve Ceza Mahkemeleri):** Özel hukuk uyuşmazlıkları ve ceza davalarına bakar; temyiz mercii **Yargıtay**'dır.
  - **İdari Yargı:** Devlet ve idarenin kamu gücünü kullanarak tesis ettiği idari işlem ve eylemlerin hukuka uygunluğunu denetler; temyiz mercii **Danıştay**'dır.
- **Uyuşmazlık Mahkemesi:** Adli ve idari yargı mercileri arasındaki görev ve hüküm uyuşmazlıklarını kesin karara bağlayan yüksek mahkemedir [TBMM-CONST-1982, AYM-REPORTS]."""

    m7["sections"][1]["title"] = "2. Üç Dereceli Mahkeme Teşkilatı: İlk Derece, İstinaf ve Temyiz"
    m7["sections"][1]["content"] = """2016'da faaliyete geçen istinaf reformuyla Türk yargısı üç dereceli hale gelmiştir:
- **İlk Derece Mahkemeleri:**
  - *Adli Mahkemeler:* Sulh Hukuk, Asliye Hukuk, Ticaret, İş, Aile ve Tüketici mahkemeleri ile Asliye Ceza ve Ağır Ceza mahkemeleri. Sulh Ceza Hâkimlikleri ise tutuklama, arama ve erişim engelleme kararlarını verir.
  - *İdari Mahkemeler:* İdare Mahkemeleri ve Vergi Mahkemeleri.
- **İstinaf Kademesi: Bölge Adliye ve Bölge İdare Mahkemeleri (BAM / BİM):** İlk derece mahkemelerinin kararlarını hem olay (vakıa) hem de hukukilik yönünden denetleyen ara temyiz mahkemeleridir.
- **Temyiz Kademesi:**
  - **Yargıtay:** Ankara merkezli olup hukuk ve ceza daireleriyle adli yargının en üst içtihat makamıdır.
  - **Danıştay:** İdari davaların en üst temyiz organı ve idari danışma makamıdır [TBMM-CONST-1982]."""

    m7["sections"][2]["title"] = "3. Anayasa Mahkemesi (AYM) ve Bireysel Başvuru Müessesesi"
    m7["sections"][2]["content"] = """1961 Anayasası ile kurulan **Anayasa Mahkemesi (AYM)** 15 üyeden oluşur (üyelerin 12'si Cumhurbaşkanı, 3'ü TBMM tarafından seçilir):
- **Norm Denetimi:** Kanunların, Cumhurbaşkanlığı kararnamelerinin ve TBMM İçtüzüğü'nün anayasaya şekil ve esas bakımından uygunluğunu denetler (iptal davası ve itiraz yolu).
- **Bireysel Başvuru:** 2010 anayasa referandumu ile kabul edilmiş ve 2012'de yürürlüğe girmiştir. Anayasa ve AİHS tarafından güvence altına alınan temel hak ve özgürlükleri kamu gücü tarafından ihlal edilen herkes olağan kanun yollarını tükettikten sonra AYM'ye başvurabilir. Yılda 70 binden fazla başvuru karara bağlanmaktadır.
- **Siyasi Parti Kapatma Davaları:** Yargıtay Cumhuriyet Başsavcısı'nın açtığı parti kapatma davalarını nihai olarak karara bağlar [AYM-REPORTS]."""

    m7["sections"][3]["title"] = "4. Hakimler ve Savcılar Kurulu (HSK), UYAP ve AİHM İlişkisi"
    m7["sections"][3]["content"] = """Yargı yönetimi ve uluslararası insan hakları standartları:
- **Hakimler ve Savcılar Kurulu (HSK):** 13 üyeden oluşur. Adalet Bakanı kurulun başkanı, Bakan Yardımcısı tabii üyesidir. 4 üyeyi Cumhurbaşkanı atar, 7 üyeyi TBMM 3/5 çoğunlukla seçer. Hâkim ve savcıların mesleğe kabulü, tayin, terfi ve disiplin işlemlerini yürütür.
- **UYAP Bilişim Sistemi:** Tüm mahkemeleri, icra dairelerini, cezaevlerini ve baroları birbirine bağlayan ödüllü e-adalet ağıdır. Dava açma, tebligat ve SEGBİS ile uzaktan duruşma imkanı sunar.
- **Anayasa Madde 90 ve AİHM:** Usulüne göre yürürlüğe konulmuş temel hak ve özgürlüklere ilişkin milletlerarası antlaşmalarla (özellikle AİHS) ulusal kanunların çelişmesi halinde milletlerarası antlaşma hükümleri esas alınır [TBMM-CONST-1982]."""

    m7["infographics"][0]["title"] = "Türk Yargı Teşkilatı Hiyerarşi ve İstinaf Şeması"
    m7["infographics"][1]["title"] = "Yüksek Yargı Organları Görev ve Yetki Karşılaştırma Matrisi"
    m7["infographics"][1]["headers"] = ["Yüksek Mahkeme", "Yargı Kolu", "Üye Sayısı", "Temel Görev ve Yetkisi", "Anayasal Dayanağı"]
    m7["infographics"][1]["rows"] = [
        ["Anayasa Mahkemesi (AYM)", "Anayasa Yargısı", "15 Üye", "Norm denetimi, Bireysel başvuru, Yüce Divan yargılaması", "Madde 146–153"],
        ["Yargıtay", "Adli Yargı", "Daireler Külliyatı", "Hukuk ve ceza mahkemelerinin son temyiz inceleme mercii", "Madde 154"],
        ["Danıştay", "İdari Yargı", "Daireler Külliyatı", "İdari ve vergi davalarının son temyiz inceleme organı", "Madde 155"],
        ["Uyuşmazlık Mahkemesi", "Yargı Uyuşmazlığı", "6 Üye + Başkan", "Adli ve idari mahkemeler arası görev uyuşmazlıklarını çözer", "Madde 158"]
    ]

    m7["infographics"][2]["title"] = "Yargı Sistemi ve Dijital Adalet Göstergeleri"
    m7["infographics"][2]["data"] = [
        {"label": "AYM Üye Sayısı", "value": "15 Hukukçu Üye", "sub": "12 yıl süreyle bir kez seçilirler"},
        {"label": "Yıllık Bireysel Başvuru", "value": "75.000+ Dava", "sub": "Hak ihlali iddialarıyla AYM'ye yapılan başvuru"},
        {"label": "HSK Üye Sayısı", "value": "13 Üye", "sub": "Adalet Bakanı başkanlığında toplanır"},
        {"label": "BAM / BİM Sayısı", "value": "18 BAM / 9 BİM", "sub": "Bölge Adliye ve İdare İstinaf Mahkemeleri"},
        {"label": "UYAP Entegrasyonu", "value": "%100 Dijital", "sub": "E-Duruşma ve elektronik dava dosyası altyapısı"},
        {"label": "AİHM / Madde 90", "value": "Üstünlük Kuralı", "sub": "Milletlerarası insan hakları sözleşmesi önceliklidir"}
    ]

    # Module 8: Demografi ve Etnik Yapı
    m8 = tr[7]
    m8["title"] = "Demografi ve Etnik Yapı"
    m8["tagline"] = "Nüfus dinamikleri, etnik topluluklar, Lozan gayrimüslim azınlıkları ve göç hareketleri."
    m8["readingTime"] = "29 dk okuma"
    m8["summary"] = "Türkiye'nin 85,37 milyonluk nüfus yapısını, doğurganlık hızındaki düşüşü (1,51), %93,2'lik kentleşmeyi, Türkler, Kürtler, Zazalar, Araplar, Çerkesler ve Lazlar gibi etnik unsurları; Lozan Anlaşması gayrimüslim azınlıklarını (Ermeniler, Museviler, Rumlar, Süryaniler) ve 3,1 milyonluk Suriyeli geçici koruma nüfusunu kapsayan demografik analiz."

    m8["sections"][0]["title"] = "1. Nüfus Artış Seyri, Yaş Piramidi ve Doğurganlık Hızındaki Düşüş"
    m8["sections"][0]["content"] = """TÜİK'in Adrese Dayalı Nüfus Kayıt Sistemi (ADNKS) verilerine göre Türkiye nüfusu yaklaşık **85,37 milyon kişidir**:
- **Tarihsel Seyir:** 1927 yılındaki ilk nüfus sayımında 13,6 milyon olan cumhuriyet nüfusu, 1980'de 44 milyona, 2020'lerde ise 85 milyonun üzerine çıkmıştır.
- **Doğurganlık Hızında Çöküş:** 1980'de kadın başına 4,3 olan **Toplam Doğurganlık Hızı (TFR)**, 2023 yılında **1,51'e gerileyerek** nüfusun kendini yenileme eşiği olan 2,1'in oldukça altına inmiştir.
- **Yaşlanan Nüfus:** Ortanca yaş 2000 yılındaki 24,8'den **34,0 yıla** yükselmiştir. 65 yaş ve üzeri nüfusun payı %10,2'yi geçerek Türkiye BM kriterlerine göre 'yaşlı nüfuslu ülke' eşiğine girmiştir [TUIK-2024-POP]."""

    m8["sections"][1]["title"] = "2. Hızlı Kentleşme ve Metropol Alanlar"
    m8["sections"][1]["content"] = """Tarımda makineleşme ve sanayileşme ile Türkiye yoğun bir iç göç yaşamıştır:
- **Kentleşme Oranı:** Nüfusun %93,2'si il ve ilçe merkezlerinde yaşamakta, kırsal köy nüfusu %6,8'e gerilemiştir.
- **Marmara Havzası Yoğunluğu:** Marmara Bölgesi ülke topraklarının %8,5'inde toplam nüfusun %30'undan fazlasını barındırır.
- **Mega Şehirler:**
  - **İstanbul (15,65 Milyon):** Ülke nüfusunun %18,3'ü, Avrupa'nın en kalabalık kenti.
  - **Ankara (5,8 M), İzmir (4,5 M), Bursa (3,2 M), Antalya (2,7 M), Konya (2,3 M), Adana (2,2 M), Gaziantep (2,2 M), Şanlıurfa (2,2 M)** [TUIK-2024-POP]."""

    m8["sections"][2]["title"] = "3. Etnik Mozaik ve Dilsel Çeşitlilik"
    m8["sections"][2]["content"] = """Resmi nüfus sayımlarında etnik köken sorulmamakla birlikte akademik sosyolojik saha araştırmaları zengin bir tabloyu ortaya koymaktadır:
- **Türkler:** Nüfusun ezici çoğunluğunu oluşturur (~%75–80); Anadolu yerlileri ile Balkan, Kırım ve Kafkas göçmenlerinin sentezidir.
- **Kürtler:** Ülkenin en büyük etnik azınlığıdır; nüfusun **yaklaşık %15–20'sini** (~13–16 milyon) teşkil eder. Tarihsel olarak Doğu ve Güneydoğu'da yoğun olmakla birlikte en büyük Kürt nüfusu İstanbul ve batı metropollerinde yaşamaktadır. Ağırlıklı olarak **Kurmanci (*Kurmancî*)** konuşurlar.
- **Zazalar:** Tunceli (Dersim), Bingöl ve Elazığ yöresinde yaşayan, İrani diller grubundan **Zazaca (*Zazaki*)** konuşan kadim topluluk.
- **Araplar:** Hatay, Mardin, Şanlıurfa ve Adana hattında yerleşik nüfus.
- **Çerkesler ve Kuzey Kafkasyalılar:** 1864 Çerkes Sürgünü ile Osmanlı'ya sığınan Adığeler, Abhazlar, Çeçenler ve Dağıstanlılar (Düzce, Balıkesir, Kayseri hattı).
- **Lazlar ve Hemşinliler:** Doğu Karadeniz'de (Rize, Artvin) yerleşik olup Lazca konuşan Güney Kafkas kökenli halk ve Hemşince konuşan topluluklar [ZURCHER-2017]."""

    m8["sections"][3]["title"] = "4. Lozan Barış Antlaşması Azınlıkları ve Gayrimüslim Cemaatler"
    m8["sections"][3]["content"] = """1923 **Lozan Antlaşması**'nın 37-45. maddeleri uyarınca azınlık statüsü yalnızca **gayrimüslim dini cemaatlere** hasredilmiştir:
- **Ermeni Cemaati:** ~50.000–60.000 kişiyle en büyük gayrimüslim gruptur. İstanbul'da vakıf okulları, hastaneleri (Yedikule Surp Pırgiç) ve Kumkapı'daki **İstanbul Ermeni Patrikhanesi** ile teşkilatlanmıştır.
- **Musevi Cemaati:** ~14.000–15.000 kişi, ağırlıklı olarak 1492'de İspanya'dan sığınan Sefarad Yahudileri (Ladino konuşurlar). **Türkiye Hahambaşılığı** idaresindedir.
- **Rum Ortodoks Cemaati:** ~2.000–3.000 kişi; Fener'deki **Ekümenik Fener Rum Patrikhanesi** etrafında toplanmıştır.
- **Süryaniler:** Mardin Turabdin ve İstanbul'da yaşayan yaklaşık 25.000 kişilik kadim Hristiyan topluluk [LAUSANNE-1923]."""

    m8["sections"][4]["title"] = "5. Çağdaş Mülteci Dinamikleri ve Geçici Koruma"
    m8["sections"][4]["content"] = """2011 Suriye iç savaşı sonrası Türkiye dünyanın en büyük sığınmacı ev sahibi ülkesi olmuştur:
- **Geçici Koruma Altındaki Suriyeliler:** 6458 Sayılı Kanun kapsamında **3,1 milyondan fazla kayıtlı Suriyeli** sağlık, eğitim ve belediye hizmetlerinden faydalanmaktadır. En yoğun iller İstanbul, Gaziantep, Şanlıurfa ve Hatay'dır.
- **18 Mart 2016 Türkiye-AB Mutabakatı:** Ege'den yasadışı göçü önleme karşılığında 6 milyar avroluk FRIT fonunu öngören mutabakat [TUIK-2024-POP, WB-TUR-2024]."""

    m8["infographics"][0]["title"] = "Çağdaş Türkiye Etnik ve İnanç Çeşitliliği Matrisi"
    m8["infographics"][0]["headers"] = ["Topluluk", "Dil Ailesi", "Tahmini Nüfus Payı", "Yoğun Yaşadığı Coğrafya", "Hukuki Statüsü"]
    m8["infographics"][0]["rows"] = [
        ["Türkler", "Türk Dilleri (Oğuz Kolu)", "~%75–80", "Ülkenin 81 ilinde ülke geneli", "Kurucu Egemen Çoğunluk"],
        ["Kürtler", "Hint-Avrupa (Kuzeybatı İrani)", "~%15–20 (~13–16 Milyon)", "Doğu/Güneydoğu, İstanbul, İzmir, Mersin", "Eşit Yurttaş (Genel Vatandaşlık)"],
        ["Zazalar", "Hint-Avrupa (Zaza-Gorani)", "~%2–3 (~1,5–2 Milyon)", "Tunceli, Bingöl, Elazığ, Diyarbakır", "Eşit Yurttaş (Genel Vatandaşlık)"],
        ["Araplar", "Hami-Sami (Sami Dilleri)", "~%2–3 Yerli + 3.1M Suriyeli", "Hatay, Mardin, Şanlıurfa, Gaziantep", "Vatandaşlar + Geçici Koruma Statüsü"],
        ["Çerkesler", "Kuzeybatı Kafkas (Adığe)", "~%1,5–2 (~1 Milyon)", "Düzce, Bolu, Balıkesir, Kayseri", "Eşit Yurttaş (Genel Vatandaşlık)"],
        ["Ermeniler", "Hint-Avrupa (Ermeni Dili)", "~50.000–60.000", "İstanbul (Kumkapı, Şişli, Kadıköy)", "Lozan Antlaşması Gayrimüslim Azınlığı"],
        ["Museviler", "Hami-Sami / Romen (Ladino)", "~14.000–15.000", "İstanbul, İzmir", "Lozan Antlaşması Gayrimüslim Azınlığı"],
        ["Rumlar", "Hint-Avrupa (Helenik)", "~2.000–3.000", "İstanbul (Fener, Beyoğlu), Gökçeada", "Lozan Antlaşması Gayrimüslim Azınlığı"],
        ["Süryaniler", "Hami-Sami (Aramice)", "~25.000", "Mardin (Turabdin), İstanbul", "Kadim Dini Cemaat"]
    ]

    m8["infographics"][1]["title"] = "Demografik Göstergeler ve Nüfus İstatistikleri (TÜİK 2024)"
    m8["infographics"][1]["data"] = [
        {"label": "Toplam Ülke Nüfusu", "value": "85,37 Milyon", "sub": "Dünyada 18. sırada"},
        {"label": "Doğurganlık Hızı (TFR)", "value": "1,51 Çocuk", "sub": "Tarihi dip (2,1 yenilenme eşiği altı)"},
        {"label": "Ortanca Yaş", "value": "34,0 Yaş", "sub": "33,2 erkek, 34,7 kadın"},
        {"label": "Kentleşme Oranı", "value": "%93,2 Kent", "sub": "İl ve ilçe merkezlerinde yaşayan oran"},
        {"label": "İstanbul Nüfusu", "value": "15,65 Milyon", "sub": "Ülke toplam nüfusunun %18,3'ü"},
        {"label": "Geçici Koruma Suriyeli", "value": "3,1 Milyon+", "sub": "Dünyanın en büyük mülteci ev sahibi"}
    ]

    # Module 9: Ulaştırma
    m9 = tr[8]
    m9["title"] = "Ulaştırma ve Lojistik Koridorları"
    m9["tagline"] = "Yüksek hızlı tren (YHT), otoyol mega projeleri, Türk Boğazları geçiş rejimi, havacılık ve Orta Koridor."
    m9["readingTime"] = "26 dk okuma"
    m9["summary"] = "TCDD Yüksek Hızlı Tren (YHT) ağı, Yap-İşlet-Devret modeliyle inşa edilen mega asma köprüler (1915 Çanakkale, Yavuz Sultan Selim, Osmangazi), Marmaray ve Avrasya Tüneli, Montrö Sözleşmesi uyarınca Boğazlar deniz trafiği, İstanbul Havalimanı (İGA), THY küresel ağı ve Trans-Hazar Orta Koridoru lojistik analizi."

    m9["sections"][0]["title"] = "1. Demiryolu Hamlesi ve Yüksek Hızlı Tren (YHT) Ağı"
    m9["sections"][0]["content"] = """Türkiye Cumhuriyeti Devlet Demiryolları (TCDD) 13.900 km'lik hat yönetmektedir:
- **İşletmedeki YHT Hatları:** Ankara–Eskişehir–İstanbul (533 km, seyahat 4 saat), Ankara–Konya (212 km, 1 saat 45 dk), Ankara–Sivas (405 km, 2 saat).
- **Yapımı Süren Hatlar:** Ankara–İzmir YHT (3,5 saate indirecek), Halkalı–Kapıkule YHT (Avrupa TEN-T ağına doğrudan bağlantı) ve Mersin–Adana–Gaziantep hattı.
- **Marmaray Tüp Geçidi:** Deniz tabanından 60 m derinden geçen batırma tüp tünel ile Asya ve Avrupa'yı kesintisiz raylı sistemle birleştirmiştir."""

    m9["sections"][1]["title"] = "2. Otoyol Ağı ve Mühendislik Mega Projeleri"
    m9["sections"][1]["content"] = """Karayolları Genel Müdürlüğü (KGM) bölünmüş yol ağını 29.200 km'nin üzerine çıkarmıştır:
- **1915 Çanakkale Köprüsü:** 2.023 metrelik orta açıklığıyla **dünyanın en uzun asma köprüsüdür**; Boğaz geçişini 6 dakikaya indirmiştir.
- **Yavuz Sultan Selim Köprüsü:** 59 metrelik genişliğiyle 8 şerit otoyol ve çift hat demiryolunu taşır.
- **Osmangazi Köprüsü:** İzmit Körfezi'ni aşarak İstanbul-İzmir seyahatini 8 saatten 3,5 saate düşürmüştür.
- **Avrasya Tüneli:** İstanbul Boğazı tabanının altından geçen çift katlı karayolu tüneli (günde 70 bin araç)."""

    m9["sections"][2]["title"] = "3. Türk Boğazları Deniz Trafiği ve Ticari Limanlar"
    m9["sections"][2]["content"] = """İstanbul ve Çanakkale Boğazları küresel deniz ticaretinin en stratejik boğazlarıdır:
- **Trafik Yoğunluğu:** Yılda yaklaşık **35.000–45.000 gemi geçer**; 150 milyon ton ham petrol ve tehlikeli madde taşınır.
- **Montrö Rejimi ve VTS:** Ticaret gemilerinin geçiş serbestisi korunurken, Türk Boğazları Gemi Trafik Hizmetleri (TBGTH/VTS) kılavuzluk ve radar gözetimiyle seyir emniyetini sağlar [UN-TREATY-MONTREUX].
- **Limanlar:** Ambarlı Limanı (yılda 3M+ TEU), Mersin Uluslararası Limanı (MIP), Aliağa ve Filyos Limanı."""

    m9["sections"][3]["title"] = "4. Havacılık Merkezi ve Trans-Hazar Orta Koridor"
    m9["sections"][3]["content"] = """Türkiye kıtalararası transit lojistik omurgasıdır:
- **İstanbul Havalimanı (İGA):** Yılda 76 milyondan fazla yolcuya hizmet vererek Avrupa'nın en yoğun havalimanı olmuştur.
- **Türk Hava Yolları (THY):** Dünyada en fazla ülkeye (129 ülke, 340+ nokta) uçan havayolu şirketi.
- **Orta Koridor (TITR):** Çin'den başlayıp Kazakistan, Hazar Denizi, Bakü-Tiflis-Kars demiryolu ve Marmaray üzerinden Avrupa'ya bağlanan demiryolu koridoru; Çin-Avrupa taşımacılığını deniz yolunun yarı süresine (12–15 güne) indirmektedir [WB-TUR-2024]."""

    m9["infographics"][0]["title"] = "Türkiye Ulaştırma Mega Projeleri Teknik Karşılaştırma Matrisi"
    m9["infographics"][0]["headers"] = ["Proje Adı", "Altyapı Türü", "Teknik Ölçüsü", "Yatırım Modeli", "Stratejik Bağlantı Sahası"]
    m9["infographics"][0]["rows"] = [
        ["1915 Çanakkale Köprüsü", "Asma Köprü", "2.023 m orta açıklık (Dünya Rekoru)", "YİD (Kamu-Özel Ortaklığı)", "İstanbul'a uğramadan Avrupa-Ege transit koridoru"],
        ["Marmaray Tüneli", "Batırma Raylı Tüp Tünel", "Boğaz tabanında -60 metre derinlik", "Kamu Yatırımı / JICA Kredisi", "Kıtalararası banliyö ve yük treni geçişi"],
        ["Yavuz Sultan Selim Köprüsü", "Hibrit Asma-Gergin Eğik", "59 metre tabliye genişliği (Otoyol + Ray)", "YİD (Kamu-Özel Ortaklığı)", "Kuzey Marmara transit yük ve otoyol koridoru"],
        ["Osmangazi Köprüsü", "Asma Köprü", "1.550 m orta açıklık", "YİD (Kamu-Özel Ortaklığı)", "İstanbul–İzmir Otoyolu (3,5 saat seyahat)"],
        ["Avrasya Tüneli", "Denizaltı Karayolu Tüneli", "Çift katlı derin karayolu tüpü", "YİD (Kamu-Özel Ortaklığı)", "İstanbul Boğazı doğrudan araç geçişi (5,4 km)"],
        ["İstanbul Havalimanı (İGA)", "Uluslararası Havalimanı", "Yıllık 90–200M yolcu kapasitesi", "YİD (Kamu-Özel Ortaklığı)", "Avrupa'nın en işlek küresel transit aktarma merkezi"]
    ]

    m9["infographics"][1]["title"] = "Ulaştırma Şebekesi ve Lojistik Göstergeleri"
    m9["infographics"][1]["data"] = [
        {"label": "Bölünmüş Yol Ağı", "value": "29.200+ km", "sub": "2002'den bu yana dört kat genişletildi"},
        {"label": "Hızlı Tren Hattı (YHT)", "value": "2.228+ km", "sub": "Ankara, İstanbul, Konya, Sivas"},
        {"label": "Boğazlardan Gemi Geçişi", "value": "40.000+ Gemi/yıl", "sub": "Montrö Sözleşmesi hükümlerine tabidir"},
        {"label": "İstanbul Havalimanı Trafik", "value": "76M+ Yolcu/yıl", "sub": "Avrupa kıtasının en yoğun havalimanı"},
        {"label": "THY Uçuş Ağı", "value": "129 Ülke", "sub": "Dünyada en fazla ülkeye uçan havayolu"},
        {"label": "Orta Koridor Transit Süresi", "value": "12–15 Gün", "sub": "Çin'den Avrupa'ya kesintisiz demiryolu"}
    ]

    # Module 10: Enerji Kaynakları
    m10 = tr[9]
    m10["title"] = "Enerji Kaynakları, Tüketim ve Düzenleme"
    m10["tagline"] = "Doğalgaz boru hatları, Sakarya gaz keşfi, Akkuyu Nükleer, yenilenebilir enerji ve EPDK yönetişimi."
    m10["readingTime"] = "28 dk okuma"
    m10["summary"] = "Türkiye'nin birincil enerji dengesi, %70'i aşan hidrokarbon ithalat bağımlılığı, uluslararası boru hattı diplomasisi (TANAP, TürkAkım, Mavi Akım, BTC), Karadeniz Sakarya derin deniz doğalgaz keşfi, Akkuyu Nükleer Güç Santrali (Rosatom BOO modeli), yenilenebilir elektrik kurulu gücü (HES, RES, GES, dünyada 4. jeotermal) ve EPDK regülasyonu."

    m10["sections"][0]["title"] = "1. Birincil Enerji Dengesi ve Hidrokarbon İthalat Bağımlılığı"
    m10["sections"][0]["content"] = """Türkiye birincil enerji arzının (TPES) yaklaşık **%70'inden fazlasını ithal etmektedir**:
- **Doğalgaz:** Yılda 50–55 milyar m³ gaz tüketilir. %98'i ithaldir: Rusya (Mavi Akım, TürkAkım), Azerbaycan (TANAP), İran ve sıvılaştırılmış doğalgaz (LNG - Cezayir, Katar, ABD).
- **Petrol:** Yılda 45–50 milyon ton ham petrol ve akaryakıt ithal edilir; Tüpraş ve SOCAR STAR rafinerilerinde işlenir [IEA-TUR-2023, EPDK-2024-NRG]."""

    m10["sections"][1]["title"] = "2. Karadeniz Sakarya Derin Deniz Gaz Keşfi"
    m10["sections"][1]["content"] = """Ağustos 2020'de Fatih sondaj gemisi Karadeniz Tuna-1 kuyusunda **Sakarya Gaz Sahası**'nı keşfetmiştir:
- **Rezerv:** 710 milyar m³ doğalgaz rezerviyle cumhuriyet tarihinin en büyük hidrokarbon keşfidir.
- **Üretim:** 2.100 m su derinliğinde deniz tabanı üretim tesisleri kurulmuş, 170 km'lik denizaltı boru hattıyla Filyos Gaz İşleme Tesisi'ne bağlanarak Nisan 2023'te ulusal şebekeye verilmiştir [EPDK-2024-NRG]."""

    m10["sections"][2]["title"] = "3. Stratejik Boru Hatları ve Enerji Transit Diplomasisi"
    m10["sections"][2]["content"] = """Türkiye Avrasya enerji koridorunun merkezindedir:
- **TANAP:** Güney Gaz Koridoru'nun ana omurgası; Şah Deniz gazını Türkiye üzerinden Avrupa'ya (TAP) taşır (16 milyar m³/yıl).
- **TürkAkım:** Karadeniz altından 31,5 milyar m³ Rus gazını Türkiye ve Güneydoğu Avrupa'ya iletir.
- **Bakü–Tiflis–Ceyhan (BTC):** Günde 1 milyon varil Hazar petrolünü Ceyhan terminalinden Akdeniz tanker trafiğine sunar [IEA-TUR-2023]."""

    m10["sections"][3]["title"] = "4. Nükleer Enerji Hamlesi: Akkuyu Nükleer Güç Santrali (NGS)"
    m10["sections"][3]["content"] = """2010 yılında Türkiye ile Rusya arasında imzalanan hükümetlerarası anlaşmayla Mersin Gülnar'da **Akkuyu Nükleer Güç Santrali** inşa edilmektedir:
- **Teknik Detaylar:** Rus Rosatom şirketi tarafından **Yap-İşlet-Sahip Ol (BOO)** modeliyle inşa edilen santral, her biri 1.200 MW'lık **4 adet VVER-1200 reaktöründen** oluşur (toplam 4.800 MW kurulu güç).
- **Katkısı:** Tam kapasiteye ulaştığında Türkiye'nin elektrik ihtiyacının yaklaşık **%10'unu tek başına karşılayacaktır** [IEA-TUR-2023]."""

    m10["sections"][4]["title"] = "5. Yenilenebilir Enerji Hamlesi ve EPDK Piyasa Yönetişimi"
    m10["sections"][4]["content"] = """Türkiye'nin elektrik kurulu gücü **107.000 MW'ı aşmış**, yenilenebilir payı **%54'e** yükselmiştir:
- **Hidroelektrik:** 32.200 MW (Atatürk, Keban, Karakaya, Ilısu barajları).
- **Güneş ve Rüzgar (YEKA):** 14.500 MW güneş, 12.100 MW rüzgar santrali.
- **Jeotermal Güç:** Türkiye kurulu güçte (~1.700 MW) **dünyada 4. sıradadır** (Ege grabenleri).
- **Regülatör Kurumlar:** Enerji Piyasası Düzenleme Kurumu (EPDK) lisanslama ve tarifeleri belirler; BOTAŞ doğalgaz iletimini, TEİAŞ ulusal elektrik iletim şebekesini yönetir [EPDK-2024-NRG]."""

    m10["infographics"][0]["title"] = "Türkiye'den Geçen Uluslararası Stratejik Boru Hatları Matrisi"
    m10["infographics"][0]["headers"] = ["Boru Hattı", "Taşınan Enerji", "İletim Kapasitesi", "Güzergah Sahası", "Pazar ve Teslim Noktası"]
    m10["infographics"][0]["rows"] = [
        ["TANAP", "Doğalgaz", "16 Milyar m³/yıl (31'e genişleyebilir)", "Azerbaycan (Şah Deniz) – Gürcistan – Türkiye", "6 Milyar m³ Türkiye / 10 Milyar m³ Güney Avrupa (TAP)"],
        ["TürkAkım", "Doğalgaz", "31,5 Milyar m³/yıl (Çift Hat)", "Rusya (Anapa) – Karadeniz – Trakya (Kıyıköy)", "Hat 1: Türkiye İç Pazarı / Hat 2: Balkanlar ve Macaristan"],
        ["Mavi Akım", "Doğalgaz", "16 Milyar m³/yıl", "Rusya – Karadeniz tabanı – Samsun – Ankara", "Türkiye ulusal doğalgaz şebekesi"],
        ["Bakü–Tiflis–Ceyhan (BTC)", "Ham Petrol", "Günde 1,0–1,2 Milyon varil", "Hazar Havzası (Bakü) – Tiflis – Ceyhan Limanı", "Akdeniz üzerinden küresel tanker taşımacılığı"],
        ["Kerkük–Ceyhan", "Ham Petrol", "Günde 1,4 Milyon varil", "Kerkük (Irak) – Ceyhan Deniz Terminali", "Akdeniz tanker piyasası"],
        ["Tebriz–Ankara", "Doğalgaz", "10 Milyar m³/yıl", "İran (Tebriz) – Doğu Anadolu – Ankara", "Türkiye iç tüketim iletim şebekesi"]
    ]

    m10["infographics"][1]["title"] = "Ulusal Enerji Dengesi ve Kurulu Güç Göstergeleri (2024)"
    m10["infographics"][1]["data"] = [
        {"label": "Elektrik Kurulu Gücü", "value": "107.000+ MW", "sub": "%54 yenilenebilir kaynak payı"},
        {"label": "Hidroelektrik Kapasite", "value": "32.200 MW", "sub": "Atatürk, Keban, Ilısu mega barajları"},
        {"label": "Sakarya Gaz Rezervi", "value": "710 Milyar m³", "sub": "Karadeniz derin deniz milli üretimi"},
        {"label": "Akkuyu NGS Kapasitesi", "value": "4.800 MW", "sub": "4x VVER-1200 reaktör ünitesi"},
        {"label": "Dünya Jeotermal Sırası", "value": "Dünyada 4. Sırada", "sub": "~1.700 MW kurulu jeotermal güç"},
        {"label": "Enerji İthalat Oranı", "value": "~%71 TPES", "sub": "Milli enerji stratejisinin odak noktası"}
    ]

    # Module 11: Ülke Ekonomisi
    m11 = tr[10]
    m11["title"] = "Ülke Ekonomisi ve Düzenleyici Kurumlar"
    m11["tagline"] = "Makroekonomik yapı, sanayi ve ihracat gücü, Rekabet Kurumu ve büyük holdingler."
    m11["readingTime"] = "29 dk okuma"
    m11["summary"] = "1,1 trilyon doları aşan nominal GSYH, hizmetler (%55), sanayi (%28) ve tarım (%6) dağılımı, yıllık 255 milyar doları aşan ihracat kapasitesi, 1995 AB Gümrük Birliği, Rekabet Kurumu, KİK, Hazine ve Maliye Bakanlığı regülasyonu ile Koç, Sabancı holdingleri ve TOBB, TÜSİAD, MÜSİAD, TİM iş dünyası örgütleri."

    m11["sections"][0]["title"] = "1. Makroekonomik Yapı, GSYH Büyüklüğü ve Sektörel Dağılım"
    m11["sections"][0]["content"] = """Türkiye ekonomisi, **1,1 trilyon doları aşan nominal Gayri Safi Yurtiçi Hasılası (GSYH)** ile dünyanın en büyük 17-18. ekonomisi, Satın Alma Gücü Paritesine (SGP) göre ise ilk 11 içerisindedir:
- **Sektörel Dağılım:**
  - **Hizmetler Sektörü (~%55):** Ticaret, ulaştırma, finans ve 56 milyondan fazla yabancı turistle 54 milyar doları aşan gelir üreten küresel **turizm sektörü**.
  - **Sanayi ve İmalat (~%28):** Otomotiv, beyaz eşya, makine, çelik, kimya ve savunma sanayiinden oluşan güçlü sanayi omurgası.
  - **Tarım ve Hayvancılık (~%6):** İşgücünün %15'ini istihdam eder; Türkiye fındık (dünya üretiminin %70'i), kuru incir, kayısı ve kirazda dünya ihracat lideridir.
- **Makroekonomik İstikrar Programı:** Yüksek enflasyon ve cari açık baskısına karşı Orta Vadeli Program (OVP) çerçevesinde parasal sıkılaşma ve mali disiplin uygulanmaktadır [WB-TUR-2024]."""

    m11["sections"][1]["title"] = "2. İmalat Sanayii Rekabetçiliği ve İhracat Profili"
    m11["sections"][1]["content"] = """Türkiye yıllık **255 milyar doların üzerinde mal ihracatı** gerçekleştirmektedir:
- **Otomotiv Sanayii:** Yıllık 1,4 milyondan fazla araç üretimiyle Avrupa'nın 4. büyük üreticisidir (Ford Otosan, Renault, Tofaş/Fiat, Toyota, Hyundai ve yerli elektrikli otomobil **Togg**). Yıllık 35 milyar doları aşan ihracatıyla Türkiye'nin lider ihracat kalemidir.
- **Beyaz Eşya ve Tüketici Elektroniği:** **Arçelik (Beko)** ve **Vestel** ile Avrupa'da satılan her dört büyük ev aletinden biri Türkiye'de üretilmektedir.
- **Tekstil ve Hazır Giyim:** Dünyanın 5. büyük hazır giyim ihracatçısı.
- **1995 AB Gümrük Birliği:** Sanayi ürünlerinde sıfır gümrük vergisi sağlamakta, Türkiye'nin toplam ihracatının %41'inden fazlası AB pazarına (başta Almanya olmak üzere) gitmektedir [WB-TUR-2024]."""

    m11["sections"][2]["title"] = "3. Düzenleyici Kurumsal Mimari: Rekabet Kurumu, KİK ve Hazine"
    m11["sections"][2]["content"] = """Piyasa mekanizmasının şeffaflığı ve dürüst rekabet bağımsız kurumlarca denetlenir:
- **Rekabet Kurumu:** 4054 Sayılı Kanun kapsamında kartelleri, hakim durumun kötüye kullanılmasını ve şirket birleşme/devralmalarını soruşturur.
- **Kamu İhale Kurumu (KİK):** 4734 Sayılı Kamu İhale Kanunu uyarınca kamu ihalelerinin rekabetçi, saydam ve eşit şartlarda yapılmasını denetler, EKAP elektronik ihale platformunu yönetir.
- **Hazine ve Maliye Bakanlığı:** Kamu maliyesi, devlet borçlanması ve Gelir İdaresi Başkanlığı (GİB) aracılığıyla vergi politikasını yürütür.
- **Strateji ve Bütçe Başkanlığı (SBB):** Kalkınma planları ve makro bütçe dengesini koordine eder [WB-TUR-2024]."""

    m11["sections"][3]["title"] = "4. Büyük Sanayi Holdingleri ve İş Dünyası Kuruluşları"
    m11["sections"][3]["content"] = """Özel sektör büyük aile holdingleri ve organize iş dünyası çatı örgütlerinden oluşur:
- **Öncü Sanayi Holdingleri:**
  - **Koç Holding:** Ülke ihracatının ~%8'ini, GSYH'nin ~%7'sini temsil eder (Tüpraş, Ford Otosan, Tofaş, Arçelik, Yapı Kredi).
  - **Sabancı Holding:** Akbank, Enerjisa, Kordsa ve Brisa ile finans, enerji ve sanayide dev güç.
  - **Eczacıbaşı, Yıldız Holding (pladis), Anadolu Grubu, Cengiz, Kalyon, Limak.**
- **İş Dünyası Kuruluşları:**
  - **TOBB:** 365 oda ve borsa ile 1,5 milyon işletmeyi temsil eden yasal çatı kuruluş.
  - **TÜSİAD:** Büyük ölçekli seküler sanayi ve finans sermayesini temsil eder.
  - **MÜSİAD:** Muhafazakar tabanlı KOBİ'leri ve Anadolu sanayicilerini temsil eder.
  - **TİM:** 27 ihracatçı sektör birliğini koordine eden Türkiye İhracatçılar Meclisi [WB-TUR-2024]."""

    m11["infographics"][0]["title"] = "Türkiye'nin Lider İhracatçı Sektörleri ve Küresel Rekabet Gücü"
    m11["infographics"][0]["headers"] = ["Sanayi Sektörü", "Yıllık İhracat Hacmi", "Öncü Üretici Şirketler", "Ana İhracat Pazarları", "Rekabet Üstünlüğü Faktörü"]
    m11["infographics"][0]["rows"] = [
        ["Otomotiv ve Yan Sanayi", "35 Milyar $+ / yıl", "Ford Otosan, Renault, Tofaş, Toyota, Togg", "Almanya, Fransa, Birleşik Krallık, İtalya", "Gümrük Birliği, yetişmiş işgücü, modern robotik hatlar"],
        ["Kimyevi Maddeler ve Petrol", "30 Milyar $+ / yıl", "Tüpraş, Petkim, SASA, Aksa Akrilik", "Hollanda, İtalya, Almanya, ABD", "Büyük rafineri kapasitesi ve petrokimya entegrasyonu"],
        ["Hazır Giyim ve Konfeksiyon", "20 Milyar $+ / yıl", "LC Waikiki, DeFacto, Koton, Yeşim Tekstil", "Almanya, İspanya, Birleşik Krallık, Hollanda", "Hızlı termin süresi, tasarım kalitesi, esnek üretim"],
        ["Çelik ve Metal Sanayii", "16 Milyar $+ / yıl", "Erdemir, İsdemir, İçdaş, Çolakoğlu", "ABD, Romanya, İtalya, Mısır", "Elektrik ark ocaklı üretim hızı ve kapasite büyüklüğü"],
        ["Elektrik ve Beyaz Eşya", "16 Milyar $+ / yıl", "Arçelik (Beko), Vestel, Karel", "Birleşik Krallık, Almanya, Fransa, Polonya", "Avrupa beyaz eşya pazarında %25'i aşan pazar payı"],
        ["Makine ve Havacılık", "12 Milyar $+ / yıl", "TUSAŞ, Aselsan, Baykar, Hidromek", "ABD, Almanya, Azerbaycan, Körfez", "Yüksek hassasiyetli CNC işleme, SİHA ihracat liderliği"]
    ]

    m11["infographics"][1]["title"] = "Makroekonomik Büyüklükler ve Dış Ticaret Göstergeleri"
    m11["infographics"][1]["data"] = [
        {"label": "Nominal GSYH", "value": "1,1+ Trilyon $", "sub": "Dünyanın en büyük 17. ekonomisi"},
        {"label": "Yıllık Mal İhracatı", "value": "255 Milyar $+ / yıl", "sub": "Cumhuriyet tarihinin ihracat rekoru"},
        {"label": "Yıllık Turizm Geliri", "value": "54 Milyar $+ / yıl", "sub": "56 Milyondan fazla yabancı ziyaretçi"},
        {"label": "Gümrük Birliği Ortağı", "value": "Avrupa Birliği", "sub": "Toplam ihracatın %41'den fazlası AB'ye"},
        {"label": "Otomotiv Üretim Adedi", "value": "1,4 Milyon Araç/yıl", "sub": "Avrupa'nın en büyük 4. üreticisi"},
        {"label": "Fındık Küresel Payı", "value": "~%70 Dünya Toplamı", "sub": "Dünyanın tartışmasız ihracat lideri"}
    ]

    # Module 12: Finansal Sistem
    m12 = tr[11]
    m12["title"] = "Finansal Sistem ve Bankacılık Mimarisi"
    m12["tagline"] = "Merkez Bankası (TCMB), BDDK, SPK, kamu bankaları, katılım bankacılığı ve Borsa İstanbul."
    m12["readingTime"] = "29 dk okuma"
    m12["summary"] = "Türkiye Cumhuriyet Merkez Bankası (TCMB) fiyat istikrarı görevi, Para Politikası Kurulu (PPK) politika faizi ve rezerv politikası; BDDK ve Basel III sermaye yeterliliği regülasyonu; SPK; Ziraat, Halk ve Vakıf kamu bankaları; İş Bankası ve Garanti özel bankaları; katılım bankacılığı (%9 pay); Borsa İstanbul (BIST) ve Türkiye Varlık Fonu (TVF)."

    m12["sections"][0]["title"] = "1. Türkiye Cumhuriyet Merkez Bankası (TCMB) ve Para Politikası"
    m12["sections"][0]["content"] = """11 Haziran 1930'da kurulan **TCMB**, fiyat istikrarını ve finansal istikrarı sağlamakla kanunen yetkili bağımsız para otoritesidir:
- **Para Politikası Kurulu (PPK):** Aylık toplanarak bir haftalık repo ihale faiz oranını (politika faizi), gecelik faiz koridorunu ve zorunlu karşılık oranlarını belirler.
- **Para Politikası Dönüşümü:** 2021-2023 döneminde uygulanan düşük faiz politikası sonrası, Haziran 2023 itibarıyla ortodoks para politikasına dönülmüş; politika faizi agresif biçimde yükseltilerek enflasyon beklentileri çıpalanmış ve rezervler güçlendirilmiştir.
- **Rezerv Yönetimi:** Resmi brüt ve net döviz ve altın rezervlerini yönetir [TCMB-ANN-2024]."""

    m12["sections"][1]["title"] = "2. Bağımsız Düzenleyici Kurullar: BDDK, SPK ve TMSF"
    m12["sections"][1]["content"] = """2001 bankacılık krizinin ardından Türk bankacılık sektörü dünyadaki en sıkı denetim standartlarına kavuşturulmuştur:
- **Bankacılık Düzenleme ve Denetleme Kurumu (BDDK):** Bankaların sermaye yeterlilik oranını (SYR / CAR) denetler; Türk bankacılık sektörü **Basel III standartlarının çok üzerinde (>%17)** sermaye yeterliliğine sahiptir.
- **Sermaye Piyasası Kurulu (SPK):** 6362 Sayılı Sermaye Piyasası Kanunu uyarınca halka arzları (GİP/BİST), yatırım fonlarını ve aracı kurumları denetler.
- **Tasarruf Mevduatı Sigorta Fonu (TMSF):** Tasarruf mevduatlarını yasal limit dahilinde sigorta eder [BDDK-2024-MONTH]."""

    m12["sections"][2]["title"] = "3. Bankacılık Sektörü: Kamu, Özel ve Katılım Bankacılığı"
    m12["sections"][2]["content"] = """Türk bankacılık sistemi **850 milyar doları aşan varlık büyüklüğüne** sahiptir:
- **Kamu Mevduat Bankaları:** Kriz dönemlerinde kredi genişlemesini destekler:
  - **Ziraat Bankası (1863):** Türkiye'nin en büyük ve köklü bankası; tarım ve kurumsal kredi lideri.
  - **Halkbank (1938):** Esnaf ve KOBİ finansmanı.
  - **VakıfBank (1954):** Vakıf gelirleri ve kurumsal bankacılık.
- **Özel ve Yabancı Bankalar:** Dijital bankacılıkta dünya öncüsü: **Türkiye İş Bankası (1924)**, **Garanti BBVA**, **Akbank**, **Yapı Kredi**, **QNB Finansbank**.
- **Katılım Bankacılığı (Faizsiz Bankacılık):** Kar-zarar ortaklığı ve sukuk finansmanına dayanır; Kuveyt Türk, Albaraka Türk, Türkiye Finans ile kamu katılım bankaları (Ziraat Katılım, Vakıf Katılım) sektörün yaklaşık **%8-10'unu** oluşturur [BDDK-2024-MONTH]."""

    m12["sections"][3]["title"] = "4. Borsa İstanbul (BIST) ve Türkiye Varlık Fonu (TVF)"
    m12["sections"][3]["content"] = """Sermaye piyasaları ve stratejik devlet yatırımları:
- **Borsa İstanbul (BIST):** Pay Piyasası (BIST 100, BIST 30), Borçlanma Araçları Piyasası, Vadeli İşlem ve Opsiyon Piyasası (VİOP) ve Kıymetli Madenler Piyasasını tek çatı altında toplar; kayıtlı yerli yatırımcı sayısı 7,5 milyonu aşmıştır.
- **Türkiye Varlık Fonu (TVF):** 2016'da kurulan devlet varlık fonudur. THY, BOTAŞ, Turkcell, Türk Telekom, Borsa İstanbul ve kamu bankalarındaki stratejik hisseleri yönetir."""

    m12["infographics"][0]["title"] = "Türk Finansal Sistemi ve Bankacılık Kurumsal Matrisi"
    m12["infographics"][0]["headers"] = ["Finansal Kurum", "Kurumsal Statüsü", "Kuruluş Yılı", "Temel Kanuni Görevi", "Denetim Mercii"]
    m12["infographics"][0]["rows"] = [
        ["TCMB (Merkez Bankası)", "Para Otoritesi", "1930", "Fiyat istikrarı, para politikası, politika faizi, rezervler", "Özel Kanunla Bağımsız"],
        ["BDDK", "Düzenleyici Kurum", "2000", "Bankacılık denetimi, Basel III sermaye yeterliliği, lisanslama", "Bağımsız İdari Otorite"],
        ["SPK", "Sermaye Piyasası Kurulu", "1981", "Borsa şirketleri, halka arzlar, fonlar, yatırımcı koruma", "Bağımsız İdari Otorite"],
        ["TMSF", "Mevduat Sigorta Fonu", "1983", "Tasarruf mevduatlarını sigortalama, sorunlu banka tasfiyesi", "Bağımsız İdari Otorite"],
        ["Ziraat Bankası", "Kamu Ticari Bankası", "1863", "Varlık büyüklüğünde lider banka, tarım ve KOBİ finansmanı", "BDDK Denetiminde"],
        ["Türkiye İş Bankası", "Özel Ticari Banka", "1924", "İlk milli özel banka, evrensel ticari ve dijital bankacılık", "BDDK Denetiminde"],
        ["Kuveyt Türk", "Katılım Bankası", "1989", "En büyük faizsiz katılım bankası (kar-zarar ortaklığı)", "BDDK / TKBB Denetiminde"],
        ["Borsa İstanbul (BIST)", "Finansal Borsa", "1873/2013", "Hisse senedi, borçlanma aracı, VİOP ve altın borsası", "SPK Düzenlemesinde"],
        ["Türkiye Varlık Fonu (TVF)", "Milli Varlık Fonu", "2016", "Stratejik devlet varlıklarının portföy yönetimi (THY, BOTAŞ)", "Cumhurbaşkanlığı"]
    ]

    m12["infographics"][1]["title"] = "Finans Sektörü Büyüklükleri ve Sermaye Rasyoları (2024)"
    m12["infographics"][1]["data"] = [
        {"label": "Toplam Bankacılık Aktifi", "value": "850 Milyar $+", "sub": "Finansal sistemin en büyük omurgası"},
        {"label": "Sermaye Yeterliliği (CAR)", "value": ">%17 Düzeyinde", "sub": "%8'lik Basel asgari sınırının çok üzerinde"},
        {"label": "Katılım Bankacılığı Payı", "value": "~%9 Aktif Payı", "sub": "Faizsiz finans prensipleriyle çalışan bankalar"},
        {"label": "BIST Yatırımcı Sayısı", "value": "7,5 Milyon+ Hesap", "sub": "Halka arzlarla bireysel yatırımcı patlaması"},
        {"label": "Kamu Bankaları Payı", "value": "~%35 Varlık Payı", "sub": "Ziraat, Halkbank ve VakıfBank şebekesi"},
        {"label": "TCMB Politika Aracı", "value": "1 Haftalık Repo", "sub": "Para Politikası Kurulu (PPK) faizi"}
    ]

    # Module 13: Din ve Dini Kurumlar
    m13 = tr[12]
    m13["title"] = "Din ve Dini Kurumlar"
    m13["tagline"] = "Laiklik ilkesi, Diyanet İşleri Başkanlığı, Sünni gelenekler, Alevilik-Bektaşilik ve gayrimüslim cemaatler."
    m13["readingTime"] = "28 dk okuma"
    m13["summary"] = "Türkiye'de din-devlet ilişkileri, Fransız laïcité esinli anayasal laiklik ilkesi, 140 binden fazla personeliyle Diyanet İşleri Başkanlığı bürokrasisi, Sünni Hanefi ve Şafii mezhepleri, Alevi-Bektaşi inanç dünyası (Cemevi ve 2022 Başkanlığı), tasavvufi tarikat ve cemaatler ile gayrimüslim patrikhane ve hahambaşılıklar."

    m13["sections"][0]["title"] = "1. Anayasal Laiklik İlkesi ve Tarihsel Sekülerleşme"
    m13["sections"][0]["content"] = """Türkiye'de laiklik ilkesi, Anglo-Amerikan pasif laikliğinden (din ve devletin mutlak ayrılığı) farklı olarak, Fransız *laïcité* geleneğinden mülhem **dinin devlet denetim ve gözetimi altında kurumsallaşması** modeline dayanır:
- **Anayasal Statü:** 1982 Anayasası'nın 2. maddesinde cumhuriyetin değiştirilemez niteliği olarak tescil edilmiştir. 24. madde vicdan ve ibadet özgürlüğünü güvenceye alırken, dini inançların devletin temel hukuki ve siyasi düzenini belirleyemeyeceğini hükme bağlar.
- **Sekülerleşme Kronolojisi:**
  - *1922:* Saltanatın kaldırılması.
  - *3 Mart 1924:* Hilafetin ilgası (431 Sayılı Kanun) ve Tevhid-i Tedrisat (eğitimin birleştirilmesi).
  - *1925:* Tekke, zaviye ve türbelerin kapatılması (677 Sayılı Kanun).
  - *1926:* İsviçre Medeni Kanunu ile şer'i mahkemelerin ve aile hukukunun ilga edilmesi.
  - *1928:* 'Devletin dini İslam'dır' ibaresinin anayasadan çıkarılması.
  - *1937:* Laiklik ilkesinin anayasaya açıkça dercedilmesi [TBMM-CONST-1982, ZURCHER-2017]."""

    m13["sections"][1]["title"] = "2. Diyanet İşleri Başkanlığı Teşkilatı"
    m13["sections"][1]["content"] = """3 Mart 1924 tarihinde Şer'iye ve Evkaf Vekâleti'nin yerine 429 Sayılı Kanun'la doğrudan Başbakanlığa (bugün Cumhurbaşkanlığına) bağlı olarak kurulmuştur:
- **Kurumsal Güç:** 140 binden fazla kadrolu kamu görevlisi (imam, müezzin, vaiz, müftü), 90 binden fazla cami ve genel bütçeden ayrılan devasa kaynak.
- **Temel Görevleri:** İslam dininin inanç ve ibadet esaslarını yürütmek, cuma hutbelerini hazırlamak, Din İşleri Yüksek Kurulu aracılığıyla fetva vermek, Kur'an kurslarını yönetmek, hac ve umre organizasyonunu sağlamak ve DİTİB gibi kuruluşlarla yurtdışındaki Türk vatandaşlarına dini hizmet sunmak [DCP-DIYANET-2024]."""

    m13["sections"][2]["title"] = "3. İslami Mezhepler: Sünni Hanefi ve Şafii Gelenek"
    m13["sections"][2]["content"] = """Nüfusun ezici çoğunluğu İslam dinine mensuptur:
- **Hanefi Mezhebi:** Müslüman nüfusun yaklaşık **%70–75'ini** oluşturur. Osmanlı'nın resmi mezhebi olan Hanefilik, akli kıyasa ve içtihada verdiği önemle Trakya, İç, Batı ve Karadeniz bölgelerinde yaygındır.
- **Şafii Mezhebi:** Müslüman nüfusun yaklaşık **%10–12'sini** oluşturur; özellikle Doğu ve Güneydoğu Anadolu'daki Kürt vatandaşlar arasında yaygındır [ZURCHER-2017]."""

    m13["sections"][3]["title"] = "4. Alevi-Bektaşi İnanç Geleneği ve Cemevleri"
    m13["sections"][3]["content"] = """Alevi-Bektaşi topluluğu, nüfusun **yaklaşık %10–15'ini** (~8–12 milyon kişi) teşkil eden ikinci büyük inanç havzasıdır:
- **İnanç Esasları:** Anadolu tasavvufu, Hz. Ali ve Ehl-i Beyt sevgisi, On İki İmamlar ve Hacı Bektaş Veli öğretileriyle şekillenmiştir. *"Eline, diline, beline sahip ol"* ahlak prensibi esastır.
- **Cem ve Cemevi:** İbadet mekanı **Cemevi**'dir; dedeler önderliğinde icra edilen **Cem** erkanında bağlama eşliğinde deyişler söylenir ve kadın-erkek birlikte **Semah** döner.
- **2022 Reformu:** Kasım 2022'de Kültür ve Turizm Bakanlığı bünyesinde **Alevi-Bektaşi Kültür ve Cemevi Başkanlığı** kurularak Cemevlerinin aydınlatma, su ve bakım giderleri devlet tarafından karşılanmaya başlanmıştır."""

    m13["sections"][4]["title"] = "5. Tarikatlar, Cemaatler ve Gayrimüslim Ruhani Merkezler"
    m13["sections"][4]["content"] = """Dini sosyolojinin diğer kilit unsurları:
- **Tarikat ve Cemaatler:** 1925'te 677 Sayılı Kanun'la kapatılmalarına rağmen vakıf ve dernek hüviyetiyle varlıklarını sürdürmüşlerdir:
  - **Nakşibendilik:** En yaygın tasavvufi ekoldür (İskenderpaşa, İsmailağa, Menzil kolları).
  - **Nur Cemaati:** Bediüzzaman Said Nursi'nin Risale-i Nur külliyatı etrafında teşekkül etmiştir.
  - **Kadirilik ve Mevlevilik.**
- **Gayrimüslim Ruhani Merkezler:**
  - **Ekümenik Fener Rum Patrikhanesi (İstanbul Fener):** Dünya Doğu Ortodoksluğunun tarihi birinci makamı (*primus inter pares*), Patrik I. Bartholomeos liderliğindedir.
  - **İstanbul Ermeni Patrikhanesi (Kumkapı):** Türkiye'deki Ermeni Gregoryen cemaatinin ruhani liderliği.
  - **Türkiye Hahambaşılığı:** Musevi cemaatinin dini idaresi.
  - **Süryani Kadim Metropolitliği:** Mardin Mor Gabriel ve Deyrulzafaran manastırları [LAUSANNE-1923]."""

    m13["infographics"][0]["title"] = "Çağdaş Türkiye Dini İnanç ve Mezhep Dağılımı Matrisi"
    m13["infographics"][0]["headers"] = ["İnanç / Gelenek", "İlahiyat / İtikad Kolu", "Tahmini Nüfus Payı", "İbadethane / Toplanma Yeri", "Kurumsal Temsil Mercii"]
    m13["infographics"][0]["rows"] = [
        ["Sünni (Hanefi)", "İslam (Hanefi Fıkhı)", "~%70–75 Nüfus Payı", "Cami ve Mescitler", "Diyanet İşleri Başkanlığı"],
        ["Sünni (Şafii)", "İslam (Şafii Fıkhı)", "~%10–12 Nüfus Payı", "Cami ve Mescitler", "Diyanet İşleri Başkanlığı"],
        ["Alevi-Bektaşi", "Anadolu Şii-Tasavvuf Sentezi", "~%10–15 Nüfus Payı", "Cemevleri", "Alevi-Bektaşi Kültür ve Cemevi Başkanlığı"],
        ["Ermeni Apostolik", "Doğu Hristiyanlığı (Gregoryen)", "~50.000–60.000 Kişi", "Surp Asdvadzadzin Patriklik Kilisesi", "İstanbul Ermeni Patrikhanesi"],
        ["Sefarad Musevilik", "Rabbanik Musevilik", "~14.000–15.000 Kişi", "Neve Şalom ve Bet İsrail Sinagogları", "Türkiye Hahambaşılığı"],
        ["Rum Ortodoks", "Doğu Ortodoks Kilisesi", "~2.000–3.000 Kişi", "Aya Yorgi Patriklik Kilisesi (Fener)", "Ekümenik Fener Rum Patrikhanesi"],
        ["Süryani Kadim", "Süryani Ortodoks Kilisesi", "~25.000 Kişi", "Deyrulzafaran ve Mor Gabriel Manastırları", "Süryani Kadim Metropolitliği"]
    ]

    m13["infographics"][1]["title"] = "Diyanet Teşkilatı ve Dini Demografi Göstergeleri"
    m13["infographics"][1]["data"] = [
        {"label": "Diyanet Personel Sayısı", "value": "140.000+ Memur", "sub": "İmam, müftü, vaiz, Kur'an öğreticisi"},
        {"label": "Türkiye'deki Cami Sayısı", "value": "90.000+ Cami", "sub": "Diyanet bünyesinde ibadete açık"},
        {"label": "Sünni Müslüman Oranı", "value": "~%80–85", "sub": "Hanefi çoğunluk, Güneydoğu'da Şafii"},
        {"label": "Alevi Nüfus Oranı", "value": "~%10–15", "sub": "Cemevi ibadet geleneği"},
        {"label": "Ekümenik Patrikhane", "value": "Fener, İstanbul", "sub": "Doğu Ortodoksluğunun tarihi merkezi"},
        {"label": "Anayasal Laiklik", "value": "Madde 2 İlkesi", "sub": "Fransız tipi devlet denetimi modeli"}
    ]

    return tr
