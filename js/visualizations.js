/**
 * Visualizations & Infographics Engine for Anatolia Academic
 * Produces crisp, responsive vector graphics (SVG), interactive regional maps,
 * seismic fault line visualizations, energy mix breakdowns, institutional organograms, and schemes.
 * Fully localized for English, Turkish, and Russian.
 */

const Visualizations = {
  // Helper to obtain current language
  getLang() {
    return (typeof MasterData !== 'undefined' && MasterData.currentLang) || 'en';
  },

  // Localized dictionary for visualization shells and metadata
  i18n: {
    en: {
      timelineSub: "Interactive chronological progression of pivotal sovereign, legal, and diplomatic milestones",
      statSub: "Key statistical benchmarks verified with official regulatory bodies, institutes, and databases",
      tableSub: "Comparative cross-sectional analysis across historical, institutional, and structural parameters",
      organogramSub: "Hierarchical administrative, operational, and command topology",
      mapTitle: "Interactive Geographical Map: The Seven Regions of Turkey",
      mapSub: "Click any geographic region to inspect morphological, climatic, demographic, and economic profiles (Source: First Geography Congress, Ankara [TUIK-2024-POP])",
      regionBadge: "Selected Region",
      areaLabel: "Area Share",
      popLabel: "Population",
      climateLabel: "Climate Profile",
      econLabel: "Key Economic Pillars",
      seas: {
        blackSea: "BLACK SEA (KARA DENİZ)",
        marmaraSea: "Sea of Marmara",
        aegeanSea: "AEGEAN SEA (EGE)",
        medSea: "MEDITERRANEAN SEA (AKDENİZ)",
        lakeVan: "Lake Van"
      },
      regionNames: {
        marmara: "MARMARA",
        aegean: "AEGEAN",
        med: "MEDITERRANEAN",
        central: "CENTRAL ANATOLIA",
        blacksea: "BLACK SEA",
        east: "EASTERN ANATOLIA",
        southeast: "SOUTHEAST"
      },
      seismicTitle: "Geotectonic & Active Seismic Fault Architecture of Anatolia",
      seismicSub: "Major strike-slip fault zones driving continental plate escape westward (Source: AFAD, MTA & Kandilli Observatory [AYM-REPORTS, WB-TUR-2024])",
      plates: {
        eurasian: "EURASIAN PLATE (Stable)",
        arabian: "ARABIAN PLATE (Moving North ~15–20 mm/yr)",
        anatolian: "ANATOLIAN MICROPLATE (Escaping Westward ~22 mm/yr)"
      },
      faultLabels: {
        nafz: "North Anatolian Fault Zone (NAFZ - Right Lateral Strike-Slip, 1,500 km)",
        eafz: "East Anatolian Fault Zone (EAFZ - Left Lateral Strike-Slip, 500 km)",
        karliova: "Karlıova Triple Junction",
        grabens: "Aegean Extensional Grabens",
        erzincan: "1939 Erzincan (Mw 7.8)",
        golcuk: "1999 Gölcük (Mw 7.6)",
        maras: "2023 Kahramanmaraş Doublet (Mw 7.8 & 7.6)"
      },
      seismicLegend: {
        nafz: "Right-Lateral Strike-Slip (NAFZ)",
        eafz: "Left-Lateral Strike-Slip (EAFZ)",
        grabens: "Extensional Horst-Graben Faults",
        epicenters: "Major Historical Seismic Epicenters"
      },
      energyTitle: "Electricity Generation Capacity Breakdown by Primary Source (2024)",
      energySub: "Total installed capacity exceeding 107,000 MW with ~54% renewable share (Source: EPDK & TEİAŞ Official Statistics [EPDK-2024-NRG, IEA-TUR-2023])",
      energySources: {
        hydro: "Hydroelectric Power (Dams & Run-of-River)",
        gas: "Natural Gas Thermal Plants (CCGT)",
        coal: "Coal & Lignite (Imported & Domestic)",
        solar: "Solar Photovoltaic (YEKA & Rooftop PV)",
        wind: "Wind Power (Aegean & Marmara Turbines)",
        geo: "Geothermal & Biomass"
      },
      pipelinesTitle: "Strategic Pipeline Transit Corridors",
      pipelineList: [
        { label: "TANAP", desc: "16 bcm/yr Shah Deniz Caspian gas to Europe" },
        { label: "TurkStream", desc: "31.5 bcm/yr Russian gas across Black Sea" },
        { label: "Blue Stream", desc: "16 bcm/yr direct Russian deepwater pipeline" },
        { label: "BTC Pipeline", desc: "1.0M bpd crude oil to Ceyhan terminal" },
        { label: "Akkuyu NPP", desc: "4,800 MW (4x VVER-1200) under Rosatom BOO" }
      ],
      citeText: "Source: EPDK Annual Sector Report [EPDK-2024-NRG]"
    },
    tr: {
      timelineSub: "Tarihsel, egemen ve diplomatik dönüm noktalarının etkileşimli kronolojik akışı",
      statSub: "Resmi düzenleyici kurumlar, enstitüler ve veri tabanlarınca teyit edilmiş temel istatistiki göstergeler",
      tableSub: "Tarihsel, kurumsal ve yapısal parametreler üzerinden karşılaştırmalı matris analizi",
      organogramSub: "Hiyerarşik idari, operasyonel ve komuta-kontrol teşkilat şeması",
      mapTitle: "Etkileşimli Coğrafi Harita: Türkiye'nin Yedi Coğrafi Bölgesi",
      mapSub: "Morfolojik, iklimsel, demografik ve ekonomik profilleri incelemek için herhangi bir bölgeye tıklayın (Kaynak: Birinci Coğrafya Kongresi, Ankara [TUIK-2024-POP])",
      regionBadge: "Seçili Bölge",
      areaLabel: "Yüzölçümü Oranı",
      popLabel: "Nüfus",
      climateLabel: "İklim Profili",
      econLabel: "Temel Ekonomik Sektörler",
      seas: {
        blackSea: "KARADENİZ",
        marmaraSea: "Marmara Denizi",
        aegeanSea: "EGE DENİZİ",
        medSea: "AKDENİZ",
        lakeVan: "Van Gölü"
      },
      regionNames: {
        marmara: "MARMARA",
        aegean: "EGE",
        med: "AKDENİZ",
        central: "İÇ ANADOLU",
        blacksea: "KARADENİZ",
        east: "DOĞU ANADOLU",
        southeast: "GÜNEYDOĞU"
      },
      seismicTitle: "Anadolu'nun Jeotektonik ve Aktif Sismik Fay Mimarisi",
      seismicSub: "Anadolu levhasının batıya kaçışını yönlendiren ana doğrultu atımlı fay hatları (Kaynak: AFAD, MTA ve Kandilli Rasathanesi [AYM-REPORTS, WB-TUR-2024])",
      plates: {
        eurasian: "AVRASYA LEVHASI (Kararlı)",
        arabian: "ARAP LEVHASI (Kuzeye hareket ~15–20 mm/yıl)",
        anatolian: "ANADOLU MİKROLEVHASI (Batıya kaçış ~22 mm/yıl)"
      },
      faultLabels: {
        nafz: "Kuzey Anadolu Fay Hattı (KAF - Sağ Yönlü Doğrultu Atımlı, 1.500 km)",
        eafz: "Doğu Anadolu Fay Hattı (DAF - Sol Yönlü Doğrultu Atımlı, 500 km)",
        karliova: "Karlıova Üçlü Eklemi",
        grabens: "Ege Horst-Graben Genişleme Sistemi",
        erzincan: "1939 Erzincan (Mw 7.8)",
        golcuk: "1999 Gölcük (Mw 7.6)",
        maras: "2023 Kahramanmaraş Depremleri (Mw 7.8 & 7.6)"
      },
      seismicLegend: {
        nafz: "Sağ Yönlü Doğrultu Atımlı (KAF)",
        eafz: "Sol Yönlü Doğrultu Atımlı (DAF)",
        grabens: "Genişlemeli Horst-Graben Fayları",
        epicenters: "Tarihsel Büyük Deprem Merkez üsleri"
      },
      energyTitle: "Birincil Kaynaklara Göre Elektrik Kurulu Güç Dağılımı (2024)",
      energySub: "%54'ü aşan yenilenebilir payıyla 107.000 MW'ı aşan toplam kurulu güç (Kaynak: EPDK ve TEİAŞ Resmi İstatistikleri [EPDK-2024-NRG, IEA-TUR-2023])",
      energySources: {
        hydro: "Hidroelektrik Santraller (Barajlı ve Akarsu)",
        gas: "Doğalgaz Kombine Çevrim Santralleri",
        coal: "Kömür ve Linyit (İthal ve Yerli)",
        solar: "Güneş Enerjisi (YEKA ve Çatı GES)",
        wind: "Rüzgar Enerjisi (Ege ve Marmara RES)",
        geo: "Jeotermal ve Biyokütle"
      },
      pipelinesTitle: "Stratejik Boru Hatları Transit Koridorları",
      pipelineList: [
        { label: "TANAP", desc: "16 milyar m³/yıl Şah Deniz Hazar gazını Avrupa'ya taşır" },
        { label: "TürkAkım", desc: "31,5 milyar m³/yıl Karadeniz derin deniz Rus doğalgazı" },
        { label: "Mavi Akım", desc: "16 milyar m³/yıl Rusya'dan doğrudan Karadeniz hattı" },
        { label: "BTC Hattı", desc: "1,0M varil/gün Ceyhan terminaline Hazar ham petrolü" },
        { label: "Akkuyu NGS", desc: "4.800 MW (4x VVER-1200) Rosatom BOO modeli" }
      ],
      citeText: "Kaynak: EPDK Yıllık Sektör Raporu [EPDK-2024-NRG]"
    },
    ru: {
      timelineSub: "Интерактивная хронология ключевых суверенных, правовых и дипломатических вех",
      statSub: "Ключевые статистические показатели, верифицированные официальными ведомствами и базами данных",
      tableSub: "Сравнительный матричный анализ по историческим, институциональным и структурным параметрам",
      organogramSub: "Иерархическая административная, оперативная и командная топология",
      mapTitle: "Интерактивная географическая карта: Семь регионов Турции",
      mapSub: "Нажмите на любой географический регион для изучения морфологического, климатического, демографического и экономического профиля (Источник: Первый географический конгресс, Анкара [TUIK-2024-POP])",
      regionBadge: "Выбранный регион",
      areaLabel: "Доля площади",
      popLabel: "Население",
      climateLabel: "Климатический профиль",
      econLabel: "Ключевые секторы экономики",
      seas: {
        blackSea: "ЧЕРНОЕ МОРЕ (KARA DENİZ)",
        marmaraSea: "Мраморное море",
        aegeanSea: "ЭГЕЙСКОЕ МОРЕ (EGE)",
        medSea: "СРЕДИЗЕМНОЕ МОРЕ (AKDENİZ)",
        lakeVan: "Озеро Ван"
      },
      regionNames: {
        marmara: "МРАМОРНОМОРСКИЙ",
        aegean: "ЭГЕЙСКИЙ",
        med: "СРЕДИЗЕМНОМОРСКИЙ",
        central: "ЦЕНТРАЛЬНАЯ АНАТОЛИЯ",
        blacksea: "ЧЕРНОМОРСКИЙ",
        east: "ВОСТОЧНАЯ АНАТОЛИЯ",
        southeast: "ЮГО-ВОСТОК"
      },
      seismicTitle: "Геотектоническая и активная сейсмическая структура Анатолии",
      seismicSub: "Основные сдвиговые зоны разломов, направляющие вытеснение Анатолийской плиты на запад (Источник: AFAD, MTA и Обсерватория Кандилли [AYM-REPORTS, WB-TUR-2024])",
      plates: {
        eurasian: "ЕВРАЗИЙСКАЯ ПЛИТА (Стабильная)",
        arabian: "АРАВИЙСКАЯ ПЛИТА (Движение на север ~15–20 мм/год)",
        anatolian: "АНАТОЛИЙСКАЯ МИКРОПЛИТА (Смещение на запад ~22 мм/год)"
      },
      faultLabels: {
        nafz: "Северо-Анатолийская зона разломов (NAFZ - правый сдвиг, 1 500 км)",
        eafz: "Восточно-Анатолийская зона разломов (EAFZ - левый сдвиг, 500 км)",
        karliova: "Тройное сочленение Карлыова",
        grabens: "Эгейские грабены растяжения",
        erzincan: "1939 г. Эрзинджан (Mw 7.8)",
        golcuk: "1999 г. Гёльджук (Mw 7.6)",
        maras: "2023 г. Кахраманмараш (Mw 7.8 & 7.6)"
      },
      seismicLegend: {
        nafz: "Правосдвиговой разлом (NAFZ)",
        eafz: "Левосдвиговой разлом (EAFZ)",
        grabens: "Сбросовые грабены растяжения",
        epicenters: "Эпицентры сильнейших исторических землетрясений"
      },
      energyTitle: "Структура установленной мощности электрогенерации по первичным источникам (2024 г.)",
      energySub: "Совокупная мощность превышает 107 000 МВт с долей ВИЭ свыше 54% (Источник: EPDK и официальная статистика TEİAŞ [EPDK-2024-NRG, IEA-TUR-2023])",
      energySources: {
        hydro: "Гидроэлектростанции (плотинные и деривационные)",
        gas: "Газовые теплоэлектростанции (ПГУ)",
        coal: "Уголь и лигнит (импортный и отечественный)",
        solar: "Солнечная энергетика (СЭС и кровельные панели)",
        wind: "Ветроэнергетика (ВЭС Эгейского и Мраморного регионов)",
        geo: "Геотермальная энергия и биомасса"
      },
      pipelinesTitle: "Стратегические транзитные трубопроводные коридоры",
      pipelineList: [
        { label: "TANAP", desc: "16 млрд м³/год каспийского газа Шах-Дениз в Европу" },
        { label: "«Турецкий поток»", desc: "31.5 млрд м³/год российского газа по дну Черного моря" },
        { label: "«Голубой поток»", desc: "16 млрд м³/год глубоководный прямой газопровод из РФ" },
        { label: "Нефтепровод БТК", desc: "1.0 млн барр./сутки каспийской нефти в терминал Джейхан" },
        { label: "АЭС «Аккую»", desc: "4 800 МВт (4 блока ВВЭР-1200) по схеме Росатома BOO" }
      ],
      citeText: "Источник: Годовой отчет регулятора EPDK [EPDK-2024-NRG]"
    }
  },

  // Interactive Region Data for all three languages
  regionsData: {
    en: {
      marmara: {
        title: "Marmara Region",
        desc: "Economic, financial, and industrial center of Turkey. Encompasses Eastern Thrace and Northwest Anatolia, connecting the Black Sea and Aegean via the Bosphorus and Dardanelles straits.",
        area: "~8.5% of National Surface",
        pop: "Over 30% (~26 Million)",
        climate: "Transitional (Mediterranean / Black Sea)",
        econ: "Finance (BIST), Automotive, Petrochemicals, Logistics"
      },
      blacksea: {
        title: "Black Sea Region (Karadeniz)",
        desc: "Characterized by the steep Pontic Alps running parallel to the coast, dense temperate forests, tea and hazelnut plantations (world leader), and high annual precipitation.",
        area: "~18.1% of National Surface",
        pop: "~8.4 Million",
        climate: "Oceanic / Humid Temperate",
        econ: "Agriculture (Hazelnuts, Tea), Forestry, Hydroelectricity, Mining"
      },
      aegean: {
        title: "Aegean Region (Ege)",
        desc: "Dominated by horst-and-graben fault lines and fertile east-west alluvial river valleys. Rich agricultural hinterland and leading geothermal electricity hub.",
        area: "~11.5% of National Surface",
        pop: "~10.8 Million",
        climate: "Mediterranean (Hot dry summers, mild winters)",
        econ: "Textiles, Olive Oil, Tourism, Geothermal Energy, Izmir Port"
      },
      central: {
        title: "Central Anatolian Region (İç Anadolu)",
        desc: "The geographic heartland of Anatolia; high semi-arid plateau (average elevation ~1,000 m). Capital city Ankara houses the national government, defense conglomerates, and supreme courts.",
        area: "~19.4% of National Surface",
        pop: "~13.2 Million",
        climate: "Semi-Arid Steppe (Continental)",
        econ: "Government Administration, Defense Industries, Wheat/Grains, Automotive"
      },
      med: {
        title: "Mediterranean Region (Akdeniz)",
        desc: "Defined by the rugged Taurus Mountains (Toroslar) plunging into the warm coastal shelf. Primary agricultural greenhouse center and global international tourism hub.",
        area: "~15.6% of National Surface",
        pop: "~10.9 Million",
        climate: "Subtropical Mediterranean",
        econ: "Tourism ($50B+ national sector), Citrus Fruits, Greenhouse Produce, Steel (İskenderun)"
      },
      east: {
        title: "Eastern Anatolian Region (Doğu Anadolu)",
        desc: "Turkey's highest and largest geographical region; rugged alpine topography with Mount Ararat (5,137 m) and Lake Van (3,755 km²). Severe continental winters and headwaters of Euphrates-Tigris.",
        area: "~21.0% of National Surface (Largest)",
        pop: "~6.5 Million",
        climate: "Severe Continental / Alpine",
        econ: "Livestock Husbandry, Hydroelectric Dams, Cross-border Transit (Iran/Caucasus)"
      },
      southeast: {
        title: "Southeastern Anatolian Region (Güneydoğu Anadolu)",
        desc: "Plateau descending into the Mesopotamian basin, bounded by Syria and Iraq. Transformed by the massive state-led Southeastern Anatolia Project (GAP) irrigation network.",
        area: "~9.6% of National Surface",
        pop: "~9.3 Million",
        climate: "Hot Dry Steppe / Continental",
        econ: "Irrigated Agriculture (Cotton, Pistachios), Hydroelectricity (Atatürk Dam), Light Manufacturing (Gaziantep)"
      }
    },
    tr: {
      marmara: {
        title: "Marmara Bölgesi",
        desc: "Türkiye'nin iktisadi, finansal ve sınai merkez üssüdür. Doğu Trakya ve Kuzeybatı Anadolu'yu kapsar; İstanbul ve Çanakkale boğazlarıyla Karadeniz'i Ege'ye bağlar.",
        area: "Ülke yüzölçümünün ~%8,5'i",
        pop: "Ülke nüfusunun %30'undan fazlası (~26 Milyon)",
        climate: "Geçiş İklimi (Akdeniz - Karadeniz)",
        econ: "Finans (Borsa İstanbul), Otomotiv, Petrokimya, Transit Lojistik"
      },
      blacksea: {
        title: "Karadeniz Bölgesi",
        desc: "Kıyıya paralel uzanan dik Kuzey Anadolu Dağları, gür orman örtüsü, dünya lideri fındık ve çay plantasyonları ile yüksek yıllık yağış miktarıyla tanımlanır.",
        area: "Ülke yüzölçümünün ~%18,1'i",
        pop: "~8,4 Milyon",
        climate: "Okyanusal / Her Mevsim Yağışlı Ilıman",
        econ: "Tarım (Fındık, Çay), Ormancılık, Hidroelektrik Enerji, Madencilik"
      },
      aegean: {
        title: "Ege Bölgesi",
        desc: "Doğu-batı uzantılı horst-graben kırık hatları ve verimli alüvyon vadileriyle öne çıkar. Zengin tarımsal artbölge ve jeotermal enerji üretim merkezidir.",
        area: "Ülke yüzölçümünün ~%11,5'i",
        pop: "~10,8 Milyon",
        climate: "Tipik Akdeniz İklimi (Sıcak kurak yazlar, ılık kışlar)",
        econ: "Tekstil, Zeytinyağı, Uluslararası Turizm, Jeotermal Enerji, İzmir Limanı"
      },
      central: {
        title: "İç Anadolu Bölgesi",
        desc: "Anadolu'nun coğrafi kalbi; ortalama 1.000 m rakımlı yarı kurak yüksek plato. Başkent Ankara devlet kurumlarına, savunma sanayii devlerine ve yüksek mahkemelere ev sahipliği yapar.",
        area: "Ülke yüzölçümünün ~%19,4'ü",
        pop: "~13,2 Milyon",
        climate: "Yarı Kurak Step / Karasal",
        econ: "Kamu Yönetimi, Savunma Sanayii, Tahıl Üretimi, Otomotiv Yan Sanayi"
      },
      med: {
        title: "Akdeniz Bölgesi",
        desc: "Kıyıya dik inen sarp Toros Dağları kuşağı ile sıcacık kıyı şeridini birleştirir. Türkiye'nin en büyük seracılık ve turunçgil merkezi ile küresel turizm başkentidir.",
        area: "Ülke yüzölçümünün ~%15,6'sı",
        pop: "~10,9 Milyon",
        climate: "Subtropikal Akdeniz İklimi",
        econ: "Turizm ($50B+ gelir), Turunçgiller, Örtüaltı Sebzecilik, Ağır Sanayi (İskenderun Demir-Çelik)"
      },
      east: {
        title: "Doğu Anadolu Bölgesi",
        desc: "Türkiye'nin en yüksek ve en geniş coğrafi bölgesi; Ağrı Dağı (5.137 m) ve Van Gölü (3.755 km²) gibi heybetli topoğrafya. Sert karasal kışlar ve Fırat-Dicle su kaynakları.",
        area: "Ülke yüzölçümünün ~%21,0'i (En Büyük Bölge)",
        pop: "~6,5 Milyon",
        climate: "Sert Karasal / Yüksek Dağ",
        econ: "Büyükbaş Hayvancılık, Hidroelektrik Barajlar, Sınır Ticareti (İran / Kafkasya)"
      },
      southeast: {
        title: "Güneydoğu Anadolu Bölgesi",
        desc: "Mezopotamya havzasına alçalan, Suriye ve Irak ile sınırlanan düzlük plato. Cumhuriyet tarihinin en büyük kalkınma projesi olan GAP sulama şebekesiyle dönüşmüştür.",
        area: "Ülke yüzölçümünün ~%9,6'sı",
        pop: "~9,3 Milyon",
        climate: "Sıcak Kurak Step / Karasal",
        econ: "Sulu Tarım (Pamuk, Antepfıstığı), Hidroelektrik (Atatürk Barajı), Hafif Sanayi (Gaziantep)"
      }
    },
    ru: {
      marmara: {
        title: "Регион Мармара (Мраморноморский)",
        desc: "Экономический, финансовый и промышленный центр Турции. Охватывает Восточную Фракию и Северо-Западную Анатолию, соединяя Черное и Эгейское моря через Босфор и Дарданеллы.",
        area: "~8,5% территории страны",
        pop: "Более 30% населения (~26 млн человек)",
        climate: "Переходный (Средиземноморский / Черноморский)",
        econ: "Финансы (Borsa Istanbul), автопром, нефтехимия, логистика"
      },
      blacksea: {
        title: "Черноморский регион (Karadeniz)",
        desc: "Характеризуется крутыми Понтийскими горами, густыми умеренными лесами, чайными и фундуковыми плантациями (мировой лидер) и высоким годовым уровнем осадков.",
        area: "~18,1% территории страны",
        pop: "~8,4 млн человек",
        climate: "Океанический / влажный умеренный",
        econ: "Сельское хозяйство (фундук, чай), лесоводство, ГЭС, горнодобыча"
      },
      aegean: {
        title: "Эгейский регион (Ege)",
        desc: "Преобладают горст-грабеновые разломные линии и плодородные аллювиальные речные долины. Богатый аграрный хинтерланд и крупнейший геотермальный хаб страны.",
        area: "~11,5% территории страны",
        pop: "~10,8 млн человек",
        climate: "Средиземноморский (жаркое сухое лето, мягкая зима)",
        econ: "Текстиль, оливковое масло, международный туризм, геотермальная энергия, порт Измир"
      },
      central: {
        title: "Центральная Анатолия (İç Anadolu)",
        desc: "Географическое сердце Анатолии; полузасушливое плато со средней высотой ~1000 м. Столица Анкара концентрирует органы власти, оборонные концерны и высшие суды.",
        area: "~19,4% территории страны",
        pop: "~13,2 млн человек",
        climate: "Семиаридный степной / континентальный",
        econ: "Госуправление, оборонная промышленность, зерновые культуры, автокомпоненты"
      },
      med: {
        title: "Средиземноморский регион (Akdeniz)",
        desc: "Окаймлен хребтами Таврских гор (Торослар), круто спускающимися к теплому морскому шельфу. Ведущий тепличный центр и глобальный международный туристический кластер.",
        area: "~15,6% территории страны",
        pop: "~10,9 млн человек",
        climate: "Субтропический средиземноморский",
        econ: "Туризм ($50+ млрд доходов), цитрусовые, тепличное овощеводство, металлургия (Искендерун)"
      },
      east: {
        title: "Восточная Анатолия (Doğu Anadolu)",
        desc: "Самый высокогорный и крупный по площади регион Турции; альпийский рельеф с массивом Арарат (5137 м) и озером Ван (3755 км²). Суровые зимы и истоки Тигра и Евфрата.",
        area: "~21,0% территории страны (Крупнейший)",
        pop: "~6,5 млн человек",
        climate: "Резко континентальный / высокогорный",
        econ: "Мясное и молочное животноводство, каскады ГЭС, приграничный транзит (Иран/Кавказ)"
      },
      southeast: {
        title: "Юго-Восточная Анатолия (Güneydoğu Anadolu)",
        desc: "Плато, спускающееся к равнинам Верхней Месопотамии у границ Сирии и Ирака. Преобразовано масштабной государственной ирригационной системой проекта GAP.",
        area: "~9,6% территории страны",
        pop: "~9,3 млн человек",
        climate: "Жаркий сухой степной / континентальный",
        econ: "Орошаемое земледелие (хлопок, фисташки), гидроэнергетика (плотина Ататюрка), промышленность Газиантепа"
      }
    }
  },

  // Render timeline component
  renderTimeline(timelineData) {
    const lang = this.getLang();
    const t = this.i18n[lang] || this.i18n.en;
    let html = `
      <div class="infographic-card timeline-card">
        <div class="infographic-header">
          <div class="infographic-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <div>
            <h4 class="infographic-title">${timelineData.title}</h4>
            <p class="infographic-sub">${t.timelineSub}</p>
          </div>
        </div>
        <div class="timeline-container">
          <div class="timeline-line"></div>
    `;

    timelineData.items.forEach((item, index) => {
      html += `
        <div class="timeline-node ${index % 2 === 0 ? 'node-left' : 'node-right'}">
          <div class="timeline-badge">${item.year}</div>
          <div class="timeline-content">
            <div class="timeline-year-label">${item.year}</div>
            <p class="timeline-desc">${item.event}</p>
          </div>
        </div>
      `;
    });

    html += `
        </div>
      </div>
    `;
    return html;
  },

  // Render responsive stat grid
  renderStatGrid(statData) {
    const lang = this.getLang();
    const t = this.i18n[lang] || this.i18n.en;
    let html = `
      <div class="infographic-card stats-card">
        <div class="infographic-header">
          <div class="infographic-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
          </div>
          <div>
            <h4 class="infographic-title">${statData.title}</h4>
            <p class="infographic-sub">${t.statSub}</p>
          </div>
        </div>
        <div class="stats-grid">
    `;

    statData.data.forEach(item => {
      html += `
        <div class="stat-box">
          <span class="stat-number">${item.value}</span>
          <span class="stat-title">${item.label}</span>
          <span class="stat-desc">${item.sub || ''}</span>
        </div>
      `;
    });

    html += `
        </div>
      </div>
    `;
    return html;
  },

  // Render comparison matrix table
  renderTable(tableData) {
    const lang = this.getLang();
    const t = this.i18n[lang] || this.i18n.en;
    let html = `
      <div class="infographic-card table-card">
        <div class="infographic-header">
          <div class="infographic-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line></svg>
          </div>
          <div>
            <h4 class="infographic-title">${tableData.title}</h4>
            <p class="infographic-sub">${t.tableSub}</p>
          </div>
        </div>
        <div class="table-responsive">
          <table class="academic-table">
            <thead>
              <tr>
    `;

    tableData.headers.forEach(h => {
      html += `<th>${h}</th>`;
    });

    html += `
              </tr>
            </thead>
            <tbody>
    `;

    tableData.rows.forEach(row => {
      html += `<tr>`;
      row.forEach((cell, idx) => {
        if (idx === 0) {
          html += `<td><strong>${cell}</strong></td>`;
        } else {
          html += `<td>${cell}</td>`;
        }
      });
      html += `</tr>`;
    });

    html += `
            </tbody>
          </table>
        </div>
      </div>
    `;
    return html;
  },

  // Render hierarchical organogram scheme
  renderOrganogram(organoData) {
    const lang = this.getLang();
    const t = this.i18n[lang] || this.i18n.en;
    let html = `
      <div class="infographic-card organogram-card">
        <div class="infographic-header">
          <div class="infographic-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
          </div>
          <div>
            <h4 class="infographic-title">${organoData.title}</h4>
            <p class="infographic-sub">${t.organogramSub}</p>
          </div>
        </div>
        <div class="organogram-flow">
    `;

    organoData.nodes.forEach(node => {
      html += `
        <div class="organogram-node node-type-${node.type}">
          <div class="node-title">${node.title}</div>
          <div class="node-sub">${node.sub}</div>
        </div>
      `;
    });

    html += `
        </div>
      </div>
    `;
    return html;
  },

  // Render Interactive Seven Geographic Regions Vector Map
  renderRegionalMap() {
    const lang = this.getLang();
    const t = this.i18n[lang] || this.i18n.en;
    const defaultData = (this.regionsData[lang] && this.regionsData[lang].marmara) || this.regionsData.en.marmara;

    return `
      <div class="infographic-card map-card">
        <div class="infographic-header">
          <div class="infographic-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>
          </div>
          <div>
            <h4 class="infographic-title">${t.mapTitle}</h4>
            <p class="infographic-sub">${t.mapSub}</p>
          </div>
        </div>

        <div class="map-layout">
          <div class="map-svg-container">
            <svg viewBox="0 0 950 480" class="turkey-svg-map" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
                  <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.15"/>
                </filter>
              </defs>

              <!-- Surrounding Seas -->
              <rect x="0" y="0" width="950" height="480" fill="var(--bg-canvas)" rx="8"/>
              
              <!-- Black Sea -->
              <text x="460" y="45" class="map-water-label" text-anchor="middle">${t.seas.blackSea}</text>

              <!-- Sea of Marmara -->
              <text x="135" y="88" class="map-water-label small" text-anchor="middle">${t.seas.marmaraSea}</text>

              <!-- Aegean Sea -->
              <text x="45" y="240" class="map-water-label vert" text-anchor="middle">${t.seas.aegeanSea}</text>

              <!-- Mediterranean Sea -->
              <text x="360" y="455" class="map-water-label" text-anchor="middle">${t.seas.medSea}</text>

              <!-- 7 Geographic Regions Paths -->
              <g class="regions-group" filter="url(#shadow)">
                <!-- 1. Marmara Region -->
                <path id="reg-marmara" class="region-path active" data-region="marmara"
                  d="M 60 70 L 140 50 L 220 70 L 230 110 L 170 150 L 110 130 L 60 110 Z" />

                <!-- 2. Aegean Region -->
                <path id="reg-aegean" class="region-path" data-region="aegean"
                  d="M 60 140 L 150 150 L 160 270 L 110 320 L 70 260 Z" />

                <!-- 3. Mediterranean Region -->
                <path id="reg-med" class="region-path" data-region="med"
                  d="M 120 320 L 250 310 L 460 360 L 580 340 L 590 380 L 320 400 L 120 330 Z" />

                <!-- 4. Central Anatolian Region -->
                <path id="reg-central" class="region-path" data-region="central"
                  d="M 230 130 L 480 130 L 560 210 L 460 310 L 240 290 L 180 160 Z" />

                <!-- 5. Black Sea Region -->
                <path id="reg-blacksea" class="region-path" data-region="blacksea"
                  d="M 230 70 L 720 70 L 760 120 L 480 120 L 230 110 Z" />

                <!-- 6. Eastern Anatolian Region -->
                <path id="reg-east" class="region-path" data-region="east"
                  d="M 570 120 L 880 110 L 920 220 L 760 290 L 570 210 Z" />

                <!-- 7. Southeastern Anatolian Region -->
                <path id="reg-southeast" class="region-path" data-region="southeast"
                  d="M 580 290 L 760 290 L 780 370 L 580 370 Z" />
              </g>

              <!-- Lake Van -->
              <ellipse cx="830" cy="225" rx="24" ry="16" fill="var(--bg-canvas)" stroke="var(--border-subtle)" stroke-width="1.5"/>
              <text x="830" y="228" class="lake-label" text-anchor="middle">${t.seas.lakeVan}</text>

              <!-- Region Names Overlaid -->
              <text x="135" y="105" class="map-label pointer-none">${t.regionNames.marmara}</text>
              <text x="110" y="225" class="map-label pointer-none">${t.regionNames.aegean}</text>
              <text x="340" y="360" class="map-label pointer-none">${t.regionNames.med}</text>
              <text x="350" y="220" class="map-label pointer-none">${t.regionNames.central}</text>
              <text x="490" y="95" class="map-label pointer-none">${t.regionNames.blacksea}</text>
              <text x="730" y="195" class="map-label pointer-none">${t.regionNames.east}</text>
              <text x="670" y="335" class="map-label pointer-none">${t.regionNames.southeast}</text>
            </svg>
          </div>

          <!-- Dynamic Region Detail Card -->
          <div class="map-details-panel" id="map-region-details">
            <div class="detail-header">
              <div class="reg-badge">${t.regionBadge}</div>
              <h5 id="reg-detail-title">${defaultData.title}</h5>
            </div>
            <p id="reg-detail-desc" class="reg-detail-desc">${defaultData.desc}</p>
            <div class="reg-stats-grid">
              <div class="stat-item"><span class="stat-label">${t.areaLabel}:</span> <span class="stat-val" id="reg-detail-area">${defaultData.area}</span></div>
              <div class="stat-item"><span class="stat-label">${t.popLabel}:</span> <span class="stat-val" id="reg-detail-pop">${defaultData.pop}</span></div>
              <div class="stat-item"><span class="stat-label">${t.climateLabel}:</span> <span class="stat-val" id="reg-detail-climate">${defaultData.climate}</span></div>
              <div class="stat-item"><span class="stat-label">${t.econLabel}:</span> <span class="stat-val" id="reg-detail-econ">${defaultData.econ}</span></div>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Render Seismotectonics & Fault Lines Vector Map
  renderFaultLinesMap() {
    const lang = this.getLang();
    const t = this.i18n[lang] || this.i18n.en;

    return `
      <div class="infographic-card seismic-card">
        <div class="infographic-header">
          <div class="infographic-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          </div>
          <div>
            <h4 class="infographic-title">${t.seismicTitle}</h4>
            <p class="infographic-sub">${t.seismicSub}</p>
          </div>
        </div>

        <div class="seismic-svg-container">
          <svg viewBox="0 0 920 400" class="seismic-svg" xmlns="http://www.w3.org/2000/svg">
            <rect width="920" height="400" fill="var(--bg-canvas)" rx="6"/>
            
            <!-- Continental Plates Indicators -->
            <g class="plate-indicators">
              <!-- Eurasian Plate -->
              <text x="460" y="35" class="plate-name" text-anchor="middle">${t.plates.eurasian}</text>
              <line x1="460" y1="45" x2="460" y2="60" stroke="#0ea5e9" stroke-width="3"/>

              <!-- Arabian Plate Moving North -->
              <text x="680" y="380" class="plate-name" text-anchor="middle">${t.plates.arabian}</text>
              <line x1="680" y1="365" x2="680" y2="340" stroke="#f59e0b" stroke-width="3"/>

              <!-- Anatolian Microplate Escape Arrow -->
              <text x="360" y="210" class="plate-name accent" text-anchor="middle">${t.plates.anatolian}</text>
              <line x1="420" y1="225" x2="260" y2="225" stroke="var(--turkish-red)" stroke-width="3.5"/>
            </g>

            <!-- Outline contour of Anatolia -->
            <path d="M 120 90 L 260 110 L 580 90 L 780 120 L 890 180 L 840 320 L 560 340 L 400 370 L 200 340 L 120 220 Z" 
              fill="none" stroke="var(--border-subtle)" stroke-width="2" stroke-dasharray="4 4"/>

            <!-- North Anatolian Fault Zone (NAFZ) -->
            <path d="M 750 170 Q 560 130 380 135 T 200 130 T 120 120" 
              fill="none" stroke="#ef4444" stroke-width="4.5" stroke-linecap="round"/>
            <text x="480" y="120" class="fault-label naff-label">${t.faultLabels.nafz}</text>

            <!-- East Anatolian Fault Zone (EAFZ) -->
            <path d="M 750 170 Q 640 240 560 320 L 530 360" 
              fill="none" stroke="#dc2626" stroke-width="4" stroke-linecap="round"/>
            <text x="660" y="250" class="fault-label eaff-label">${t.faultLabels.eafz}</text>

            <!-- Karlıova Triple Junction -->
            <circle cx="750" cy="170" r="7" fill="#b91c1c"/>
            <text x="765" y="165" class="junction-label">${t.faultLabels.karliova}</text>

            <!-- Aegean Graben System -->
            <g class="graben-lines">
              <line x1="130" y1="200" x2="210" y2="210" stroke="#ea580c" stroke-width="2.5"/>
              <line x1="125" y1="230" x2="220" y2="240" stroke="#ea580c" stroke-width="2.5"/>
              <line x1="130" y1="260" x2="215" y2="270" stroke="#ea580c" stroke-width="2.5"/>
              <text x="140" y="295" class="fault-label graben-label">${t.faultLabels.grabens}</text>
            </g>

            <!-- Major Historical Rupture Epicenters -->
            <g class="epicenter-group">
              <!-- 1939 Erzincan Mw 7.8 -->
              <circle cx="650" cy="155" r="5" fill="#f43f5e" class="pulse-circle"/>
              <text x="650" y="145" class="quake-text">${t.faultLabels.erzincan}</text>

              <!-- 1999 Gölcük/İzmit Mw 7.6 -->
              <circle cx="210" cy="125" r="5" fill="#f43f5e" class="pulse-circle"/>
              <text x="210" y="112" class="quake-text">${t.faultLabels.golcuk}</text>

              <!-- 2023 Kahramanmaraş Doublet Mw 7.8 & 7.6 -->
              <circle cx="560" cy="320" r="6" fill="#7f1d1d" class="pulse-circle"/>
              <text x="575" y="315" class="quake-text major">${t.faultLabels.maras}</text>
            </g>
          </svg>
        </div>

        <div class="seismic-legend">
          <div class="legend-item"><span class="legend-color naf-color"></span> ${t.seismicLegend.nafz}</div>
          <div class="legend-item"><span class="legend-color eaf-color"></span> ${t.seismicLegend.eafz}</div>
          <div class="legend-item"><span class="legend-color graben-color"></span> ${t.seismicLegend.grabens}</div>
          <div class="legend-item"><span class="legend-color quake-color"></span> ${t.seismicLegend.epicenters}</div>
        </div>
      </div>
    `;
  },

  // Render Energy Generation Mix Interactive Chart
  renderEnergyChart() {
    const lang = this.getLang();
    const t = this.i18n[lang] || this.i18n.en;

    return `
      <div class="infographic-card energy-chart-card">
        <div class="infographic-header">
          <div class="infographic-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>
          </div>
          <div>
            <h4 class="infographic-title">${t.energyTitle}</h4>
            <p class="infographic-sub">${t.energySub}</p>
          </div>
        </div>

        <div class="chart-content-flex">
          <div class="energy-bar-list">
            <div class="energy-bar-item">
              <div class="energy-bar-header">
                <span class="energy-source-name">${t.energySources.hydro}</span>
                <span class="energy-source-val">32,200 MW (30.1%)</span>
              </div>
              <div class="energy-track"><div class="energy-fill hydro" style="width: 30.1%;"></div></div>
            </div>

            <div class="energy-bar-item">
              <div class="energy-bar-header">
                <span class="energy-source-name">${t.energySources.gas}</span>
                <span class="energy-source-val">25,800 MW (24.1%)</span>
              </div>
              <div class="energy-track"><div class="energy-fill gas" style="width: 24.1%;"></div></div>
            </div>

            <div class="energy-bar-item">
              <div class="energy-bar-header">
                <span class="energy-source-name">${t.energySources.coal}</span>
                <span class="energy-source-val">21,800 MW (20.3%)</span>
              </div>
              <div class="energy-track"><div class="energy-fill coal" style="width: 20.3%;"></div></div>
            </div>

            <div class="energy-bar-item">
              <div class="energy-bar-header">
                <span class="energy-source-name">${t.energySources.solar}</span>
                <span class="energy-source-val">14,500 MW (13.5%)</span>
              </div>
              <div class="energy-track"><div class="energy-fill solar" style="width: 13.5%;"></div></div>
            </div>

            <div class="energy-bar-item">
              <div class="energy-bar-header">
                <span class="energy-source-name">${t.energySources.wind}</span>
                <span class="energy-source-val">12,100 MW (11.3%)</span>
              </div>
              <div class="energy-track"><div class="energy-fill wind" style="width: 11.3%;"></div></div>
            </div>

            <div class="energy-bar-item">
              <div class="energy-bar-header">
                <span class="energy-source-name">${t.energySources.geo}</span>
                <span class="energy-source-val">3,200 MW (3.0%)</span>
              </div>
              <div class="energy-track"><div class="energy-fill geo" style="width: 3.0%;"></div></div>
            </div>
          </div>

          <div class="energy-callout-box">
            <h6>${t.pipelinesTitle}</h6>
            <ul class="pipeline-list">
              ${t.pipelineList.map(item => `<li><strong>${item.label}:</strong> ${item.desc}</li>`).join('')}
            </ul>
            <div class="citation-callout">
              <span class="cite-tag" data-cite-id="EPDK-2024-NRG">${t.citeText}</span>
            </div>
          </div>
        </div>
      </div>
    `;
  },

  // Setup interactive map click handlers
  initMapEvents() {
    const lang = this.getLang();
    const currentRegionDict = this.regionsData[lang] || this.regionsData.en;

    document.querySelectorAll('.region-path').forEach(path => {
      path.addEventListener('click', (e) => {
        const regKey = e.currentTarget.getAttribute('data-region');
        const data = currentRegionDict[regKey];
        if (!data) return;

        document.querySelectorAll('.region-path').forEach(p => p.classList.remove('active'));
        e.currentTarget.classList.add('active');

        const titleEl = document.getElementById('reg-detail-title');
        const descEl = document.getElementById('reg-detail-desc');
        const areaEl = document.getElementById('reg-detail-area');
        const popEl = document.getElementById('reg-detail-pop');
        const climateEl = document.getElementById('reg-detail-climate');
        const econEl = document.getElementById('reg-detail-econ');

        if (titleEl) titleEl.textContent = data.title;
        if (descEl) descEl.textContent = data.desc;
        if (areaEl) areaEl.textContent = data.area;
        if (popEl) popEl.textContent = data.pop;
        if (climateEl) climateEl.textContent = data.climate;
        if (econEl) econEl.textContent = data.econ;
      });
    });
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = Visualizations;
} else if (typeof window !== 'undefined') {
  window.Visualizations = Visualizations;
}
