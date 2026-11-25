#!/usr/bin/env python3
import json

def get_en_modules():
    from generate_all_locales import build_data
    # We will build modules 1 to 13
    modules = []
    
    # Module 1 (History)
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
- **Post-Cold War 'Compartmentalized Diplomacy' (1991–Present):** Bilateral trade boomed through shuttle trade and massive Turkish construction contracts in Russia. Strategic energy infrastructure forged deep interdependence: the **Blue Stream** pipeline (opened 2003) and the dual-string **TurkStream** pipeline (opened 2020) across the Black Sea seabed, supplying Russian gas to Turkey and southeastern Europe. In 2010, Turkey contracted Russian state atomic agency Rosatom to construct the $20 billion **Akkuyu Nuclear Power Plant** (4x 1,200 MW VVER reactors).
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
    modules.append(mod1)
    
    # Modules 2 & 3
    from generate_all_locales import build_data
    # We will get mod2 and mod3 from previous definitions
    return modules

print("Module generator script ready.")
