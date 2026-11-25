#!/usr/bin/env python3
"""
Full English definitions for Modules 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13.
"""

def get_modules_en():
    from generate_all_locales import build_data
    # We will construct modules 2 through 13
    mods = []

    # Module 2 (Geography - concise)
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
    mods.append(mod2)

    # Module 3 (Nature - concise)
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
    mods.append(mod3)

    # Module 4 (Constitution - expanded)
    import generate_all_locales
    # mod4 is defined there, let's include it
    import json
    with open("generate_all_locales.py", "r") as f:
        pass

    # Let's import mod4, mod5, mod6, mod7, mod8, mod9, mod10, mod11, mod12, mod13 from expanded definitions
    import modules_expanded_text
    mods.append(modules_expanded_text.get_mod4())
    mods.append(modules_expanded_text.get_mod5())
    mods.append(modules_expanded_text.get_mod6())
    mods.append(modules_expanded_text.get_mod7())
    mods.append(modules_expanded_text.get_mod8())
    mods.append(modules_expanded_text.get_mod9())
    mods.append(modules_expanded_text.get_mod10())
    mods.append(modules_expanded_text.get_mod11())
    mods.append(modules_expanded_text.get_mod12())
    mods.append(modules_expanded_text.get_mod13())

    return mods
