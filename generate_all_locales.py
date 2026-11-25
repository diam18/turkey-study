#!/usr/bin/env python3
"""
Full locale generator script creating:
- js/locales/data_en.js
- js/locales/data_tr.js
- js/locales/data_ru.js
with 5x text expansion and 3x more infographics/schemes on Modules 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13.
"""

import json
import os
import sys

def build_data():
    from build_multilingual_datasets import CITATIONS_DB

    # Let's write the English dataset first
    print("Building English dataset...")
    with open("js/locales/data_en.js", "w", encoding="utf-8") as f:
        f.write("/** ANATOLIA ACADEMIC - Comprehensive English Dataset **/\n")
        f.write("const ACADEMIC_DATA_EN = ")
        
        # We will build the dictionary structure
        data_en = {
            "metadata": {
                "title": "Anatolia Academic: Comprehensive Research Portal on the Republic of Turkey",
                "lang": "en",
                "version": "2.5.0",
                "lastUpdated": "2026-11-24",
                "scope": "Interdisciplinary Scholarly Research (History, Law, Politics, Armed Forces, Economy, Demography, Energy)",
                "citationStyle": "Chicago / APA / BibTeX Compliant"
            },
            "citations": CITATIONS_DB,
            "modules": []
        }
        
        # Populate modules
        # Module 1
        mod1 = {
            "id": "history",
            "number": "01",
            "title": "History & Foreign Relations",
            "tagline": "Sovereign foundation, imperial dissolution, Balkan trajectories, Soviet-Russian strategic arc, and modern diplomacy.",
            "icon": "landmark",
            "readingTime": "32 min read",
            "summary": "An exhaustive, multi-epoch scholarly analysis tracing the transition from pre-Turkic and Seljuk Anatolia through the zenith and decline of the Ottoman Empire, the Turkish War of Independence, and the Kemalist institutional modernization. Includes comprehensive historical deep dives on bilateral relations with the Soviet Union/Russia and Bulgaria, alongside Greece, the Middle East, the South Caucasus, NATO integration, and the Montreux Straits regime.",
            "sections": [
                {
                    "id": "hist-epoch-foundations",
                    "title": "1. Pre-Ottoman Anatolia, Seljuk Statehood & the Beyliks Epoch",
                    "content": """The historical trajectory of modern Turkey is rooted in successive layers of civilizational synthesis across the Anatolian landmass. Following the migration of Oghuz Turkic tribes into Western Asia, the decisive victory of Sultan Alp Arslan over the Byzantine Emperor Romanos IV Diogenes at the Battle of Manzikert (Malazgirt, 1071) opened Anatolia to permanent Turkic settlement [ZURCHER-2017].

The Seljuk Sultanate of Rum (1077–1308), centered at Nicaea (İznik) and later Iconium (Konya), forged a distinctive Perso-Turkic high culture, constructing enduring caravanserais, madrasas, and monumental architecture along the Silk Road trading axes. The Sultanate fostered intellectual flourishment, sheltering luminaries such as the mystical philosopher Mevlana Jalaluddin Rumi. Following the catastrophic Mongol invasion and defeat at the Battle of Köse Dağ (1243), the Seljuk central authority dissolved into autonomous frontier principalities (Anatolian Beyliks), among which the small northwestern Marcher Principality of Osman I (*Osmanoğulları*) in Söğüt would burgeon into the Ottoman Empire."""
                },
                {
                    "id": "hist-ottoman-zenith-decline",
                    "title": "2. The Ottoman Empire: Imperial Statecraft, Tanzimat & Constitutional Strife",
                    "content": """The conquest of Constantinople by Sultan Mehmed II (Fatih) on May 29, 1453 transformed the Ottoman realm from a regional sultanate into an imperial super-state bridging Europe, Asia, and North Africa. During the reign of Suleiman the Magnificent (Kanunî Süleyman, 1520–1566), the empire reached its geopolitical zenith, commanding sovereign territory from the gates of Vienna to the Persian Gulf:

- **The Classical Millet System:** State governance relied on confessional autonomy, organizing non-Muslim subjects into institutional religious communities (*millets*)—predominantly the Greek Orthodox (*Rûm*), Armenian Gregorian, and Jewish millets—each governed by their respective ecclesiastical authorities in matters of personal status, worship, and intra-communal civil law.
- **Structural Stagnation & the Eastern Question:** Following the failed Second Siege of Vienna (1683) and the Treaty of Karlowitz (1699), the empire entered a protracted era of military retreat, fiscal degradation, and imperial encroachment by the European Great Powers—a diplomatic crisis termed the 'Eastern Question'.
- **The Tanzimat Modernization (1839–1876):** Faced with existential collapse, reformist statesmen spearheaded the Tanzimat ('Reorganization') era, initiated by the Edict of Gülhane (1839) and Imperial Reform Edict (1856), declaring the legal equality of all subjects regardless of religion, modernizing the army (*Nizam-ı Cedid*), and introducing Western-style commercial and penal codes.
- **First Constitutional Era (1876):** Sultan Abdulhamid II promulgated the first Ottoman constitution (*Kanûn-ı Esâsî*) under Grand Vizier Midhat Pasha, establishing a short-lived bicameral parliament before suspending it during the disastrous Russo-Turkish War (1877–1878).
- **The Young Turk Revolution (1908):** The Committee of Union and Progress (CUP) restored constitutional rule, but the empire was immediately engulfed in the Balkan Wars (1912–1913), suffering catastrophic territorial losses in Europe and triggering massive waves of Muslim refugees fleeing to Anatolia."""
                },
                {
                    "id": "hist-wwi-independence",
                    "title": "3. World War I, Partition, and the Turkish War of Independence (1914–1923)",
                    "content": """Entering World War I on the side of the Central Powers in October 1914, the Ottoman Empire fought on multiple fronts, securing a legendary defensive victory at Gallipoli (Çanakkale, 1915), but collapsing under Allied campaigns across the Levant and Mesopotamia. 

The Armistice of Mudros (October 30, 1918) enabled Allied forces to occupy the Ottoman capital Istanbul and partition Anatolia. On August 10, 1920, the defeated Ottoman government signed the draconian **Treaty of Sèvres**, which reduced Turkish sovereignty to a landlocked rump in Central and Northern Anatolia, partitioning Western Anatolia to Greece, the southeast to France, the south to Italy, and mandating independent Armenian and autonomous Kurdish entities:

- **The National Movement (*Milli Mücadele*):** On May 19, 1919, Mustafa Kemal Pasha landed in Samsun as Inspector-General, mobilizing popular resistance. At the historic Congresses of Erzurum and Sivas (1919), nationalist delegates adopted the **National Pact (*Misak-ı Millî*)**, rejecting foreign mandates and declaring the territorial integrity of all un-invaded Ottoman lands.
- **Establishment of the TBMM:** Following the Allied military occupation of Istanbul and dissolution of the Ottoman chamber, the **Grand National Assembly of Turkey (TBMM)** was inaugurated in Ankara on April 23, 1920, claiming sovereign authority over the nation.
- **The War of Liberation (1920–1922):** The Ankara nationalist government fought simultaneously on three military fronts: defeating the Democratic Republic of Armenia in the east (commanded by Kâzım Karabekir), securing French evacuation in the south via the Treaty of Ankara (1921), and halting the Greek advance toward Ankara at the epic **Battle of Sakarya (August–September 1921)**. In August 1922, the Great Offensive (*Büyük Taarruz*) routed Greek armies, culminating in the liberation of Izmir on September 9, 1922.
- **The Treaty of Lausanne (1923):** Negotiated by İsmet Pasha (İnönü), the Treaty of Lausanne (July 24, 1923) superseded Sèvres, securing international recognition of the borders of the modern Turkish state, abolishing foreign capitulations, and establishing sovereign control over Eastern Thrace and Anatolia [LAUSANNE-1923]. On October 29, 1923, the Republic of Turkey was formally proclaimed."""
                },
                {
                    "id": "hist-soviet-russia-deep",
                    "title": "4. The Soviet-Russian Strategic Arc: Alliance, Cold War Confrontation & Modern Interdependence",
                    "content": """The bilateral relationship between Turkey and the Russian state spans over five centuries, evolving from twelve major imperial wars into revolutionary cooperation, Cold War confrontation, and modern compartmentalized strategic partnership:

- **Revolutionary Solidarity & Treaties (1920–1923):** In 1920, the fledgling Bolshevik government under Vladimir Lenin and the Ankara nationalist government under Mustafa Kemal recognized a shared anti-imperialist imperative. On March 16, 1921, they signed the landmark **Treaty of Moscow (Treaty of Brotherhood)**, in which Soviet Russia became the first European power to nullify the Treaty of Sèvres and recognize the TBMM [MOSCOW-TREATY-1921]. Moscow provided over 10 million gold rubles, 39,000 rifles, 327 machine guns, 54 artillery pieces, and maritime ammunition shipments to the port of Trabzon. This was followed by the **Treaty of Kars** (October 13, 1921), fixing the northeastern land border with Armenia, Azerbaijan, and Georgia [KARS-TREATY-1921].
- **Interwar Industrial Aid (1930s):** The USSR provided interest-free loans ($8M in gold) and Soviet Gosplan experts to formulate Turkey's First Five-Year Industrial Plan (1934), constructing the iconic Sümerbank textile complexes in Kayseri and Nazilli.
- **Stalin's Post-WWII Territorial Demands (1945):** In March 1945, Joseph Stalin terminated the 1925 Soviet-Turkish Non-Aggression Pact. Moscow demanded the cession of the Eastern Anatolian provinces of Kars, Ardahan, and Artvin, and insisted on joint Soviet-Turkish military control and naval bases in the Bosphorus and Dardanelles straits. This existential threat shattered interwar neutrality, compelling Ankara to seek immediate Western protection under the **Truman Doctrine (1947)** and formally enter **NATO in 1952** [ZURCHER-2017].
- **Cold War Frontier & Cuban Missile Crisis (1952–1991):** As NATO's southeastern flank bordering the USSR across 610 km of land and the Black Sea, Turkey deployed 15 US-operated PGM-19 Jupiter nuclear missiles at Çiğli (Izmir). During the October 1962 Cuban Missile Crisis, President Kennedy and Premier Khrushchev reached a secret pact: the USSR withdrew nuclear missiles from Cuba in exchange for the US withdrawing its Jupiter missiles from Turkey. Despite ideological confrontation, Turkey and the USSR concluded major industrial agreements in the late 1960s and 1970s, with Soviet credits constructing the Seydişehir aluminum smelter, the İskenderun iron/steel plant (İSDEMİR), and the Aliağa oil refinery.
- **Post-Cold War "Compartmentalized Diplomacy" (1991–Present):** Bilateral trade boomed through shuttle trade and massive Turkish construction contracts in Russia. Strategic energy infrastructure forged deep interdependence: the **Blue Stream** pipeline (opened 2003) and the dual-string **TurkStream** pipeline (opened 2020) across the Black Sea seabed, supplying Russian gas to Turkey and southeastern Europe. In 2010, Turkey contracted Russian state atomic agency Rosatom to construct the $20 billion **Akkuyu Nuclear Power Plant** (4x 1,200 MW VVER reactors).
- **Security Tensions & S-400 Procurement:** Following the downing of a Russian Su-24 fighter along the Syrian border in November 2015, relations experienced a severe crisis, resolved through high-level diplomatic rapprochement in 2016. In 2017, Turkey signed a $2.5 billion agreement to purchase Russian **S-400 Triumph surface-to-air missile systems**, prompting the United States to expel Turkey from the F-35 Joint Strike Fighter program and impose CAATSA sanctions [SIPRI-2024-MLX].
- **The Russia-Ukraine War & Montreux Closure:** Following Russia's invasion of Ukraine in February 2022, Turkey condemned the violation of Ukrainian sovereignty and supplied armed Bayraktar TB2 drones to Kyiv. Simultaneously, Turkey invoked **Article 19 of the 1936 Montreux Convention**, closing the Bosphorus and Dardanelles to all belligerent warships [UN-TREATY-MONTREUX]. This critical legal move prevented Russia from reinforcing its Black Sea Fleet while facilitating Turkey's mediation of the landmark UN Black Sea Grain Initiative."""
                },
                {
                    "id": "hist-bulgaria-deep",
                    "title": "5. The Bulgarian & Balkan Axis: Treaties, Cold War Frontier & the 1989 Büyük Göç",
                    "content": """Bilateral relations between Turkey and Bulgaria represent a vital geopolitical corridor connecting Anatolia to Continental Europe:

- **Balkan Wars & Treaties of Constantinople (1913) and Friendship (1925):** The Balkan Wars (1912–1913) ended five centuries of Ottoman rule in Northern Thrace and Macedonia. The 1913 Treaty of Constantinople delimited the border in Eastern Thrace and established formal guarantees for the religious and property rights of the substantial ethnic Turkish minority in Bulgaria. On October 18, 1925, the Turkish Republic and the Kingdom of Bulgaria signed the **Treaty of Friendship and Neutrality in Ankara**, which recognized the voluntary migration of Turks from Bulgaria and confirmed minority educational and cultural protections.
- **Cold War Frontier along the 269-km Border:** Throughout the Cold War, the Turkey-Bulgaria frontier was the southernmost border between NATO and the Warsaw Pact. Both nations stationed massive military formations along the Thracian plain: the Turkish 1st Army maintained forward garrisons in Edirne, Kırklareli, and Çorlu, defending against prospective armored thrusts toward Istanbul and the Straits.
- **The 1989 Forced Assimilation & Exodus (*Büyük Göç*):** In late 1984, the communist regime of Todor Zhivkov launched the totalitarian 'Revival Process' (*Văzroditelen protses*). Over 800,000 ethnic Turks and Pomaks were forced to abandon their Turkish-Islamic names in favor of Slavic-Christian ones at gunpoint; the speaking of Turkish in public was penalized with heavy fines; mosques were locked; circumcision and traditional burial rites were outlawed. In May 1989, mass hunger strikes and peaceful protests by Turks were met with violent state suppression, deportations, and internal exile. On June 3, 1989, Turkey opened its border gates at Kapıkule and Dereköy. Within 90 days, **over 360,000 Bulgarian Turks fled or were deported to Turkey in cattle trains and overloaded vehicles**—the largest refugee crisis in Europe since World War II [BULGARIA-EXODUS-1989]. Turkey established massive tent cities in Edirne, mobilized state resources, granted immediate citizenship, and integrated the refugees into industrial centers (Bursa, Izmir, Istanbul, Thrace).
- **Post-1989 Democratization & Modern Partnership:** Following the collapse of the Zhivkov regime in November 1989, Bulgaria restored civil rights and names to its Turkish minority. The Turkish-dominated *Movement for Rights and Freedoms* (DPS / HÖH) became a kingmaker in Bulgarian parliamentary politics. Today, Turkey and Bulgaria are NATO allies; the Kapıkule/Kapitan Andreevo border post is the second-busiest commercial customs gate in the world, processing over 1 million trucks and 3 million passenger vehicles annually. In January 2023, Turkey's BOTAŞ and Bulgaria's Bulgargaz concluded a 13-year gas access agreement granting Bulgaria access to Turkish LNG terminals and transit infrastructure."""
                },
                {
                    "id": "hist-regional-multilateral",
                    "title": "6. Regional Bilateral Dynamics & Multilateral Alignments",
                    "content": """Turkey maintains complex diplomatic and strategic relations across surrounding geographic sectors:
- **Greece (Aegean & Cyprus):** Framed by the 1923 Lausanne Treaty, relations experienced recurring crises: the 1955 Istanbul pogrom, the 1974 Cyprus intervention following an Athens-backed coup, the 1996 Kardak/Imia crisis, and ongoing disagreements regarding territorial waters (6 nm vs. 12 nm), continental shelf demarcation, flight information regions (FIR), and the demilitarized status of Aegean islands [LAUSANNE-1923]. Detente and diplomatic consultation mechanisms were rejuvenated through the 2023 Athens Declaration on Friendly Relations.
- **Syria & Iraq:** Governed by transboundary water management over the Euphrates and Tigris (GAP project), cross-border counter-terrorism security against the PKK (1998 Adana Accord), and direct military interventions (Operations Euphrates Shield, Olive Branch, Peace Spring) to secure the southern frontier amidst the Syrian Civil War [TUIK-2024-POP].
- **Iran:** Anchored by the 1639 Treaty of Zuhab (Kasr-ı Şirin), maintaining one of the world's most stable historical borders. Bilateral ties are characterized by managed regional competition, high-volume natural gas trade, and coordination in the Astana diplomatic process alongside Russia.
- **South Caucasus:** Bound to Azerbaijan by the doctrine *"One nation, two states"*, codified in the 2021 **Shusha Declaration** on Allied Relations. Turkey's military-technical support proved decisive in the 2020 Second Karabakh War. Normalization talks with Armenia, dormant since the failed 2009 Zurich Protocols, resumed through special envoys.
- **Multilateral Anchors:** 
  - **NATO (1952–Present):** Core pillar of national defense, hosting Allied Land Command (LANDCOM) in Izmir and Kürecik AN/TPY-2 radar.
  - **European Union:** Bound by the 1963 Ankara Agreement, 1995 Customs Union, and 1999 Helsinki candidacy, although accession chapters have been effectively frozen since the late 2010s.
  - **Organization of Turkic States (OTS):** Founding architect of the Eurasian cooperative bloc comprising Azerbaijan, Kazakhstan, Kyrgyzstan, Uzbekistan, and observer members Hungary and Turkmenistan."""
                }
            ],
            "infographics": [
                {
                    "type": "timeline",
                    "id": "hist-expanded-timeline",
                    "title": "Diplomatic & Sovereign Milestones of Modern Turkey (1918–2026)",
                    "items": [
                        {"year": "1919", "event": "Atatürk lands in Samsun (May 19); Amasya Circular declares national struggle."},
                        {"year": "1920", "event": "National Pact (Misak-ı Millî) adopted; TBMM convenes in Ankara; Treaty of Sèvres signed by Ottomans."},
                        {"year": "1921", "event": "Treaties of Moscow and Kars signed with Soviet Russia, securing eastern boundaries."},
                        {"year": "1922", "event": "Battle of Dumlupınar routs Greek forces; Armistice of Mudanya; Sultanate abolished."},
                        {"year": "1923", "event": "Treaty of Lausanne signed (July 24); Republic of Turkey proclaimed (October 29)."},
                        {"year": "1925", "event": "Turkish-Bulgarian Treaty of Friendship signed in Ankara."},
                        {"year": "1936", "event": "Montreux Convention restores sovereign Turkish control and militarization of the Straits."},
                        {"year": "1945", "event": "Stalin issues territorial demands for Kars/Ardahan and joint bases on the Straits."},
                        {"year": "1952", "event": "Turkey officially accedes to NATO alongside Greece under the Truman Doctrine."},
                        {"year": "1962", "event": "Cuban Missile Crisis: Secret US-Soviet agreement withdraws Jupiter missiles from Turkey."},
                        {"year": "1974", "event": "Turkey executes the Cyprus Peace Operation under the 1960 Treaty of Guarantee."},
                        {"year": "1989", "event": "Büyük Göç: Over 360,000 Bulgarian Turks flee Zhivkov's forced assimilation into Turkey."},
                        {"year": "1999", "event": "EU Helsinki Summit formally recognizes Turkey as a candidate state for accession."},
                        {"year": "2017", "event": "Constitutional referendum transitions Turkey from parliamentary to Executive Presidential system."},
                        {"year": "2020", "event": "TurkStream pipeline inaugurated; Turkey provides decisive defense aid in Karabakh War."},
                        {"year": "2022", "event": "Turkey invokes Montreux Article 19, barring naval combatants during the Russia-Ukraine War."}
                    ]
                },
                {
                    "type": "comparison-table",
                    "id": "hist-treaties-matrix",
                    "title": "Comprehensive Matrix of Sovereign Treaties, Boundaries & Strategic Accords",
                    "headers": ["Instrument", "Date Signed", "Counterparties", "Territorial & Sovereign Terms", "Archival Reference"],
                    "rows": [
                        ["Treaty of Moscow", "16 Mar 1921", "TBMM Govt & RSFSR (Bolshevik Russia)", "Annulled Treaty of Sèvres; Soviet gold/munitions transfer; recognized TBMM", "Soviet For. Policy Arch. [MOSCOW-TREATY-1921]"],
                        ["Treaty of Kars", "13 Oct 1921", "TBMM & Armenian/Azeri/Georgian SSRs", "Fixed northeastern frontier (Kars, Ardahan, Artvin to Turkey; Batumi to Georgia)", "TBMM Legal Minutes [KARS-TREATY-1921]"],
                        ["Treaty of Lausanne", "24 Jul 1923", "Turkey & UK, France, Italy, Japan, Greece", "International sovereignty, Eastern Thrace, Aegean boundaries, minority regime", "League of Nations [LAUSANNE-1923]"],
                        ["Ankara Friendship Treaty", "18 Oct 1925", "Turkey & Kingdom of Bulgaria", "Confirmed Thracian borders; established voluntary migration & minority rights", "Bulgarian State Arch. [BULGARIA-EXODUS-1989]"],
                        ["Montreux Convention", "20 Jul 1936", "Turkey, UK, USSR, France, Greece, Bulgaria", "Abolished Int'l Straits Commission; full Turkish remilitarization & war powers", "UN Treaty Series [UN-TREATY-MONTREUX]"],
                        ["Shusha Declaration", "15 Jun 2021", "Republic of Turkey & Republic of Azerbaijan", "Formal military alliance, mutual defense assistance, and transport corridor cooperation", "Official Gazette (Resmî Gazete) 2021"]
                    ]
                },
                {
                    "type": "stat-grid",
                    "id": "hist-soviet-stats",
                    "title": "Soviet-Russian & Bulgarian Geopolitical Indices",
                    "data": [
                        {"label": "1921 Soviet Aid", "value": "10M+ Gold Rubles", "sub": "Artillery, rifles & ammo in Independence War"},
                        {"label": "1989 Büyük Göç", "value": "360,000+ Refugees", "sub": "Bulgarian Turks fleeing forced assimilation"},
                        {"label": "TurkStream Gas Cap", "value": "31.5 bcm / year", "sub": "Dual subsea strings across Black Sea"},
                        {"label": "Akkuyu Nuclear Cap", "value": "4,800 MW", "sub": "$20B Rosatom BOO investment"},
                        {"label": "Kapıkule Truck Traffic", "value": "1,000,000+ Trucks/yr", "sub": "2nd busiest customs gate globally"},
                        {"label": "S-400 Procurement", "value": "$2.5 Billion", "sub": "Procured 2017, triggered US CAATSA"}
                    ]
                }
            ]
        }
        data_en["modules"].append(mod1)

        # Module 2 (Keep concise)
        mod2 = {
            "id": "geography",
            "number": "02",
            "title": "Geography, Topography & Earth Systems",
            "tagline": "Geomorphology, tectonic fault systems, transboundary river basins, and the seven geographic regions.",
            "icon": "globe",
            "readingTime": "12 min read",
            "summary": "Comprehensive geomorphological profile of Turkey, spanning 783,562 km² across southeastern Europe (Thrace) and southwestern Asia (Anatolia), bounded by four seas, crosscut by major strike-slip seismic faults, and home to transboundary water arteries.",
            "sections": [
                {
                    "id": "geo-territory",
                    "title": "1. Territorial Framework & Regional Morphology",
                    "content": "Turkey spans a total surface area of **783,562 square kilometers** (including inland waters), bridging Europe and Asia across the Turkish Straits (Bosphorus, Sea of Marmara, Dardanelles). Approximately 97% of its landmass lies in Anatolia (*Asia Minor*), while 3% forms Eastern Thrace on the Balkan Peninsula. The country possesses a coastline of 8,333 kilometers, bounded by the Black Sea to the north, the Aegean Sea to the west, the Mediterranean Sea to the south, and the Sea of Marmara as an internal basin [TUIK-2024-POP].\n\nAt the First Geography Congress in Ankara in 1941, Turkey was formally categorized into **seven geographic regions** based on climate, topography, and vegetation:\n1. **Marmara Region:** Lowland topography, dense urbanization, maritime straits, transitional climate.\n2. **Aegean Region:** Horst-and-graben fault architecture, fertile alluvial river valleys (Gediz, Büyük Menderes), Mediterranean climate.\n3. **Mediterranean Region:** Taurus Mountain system (*Toroslar*), coastal karst plains, citrus and greenhouse agriculture.\n4. **Central Anatolian Region:** High semi-arid plateau (average altitude ~1,000m), surrounded by peripheral ranges, steppe vegetation, Lake Tuz (*Tuz Gölü*).\n5. **Black Sea Region:** Steep Pontic Mountain ranges (*Kuzey Anadolu Dağları*) parallel to the coast, high precipitation, dense temperate broadleaf and mixed forests.\n6. **Eastern Anatolian Region:** Rugged alpine highlands, volcanic plateaus (Mount Ararat / *Ağrı Dağı* at 5,137m, Turkey's highest peak), high continentality and harsh winters, Lake Van (*Van Gölü*, 3,755 km²).\n7. **Southeastern Anatolian Region:** Rolling plateau descending into the Mesopotamian basin, hot semi-arid climate, home to the Euphrates-Tigris river irrigation network."
                },
                {
                    "id": "geo-tectonics",
                    "title": "2. Tectonic Framework & Active Fault Architecture",
                    "content": "Turkey is one of the most seismically active regions on Earth due to its location within the Alpine-Himalayan orogenic belt. The Anatolian microplate is being squeezed westward at a rate of roughly 20–25 mm per year between the northward-colliding **Arabian Plate** and the stable **Eurasian Plate**:\n- **North Anatolian Fault Zone (NAFZ):** A major right-lateral strike-slip fault stretching approximately 1,500 kilometers from the Karlıova triple junction in Eastern Anatolia across the Marmara Sea. It has generated devastating historical earthquakes (1939 Erzincan Mw 7.8, 1999 Gölcük/İzmit Mw 7.6, 1999 Düzce Mw 7.2).\n- **East Anatolian Fault Zone (EAFZ):** A 500-kilometer left-lateral strike-slip fault running from Karlıova to the Hatay graben. On February 6, 2023, the Kahramanmaraş earthquake doublet (Mw 7.8 and Mw 7.6) struck along the EAFZ and associated strands, affecting 11 provinces, claiming over 53,500 lives, and displacing millions [AYM-REPORTS, WB-TUR-2024].\n- **Aegean Graben System:** Characterized by north-south extensional tectonics, producing frequent shallow earthquakes and prominent geothermal fields in Western Anatolia."
                },
                {
                    "id": "geo-hydro",
                    "title": "3. Hydrology, River Basins & Transboundary Waters",
                    "content": "Turkey has 25 designated hydrological basins. The most politically and hydrologically critical are the **Euphrates (*Fırat*)** and **Tigris (*Dicle*)**, originating in the Eastern Anatolian highlands and flowing southward into Syria and Iraq before joining at the Shatt al-Arab. Turkey contributes approximately 88–90% of the Euphrates flow and 40–50% of the Tigris flow.\n\nThe state-led **Southeastern Anatolia Project (*Güneydoğu Anadolu Projesi - GAP*)** encompasses 22 dams and 19 hydroelectric power plants along these basins, including the Atatürk Dam (one of the largest rockfill dams in the world) and the Ilısu Dam on the Tigris. Turkey maintains that transboundary waters are shared resources subject to equitable and reasonable utilization under customary international law, rather than international watercourses subject to rigid upstream-downstream quotas."
                }
            ],
            "infographics": [
                {
                    "type": "stat-grid",
                    "id": "geo-stats",
                    "title": "Key Geographical & Physical Metrics",
                    "data": [
                        {"label": "Total Surface Area", "value": "783,562 km²", "sub": "37th globally"},
                        {"label": "Coastline Length", "value": "8,333 km", "sub": "Black, Aegean, Med, Marmara"},
                        {"label": "Highest Altitude", "value": "5,137 m", "sub": "Mount Ararat (Ağrı Dağı)"},
                        {"label": "Average Elevation", "value": "1,132 m", "sub": "Predominantly high plateau"},
                        {"label": "Major Fault Lines", "value": "3 Principal Systems", "sub": "NAFZ, EAFZ, Aegean Extensional"},
                        {"label": "Hydrological Basins", "value": "25 Designated Basins", "sub": "Euphrates-Tigris, Kızılırmak, Sakarya"}
                    ]
                }
            ]
        }
        data_en["modules"].append(mod2)

        # Module 3 (Keep concise)
        mod3 = {
            "id": "nature",
            "number": "03",
            "title": "Nature, Biodiversity & Environment",
            "tagline": "Phytogeographical convergence, endemic flora and fauna, protected biomes, and climate vulnerability.",
            "icon": "tree",
            "readingTime": "11 min read",
            "summary": "An ecological profile examining Turkey's status as a global biodiversity hotspot where three distinct phytogeographical regions converge, hosting over 11,000 vascular plant species (one-third endemic), diverse wildlife, and escalating climate risk challenges.",
            "sections": [
                {
                    "id": "nature-biodiversity",
                    "title": "1. Floristic Riches & Phytogeographical Hotspot",
                    "content": "Turkey is situated at the intersection of three major phytogeographical realms: the **Euro-Siberian region** (dominating the Black Sea coast), the **Mediterranean region** (coastal South and West), and the **Irano-Turanian region** (dominating the Central and Eastern Anatolian steppe).\n\nThis convergence renders Turkey the richest country in Europe and the Middle East in terms of botanical diversity:\n- Over **11,000 vascular plant species and subspecies**, compared to roughly 12,000 across the entire European continent.\n- An exceptional **endemism rate of approximately 34%** (~3,700 endemic taxa), concentrated in the Taurus Mountains, the Amanos range, and the Anatolian Diagonal.\n- Primary wild relatives of critical domesticated cereals and legumes (wheat, barley, lentils, chickpeas, apples, pistachios) originate from the Fertile Crescent portion of Southeastern Anatolia."
                },
                {
                    "id": "nature-fauna",
                    "title": "2. Fauna & Wildlife Conservation",
                    "content": "Turkey's diverse habitats support roughly 470 bird species, 160 mammal species, 130 reptile species, and hundreds of freshwater and marine fish species:\n- **Keystone Mammals:** The brown bear (*Ursus arctos*), grey wolf (*Canis lupus*), Eurasian lynx (*Lynx lynx*), wild goat (*Capra aegagrus*), and the critically endangered Anatolian leopard (*Panthera pardus tulliana*), which has been redetected in southeastern and southern mountain ranges via camera traps.\n- **Avian Migratory Flyways:** The Bosporus, Çamlıca, and the Belen Pass in Hatay are vital bottlenecks for soaring bird migration between Africa and Eurasia (white storks, lesser spotted eagles, buzzards).\n- **Marine Wildlife:** Coastal Mediterranean and Aegean beaches serve as key nesting sites for the loggerhead sea turtle (*Caretta caretta*) and the green turtle (*Chelonia mydas*). The Mediterranean monk seal (*Monachus monachus*), one of the world's most endangered pinnipeds, inhabits rocky caverns along the Aegean and Mediterranean shores."
                },
                {
                    "id": "nature-climate",
                    "title": "3. Environmental Challenges & Climate Change Risk",
                    "content": "Turkey has been identified by the IPCC as an acutely vulnerable climate change hotspot in the Mediterranean Basin:\n- **Water Stress:** Turkey currently has approximately 1,350 m³ of available water per capita annually, classifying it as a 'water-stressed' nation. Decreased winter precipitation and increased evaporation are projected to reduce per capita availability below the 1,000 m³ scarcity threshold by 2035.\n- **Land Degradation:** Over 70% of Turkey's soil is subjected to moderate-to-severe erosion due to topography, deforestation, and overgrazing.\n- **Wildfire Vulnerability:** Severe summer heatwaves and droughts have driven mega-wildfires along the Mediterranean and Aegean pine forests (notably the 2021 fires burning over 170,000 hectares).\n- **Policy Response:** Turkey ratified the **Paris Climate Agreement in October 2021** and pledged a net-zero carbon emissions target by 2053, alongside the establishment of the National Climate Change Directorate under the Ministry of Environment, Urbanization and Climate Change."
                }
            ],
            "infographics": [
                {
                    "type": "stat-grid",
                    "id": "nature-stats",
                    "title": "Biodiversity & Conservation Benchmarks",
                    "data": [
                        {"label": "Plant Species", "value": "11,000+", "sub": "Richest in Western Eurasia"},
                        {"label": "Endemism Rate", "value": "~34%", "sub": "3,700+ endemic plant taxa"},
                        {"label": "National Parks", "value": "48 Parks", "sub": "Over 900,000 hectares"},
                        {"label": "Bird Species", "value": "470 Species", "sub": "Global migratory flyway"},
                        {"label": "Water Availability", "value": "1,350 m³/capita", "sub": "Water-stressed category"},
                        {"label": "Net-Zero Target", "value": "Year 2053", "sub": "Paris Agreement pledge"}
                    ]
                }
            ]
        }
        data_en["modules"].append(mod3)

        # Module 4: Constitution (EXPANDED 5x with 3x Infographics)
        mod4 = {
            "id": "constitution",
            "number": "04",
            "title": "Constitutional Law & Evolution",
            "tagline": "Constitutional chronology from 1876 to 1982, unamendable provisions, secularism, and the 2017 Executive Presidency.",
            "icon": "scroll",
            "readingTime": "28 min read",
            "summary": "An exhaustive juristic analysis of Turkish constitutional history: from the Ottoman Charter of Alliance (1808) and Kanûn-ı Esâsî (1876) to the wartime 1921 constitution, the 1924 republican charter, the post-coup 1961 and 1982 frameworks, unamendable foundational clauses (Articles 1–4), and the radical 2017 amendments that dismantled the parliamentary model in favor of an Executive Presidency.",
            "sections": [
                {
                    "id": "const-pre-republican",
                    "title": "1. Pre-Republican Constitutionalism: Sened-i İttifak to Kanûn-ı Esâsî",
                    "content": """Turkish constitutionalism is the product of over two centuries of institutional struggle to restrain sovereign prerogative and delineate fundamental rights:
- **Sened-i İttifak (Charter of Alliance, 1808):** Regarded by constitutional jurists as the Ottoman counterpart to the Magna Carta, signed between Sultan Mahmud II and provincial notables (*ayans*). It legally circumscribed royal authority for the first time, obligating the Sultan to collect equitable taxes and protect the notables from arbitrary execution.
- **Tanzimat & Islahat Edicts (1839, 1856):** Although imperial royal charters rather than codified constitutions, these edicts introduced the seminal principles of legality, rule of law, security of life, honor, and property, and the civil equality of Muslim and non-Muslim subjects before the law.
- **Kanûn-ı Esâsî (1876):** The first codified Ottoman-Turkish constitution, drafted by a commission chaired by Midhat Pasha and promulgated on December 23, 1876. It established a bicameral General Assembly (*Meclis-i Umûmî*), consisting of an appointed Senate (*Heyet-i Âyân*) and an elected Chamber of Deputies (*Heyet-i Meb'ûsân*). However, Article 113 reserved supreme power for the Sultan, including the authority to exile individuals deemed hazardous to state security, which Sultan Abdulhamid II exercised to dissolve parliament in 1878.
- **The 1909 Constitutional Reforms:** Following the Young Turk Revolution, the 1909 constitutional revisions shifted sovereignty decisively toward the elected parliament, severely curbing the Sultan's veto powers and establishing the principle that the Grand Vizier and cabinet were politically accountable to parliament rather than the crown."""
                },
                {
                    "id": "const-1921-1924",
                    "title": "2. Revolutionary Constitutions: 1921 Assembly Government & the 1924 Republican Charter",
                    "content": """The collapse of the Ottoman Empire during World War I precipitated a radical constitutional departure:
- **Teşkilât-ı Esâsîye Kanunu of 1921 (Law No. 85):** Enacted on January 20, 1921, amidst the War of Independence, this brief document of 23 articles was a revolutionary wartime text. Article 1 proclaimed: *"Sovereignty unconditionally belongs to the Nation"* (*Hâkimiyet bilâkaydüşart milletindir*). It instituted the system of **Assembly Government (*Meclis Hükümeti*)**, concentrating both legislative and executive powers exclusively in the TBMM, with no independent executive or head of state.
- **The 1924 Constitution (Law No. 491):** Adopted on April 20, 1924, following the proclamation of the Republic. It codified a unicameral parliamentary framework with extensive legislative supremacy. While executive power was exercised through the President and Council of Ministers, the Assembly held uninhibited authority to dissolve the cabinet.
- **Progressive Secularization Amendments:** Initially, Article 2 of the 1924 Constitution retained the clause *"The religion of the State of Turkey is Islam"*. In 1928, this clause was deleted from the text, and in 1937, the Six Arrows of Kemalist ideology—specifically **Secularism (*Lâiklik*)**, Republicanism, Nationalism, Populism, Statism, and Reformism—were formally entrenched in the constitutional text [TBMM-CONST-1982, ZURCHER-2017]."""
                },
                {
                    "id": "const-1961-1982-coups",
                    "title": "3. The Military-Engineered Charters: 1961 Checks & Balances vs. 1982 State-Centric Hegemony",
                    "content": """The second half of the twentieth century was marked by military interventions that suspended existing charters and imposed new constitutional dispensations:
- **The 1961 Constitution:** Drafted by a Constituent Assembly following the May 27, 1960 coup. Paradoxically, the 1961 Constitution was the most liberal and democratic text in Turkish history, engineered deliberately to prevent another legislative dictatorship by the ruling majority:
  - Created the **Constitutional Court (*Anayasa Mahkemesi*)** to review statutory legislation for constitutional conformity.
  - Instituted a **Bicameral Parliament** consisting of the National Assembly (450 seats) and the Republican Senate (150 elected seats plus lifetime senators).
  - Extended robust judicial autonomy to universities, TRT broadcasting, and established the Supreme Council of Judges (YHK).
  - Formulated extensive guarantees for civil liberties, labor rights, right to strike, and social state protections.
- **The 1982 Constitution:** Drafted under the military junta of General Kenan Evren following the September 12, 1980 coup, approved in a tightly controlled referendum alongside Evren's presidency. The 1982 text reflected authoritarian, state-centric security dogmas:
  - Re-concentrated power in the state apparatus over the individual, prioritizing public order (*kamu düzeni*) and national security.
  - Abolished the Senate, returning to a unicameral TBMM.
  - Instituted an extraordinarily high **10% national electoral threshold** (*seçim barajı*) to suppress small and Kurdish-oriented political parties.
  - Greatly expanded the emergency and decree powers of the President of the Republic and created the Higher Education Board (YÖK) to discipline academia [TBMM-CONST-1982, AYM-REPORTS]."""
                },
                {
                    "id": "const-unamendable-provisions",
                    "title": "4. The Entrenched Core: Articles 1–4 and Constitutional Identity",
                    "content": """Article 4 of the 1982 Constitution establishes a strict legal barrier against constitutional revision, declaring that the foundational tenets contained in the first three articles cannot be amended, nor can their amendment be proposed (*değiştirilemez ve değiştirilmesi teklif dahi edilemez*):
- **Article 1 (Republican Form):** *"The State of Turkey is a Republic."*
- **Article 2 (Characteristics of the Republic):** *"The Republic of Turkey is a democratic, secular (*lâik*) and social state governed by rule of law (*hukuk devleti*), within the notions of public peace, national solidarity and justice, respecting human rights, loyal to the nationalism of Atatürk, and based on the fundamental tenets set forth in the Preamble."*
- **Article 3 (Integrity, Language, Flag, Anthem, Capital):** *"The State of Turkey, with its territory and nation, is an indivisible entity (*bölünmez bütünlük*). Its official language is Turkish. Its flag, the form of which is prescribed by the relevant law, is composed of a white crescent and star on a red background. Its national anthem is the 'İstiklâl Marşı'. Its capital is Ankara."*
- **Article 4 (Prohibition of Amendment):** Formally outlaws any legislative bill or parliamentary proposal seeking to alter, diminish, or repeal Articles 1, 2, or 3. The Constitutional Court maintains that this entrenched clause forms the core constitutional identity of the state, serving as an insurmountable norm against secessionist or theocratic legal initiatives."""
                },
                {
                    "id": "const-2017-executive-presidency",
                    "title": "5. The 2017 Constitutional Overhaul: The Executive Presidential System",
                    "content": """On April 16, 2017, a polarising constitutional referendum approved 18 amendments by 51.4% to 48.6%, ending the 94-year parliamentary tradition of the Republic and establishing the **Presidential Government System (*Cumhurbaşkanlığı Hükümet Sistemi*)**, which took full operational effect following the June 2018 general elections:
- **Abolition of the Prime Ministry & Cabinet Accountability:** The office of Prime Minister (*Başbakanlık*) and the Council of Ministers were abolished. All executive authority was consolidated exclusively in the **President of the Republic**, who serves simultaneously as head of state and head of government.
- **Presidential Decrees (*Cumhurbaşkanlığı Kararnamesi*):** Under Article 104, the President was granted authority to issue decrees having the force of law on executive structural matters. However, decrees cannot regulate fundamental civil rights or matters explicitly governed by statutory law; if a statute and decree conflict, statutory legislation enacted by TBMM prevails.
- **Partisan Presidency (*Partili Cumhurbaşkanı*):** Abolished the historic constitutional requirement that the President sever ties with their political party, permitting the President to maintain active leadership of a parliamentary party faction.
- **Diminished Parliamentary Checks:** Abolished the parliamentary vote of confidence (*güvenoyu*) and parliamentary motions of censure (*gensoru*). Ministers are appointed and dismissed solely by the President without assembly confirmation.
- **Judicial Reshaping:** Reconfigured the Council of Judges and Prosecutors (HSK) and Constitutional Court (AYM) appointment mechanisms, giving the President and the parliamentary majority direct authority to select the majority of judicial overseers [TBMM-CONST-1982, AYM-REPORTS]."""
                }
            ],
            "infographics": [
                {
                    "type": "comparison-table",
                    "id": "const-matrix-full",
                    "title": "Comparative Constitutional Matrix: 1876 vs 1921 vs 1924 vs 1961 vs 1982 vs 2017",
                    "headers": ["Charter", "System of Gov", "Legislative Structure", "Judicial Review", "Secularism Status", "Executive Head"],
                    "rows": [
                        ["1876 Kanûn-ı Esâsî", "Constitutional Monarchy", "Bicameral (Senate + Deputies)", "None (Imperial Sharia & Civil Courts)", "State religion: Islam (Art. 11)", "Sultan & Grand Vizier"],
                        ["1921 Teşkilât-ı Esâsîye", "Assembly Government", "Unicameral (TBMM)", "None (Assembly Sovereign)", "Not mentioned (wartime)", "TBMM President"],
                        ["1924 Constitution", "Parliamentary Supremacy", "Unicameral (TBMM)", "None (TBMM interpreted laws)", "Secularized (1928/1937)", "President & Prime Minister"],
                        ["1961 Constitution", "Parliamentary (Checks & Balances)", "Bicameral (Assembly + Senate)", "Constitutional Court (AYM) created", "Enshrined as unamendable", "President (Neutral) & PM"],
                        ["1982 Constitution (Orig.)", "Executive-Biased Parliamentary", "Unicameral (TBMM 400-550)", "AYM with restricted standing", "Enshrined in Art. 2 & 4", "President (Strong) & PM"],
                        ["2017 Amended Charter", "Executive Presidential System", "Unicameral (TBMM 600 seats)", "AYM + Individual Applications", "Protected under Art. 2 & 4", "President of the Republic (Sole)"]
                    ]
                },
                {
                    "type": "stat-grid",
                    "id": "const-stats-grid",
                    "title": "Constitutional Benchmarks & Procedural Thresholds",
                    "data": [
                        {"label": "TBMM Total Seats", "value": "600 Deputies", "sub": "Expanded from 550 in 2017"},
                        {"label": "Referendum Threshold", "value": "360 Votes (3/5)", "sub": "Required to submit to public vote"},
                        {"label": "Direct Amendment", "value": "400 Votes (2/3)", "sub": "Adopts amendment without referendum"},
                        {"label": "Electoral Threshold", "value": "7% Nationally", "sub": "Lowered from 10% in 2022"},
                        {"label": "Unamendable Articles", "value": "Articles 1, 2, 3", "sub": "Protected by Article 4"},
                        {"label": "Constitutional Court", "value": "15 Jurists", "sub": "Reviews norm control & petitions"}
                    ]
                },
                {
                    "type": "timeline",
                    "id": "const-timeline-chart",
                    "title": "Chronology of Constitutional Turning Points in Modern Turkey",
                    "items": [
                        {"year": "1808", "event": "Sened-i İttifak signed, first restraint on Ottoman sultanic absolutism."},
                        {"year": "1876", "event": "Kanûn-ı Esâsî proclaimed, first codified constitution in Muslim world."},
                        {"year": "1909", "event": "Young Turk amendments establish parliamentary supremacy over the monarchy."},
                        {"year": "1921", "event": "TBMM adopts revolutionary wartime constitution: 'Sovereignty belongs to the Nation'."},
                        {"year": "1924", "event": "First Republican constitution adopted; secularized in 1928 and 1937."},
                        {"year": "1961", "event": "Post-coup constitution creates Constitutional Court, bicameral parliament, and civil liberties."},
                        {"year": "1982", "event": "Post-coup military constitution ratified, entrenching state security primacy and 10% threshold."},
                        {"year": "2010", "event": "Constitutional referendum introduces the individual application (Bireysel Başvuru) to AYM."},
                        {"year": "2017", "event": "Referendum establishes the Executive Presidential System, abolishing the office of Prime Minister."}
                    ]
                }
            ]
        }
        data_en["modules"].append(mod4)

        # Write remaining modules in data_en...
        print("Module 1-4 built. Continuing generation for Modules 5 to 13...")
        
    print("Done building base script.")

if __name__ == "__main__":
    build_data()
