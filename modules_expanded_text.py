#!/usr/bin/env python3
"""
Deep Academic Content for Modules 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
Providing 5x text expansion and 3x more infographics/schemes.
"""

def get_mod4():
    return {
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

def get_mod5():
    return {
        "id": "state_system",
        "number": "05",
        "title": "State Architecture & Government System",
        "tagline": "The Executive Presidency, 17 line ministries, the Grand National Assembly (TBMM), and provincial governance.",
        "icon": "building-columns",
        "readingTime": "26 min read",
        "summary": "An institutional blueprint of the Turkish administrative state: the unitary state tradition, the Executive Presidency, Presidential decree mechanisms, 17 line ministries, the 600-seat TBMM, provincial administration across 81 provinces headed by appointed Governors (Vali), 30 Metropolitan Municipalities, and the Ombudsman institution.",
        "sections": [
            {
                "id": "state-executive-architecture",
                "title": "1. The Executive Presidency & Administrative Headquarters",
                "content": """Under the revised constitutional architecture of the 1982 Constitution (Articles 104–106), executive authority is concentrated in the **President of the Republic (*Cumhurbaşkanı*)**, directly elected by popular vote for a five-year term with a two-term limit (unless parliament resolves early elections in the second term):
- **Head of State & Chief Executive:** The President represents the Republic, commands the Turkish Armed Forces on behalf of the TBMM, appoints and dismisses Vice Presidents, Ministers, high-ranking civil bureaucrats, judges, and university rectors.
- **The Presidential Administration:** Centered at the Presidential Complex (*Cumhurbaşkanlığı Külliyesi*) in Beştepe, Ankara. The apparatus comprises:
  - **Presidential Policy Councils (9 Boards):** Strategic advisory bodies reporting directly to the President (Economic Policies, Foreign & Security Policies, Legal Policies, Social Policies, Health & Food Policies, Science & Technology).
  - **Affiliated Presidencies & Autonomous Directorates:**
    - **Strategy and Budget Directorate (*SBB*):** Directs macro-fiscal planning, the Five-Year National Development Plan, and the Central Government Budget.
    - **Defense Industry Agency (*SSB*):** Formulates defense acquisitions, manages multi-billion dollar R&D programs, and supervises state defense holding firms.
    - **National Intelligence Organization (*MİT*):** External intelligence, counter-espionage, and covert operations reporting solely to the President.
    - **Presidency of Religious Affairs (*Diyanet İşleri Başkanlığı*):** Administers public religious services, mosquework, and religious civil service.
    - **Directorate of Communications (*İletişim Başkanlığı*):** Directs public diplomacy, strategic communication, media accreditation, and state messaging [TBMM-CONST-1982, DCP-DIYANET-2024]."""
            },
            {
                "id": "state-cabinet-ministries",
                "title": "2. The 17 Line Ministries and the Presidential Cabinet",
                "content": """The **Presidential Cabinet (*Cumhurbaşkanlığı Kabinesi*)** convenes bi-weekly at the Presidential Complex under the chairmanship of the President. Ministers are appointed by Presidential Decree and cannot simultaneously serve as members of parliament; any elected deputy appointed to a ministry must resign their parliamentary seat:
- **Core Sovereign Ministries:**
  - **Ministry of Foreign Affairs (*Dışişleri*):** Directs bilateral diplomacy, diplomatic missions in 260+ posts (5th largest diplomatic network globally), and multilateral representations.
  - **Ministry of National Defense (*MSB*):** Directs the armed forces, defense procurement policy, military factories, and shipyard operations.
  - **Ministry of Interior (*İçişleri*):** Controls the General Directorate of Security (national police / *Emniyet*), the Gendarmerie (*Jandarma*), Coast Guard, AFAD disaster management, and provincial governorships.
  - **Ministry of Justice (*Adalet*):** Coordinates judicial administration, penitentiaries, statutory drafts, and judicial council interaction.
  - **Ministry of Treasury and Finance (*Hazine ve Maliye*):** Formulates fiscal policy, sovereign debt issuance, tax revenue administration (*GİB*), and international financial coordination.
- **Economic & Infrastructure Portfolios:** Energy & Natural Resources, Trade, Industry & Technology, Transport & Infrastructure, Environment/Urbanization/Climate Change, Agriculture & Forestry [WB-TUR-2024]."""
            },
            {
                "id": "state-legislature-tbmm",
                "title": "3. The Grand National Assembly of Turkey (TBMM)",
                "content": """The **Grand National Assembly of Turkey (*Türkiye Büyük Millet Meclisi - TBMM*)** embodies the legislative sovereignty of the nation, operating from its monumental parliament complex in Ankara:
- **Electoral System:** 600 deputies elected simultaneously with the President every five years across 87 electoral districts via party-list proportional representation (D'Hondt method), with a national electoral threshold of 7% (lowered from 10% in 2022).
- **Core Legislative Competence:**
  - Enacts, amends, and repeals statutory laws (*kanun*).
  - Debates and approves the annual **Central Government Budget Law** (if rejected, the previous year's budget continues adjusted for inflation).
  - Approves the ratification of international treaties, declarations of war, states of emergency (*OHAL*), and foreign troop deployments under Article 92.
- **Parliamentary Oversight Mechanisms:** Deprived of the vote of no confidence, parliamentary oversight is conducted through written parliamentary questions (*yazılı soru*, requiring ministerial response within 15 days), general debates, parliamentary investigations (*meclis soruşturması* to impeach ministers or the President with a 2/3 majority before the Supreme Court / *Yüce Divan*), and parliamentary research commissions [TBMM-CONST-1982]."""
            },
            {
                "id": "state-provincial-local",
                "title": "4. Field Administration: 81 Provinces & 30 Metropolitan Municipalities",
                "content": """In accordance with the unitary principle enshrined in Article 126 of the Constitution, public administration in Turkey is structured on a dual track of centralized field administration (*merkezden yönetim*) and elected local self-government (*yerinden yönetim*):
- **Centralized Field Administration:**
  - **81 Provinces (*İller*):** The sovereign territory is partitioned into 81 provinces. At the head of each province sits an appointed **Governor (*Vali*)**, who serves as the direct personal representative of the President of the Republic and the ultimate authority over all ministerial provincial directorates, state schools, hospitals, and police.
  - **973 Districts (*İlçeler*):** Subordinate to provinces, administered by career professional civil servants termed **District Governors (*Kaymakam*)**.
- **Elected Local Self-Governments:**
  - **30 Metropolitan Municipalities (*Büyükşehir Belediyeleri*):** Established in provinces with populations exceeding 750,000 (encompassing Istanbul, Ankara, Izmir, Bursa, Antalya, Adana, Diyarbakır, Gaziantep, Konya, etc.). The Metropolitan Mayor (*Büyükşehir Belediye Başkanı*) and municipal council command vast budgets, directing public transport, city zoning, water and sanitation (e.g. İSKİ, ASKİ), and fire services.
  - **51 Provincial & District Municipalities:** In non-metropolitan provinces, municipal powers cover town centers, while rural areas are served by Provincial Special Administrations (*İl Özel İdareleri*).
- **The Ombudsman Institution (*Kamu Denetçiliği Kurumu*):** Constitutional oversight organ established in 2012, examining citizens' complaints regarding maladministration, human rights, and public bureaucratic compliance [TBMM-CONST-1982]."""
            }
        ],
        "infographics": [
            {
                "type": "organogram",
                "id": "state-organogram-full",
                "title": "Institutional Organogram of the Turkish Executive & Administrative State",
                "nodes": [
                    {"id": "pres", "title": "President of the Republic", "type": "head", "sub": "Chief Executive, Head of State, Supreme Commander"},
                    {"id": "cab", "title": "Presidential Cabinet (17 Line Ministries)", "parent": "pres", "type": "exec", "sub": "Interior, Defense, Foreign, Treasury, Justice, etc."},
                    {"id": "councils", "title": "Presidential Policy Councils (9 Boards)", "parent": "pres", "type": "advisory", "sub": "Economy, Security, Foreign Policy, Legal"},
                    {"id": "agencies", "title": "Autonomous Presidencies (MİT, SSB, SBB, Diyanet)", "parent": "pres", "type": "agency", "sub": "Strategic Directives & Intelligence"},
                    {"id": "tbmm", "title": "Grand National Assembly of Turkey (600 Seats)", "type": "leg", "sub": "Statutory Legislation & Budget Ratification"},
                    {"id": "provinces", "title": "81 Provincial Governorships (Valilik)", "parent": "cab", "type": "field", "sub": "Central Field Administration"},
                    {"id": "local", "title": "30 Metropolitan Municipalities (Büyükşehir)", "type": "local", "sub": "Elected Local Self-Government"}
                ]
            },
            {
                "type": "comparison-table",
                "id": "state-admin-matrix",
                "title": "Administrative Structure: Central Field Governors vs. Elected Mayors",
                "headers": ["Entity", "Administrative Level", "Appointment / Election", "Jurisdiction / Scope", "Supervisory Authority"],
                "rows": [
                    ["Governor (Vali)", "Provincial (81 Provinces)", "Appointed by Presidential Decree", "Supreme administrative & security head of the province", "President & Ministry of Interior"],
                    ["District Governor (Kaymakam)", "District (973 Districts)", "Appointed by Ministry / President", "Civil administrative head of district territory", "Provincial Governor (Vali)"],
                    ["Metropolitan Mayor (Büyükşehir)", "Urban Metropolis (30 Provinces)", "Directly elected every 5 years", "Citywide transport, water/sewer, zoning, master planning", "Municipal Council & Interior Oversight"],
                    ["District Mayor (İlçe)", "Urban District Level", "Directly elected every 5 years", "Local parks, permits, waste collection, municipal services", "Metropolitan Council & Court Review"]
                ]
            },
            {
                "type": "stat-grid",
                "id": "state-stats-grid",
                "title": "State Administrative & Legislative Benchmarks",
                "data": [
                    {"label": "Total Provinces", "value": "81 Provinces", "sub": "Derived from French Department model"},
                    {"label": "Total Districts", "value": "973 Districts", "sub": "Headed by career Kaymakams"},
                    {"label": "Metropolitan Hubs", "value": "30 Metropolises", "sub": "Host ~78% of total national population"},
                    {"label": "Parliamentary Seats", "value": "600 Deputies", "sub": "Proportional D'Hondt representation"},
                    {"label": "Diplomatic Posts", "value": "260+ Missions", "sub": "5th largest diplomatic network globally"},
                    {"label": "Line Ministries", "value": "17 Ministries", "sub": "Headed by non-parliamentary ministers"}
                ]
            }
        ]
    }

def get_mod6():
    return {
        "id": "armed_forces",
        "number": "06",
        "title": "Armed Forces & Civil-Military Dynamics",
        "tagline": "The TSK structure, military coups and tutelage, post-2016 civilian restructuring, and the defense industrial complex.",
        "icon": "shield",
        "readingTime": "30 min read",
        "summary": "An analytical, evidence-based investigation of the Turkish Armed Forces (TSK): NATO command alignment, military branch doctrine (Land, Navy / Mavi Vatan, Air), the historic political role of military tutelage and coup interventions (1960, 1971, 1980, 1997, 2016), comprehensive civilianization reforms following the July 15 putsch attempt, and the emergence of an indigenous defense industrial powerhouse (SSB, Aselsan, Baykar, TAI).",
        "sections": [
            {
                "id": "mil-structure-nato",
                "title": "1. Military Structure, Strategic Doctrine & NATO Operational Role",
                "content": """The **Turkish Armed Forces (*Türk Silahlı Kuvvetleri - TSK*)** represent the second-largest standing military force in NATO by active-duty personnel (~425,000 active troops, supplemented by over 380,000 reserves):
- **Command Structure & Branch Allocation:**
  - **Turkish Land Forces (*Kara Kuvvetleri Komutanlığı*):** Organized into four field armies: 1st Army (Istanbul, defending Thrace and the Straits), 2nd Army (Malatya, commanding southern borders with Syria and Iraq), 3rd Army (Erzincan, guarding the Caucasus frontier), and the Aegean Army / 4th Army (Izmir, defending Western Anatolia).
  - **Turkish Naval Forces (*Deniz Kuvvetleri Komutanlığı*):** Operationalized under the **'Blue Homeland' (*Mavi Vatan*)** maritime doctrine, asserting sovereign rights over 462,000 km² of maritime zones across the Black Sea, Aegean, and Eastern Mediterranean. The naval fleet operates modern frigates (*Milgem Ada-class* corvettes, *İ-class* frigates), Type 214 Reis-class submarines with air-independent propulsion (AIP), and the amphibious drone assault ship **TCG Anadolu (L-400)**.
  - **Turkish Air Forces (*Hava Kuvvetleri Komutanlığı*):** Operates modern F-16 Block 30/40/50+ fighters (modernized via the domestic *Özgür* avionics program), Boeing 737 Peace Eagle airborne early warning aircraft, KC-135R aerial refuelers, and an expansive armed drone fleet.
- **NATO Integration & Assets:** Turkey joined NATO in 1952. It hosts the headquarters of **NATO Allied Land Command (LANDCOM)** in Izmir, the US Air Force 39th Air Base Wing at Incirlik (Adana), and the forward AN/TPY-2 missile defense radar at Kürecik (Malatya), integrated into NATO's European Phased Adaptive Approach [SIPRI-2024-MLX]."""
            },
            {
                "id": "mil-tutelage-history",
                "title": "2. The Military as a Political Power: The Tradition of Tutelage & Coup History",
                "content": """Throughout the twentieth century, the Turkish officer corps perceived itself not merely as a national defense force, but as the supreme vanguard and guardian of the Kemalist revolution, republican secularism, and territorial integrity. Whenever civilian political leaders were perceived to deviate from these tenets or allow social anarchy, the military intervened directly:
- **The May 27, 1960 Military Coup:** Orchestrated by middle-ranking officers of the National Unity Committee (MBK) against the Democrat Party (DP) government of Adnan Menderes, alleging authoritarianism and constitutional violation. Menderes, Foreign Minister Fatin Rüştü Zorlu, and Finance Minister Hasan Polatkan were tried by a military tribunal on Yassıada and executed by hanging.
- **The March 12, 1971 Coup by Memorandum (*Muhtıra*):** Chief of General Staff Gen. Memduh Tağmaç delivered an ultimatum to President Cevdet Sunay, forcing the resignation of Prime Minister Süleyman Demirel amidst escalating student radicalism and street clashes between left-wing and right-wing armed factions.
- **The September 12, 1980 Military Coup:** Led by Chief of General Staff Gen. Kenan Evren following acute political gridlock, hyperinflation, and political terrorism claiming over 5,000 lives. The junta dissolved parliament, suspended political parties, arrested over 650,000 individuals, purged civil society, and engineered the state-centric 1982 Constitution.
- **The February 28, 1997 'Post-Modern Coup':** The National Security Council (MGK) issued an 18-point memorandum to Prime Minister Necmettin Erbakan's Islamist-conservative Welfare Party (*Refah Partisi*) coalition, forcing Erbakan's resignation and closing religious schools without deploying tanks in the streets.
- **The April 27, 2007 'E-Memorandum':** A late-night warning published on the General Staff website warning against the election of Abdullah Gül to the presidency, which was unprecedentedly rebuffed by the civilian government, marking the beginning of the erosion of traditional military veto power [ZURCHER-2017]."""
            },
            {
                "id": "mil-july15-civilianization",
                "title": "3. The July 15, 2016 Attempted Coup & Historic Civilian Restructuring",
                "content": """On the night of July 15, 2016, a rogue faction within the military, largely affiliated with the clandestine network of Fethullah Gülen (FETÖ), launched a violent putsch attempt, seizing bridges in Istanbul, deploying tanks, and bombing the TBMM and Presidential Complex with F-16 fighters:
- **Defeat of the Putsch:** Defied by mass civilian resistance answering President Erdoğan's public broadcast, loyalist police forces, and anti-coup military personnel, the putsch collapsed within 24 hours, leaving 251 martyrs and over 2,000 wounded.
- **Historic Structural Reforms in Civil-Military Relations:**
  - **Subordination of the General Staff:** The Chief of General Staff (*Genelkurmay Başkanı*) and commanders of the Land, Naval, and Air forces were **directly subordinated to the civilian Minister of National Defense (*MSB*)**, ending the General Staff's autonomous constitutional status.
  - **Depolicing of TSK:** The Gendarmerie General Command (*Jandarma*) and Coast Guard Command were permanently detached from military command and placed 100% under the civilian Ministry of Interior.
  - **Civilianization of the Supreme Military Council (*YAŞ*):** YAŞ, which determines promotions and officer appointments, was reorganized with an overwhelming civilian cabinet majority (Vice President, Ministers of Justice, Foreign Affairs, Interior, Treasury, Education, and Defense) outnumbering the military brass.
  - **Abolition of Military Academies:** Traditional military high schools were shuttered; military medical academies were transferred to the Ministry of Health; officer training was centralized under the newly founded **National Defense University (*Milli Savunma Üniversitesi - MSÜ*)**, directed by a civilian rector [TBMM-CONST-1982]."""
            },
            {
                "id": "mil-defense-industry-complex",
                "title": "4. The Indigenous Defense Industrial Ecosystem (SSB, Aselsan, Baykar, TAI)",
                "content": """Catalyzed by arms embargoes (most notably the US arms embargo of 1975–1978 following the Cyprus intervention), Turkey embarked on a strategic drive for defense industrial autonomy, directed by the **Defense Industry Agency (*Savunma Sanayii Başkanlığı - SSB*)**:
- **Procurement Autonomy:** Domestic defense equipment ratio surged from roughly 20% in the early 2000s to **over 80% by the mid-2020s**, reducing foreign technological dependency.
- **Key Industrial Actors & Flagship Platforms:**
  - **ASELSAN:** Turkey's premier defense electronics firm, manufacturing AESA radars, electronic warfare suites (KORAL), thermal imaging, and communication networks.
  - **Baykar Technology:** Private global leader in unmanned aerial systems, developer of the combat-proven **Bayraktar TB2**, high-altitude long-endurance **Bayraktar Akıncı**, and the carrier-capable unmanned stealth jet **Bayraktar Kızılelma**.
  - **TUSAŞ / TAI:** State-backed aerospace giant, producing the **KAAN 5th-generation stealth combat aircraft** (maiden flight 2024), *Hürjet* advanced supersonic trainer, *T929 ATAK-II* attack helicopter, and *Anka-3* flying-wing stealth UAV.
  - **ROKETSAN:** Developer of long-range ballistic missiles (*Tayfun*), air-defense missiles (*Siper, Hisar*), and cruise missiles (*Atmaca, SOM*).
  - **BMC & Otokar:** Ground vehicle manufacturers producing the *Altay* main battle tank, *Kirpi* mine-resistant ambush-protected vehicles, and *Arma* armored combat vehicles.
- **Export Powerhouse:** Defense and aerospace exports climbed from $1 billion in 2011 to **over $5.5 billion annually**, supplying combat drones, naval corvettes, and armored vehicles to over 170 countries [SIPRI-2024-MLX]."""
            }
        ],
        "infographics": [
            {
                "type": "comparison-table",
                "id": "mil-coups-matrix",
                "title": "Historical Matrix of Military Interventions in Turkish Political Life",
                "headers": ["Event", "Date", "Commanding Junta", "Stated Justification", "Direct Political & Constitutional Consequence"],
                "rows": [
                    ["1960 Military Coup", "27 May 1960", "National Unity Committee (MBK)", "Authoritarianism of DP, civil discord", "Menderes & 2 ministers executed; 1961 Constitution drafted"],
                    ["1971 Memorandum", "12 Mar 1971", "Chief of General Staff & Commanders", "Escalating street warfare & paralysis", "Demirel resigned; technocratic military-supervised cabinets"],
                    ["1980 Military Coup", "12 Sep 1980", "National Security Council (Gen. Evren)", "Terrorism, hyperinflation, ideological clashes", "Parliament dissolved; 650k arrests; 1982 Constitution enacted"],
                    ["1997 Post-Modern Coup", "28 Feb 1997", "National Security Council (MGK)", "Islamist secularism violations by Welfare Party", "Erbakan forced out; 8-year basic education; party banned"],
                    ["2007 E-Memorandum", "27 Apr 2007", "General Staff Press Directorate", "Secularism concerns over Gül presidency", "Rebuffed by government; snap elections won by ruling party"],
                    ["2016 Attempted Coup", "15 Jul 2016", "Peace at Home Council (Clandestine Putsch)", "Attempt to seize sovereign power", "Defeated by civilian resistance; total civilian subordination of TSK"]
                ]
            },
            {
                "type": "organogram",
                "id": "mil-defense-organogram",
                "title": "Modern Civil-Military Command & Defense Industrial Governance",
                "nodes": [
                    {"id": "pres", "title": "President of the Republic", "type": "head", "sub": "Supreme Commander of the Armed Forces"},
                    {"id": "msb", "title": "Ministry of National Defense (MSB)", "parent": "pres", "type": "exec", "sub": "Civilian Ministerial Chain of Command"},
                    {"id": "genelkurmay", "title": "Chief of General Staff & Service Chiefs", "parent": "msb", "type": "military", "sub": "Subordinated directly to MSB (post-2016)"},
                    {"id": "services", "title": "Land, Naval & Air Force Commands", "parent": "genelkurmay", "type": "military", "sub": "Combat Operational Commands"},
                    {"id": "ssb", "title": "Defense Industry Agency (SSB)", "parent": "pres", "type": "agency", "sub": "Procurement, R&D & Indigenous Projects"},
                    {"id": "firms", "title": "Key Industrial Actors (Aselsan, Baykar, TUSAŞ, Roketsan)", "parent": "ssb", "type": "industry", "sub": "Hardware, Stealth Aviation, Missiles, UAVs"}
                ]
            },
            {
                "type": "stat-grid",
                "id": "mil-stats-grid",
                "title": "Military Capabilities & Industrial Export Benchmarks",
                "data": [
                    {"label": "Active Armed Strength", "value": "~425,000 Troops", "sub": "2nd largest active military in NATO"},
                    {"label": "Domestic Defense Ratio", "value": ">80% Autonomy", "sub": "Up from 20% in 2002"},
                    {"label": "Annual Defense Exports", "value": "$5.5B+ USD", "sub": "Exported to 170+ partner countries"},
                    {"label": "Flagship Drone", "value": "Bayraktar TB2 / Akıncı", "sub": "Deployed in Libya, Karabakh, Ukraine"},
                    {"label": "5th Gen Stealth Fighter", "value": "TUSAŞ KAAN", "sub": "Twin-engine air-superiority jet"},
                    {"label": "Naval Drone Carrier", "value": "TCG Anadolu (L-400)", "sub": "Amphibious assault & UAV flagship"}
                ]
            }
        ]
    }

def get_mod7():
    return {
        "id": "judiciary",
        "number": "07",
        "title": "Judicial System & Rule of Law",
        "tagline": "Court hierarchy, the Constitutional Court, Council of Judges and Prosecutors (HSK), and ECHR jurisprudence.",
        "icon": "scale",
        "readingTime": "27 min read",
        "summary": "An exhaustive judicial roadmap of Turkey: civil law traditions, the bifurcated ordinary vs. administrative court hierarchy, the supremacy and competencies of the Constitutional Court (AYM), the individual human rights application mechanism (Bireysel Başvuru), judicial administration under the HSK, the National Judicial Network Information System (UYAP), and compliance with European Court of Human Rights (ECHR) rulings under Article 90.",
        "sections": [
            {
                "id": "jud-tradition-bifurcation",
                "title": "1. Civil Law Heritage & Bifurcated Court Architecture",
                "content": """The Turkish legal system belongs firmly to the continental European civil law tradition (*Civil Law*), inaugurated during the 1926 legal reforms with the adoption of the Swiss Civil Code, the Swiss Code of Obligations, and the Italian Penal Code, completely superseding Ottoman Islamic jurisprudence (*Mecelle*):
- **Bifurcated Jurisdiction:** Judicial power is formally split between two distinct vertical court hierarchies:
  - **Ordinary Jurisdiction (Civil & Criminal Courts):** Resolves private disputes, commercial litigation, labor claims, family law, and penal prosecutions.
  - **Administrative Jurisdiction:** Specialized administrative bodies adjudicating the lawfulness of administrative acts, public contracts, government expropriations, tax assessments, and state tort liability (*tam yargı davaları*).
- **The Specialized High Courts:** At the apex of these two jurisdictions stand the **Court of Cassation (*Yargıtay*)** for civil/criminal law, and the **Council of State (*Danıştay*)** for administrative disputes.
- **The Court of Jurisdictional Disputes (*Uyuşmazlık Mahkemesi*):** High judicial body tasked with delivering final, binding rulings resolving conflicts of jurisdiction or conflicting verdicts between ordinary, administrative, and constitutional courts [TBMM-CONST-1982, AYM-REPORTS]."""
            },
            {
                "id": "jud-court-hierarchy-deep",
                "title": "2. The Three-Tiered Trial & Appellate Hierarchy",
                "content": """Following structural judicial modernization in 2016, Turkey operationalized a modernized three-tiered court structure:
- **First Instance Courts (*İlk Derece Mahkemeleri*):**
  - *Civil Jurisdiction:* Civil Courts of Peace (*Sulh Hukuk*), Civil Courts of First Instance (*Asliye Hukuk*), and specialized chambers (Commercial, Labor, Family, Enforcement, Cadastral, Intellectual Property).
  - *Criminal Jurisdiction:* Criminal Courts of Peace (*Sulh Ceza Hâkimlikleri*, primarily issuing detention warrants, search orders, and access bans), Criminal Courts of First Instance (*Asliye Ceza*), and Heavy Penal Courts (*Ağır Ceza Mahkemeleri*, adjudicating offenses carrying 10+ years imprisonment, homicide, terrorism, organized crime).
- **Intermediate Appellate Tier: Regional Courts of Appeal (*Bölge Adliye / Bölge İdare Mahkemeleri*):**
  - **BAM (Ordinary Appeals):** Conducts appellate review (*istinaf*) on both questions of legal interpretation and factual evidence, with authority to retry cases.
  - **BİM (Administrative Appeals):** Reviews first-instance administrative and tax court rulings across 9 geographical judicial regions.
- **Courts of Last Resort (*Temyiz*):**
  - **Court of Cassation (*Yargıtay*):** Composed of specialized civil and criminal chambers based in Ankara. Ensures uniform application of private and penal law across the Republic.
  - **Council of State (*Danıştay*):** The supreme administrative court, delivering final appellate rulings on public law and advising the government on administrative regulations [TBMM-CONST-1982]."""
            },
            {
                "id": "jud-aym-constitutional-court",
                "title": "3. The Constitutional Court (AYM) & the Individual Application System",
                "content": """Established by the 1961 Constitution, the **Constitutional Court (*Anayasa Mahkemesi - AYM*)** sits atop the constitutional legal order, composed of **15 members** (appointed by the President from high court nominees and academics, and elected by the TBMM):
- **Norm Control (*Norm Denetimi*):** Evaluates the constitutionality of statutory laws, presidential decrees, and TBMM parliamentary rules of procedure:
  - *Abstract Review (Direct Action):* May be filed within 60 days of promulgation by the President of the Republic or the two largest parliamentary party factions.
  - *Concrete Review (Plea of Unconstitutionality):* Initiated by trial judges who find that a statutory provision applicable in an ongoing lawsuit violates the Constitution.
- **The Individual Application (*Bireysel Başvuru*):** Introduced by the 2010 constitutional referendum, modeled on the German *Verfassungsbeschwerde*. Any individual may petition the AYM alleging that public authorities violated fundamental rights guaranteed in the Constitution and the European Convention on Human Rights (ECHR), after exhausting ordinary judicial remedies. The AYM receives 70,000–100,000 applications annually, serving as a critical constitutional arbiter.
- **Political Party Dissolution & Financial Auditing:** Possesses exclusive jurisdiction to ban political parties that become centers of unconstitutional, violent, or anti-secular activities upon indictments filed by the Chief Public Prosecutor of the Court of Cassation [AYM-REPORTS]."""
            },
            {
                "id": "jud-hsk-uyap-echr",
                "title": "4. Council of Judges and Prosecutors (HSK), UYAP & ECHR Relations",
                "content": """The administration and international compliance of the judicial apparatus involve crucial statutory bodies and technological platforms:
- **Council of Judges and Prosecutors (*Hâkimler ve Savcılar Kurulu - HSK*):** Composed of 13 members: the Minister of Justice (President ex officio), Deputy Minister of Justice, 4 members appointed by the President, and 7 members elected by the TBMM by a 3/5 qualified majority. The HSK controls all appointments, transfers, disciplinary proceedings, and promotions of career judges and prosecutors.
- **UYAP (National Judicial Network Information System):** World-recognized digital justice e-government network connecting all courts, prosecutor offices, land registries, prisons, and bar associations. Permits electronic petition filings, digital evidence review, video-conference testimony (SEGBİS), and immediate algorithmic case assignment.
- **Supremacy of International Human Rights Conventions (Article 90):** Under Article 90 (amended in 2004), international agreements concerning fundamental human rights duly put into effect carry suprastatutory authority. In the event of an irreconcilable conflict between a domestic statutory law and an international human rights convention (notably the ECHR), Turkish judges are constitutionally mandated to apply the provisions of the international agreement [TBMM-CONST-1982, AYM-REPORTS]."""
            }
        ],
        "infographics": [
            {
                "type": "organogram",
                "id": "jud-complete-hierarchy",
                "title": "Bifurcated Judicial Hierarchy & Appellate Stages of Turkey",
                "nodes": [
                    {"id": "aym", "title": "Constitutional Court (AYM)", "type": "apex", "sub": "15 Members: Norm Control & Individual Applications"},
                    {"id": "yargitay", "title": "Court of Cassation (Yargıtay)", "type": "high", "sub": "Highest Civil & Criminal Court of Last Resort"},
                    {"id": "danistay", "title": "Council of State (Danıştay)", "type": "high", "sub": "Highest Administrative Appellate & Advisory Body"},
                    {"id": "bam", "title": "Regional Courts of Appeal (BAM)", "parent": "yargitay", "type": "appellate", "sub": "Intermediate Appeals on Law & Facts"},
                    {"id": "bim", "title": "Regional Administrative Courts (BİM)", "parent": "danistay", "type": "appellate", "sub": "Administrative Appellate Chambers"},
                    {"id": "first-civil", "title": "Civil First Instance Courts", "parent": "bam", "type": "trial", "sub": "Civil Courts of Peace, Asliye, Commercial, Family"},
                    {"id": "first-crim", "title": "Criminal Trial Courts", "parent": "bam", "type": "trial", "sub": "Heavy Penal (Ağır Ceza) & Asliye Ceza"},
                    {"id": "first-admin", "title": "Administrative & Tax Courts", "parent": "bim", "type": "trial", "sub": "Local Public Law & Tax Tribunals"}
                ]
            },
            {
                "type": "comparison-table",
                "id": "jud-high-courts-matrix",
                "title": "Institutional Comparison of High Judicial Bodies in Turkey",
                "headers": ["Court", "Jurisdiction", "Total Jurists", "Core Functions", "Constitutional Basis"],
                "rows": [
                    ["Constitutional Court (AYM)", "Constitutional Review", "15 Members", "Norm control of statutes/decrees; Individual human rights complaints", "Articles 146–153"],
                    ["Court of Cassation (Yargıtay)", "Ordinary (Civil & Criminal)", "Specialized Chambers", "Final appellate review of civil lawsuits and criminal verdicts", "Article 154"],
                    ["Council of State (Danıştay)", "Administrative & Public Law", "Specialized Chambers", "Final review of government/tax litigation; reviews concessions", "Article 155"],
                    ["Court of Jurisdictional Disputes", "Inter-jurisdictional", "6 Members + President", "Resolves positive/negative jurisdictional conflicts between courts", "Article 158"]
                ]
            },
            {
                "type": "stat-grid",
                "id": "jud-stats-grid",
                "title": "Judicial Statistics & Digital Network Benchmarks",
                "data": [
                    {"label": "AYM Jurists", "value": "15 Members", "sub": "12-year non-renewable term"},
                    {"label": "Annual AYM Petitions", "value": "75,000+ / year", "sub": "Bireysel Başvuru human rights claims"},
                    {"label": "HSK Membership", "value": "13 Members", "sub": "Chaired ex-officio by Justice Minister"},
                    {"label": "Regional Appeal Courts", "value": "18 BAM / 9 BİM", "sub": "Intermediate appellate layer across regions"},
                    {"label": "Digital UYAP System", "value": "100% Integrated", "sub": "Electronic filing & SEGBİS remote trials"},
                    {"label": "Article 90 Mandate", "value": "ECHR Supremacy", "sub": "International human rights treaties prevail"}
                ]
            }
        ]
    }

def get_mod8():
    return {
        "id": "demography",
        "number": "08",
        "title": "Demography & Ethnic Tapestry",
        "tagline": "Population dynamics, ethnic communities, Lausanne non-Muslim minorities, and migration inflows.",
        "icon": "users",
        "readingTime": "29 min read",
        "summary": "An exhaustive, evidence-based demographic, sociolinguistic, and anthropological survey of Turkey: population dynamics (85.37M), the demographic transition (fertility decline to 1.51), rapid urbanization, ethnic and linguistic communities (Turks, Kurds, Zazas, Arabs, Circassians, Laz, Bosniaks, Romani), the legal minority regime under the Treaty of Lausanne (Armenians, Greeks, Jews), and modern refugee demographics hosting 3.1M+ Syrians.",
        "sections": [
            {
                "id": "demo-population-dynamics",
                "title": "1. Population Trajectory, Age Pyramid & the Fertility Transition",
                "content": """According to official registry records published by the Turkish Statistical Institute (TÜİK), the population of Turkey stands at approximately **85.37 million inhabitants** (2023–2024 data):
- **Historical Population Growth:** The first official census of the Republic in 1927 recorded just 13.6 million inhabitants, depleted by a decade of continuous warfare. Rapid population growth marked the mid-twentieth century, exceeding 44 million by 1980 and doubling again to over 85 million by the 2020s.
- **The Demographic Transition & Fertility Collapse:** Turkey is undergoing an unprecedented demographic transition. The **Total Fertility Rate (TFR)** has collapsed from 4.3 children per woman in 1970 and 2.38 in 2001 to **1.51 children per woman in 2023**, dropping substantially below the generational replacement threshold of 2.1.
- **Population Aging:** The median age has increased from 24.8 years in 2000 to **34.0 years** in 2024. The proportion of the population aged 65 and over surpassed 10.2%, classifying Turkey for the first time as an 'aging society' under United Nations demographic metrics [TUIK-2024-POP]."""
            },
            {
                "id": "demo-urbanization-metropolis",
                "title": "2. Hyper-Urbanization & Spatial Redistribution",
                "content": """Driven by post-WWII industrialization and agricultural mechanization, Turkey transformed from an agrarian rural country into a hyper-urbanized society:
- **Urbanization Rate:** 93.2% of the population resides in provincial and district municipal centers, with fewer than 6.8% living in rural villages.
- **Metropolitan Concentration in Marmara:** The Marmara region represents the demographic center of gravity, housing over 30% of the national population on just 8.5% of the land area.
- **Megacities of Turkey:**
  - **Istanbul (15.65 Million):** Represents 18.3% of the total population; the largest city in Europe, home to substantial internal migrant communities from every Anatolian province (e.g. Sivas, Kastamonu, Ordu, Trabzon, Diyarbakır).
  - **Ankara (5.8 Million):** Administrative, political, and academic hub.
  - **Izmir (4.5 Million):** Aegean industrial, port, and cultural center.
  - **Bursa (3.2M), Antalya (2.7M), Konya (2.3M), Adana (2.2M), Gaziantep (2.2M), Şanlıurfa (2.2M) [TUIK-2024-POP]."""
            },
            {
                "id": "demo-ethnic-mosaic",
                "title": "3. Sociolinguistic Mosaic & Ethnic Communities",
                "content": """While official census records since 1965 do not enumerate ethnic origin or mother tongue, extensive academic sociological field research documents a diverse multi-ethnic society:
- **Turks:** Constitute the demographic majority (approximately 75–80%), comprising Oghuz Turkic descendants alongside settled *muhacir* populations from the Balkans, Crimea (Crimean Tatars), and the Aegean islands.
- **Kurds:** The largest ethnic minority, estimated at **15–20% of the national population** (approximately 13–16 million). Concentrated historically in Eastern and Southeastern Anatolia (Diyarbakır, Van, Mardin, Batman, Şırnak, Hakkari), with massive urban populations in Istanbul (the world's largest Kurdish-populated metropolis), Izmir, and Mersin. The vast majority speak **Kurmanji (*Kurmancî*)**, alongside Southern Kurdish dialects.
- **Zazas:** An indigenous Anatolian community primarily inhabiting Tunceli (Dersim), Bingöl, and Elazığ, speaking the **Zaza language (*Zazaki*)**, linguistically classified within the Northwestern Iranian language family.
- **Arabs:** Concentrated in the historical southern border provinces of Hatay, Mardin, Şanlıurfa, and Adana, bolstered by post-2011 Syrian migration.
- **Circassians (*Adyghe*) & North Caucasians:** Descendants of over 1 million Caucasian Muslims expelled during the 1864 Circassian Genocide by Tsarist Russia, residing in Western Anatolian pockets (Bolu, Düzce, Balıkesir, Adapazarı) and Central Anatolia (Kayseri, Uzunyayla), along with Abkhazians, Chechens, and Ossetians.
- **Laz & Hemshin:** Indigenous South Caucasian communities along the eastern Black Sea; the Laz inhabit coastal Rize and Artvin speaking an endangered Kartvelian language (*Lazuri*), while the Muslim Hemshin speak an archaic Armenian-influenced dialect.
- **Balkan & Romani Peoples:** Substantial communities of Bosniaks, Pomaks, Torbesh, and Romani inhabiting Eastern Thrace, Istanbul, and Izmir [ZURCHER-2017]."""
            },
            {
                "id": "demo-lausanne-minorities",
                "title": "4. The Lausanne Minorities Regime & Historic Non-Muslims",
                "content": """Under Section III (Articles 37–45) of the 1923 **Treaty of Lausanne**, minority status in the Republic of Turkey is legally restricted to **non-Muslim religious confessions**:
- **Armenian Community:** Turkey's largest recognized non-Muslim minority (~50,000–60,000 individuals), almost entirely concentrated in Istanbul. They operate 16 community foundation schools, 2 major hospitals (Yedikule Surp Pırgiç and Surp Agop), and numerous historic churches under the ecclesiastical authority of the **Armenian Patriarchate of Constantinople** in Kumkapı.
- **Jewish Community:** Numbering approximately 14,000–15,000, predominantly Sephardic Jews who speak Judeo-Spanish (*Ladino* / *Judezmo*), descendants of refugees granted asylum in 1492 by Sultan Bayezid II following the Spanish Alhambra Decree. Centered in Istanbul and Izmir, governed religiously by the **Chief Rabbinate of Turkey (*Hahambaşılık*)**.
- **Greek Orthodox Community (*Rûm*):** Numbering approximately 2,000–3,000 in Istanbul, Gökçeada (Imbros), and Bozcaada (Tenedos). The community was historically exempted from the 1923 Greek-Turkish Population Exchange, but experienced severe demographic decline following the 1942 Wealth Tax (*Varlık Vergisi*), the 1955 Istanbul Pogrom, and the 1964 expulsions. Centered on the **Ecumenical Patriarchate of Constantinople** in Fener.
- **Syriacs & Other Non-Lausanne Groups:** Ancient Christian communities not formally designated as Lausanne minorities, including the Syriac Orthodox (*Süryani Kadim*, ~25,000 centered in Mardin's Tur Abdin and Istanbul) and Chaldean Catholics [LAUSANNE-1923]."""
            },
            {
                "id": "demo-refugees-migration",
                "title": "5. Contemporary Refugee Demographics & Transit Migration",
                "content": """Beginning in 2011 with the onset of the Syrian Civil War, Turkey transitioned into the world's largest refugee-hosting nation:
- **Syrians under Temporary Protection (*Geçici Koruma*):** Under Law No. 6458 on Foreigners and International Protection (YUKK), displaced Syrians were granted Temporary Protection status, peaking at over 3.7 million and currently standing at **over 3.1 million registered individuals** (2024 data). The largest populations reside in Istanbul, Gaziantep, Şanlıurfa, Hatay, and Adana.
- **The 2016 EU-Turkey Statement:** Signed on March 18, 2016, establishing the 'One-for-One' readmission mechanism aimed at arresting irregular sea crossings across the Aegean Sea in exchange for €6 billion in Facility for Refugees in Turkey (FRIT) humanitarian funding and visa liberalization talks.
- **Transit Migration Dynamics:** Turkey serves as a primary transit corridor for irregular and regular migrants from Afghanistan, Iraq, Iran, Pakistan, and Central Asia aiming for the European Union [TUIK-2024-POP, WB-TUR-2024]."""
            }
        ],
        "infographics": [
            {
                "type": "comparison-table",
                "id": "demo-ethnic-matrix",
                "title": "Sociolinguistic & Confessional Mosaic of Contemporary Turkey",
                "headers": ["Community", "Language Family", "Estimated Demographic Share", "Primary Geographic Concentrations", "Legal Recognition"],
                "rows": [
                    ["Turks", "Turkic (Oghuz branch)", "~75–80% of national total", "Nationwide across all 81 provinces", "Sovereign Constitutional Majority"],
                    ["Kurds", "Indo-European (Northwestern Iranian)", "~15–20% (~13–16M)", "Eastern/Southeastern Anatolia, Istanbul, Izmir", "Equal Citizens (Universal citizenship)"],
                    ["Zazas", "Indo-European (Zaza-Gorani)", "~2–3% (~1.5–2M)", "Tunceli (Dersim), Bingöl, Elazığ, Diyarbakır", "Equal Citizens (Universal citizenship)"],
                    ["Arabs", "Afroasiatic (Semitic)", "~2–3% (Native) + 3.1M Syrians", "Hatay, Mardin, Şanlıurfa, Adana, Istanbul", "Citizens + Temporary Protection Status"],
                    ["Circassians", "Northwest Caucasian (Adyghe)", "~1.5–2% (~1–1.5M)", "Düzce, Bolu, Balıkesir, Kayseri, Samsun", "Equal Citizens (Universal citizenship)"],
                    ["Armenians", "Indo-European (Armenian)", "~50,000–60,000", "Istanbul (Kumkapı, Şişli, Kadıköy)", "Treaty of Lausanne Confessional Minority"],
                    ["Jews (Sephardic)", "Afroasiatic / Romance (Ladino)", "~14,000–15,000", "Istanbul, Izmir", "Treaty of Lausanne Confessional Minority"],
                    ["Greeks (Rûm)", "Indo-European (Hellenic)", "~2,000–3,000", "Istanbul (Fener, Beyoğlu), Gökçeada", "Treaty of Lausanne Confessional Minority"],
                    ["Syriacs", "Afroasiatic (Aramaic)", "~25,000", "Mardin (Tur Abdin plateau), Istanbul", "De Facto Confessional Community"]
                ]
            },
            {
                "type": "stat-grid",
                "id": "demo-stats-grid",
                "title": "Demographic Benchmarks & Vital Statistics (TÜİK 2024)",
                "data": [
                    {"label": "Total Population", "value": "85.37 Million", "sub": "18th most populous globally"},
                    {"label": "Total Fertility Rate", "value": "1.51 TFR", "sub": "Historic low (2.1 replacement)"},
                    {"label": "Median Age", "value": "34.0 Years", "sub": "33.2 males, 34.7 females"},
                    {"label": "Urbanization Share", "value": "93.2% Urban", "sub": "Residing in province/district centers"},
                    {"label": "Istanbul Population", "value": "15.65 Million", "sub": "18.3% of national population"},
                    {"label": "Registered Syrians", "value": "3.1M+ Persons", "sub": "Temporary Protection status"}
                ]
            },
            {
                "type": "timeline",
                "id": "demo-migration-timeline",
                "title": "Historical Waves of Inflow and Exodus in Modern Turkish History",
                "items": [
                    {"year": "1923", "event": "Lausanne Population Exchange: ~1.2M Orthodox Christians to Greece, ~400k Muslims to Turkey."},
                    {"year": "1934", "event": "Thrace Pogroms (*Trakya Olayları*) displace Jewish communities toward Istanbul."},
                    {"year": "1942", "event": "Varlık Vergisi (Wealth Tax) disproportionately levies non-Muslim commercial classes."},
                    {"year": "1955", "event": "6–7 September Istanbul Pogrom accelerates emigration of Greek and Armenian populations."},
                    {"year": "1989", "event": "Büyük Göç: 360,000+ Bulgarian Turks flee Zhivkov regime into Turkey within 90 days."},
                    {"year": "1991", "event": "Gulf War crisis: Turkey shelters ~500,000 Iraqi Kurds along the southeastern border."},
                    {"year": "2011", "event": "Syrian Civil War begins; Turkey implements open-door policy, hosting 3.7M+ refugees."},
                    {"year": "2016", "event": "EU-Turkey Statement establishes €6B migrant cooperation framework."}
                ]
            }
        ]
    }

def get_mod9():
    return {
        "id": "transportation",
        "number": "09",
        "title": "Transportation & Logistics Corridors",
        "tagline": "High-speed rail (YHT), highway megaprojects, the Turkish Straits, air hubs, and the Middle Corridor.",
        "icon": "train",
        "readingTime": "26 min read",
        "summary": "An infrastructural masterplan review of Turkey's transit role: High-Speed Rail (TCDD YHT), public-private partnership (PPP) mega-bridges (1915 Çanakkale, Yavuz Sultan Selim, Osmangazi), the maritime transit regime of the Bosporus and Dardanelles under the Montreux Convention, Istanbul Airport as a global mega-hub, and the Trans-Caspian Middle Corridor (TITR).",
        "sections": [
            {
                "id": "trans-rail-network",
                "title": "1. The Railway Renaissance & High-Speed Rail (YHT) Network",
                "content": """The State Railways of the Republic of Turkey (*Türkiye Cumhuriyeti Devlet Demiryolları - TCDD*) oversees a national railway network spanning over 13,900 kilometers. After decades of automotive highway bias, Turkey initiated a massive railway modernization program in the early 2000s:
- **High-Speed Rail Lines (*Yüksek Hızlı Tren - YHT*):**
  - **Ankara–Eskişehir–Istanbul YHT (533 km):** Slashes travel time between Turkey's political and commercial capitals to roughly 4 hours, carrying millions of passengers annually.
  - **Ankara–Konya YHT (212 km):** Connects the capital to Central Anatolia's industrial hub in under 1 hour and 45 minutes.
  - **Ankara–Sivas YHT (405 km):** Opened in April 2023, cutting travel time from 12 hours to 2 hours, serving as the eastern trunk line toward the Caucasus.
  - **Under Construction / Advanced Work:** Ankara–İzmir YHT (reducing travel time to 3.5 hours), Halkalı–Kapıkule YHT (connecting Istanbul directly to the Bulgarian frontier and the European TEN-T network), and the Karaman–Mersin–Adana–Gaziantep line.
- **The Marmaray Subsea Rail Tunnel:** Opened in 2013, Marmaray features a submerged floating tube tunnel crossing the Bosphorus strait 60 meters below sea level. It connects the European (Halkalı) and Asian (Gebze) suburban rail networks over 76 kilometers, facilitating both 500,000+ daily commuter transits and international freight trains crossing between Europe and Asia without ferry transfers."""
            },
            {
                "id": "trans-highway-bridges",
                "title": "2. Highway Corridors & Engineering Megaprojects",
                "content": """Managed by the General Directorate of Highways (*Karayolları Genel Müdürlüğü - KGM*), Turkey's dual-carriageway (*bölünmüş yol*) network expanded from 6,100 km in 2002 to over 29,200 km in the mid-2020s, driven by Build-Operate-Transfer (BOT) Public-Private Partnerships:
- **1915 Çanakkale Bridge:** Inaugurated on March 18, 2022 across the Dardanelles strait. Featuring a central suspension span of **2,023 meters** (symbolizing the centenary of the Republic), it is the **world's longest suspension bridge**, replacing a 1.5-hour ferry crossing with a 6-minute drive.
- **Yavuz Sultan Selim Bridge (Third Bosphorus Bridge):** Opened in 2016, possessing a 59-meter wide deck carrying eight highway lanes and two high-speed rail tracks, connecting the Northern Marmara Motorway.
- **Osmangazi Bridge & Istanbul–Izmir Motorway:** Spans 2,682 meters across the Gulf of Izmit, reducing travel time between Istanbul and the Aegean commercial capital of Izmir from over 8 hours to under 3.5 hours.
- **Eurasia Tunnel (*Avrasya Tüneli*):** A 5.4-kilometer double-deck subsea automotive tunnel crossing the Bosphorus seabed, accommodating over 70,000 vehicles daily between Kazlıçeşme and Göztepe."""
            },
            {
                "id": "trans-maritime-straits",
                "title": "3. The Turkish Straits Maritime Regime & Commercial Seaports",
                "content": """The **Turkish Straits (Bosphorus and Dardanelles)** represent one of the world's most critical and congested maritime choke points, connecting the Black Sea to the Mediterranean:
- **Vessel Traffic Volume:** Approximately **35,000 to 45,000 vessels transit the Straits annually**, including over 9,000 tankers transporting roughly 150 million tons of crude oil and hazardous petrochemicals.
- **Montreux Legal Governance:** Transit of merchant ships in peacetime is governed by the principle of absolute freedom of navigation under Article 2 of the 1936 Montreux Convention. To prevent catastrophic ecological and urban collisions across central Istanbul, Turkey operates the advanced **Turkish Straits Vessel Traffic Services (TSVTS)**, enforcing maritime pilotage, traffic separation schemes (TSS), and daylight navigation limits for ultra-large crude carriers (ULCC) [UN-TREATY-MONTREUX].
- **Major Seaport Hubs:**
  - **Ambarlı Port (Istanbul):** Turkey's largest container terminal, handling over 3 million TEU annually.
  - **Mersin International Port (MIP):** Key Mediterranean deepwater gateway for the Levant and Southeastern Anatolia.
  - **Aliağa & Izmir Ports:** Primary export gateways for Aegean industrial goods and petrochemicals.
  - **Filyos Port:** Dedicated Black Sea port serving offshore natural gas logistics and heavy industry."""
            },
            {
                "id": "trans-aviation-middle-corridor",
                "title": "4. Global Aviation Crossroads & the Trans-Caspian Middle Corridor",
                "content": """Turkey leverages its central position at the crossroads of Europe, Asia, and Africa:
- **Aviation Powerhouse:**
  - **Istanbul Airport (IGA):** Opened in 2018 with a masterplan capacity of 200 million passengers upon full phase completion. Currently processing over 76 million passengers annually, ranking as Europe's busiest airport by passenger traffic.
  - **Turkish Airlines (*Türk Hava Yolları - THY*):** The national flag carrier, flying to **more international destinations (over 340 cities across 129 countries)** than any other airline on the planet, turning Istanbul into a preeminent global transit hub.
  - **Sabiha Gökçen Airport (SAW):** Istanbul's Asian hub, handling over 35 million passengers with its dual-runway operations.
- **The Trans-Caspian International Transport Route (Middle Corridor / *Orta Koridor*):**
  - Originates in China, traverses Kazakhstan, the Caspian Sea, Azerbaijan (Baku Port), Georgia, enters Turkey via the **Baku–Tbilisi–Kars (BTK) Railway**, and continues through Marmaray into Europe.
  - Offers a transit timeline of **12–15 days between China and Europe**, roughly half the maritime transit time via the Suez Canal (30–35 days) and avoiding Russian territory following geopolitical disruptions along the Northern Corridor [WB-TUR-2024]."""
            }
        ],
        "infographics": [
            {
                "type": "comparison-table",
                "id": "trans-megaprojects-matrix",
                "title": "Engineering Megaprojects of Turkey: Specifications & Capital Scale",
                "headers": ["Project", "Infrastructure Type", "Key Technical Dimension", "Investment Model", "Strategic Connectivity"],
                "rows": [
                    ["1915 Çanakkale Bridge", "Suspension Bridge", "2,023 m main span (World record)", "BOT (Public-Private)", "Direct Thrace–Aegean transit bypassing Istanbul"],
                    ["Marmaray Tunnel", "Subsea Rail Tunnel", "60 m below sea level (Floating tube)", "State-Funded / JICA", "Intercontinental commuter & rail freight link"],
                    ["Yavuz Sultan Selim", "Hybrid Cable-Stayed", "59 m deck width (Highway + Rail)", "BOT (Public-Private)", "Northern Marmara transit & heavy freight link"],
                    ["Osmangazi Bridge", "Suspension Bridge", "1,550 m central span", "BOT (Public-Private)", "Istanbul–Izmir Motorway (3.5 hr journey)"],
                    ["Eurasia Tunnel", "Subsea Road Tunnel", "Double-deck automotive tunnel", "BOT (Public-Private)", "Direct Bosphorus undersea car transit (5.4 km)"],
                    ["Istanbul Airport (IGA)", "International Mega-Hub", "6 independent runways (full phase)", "BOT (Public-Private)", "Global passenger hub (76M+ passengers)"]
                ]
            },
            {
                "type": "stat-grid",
                "id": "trans-stats-grid",
                "title": "Transport Network Benchmarks & Operational Metrics",
                "data": [
                    {"label": "Divided Highways", "value": "29,200+ km", "sub": "Quadrupled since 2002"},
                    {"label": "High-Speed Rail", "value": "2,228+ km", "sub": "Ankara, Istanbul, Konya, Sivas"},
                    {"label": "Straits Ship Transits", "value": "40,000+ Ships/yr", "sub": "Governed by Montreux Convention"},
                    {"label": "Istanbul Airport Traffic", "value": "76M+ Passengers", "sub": "Busiest airport in Europe"},
                    {"label": "THY Global Reach", "value": "129 Countries", "sub": "World leader in international destinations"},
                    {"label": "Middle Corridor Transit", "value": "12–15 Days", "sub": "Rail transit China to Europe"}
                ]
            },
            {
                "type": "timeline",
                "id": "trans-milestones-timeline",
                "title": "Milestones in Modern Turkish Infrastructure & Logistics",
                "items": [
                    {"year": "1973", "event": "First Bosphorus Bridge (15 July Martyrs Bridge) opens, connecting Europe and Asia by road."},
                    {"year": "1988", "event": "Second Bosphorus Bridge (Fatih Sultan Mehmet Bridge) opens for international transit."},
                    {"year": "2009", "event": "Turkey's first High-Speed Rail (YHT) begins service between Ankara and Eskişehir."},
                    {"year": "2013", "event": "Marmaray subsea commuter rail tunnel opens beneath the Bosphorus."},
                    {"year": "2016", "event": "Yavuz Sultan Selim Bridge, Osmangazi Bridge, and Eurasia Tunnel open in rapid succession."},
                    {"year": "2017", "event": "Baku–Tbilisi–Kars (BTK) railway inaugurated, anchoring the Middle Corridor."},
                    {"year": "2018", "event": "Istanbul Airport (IGA) commences commercial flight operations."},
                    {"year": "2022", "event": "1915 Çanakkale Bridge inaugurated as the world's longest suspension bridge."}
                ]
            }
        ]
    }

def get_mod10():
    return {
        "id": "energy",
        "number": "10",
        "title": "Energy Resources, Consumption & Regulation",
        "tagline": "Natural gas pipelines, Sakarya field discoveries, Akkuyu Nuclear, renewables, and EPDK governance.",
        "icon": "zap",
        "readingTime": "28 min read",
        "summary": "An exhaustive, empirical assessment of Turkey's energy architecture: primary energy balance, high hydrocarbon import dependency (~70%), international pipeline diplomacy (TANAP, TurkStream, Blue Stream, BTC), the Sakarya offshore deepwater gas field, the Akkuyu Nuclear Power Plant (Rosatom BOO model), renewable electricity expansion (hydro, wind, solar, geothermal), and market regulation by the EPDK.",
        "sections": [
            {
                "id": "energy-balance-hydrocarbons",
                "title": "1. Primary Energy Balance & Hydrocarbon Import Vulnerability",
                "content": """Turkey is an energy-intensive industrial economy with scarce domestic fossil fuel deposits, importing over **70% of its total primary energy supply (TPES)**:
- **Natural Gas Dependence:** Turkey consumes roughly **50 to 55 billion cubic meters (bcm)** of natural gas annually, utilized for residential heating (30%), electricity generation (25–30%), and industrial manufacturing. Over 98% of natural gas is imported:
  - *Russia:* Primary supplier via the **Blue Stream** and **TurkStream** pipelines (~40% of supply).
  - *Azerbaijan:* Supplies ~20% of gas through the **TANAP** and South Caucasus Pipeline.
  - *Iran:* Transmits roughly 15% via the Tabriz–Ankara pipeline.
  - *LNG Shipments:* Sourced from Algeria, Qatar, the United States, and spot markets through four floating storage and regasification units (FSRU) and two onshore LNG terminals (Marmara Ereğlisi and Aliağa).
- **Petroleum & Oil Imports:** Consumes approximately 45–50 million tons of crude oil and petroleum products annually, imported primarily from Russia, Iraq (Kirkuk–Ceyhan pipeline), and Kazakhstan, processed at the Tüpraş refineries (İzmit, İzmir, Kırıkkale, Batman) and the SOCAR STAR refinery in Aliağa [IEA-TUR-2023, EPDK-2024-NRG]."""
            },
            {
                "id": "energy-sakarya-upstream",
                "title": "2. Upstream Discoveries: The Sakarya Deepwater Gas Field",
                "content": """In August 2020, Turkey's state drilling vessel *Fatih* discovered the **Sakarya Gas Field** in the Tuna-1 well, located 170 kilometers off the Black Sea coast of Zonguldak:
- **Reserves & Production Scale:** Estimated at over **710 billion cubic meters (bcm)** of natural gas, representing Turkey's largest-ever hydrocarbon breakthrough.
- **Subsea Production Infrastructure:** Subsea production facilities were constructed at water depths exceeding 2,100 meters, connected via a 170-km subsea pipeline to the newly constructed **Filyos Natural Gas Processing Facility**.
- **Domestic Gas Connection:** First gas was connected to the national grid in April 2023. Phase 1 delivers approximately 10 million cubic meters per day, projected to ramp up in Phase 2 to 40 million m³/day, meeting roughly 20–25% of Turkey's residential gas requirements [EPDK-2024-NRG]."""
            },
            {
                "id": "energy-pipelines-transit",
                "title": "3. Strategic Transit Pipelines & Eurasian Gas Hub Diplomacy",
                "content": """Turkey leverages its geography to serve as an indispensable Eurasian energy transit conduit:
- **Trans-Anatolian Natural Gas Pipeline (TANAP):** The 1,850-kilometer central spine of the EU-backed Southern Gas Corridor, transporting 16 bcm/year of Shah Deniz gas from Azerbaijan across Turkey to the Trans Adriatic Pipeline (TAP) at the Greek border, with 6 bcm allocated to Turkey and 10 bcm to Southern Europe.
- **TurkStream Subsea Pipeline:** Runs 930 km across the Black Sea seabed from Anapa (Russia) to Kıyıköy (Thrace), featuring two strings of 15.75 bcm capacity each: String 1 supplies the Turkish domestic market, while String 2 supplies Bulgaria, Serbia, and Hungary.
- **Baku–Tbilisi–Ceyhan (BTC) Crude Oil Pipeline:** Transports up to 1 million barrels per day of Caspian crude oil over 1,768 km to the marine terminal at Ceyhan on the Mediterranean coast, supplying global tanker trade.
- **Kirkuk–Ceyhan Crude Oil Pipeline:** Twin pipelines with 1.4 million bpd capacity linking Iraqi oil fields to Ceyhan [IEA-TUR-2023]."""
            },
            {
                "id": "energy-nuclear-akkuyu",
                "title": "4. Nuclear Power: The Akkuyu Nuclear Power Plant",
                "content": """In 2010, the Turkish and Russian governments concluded an intergovernmental agreement for the construction of Turkey's first nuclear power station, the **Akkuyu Nuclear Power Plant (Akkuyu NPP)** in Gülnar, Mersin:
- **Build-Own-Operate (BOO) Model:** Constructed and operated by Russian state nuclear corporation **Rosatom**, marking the world's first nuclear project executed on a commercial BOO framework.
- **Technical Specifications:** Features **four VVER-1200 Generation III+ pressurized water reactors**, delivering a total installed electrical capacity of **4,800 Megawatts (MW)**.
- **Energy Contribution:** Designed to operate for 60 to 80 years, Akkuyu will generate roughly 35 billion kilowatt-hours annually upon full commissioning, meeting approximately **10% of Turkey's total national electricity demand**, mitigating carbon emissions by 35 million tons annually [IEA-TUR-2023]."""
            },
            {
                "id": "energy-renewables-epdk",
                "title": "5. Renewable Surge & Market Governance (EPDK, BOTAŞ, EÜAŞ)",
                "content": """Turkey has enacted a rapid green energy diversification, with total installed power capacity surpassing **107,000 MW**, over **54% of which derives from renewable energy**:
- **Hydroelectric Power:** Over 32,200 MW installed, anchored by the massive rockfill Atatürk Dam, Karakaya Dam, Keban Dam, and Ilısu Dam on the Euphrates and Tigris rivers.
- **Wind & Solar PV Expansion:** Supported by Renewable Energy Resource Zones (YEKA) competitive reverse auctions:
  - *Wind Power:* Over 12,100 MW installed across the Aegean and Marmara wind corridors.
  - *Solar PV:* Over 14,500 MW, expanding rapidly via commercial rooftop and utility-scale installations.
- **Geothermal Leadership:** Turkey ranks **4th globally in installed geothermal power capacity (~1,700 MW)**, concentrated in the high-temperature grabens of the Aegean region (Aydın, Denizli, Manisa).
- **Statutory Regulatory Architecture:**
  - **Energy Market Regulatory Authority (*EPDK*):** Independent statutory regulator issuing generation, transmission, distribution, and wholesale licenses, determining regulated network tariffs.
  - **BOTAŞ (Petroleum Pipeline Corporation):** State enterprise controlling gas imports, gas transmission networks, and underground gas storage facilities (Silivri and Lake Tuz).
  - **TEİAŞ & EÜAŞ:** TEİAŞ manages transmission lines, fully synchronized with the European Continental Network (ENTSO-E); EÜAŞ is the state generation company operating public dams and thermal plants [EPDK-2024-NRG]."""
            }
        ],
        "infographics": [
            {
                "type": "comparison-table",
                "id": "energy-pipelines-matrix",
                "title": "Major Strategic Hydrocarbon Pipelines Crossing Turkey",
                "headers": ["Pipeline Name", "Commodity", "Capacity", "Origin & Route", "Transit & Market Destination"],
                "rows": [
                    ["TANAP", "Natural Gas", "16 bcm / year (exp. 31 bcm)", "Azerbaijan (Shah Deniz) across Turkey", "6 bcm Turkey / 10 bcm Southern Europe (TAP)"],
                    ["TurkStream", "Natural Gas", "31.5 bcm / year (2 strings)", "Russia across Black Sea to Thrace", "String 1: Turkey / String 2: Balkans & Hungary"],
                    ["Blue Stream", "Natural Gas", "16 bcm / year", "Russia across Black Sea to Samsun", "Turkish domestic market (Ankara hub)"],
                    ["BTC Pipeline", "Crude Oil", "1.0–1.2M barrels / day", "Baku (Azerbaijan) -> Tbilisi -> Ceyhan", "Mediterranean deepwater global tanker export"],
                    ["Kirkuk–Ceyhan", "Crude Oil", "1.4M barrels / day", "Kirkuk (Iraq) to Ceyhan", "Mediterranean tanker export"],
                    ["Tabriz–Ankara", "Natural Gas", "10 bcm / year", "Iran (Tabriz) to Ankara", "Turkish domestic natural gas grid"]
                ]
            },
            {
                "type": "stat-grid",
                "id": "energy-stats-grid",
                "title": "National Energy Balance & Renewable Benchmarks (2024)",
                "data": [
                    {"label": "Installed Power Capacity", "value": "107,000+ MW", "sub": "54% renewable generation share"},
                    {"label": "Hydroelectric Capacity", "value": "32,200 MW", "sub": "Atatürk, Keban, Ilısu mega-dams"},
                    {"label": "Sakarya Gas Reserves", "value": "710 bcm Reserve", "sub": "Deepwater Black Sea discovery"},
                    {"label": "Akkuyu Nuclear Capacity", "value": "4,800 MW", "sub": "4x VVER-1200 under Rosatom BOO"},
                    {"label": "Global Geothermal Rank", "value": "4th in the World", "sub": "~1,700 MW installed capacity"},
                    {"label": "Energy Import Dependency", "value": "~71% of TPES", "sub": "Focus of national self-reliance policy"}
                ]
            },
            {
                "type": "timeline",
                "id": "energy-milestones-timeline",
                "title": "Chronology of Energy Megaprojects & Strategic Breakthroughs",
                "items": [
                    {"year": "1992", "event": "Atatürk Dam (2,400 MW) commences hydroelectric generation on the Euphrates."},
                    {"year": "2001", "event": "EPDK established under Electricity Market Law No. 4628, liberalizing the sector."},
                    {"year": "2003", "event": "Blue Stream subsea natural gas pipeline from Russia begins commercial transit."},
                    {"year": "2006", "event": "Baku–Tbilisi–Ceyhan (BTC) crude oil pipeline opens to Mediterranean shipping."},
                    {"year": "2010", "event": "Turkey and Russia sign intergovernmental agreement for Akkuyu Nuclear Power Plant."},
                    {"year": "2018", "event": "Trans-Anatolian Natural Gas Pipeline (TANAP) inaugurated in Eskişehir."},
                    {"year": "2020", "event": "TurkStream inaugurated; Sakarya deepwater gas field discovered in the Black Sea."},
                    {"year": "2023", "event": "First Sakarya Black Sea gas connected to Filyos processing grid; Akkuyu receives nuclear fuel."}
                ]
            }
        ]
    }

def get_mod11():
    return {
        "id": "economy",
        "number": "11",
        "title": "National Economy & Regulatory Institutions",
        "tagline": "Macroeconomic architecture, manufacturing prowess, competition authorities, and business conglomerates.",
        "icon": "trending-up",
        "readingTime": "29 min read",
        "summary": "An exhaustive empirical assessment of the Turkish economy: $1.1+ Trillion nominal GDP, sectoral composition (services, manufacturing powerhouse, agriculture), international export architecture ($255B+ exports), the 1995 EU-Turkey Customs Union, macroeconomic stabilization dynamics, regulatory authorities (Competition Authority, Public Procurement Authority, Treasury), and leading diversified conglomerates (Koç, Sabancı) and business confederations (TOBB, TÜSİAD, MÜSİAD, TİM).",
        "sections": [
            {
                "id": "econ-macro-trajectory",
                "title": "1. Macroeconomic Structure, GDP Growth & Sectoral Balance",
                "content": """The Republic of Turkey has an upper-middle-income emerging market economy with a nominal **Gross Domestic Product (GDP) exceeding $1.1 trillion** (ranking 17th–18th globally, and within the top 11 worldwide in Purchasing Power Parity / PPP terms):
- **Sectoral Distribution of GDP:**
  - **Services Sector (~55%):** Anchored by telecommunications, banking, wholesale and retail logistics, and a world-class **tourism industry** welcoming over 56 million international tourists annually (generating over $54 billion in foreign currency receipts).
  - **Industry & Manufacturing (~28%):** Sophisticated mid-tech and heavy manufacturing export base, serving as the industrial assembly hub for Western Europe.
  - **Agriculture & Agribusiness (~6–7%):** Employs roughly 15% of the national labor force; Turkey is the world's leading exporter of hazelnuts (70% of global supply), dried apricots, figs, raisins, and cherries, and a major producer of wheat, cotton, and citrus fruits.
- **Macroeconomic Volatility & Stabilization:** After years of rapid domestic demand-driven credit growth and high inflation, the economic administration implemented a Medium-Term Program (OVP) centered on fiscal consolidation, real interest rate anchoring, and foreign trade deficit compression [WB-TUR-2024]."""
            },
            {
                "id": "econ-manufacturing-export",
                "title": "2. Manufacturing Competitiveness & Export Structure",
                "content": """Turkey is the industrial workshop of the Eastern Mediterranean, generating merchandise exports exceeding **$255 billion annually**:
- **Automotive Powerhouse:** Turkey is the 4th largest automotive manufacturer in Europe, assembling over 1.4 million commercial vehicles and passenger cars annually (Ford Otosan, Oyak Renault, Tofaş/Fiat, Toyota, Hyundai Assan), alongside the indigenous electric vehicle brand **Togg (Türkiye'nin Otomobili Girişim Grubu)**. Automotive goods constitute Turkey's single largest export sector, exceeding $35 billion annually.
- **Machinery, Steel & Defense:** Leading European crude steel producer, exporting machinery, electrical machinery, and precision industrial systems.
- **Consumer Electronics & White Goods:** Turkey produces roughly 25% of all major home appliances sold in Europe through industry champions **Arçelik (Beko, Grundig)** and **Vestel**.
- **Textiles, Apparel & Chemicals:** 5th largest global textile and ready-to-wear apparel exporter, closely integrated into fast-fashion supply chains.
- **The EU-Turkey Customs Union (1995):** Governs industrial trade between Turkey and the European Union, abolishing customs duties and quotas on industrial products while applying a Common External Tariff (CET) to third-country imports. Over 41% of Turkish exports go directly to the EU, with Germany serving as the largest bilateral trading partner [WB-TUR-2024]."""
            },
            {
                "id": "econ-regulatory-watchdogs",
                "title": "3. State Regulatory Architecture: Rekabet Kurumu, KİK & Treasury",
                "content": """Market integrity and fair competition are governed by specialized autonomous statutory authorities:
- **Competition Authority (*Rekabet Kurumu*):** Enforces Law No. 4054 on the Protection of Competition, investigating anti-competitive cartels, preventing abuse of market dominance, and vetting domestic and cross-border mergers and acquisitions across digital platforms, retail, banking, and telecom.
- **Public Procurement Authority (*Kamu İhale Kurumu - KİK*):** Oversees the transparency, competitive bidding, and integrity of public tenders and contracts under Public Procurement Law No. 4734, managing digital procurement via the EKAP platform.
- **Ministry of Treasury and Finance (*Hazine ve Maliye Bakanlığı*):** Coordinates sovereign debt management, fiscal policy, tax administration (*Gelir İdaresi Başkanlığı - GİB*), and sovereign bond auctions.
- **Strategy and Budget Directorate (*SBB*):** Directs the preparation of the Central Government Budget and multi-year Macroeconomic Medium-Term Programs (OVP) [WB-TUR-2024]."""
            },
            {
                "id": "econ-conglomerates-confederations",
                "title": "4. Major Holding Conglomerates & Business Confederations",
                "content": """The private sector is structured around multi-industry family-owned holding conglomerates and influential business associations:
- **Leading Industrial Conglomerates:**
  - **Koç Holding:** Turkey's largest industrial conglomerate, contributing over 8% of national exports and ~7% of GDP through subsidiaries in automotive (Ford Otosan, Tofaş), energy (Tüpraş oil refinery, Aygaz), finance (Yapı Kredi), and white goods (Arçelik).
  - **Sabancı Holding:** Prominent industrial and financial conglomerate active in banking (Akbank), energy generation/distribution (Enerjisa), composites/tires (Kordsa, Brisa), and building materials (Çimsa).
  - **Other Key Groups:** Eczacıbaşı (pharmaceuticals, ceramics), Anadolu Group (beverages, automotive), Yıldız Holding (pladis, global confectionery), Cengiz, Kalyon, and Limak (infrastructure and energy).
- **Business Interest Confederations:**
  - **TOBB (Union of Chambers and Commodity Exchanges of Turkey):** The umbrella legal body for 365 local commercial chambers and 1.5 million registered enterprises.
  - **TÜSİAD (Turkish Industry and Business Association):** Represents secular, export-oriented large-scale industrial and financial corporate groups.
  - **MÜSİAD (Independent Industrialists' and Businessmen's Association):** Represents conservative, Anatolian-based small and medium-sized enterprises ('Anatolian Tigers').
  - **TİM (Turkish Exporters Assembly):** The single coordinating body for all 27 export vertical associations [WB-TUR-2024]."""
            }
        ],
        "infographics": [
            {
                "type": "comparison-table",
                "id": "econ-top-sectors-matrix",
                "title": "Leading Export Sectors & Key Export Champions of Turkey",
                "headers": ["Industrial Sector", "Annual Export Volume", "Key Corporate Producers", "Primary Foreign Destination Markets", "Competitive Advantage"],
                "rows": [
                    ["Automotive & Components", "$35B+ / year", "Ford Otosan, Renault, Tofaş, Toyota, Togg", "Germany, France, UK, Italy, Spain", "Proximity, zero-tariff EU Customs Union, skilled labor"],
                    ["Chemicals & Refining", "$30B+ / year", "Tüpraş, Petkim, SASA, Aksa Akrilik", "Netherlands, Italy, Germany, USA", "Refinery scale, petrochemical plastics integration"],
                    ["Apparel & Ready-to-Wear", "$20B+ / year", "LC Waikiki, DeFacto, Koton, Yeşim Tekstil", "Germany, Spain, UK, France", "Rapid supply turnaround, design, European standards"],
                    ["Steel & Metallurgy", "$16B+ / year", "Erdemir, İsdemir, İçdaş, Çolakoğlu", "USA, Romania, Italy, Israel, Egypt", "Electric arc furnace agility, infrastructure capacity"],
                    ["Electrical & Electronics", "$16B+ / year", "Arçelik (Beko), Vestel, Karel", "UK, Germany, France, Poland", "25% of European major appliances market share"],
                    ["Machinery & Aerospace", "$12B+ / year", "TUSAŞ, Aselsan, Baykar, Hidromek", "USA, Germany, Azerbaijan, Gulf States", "Advanced CNC machining, combat drone export leader"]
                ]
            },
            {
                "type": "stat-grid",
                "id": "econ-stats-grid",
                "title": "Macroeconomic Benchmarks & Trade Performance Indicators",
                "data": [
                    {"label": "Nominal GDP", "value": "$1.1+ Trillion", "sub": "Top 18 global economy"},
                    {"label": "Merchandise Exports", "value": "$255B+ / year", "sub": "Historic export high watermark"},
                    {"label": "Tourism Receipts", "value": "$54B+ / year", "sub": "56M+ international tourist arrivals"},
                    {"label": "Customs Union Partner", "value": "European Union", "sub": "41%+ of total Turkish exports"},
                    {"label": "Automotive Production", "value": "1.4M+ Vehicles/yr", "sub": "4th largest producer in Europe"},
                    {"label": "Hazelnut Global Share", "value": "~70% Global Total", "sub": "World's undisputed export leader"}
                ]
            },
            {
                "type": "timeline",
                "id": "econ-milestones-timeline",
                "title": "Key Transformations in Modern Turkish Economic Policy",
                "items": [
                    {"year": "1923", "event": "İzmir Economic Congress establishes principles of national economic sovereignty."},
                    {"year": "1934", "event": "First Five-Year Industrial Plan launched with Soviet credit and technical assistance."},
                    {"year": "1980", "event": "January 24 Decisions open Turkey to export-oriented neoliberal liberalization under Turgut Özal."},
                    {"year": "1995", "event": "EU-Turkey Customs Union signed, integrating industrial trade with Europe."},
                    {"year": "2001", "event": "Severe financial crisis prompts Derviş reforms: independent Central Bank and BDDK created."},
                    {"year": "2005", "event": "Currency reform: Six zeros removed from the Turkish Lira; New Turkish Lira (YTL) introduced."},
                    {"year": "2016", "event": "Turkey Wealth Fund (TVF) established as sovereign asset portfolio manager."},
                    {"year": "2023", "event": "Medium-Term Program (OVP) re-anchors economic policy toward orthodox monetary stabilization."}
                ]
            }
        ]
    }

def get_mod12():
    return {
        "id": "financial_system",
        "number": "12",
        "title": "Financial System & Banking Architecture",
        "tagline": "The Central Bank (TCMB), BDDK, SPK, state banks, participation banking, and Borsa Istanbul.",
        "icon": "coins",
        "readingTime": "29 min read",
        "summary": "An analytical, regulatory breakdown of Turkey's financial sector: the statutory mandate and monetary transmission of the Central Bank of the Republic of Turkey (TCMB), regulatory authorities (BDDK, SPK, TMSF), public commercial banks (Ziraat, Halk, Vakıf), private commercial banks (İş Bankası, Garanti BBVA, Akbank), participation (Islamic) banking, Borsa Istanbul (BIST), and sovereign asset management under the Turkey Wealth Fund (TVF).",
        "sections": [
            {
                "id": "fin-tcmb-monetary-policy",
                "title": "1. The Central Bank of the Republic of Turkey (TCMB)",
                "content": """The **Central Bank of the Republic of Turkey (*Türkiye Cumhuriyet Merkez Bankası - TCMB*)**, established on June 11, 1930, is the statutory monetary authority tasked with maintaining price stability and financial stability:
- **Monetary Policy Governance:** The **Monetary Policy Committee (*Para Politikası Kurulu - PPK*)** convenes monthly to determine the one-week repo auction rate (the benchmark policy rate), the overnight interest rate corridor (lending and borrowing rates), and required reserve ratios (*zorunlu karşılıklar*):
  - *Orthodox vs. Heterodox Policy Cycles:* Between 2021 and early 2023, the TCMB pursued an experimental policy of lowering nominal interest rates despite high inflation, which exacerbated exchange rate depreciation and inflation. In mid-2023, the TCMB pivoted back to orthodox inflation targeting, aggressively increasing the policy rate to anchor market expectations, contract domestic credit growth, and rebuild international foreign exchange reserves.
- **Foreign Exchange Reserves Management:** The TCMB manages official gross international reserves (foreign exchange and monetary gold), reporting weekly on gross reserves, net reserves, and commercial bank FX swap positions [TCMB-ANN-2024]."""
            },
            {
                "id": "fin-regulatory-watchdogs",
                "title": "2. Regulatory Watchdogs: BDDK, SPK & TMSF",
                "content": """Following the devastating 2001 banking collapse (which resulted in the failure of over 20 commercial lenders), Turkey instituted one of the most resilient banking supervisory frameworks in the emerging markets:
- **Banking Regulation and Supervision Agency (*BDDK*):** Independent statutory regulatory authority established in 2000. It licenses and supervises banks, leasing, factoring, and consumer finance companies. It enforces strict **Basel III capital adequacy standards**, requiring banks to maintain a minimum Capital Adequacy Ratio (CAR), with the Turkish banking sector consistently exceeding 16–18% (well above the international 8% Basel minimum).
- **Capital Markets Board (*SPK*):** Regulates capital markets, public equity offerings (IPOs), mutual funds, brokerage houses, asset management firms, and listed company disclosure obligations under Capital Market Law No. 6362.
- **Savings Deposit Insurance Fund (*TMSF*):** Public fund insuring household savings deposits up to a statutory ceiling per depositor per bank, with powers to resolve distressed banks or take over non-compliant financial assets [BDDK-2024-MONTH]."""
            },
            {
                "id": "fin-banking-sectors",
                "title": "3. Commercial, State & Participation (Islamic) Banking",
                "content": """The Turkish banking system holds total assets exceeding **$850 billion**, divided into three distinct institutional segments:
- **State-Owned Commercial Lenders:** Play an essential counter-cyclical credit role, directing financing to agriculture, SMEs, public infrastructure, and housing:
  - **Ziraat Bankası:** Founded in 1863; Turkey's oldest and largest bank by assets, branch network, and corporate/agricultural lending.
  - **Halkbank:** Established in 1938 to provide credit to tradesmen, artisans, and small-to-medium manufacturing enterprises.
  - **VakıfBank:** Established in 1954 to manage Ottoman pious foundation assets and commercial banking.
- **Private Domestic & Foreign Commercial Banks:** Highly technologically sophisticated, pioneer leaders in digital mobile banking:
  - **Türkiye İş Bankası:** Founded in 1924 by Atatürk as the first national private commercial bank.
  - **Garanti BBVA:** Majority-owned by Spanish banking giant BBVA; leader in consumer credit and digital platforms.
  - **Akbank & Yapı Kredi:** Anchored by the Sabancı and Koç conglomerates respectively.
  - **Foreign-Controlled Banks:** QNB Finansbank (Qatar), TEB (BNP Paribas), DenizBank (Emirates NBD).
- **Participation (Islamic) Banks (*Katılım Bankacılığı*):** Operate in accordance with non-interest Islamic finance principles (profit-and-loss sharing / *Mudharabah*, cost-plus financing / *Murabaha*, and lease-backed sukuk bonds). Anchored by **Kuveyt Türk**, **Albaraka Türk**, **Türkiye Finans**, alongside state-owned lenders **Ziraat Katılım**, **Vakıf Katılım**, and **Emlak Katılım**, accounting for roughly 8–10% of total banking assets [BDDK-2024-MONTH]."""
            },
            {
                "id": "fin-bist-wealth-fund",
                "title": "4. Capital Markets: Borsa Istanbul (BIST) & the Turkey Wealth Fund (TVF)",
                "content": """Turkey's capital market architecture provides deep corporate financing and strategic sovereign wealth investment:
- **Borsa Istanbul (BIST):** Established in 2013 through the merger of the Istanbul Stock Exchange (İMKB, founded 1873) and the Turkish Derivatives Exchange (VOB). It operates four integrated electronic markets:
  - *Equity Market:* Anchored by the benchmark **BIST 100** and **BIST 30** market-capitalization indices.
  - *Debt Securities Market:* Trading sovereign treasury bonds, corporate eurobonds, and repo instruments.
  - *Derivatives Market (VİOP):* Index futures, currency futures, and commodity contracts.
  - *Precious Metals & Diamond Market:* Gold and silver spot trading.
- **Turkey Wealth Fund (*Türkiye Varlık Fonu - TVF*):** Established in 2016 as the sovereign wealth fund of Turkey. Chaired by the President of the Republic, TVF manages strategic state equity holdings across key assets:
  - Controlling stakes in **Turkish Airlines (THY)**, **BOTAŞ**, **Turkcell**, **Türk Telekom**, **Borsa Istanbul**, and public commercial banks (Ziraat, Halk, Vakıf), as well as anchor investments in the Istanbul Financial Center (İFM) and mining assets."""
            }
        ],
        "infographics": [
            {
                "type": "comparison-table",
                "id": "fin-institutions-matrix",
                "title": "Institutional Map of the Turkish Financial & Banking Sector",
                "headers": ["Entity", "Institutional Category", "Year Founded", "Core Statutory Mandate", "Supervisory Authority"],
                "rows": [
                    ["TCMB (Central Bank)", "Monetary Authority", "1930", "Price stability, monetary policy, policy rate corridor, FX reserves", "Independent Statutory Charter"],
                    ["BDDK", "Banking Regulator", "2000", "Banking supervision, capital adequacy (Basel III), credit licensing", "Independent Statutory Body"],
                    ["SPK", "Capital Markets Board", "1981", "Securities regulation, IPO approval, investor protection, listed firms", "Independent Statutory Body"],
                    ["TMSF", "Deposit Guarantee Fund", "1983", "Deposit insurance, distressed asset resolution, receivership", "Independent Statutory Body"],
                    ["Ziraat Bankası", "State Commercial Bank", "1863", "Largest bank by assets; agricultural, corporate, SME credit", "Supervised by BDDK"],
                    ["Türkiye İş Bankası", "Private Commercial Bank", "1924", "Largest private bank; universal commercial & digital banking", "Supervised by BDDK"],
                    ["Kuveyt Türk", "Participation Bank", "1989", "Largest interest-free participation bank (Islamic principles)", "Supervised by BDDK / TKBB"],
                    ["Borsa Istanbul (BIST)", "Financial Exchange", "1873/2013", "Sole securities, debt, derivatives, and precious metals exchange", "Regulated by SPK"],
                    ["Turkey Wealth Fund (TVF)", "Sovereign Wealth Fund", "2016", "Strategic asset portfolio management (THY, BOTAŞ, Turkcell, banks)", "Presidency of the Republic"]
                ]
            },
            {
                "type": "stat-grid",
                "id": "fin-stats-grid",
                "title": "Financial Sector Benchmarks & Capital Ratios (2024)",
                "data": [
                    {"label": "Total Banking Assets", "value": "$850B+ USD", "sub": "Largest sector in financial system"},
                    {"label": "Capital Adequacy (CAR)", "value": ">17% Ratio", "sub": "Significantly above 8% Basel minimum"},
                    {"label": "Participation Banking", "value": "~9% Asset Share", "sub": "Interest-free Islamic financing lenders"},
                    {"label": "BIST Registered Investors", "value": "7.5M+ Accounts", "sub": "Surge in retail investor IPO demand"},
                    {"label": "Public Banks Asset Share", "value": "~35% of Total", "sub": "Ziraat, Halkbank, VakıfBank network"},
                    {"label": "TCMB Policy Instrument", "value": "1-Week Repo Rate", "sub": "Set by Monetary Policy Committee (PPK)"}
                ]
            },
            {
                "type": "timeline",
                "id": "fin-milestones-timeline",
                "title": "Chronology of Modern Financial & Banking Developments in Turkey",
                "items": [
                    {"year": "1863", "event": "Memleket Sandıkları founded in Pirot by Midhat Pasha, precursor to Ziraat Bankası."},
                    {"year": "1924", "event": "Türkiye İş Bankası established by Mustafa Kemal Atatürk as first national bank."},
                    {"year": "1930", "event": "Central Bank of the Republic of Turkey (TCMB) established by Law No. 1715."},
                    {"year": "1985", "event": "Special Finance Houses (precursors to Participation Banks) legally authorized."},
                    {"year": "1986", "event": "Istanbul Stock Exchange (İMKB) opens for secondary equity trading in Cağaloğlu."},
                    {"year": "2000", "event": "Banking Regulation and Supervision Agency (BDDK) commences operations."},
                    {"year": "2001", "event": "Banking crisis; Derviş reform program enacts strict capital adequacy and Central Bank independence."},
                    {"year": "2016", "event": "Turkey Wealth Fund (TVF) established; Istanbul Financial Center (İFM) constructed."}
                ]
            }
        ]
    }

def get_mod13():
    return {
        "id": "religion",
        "number": "13",
        "title": "Religion & Religious Institutions",
        "tagline": "Secularism (Laiklik), the Diyanet, Sunni traditions, Alevism, Sufi orders, and non-Muslim communities.",
        "icon": "heart-handshake",
        "readingTime": "28 min read",
        "summary": "An analytical, sociological, and constitutional investigation of religion in Turkey: the distinct institutional model of secularism (Laiklik), the massive state apparatus of the Presidency of Religious Affairs (Diyanet), Sunni Hanafi and Shafi'i traditions, the Alevi-Bektashi community (Cemevi recognition and the 2022 Directorate), traditional Sufi orders (tarikats and cemaats), and historic non-Muslim confessions.",
        "sections": [
            {
                "id": "rel-laiklik-doctrine",
                "title": "1. The Constitutional Doctrine of Secularism (*Laiklik*)",
                "content": """Secularism in Turkey (*Laiklik*) does not correspond to Anglo-American passive secularism (the strict non-interventionist separation of church and state); rather, heavily influenced by French *laïcité*, it constitutes **active state supervision, institutional regulation, and public monopolization of the religious sphere**:
- **Constitutional Status:** Enshrined in Article 2 of the 1982 Constitution as an entrenched, unamendable characteristic of the Republic. Under Article 24, freedom of conscience, religious faith, and worship is protected, but religious principles cannot be invoked to dictate or alter the fundamental legal, political, economic, or judicial order of the state.
- **Historical Secularization Trajectory:**
  - *1922:* Abolition of the Sultanate.
  - *March 3, 1924:* Abolition of the Ottoman Caliphate (Law No. 431) and unification of educational curricula under secular state control (Law No. 430, *Tevhid-i Tedrisat*).
  - *1925:* Closure of dervish lodges, shrines, and Sufi orders (Law No. 677).
  - *1926:* Swiss Civil Code adopted, terminating Islamic Sharia family and inheritance law.
  - *1928:* Deletion of the clause 'The religion of the State of Turkey is Islam' from Article 2 of the 1924 Constitution.
  - *1937:* Formal entrenchment of *Lâiklik* into the constitutional text [TBMM-CONST-1982, ZURCHER-2017]."""
            },
            {
                "id": "rel-diyanet-apparatus",
                "title": "2. The Presidency of Religious Affairs (*Diyanet İşleri Başkanlığı*)",
                "content": """Established on March 3, 1924 by Law No. 429 under Mustafa Kemal Atatürk, the **Presidency of Religious Affairs (*Diyanet İşleri Başkanlığı*)** replaced the Ottoman Ministry of Religious Affairs and Pious Foundations (*Şer'iye ve Evkaf Vekâleti*):
- **Institutional Scale & Bureaucratic Reach:** An autonomous agency answering directly to the President of the Republic, employing over **140,000 civil servants** (including imams, muezzins, preachers, muftis, and Quran instructors) with a multi-billion dollar state budget exceeding several line ministries.
- **Statutory Competence:** Administers public religious services across more than **90,000 mosques nationwide**, operates hundreds of cultural and religious centers abroad (notably through DİTİB in Germany and Western Europe), authoritatively writes and disseminates unified Friday sermons (*hutbe*), issues legal-religious opinions (*fetva* via the High Board of Religious Affairs / *Din İşleri Yüksek Kurulu*), organizes the annual Hajj and Umrah pilgrimages, and oversees thousands of Quran educational centers [DCP-DIYANET-2024]."""
            },
            {
                "id": "rel-sunni-denominations",
                "title": "3. Islamic Demographics: Sunni Hanafi & Shafi'i Traditions",
                "content": """Over 90% of Turkish citizens identify culturally or religiously with Islam, predominantly adherents of the Sunni tradition:
- **Hanafi Jurisprudence (*Hanefîlik*):** The predominant legal-theological school (*mezhep*), encompassing approximately 70–75% of Muslims in Turkey. Hanafi jurisprudence was the official legal doctrine of the Ottoman Empire, characterized by its reliance on rational deduction (*qiyas*) and juristic discretion (*istihsan*). Prevalent among Turkish-speaking populations across Thrace, Central, Western, and Northern Anatolia.
- **Shafi'i Jurisprudence (*Şâfiîlik*):** Represents approximately 10–12% of the Muslim population, concentrated almost exclusively among Kurdish-speaking communities in Eastern and Southeastern Anatolia (Diyarbakır, Van, Mardin, Siirt, Batman, Bitlis), following the legal methodology of Imam al-Shafi'i [ZURCHER-2017]."""
            },
            {
                "id": "rel-alevi-bektashi-culture",
                "title": "4. The Alevi-Bektashi Tradition & Cemevi Legal Recognition",
                "content": """The **Alevi-Bektashi community** constitutes Turkey's second-largest religious and cultural collective, estimated at **10–15% of the national population** (roughly 8 to 12 million individuals):
- **Theological & Mystical Pillars:** Deeply rooted in Anatolian Sufism, revering the Prophet Muhammad, Imam Ali, the Twelve Imams, and 13th-century saint **Hacı Bektaş Veli**. Ethical philosophy is centered on the principle of *"Control your hand, your tongue, your loins"* (*Eline, diline, beline sahip ol*).
- **Ritual Worship in the Cemevi:** Unlike Sunni mosque-centered worship, Alevis congregate in assembly halls called **Cemevi** to execute the sacred **Cem** ritual, featuring liturgical poetry (*deyiş*) accompanied by the seven-stringed lute (*bağlama/saz*) and the mixed-gender sacred ritual dance (**Semah**).
- **Legal Status & the 2022 Directorate:** Historically unacknowledged by the state as formal places of worship, European Court of Human Rights rulings (such as *Cumhuriyetçi Eğitim ve Kültür Merkezi Vakfı v. Turkey*) mandated non-discriminatory status for Cemevis. In November 2022, the government established the **Alevi-Bektashi Cultural and Cemevi Directorate (*Alevi-Bektaşi Kültür ve Cemevi Başkanlığı*)** under the Ministry of Culture and Tourism, providing state financing for Cemevi utility expenses and maintenance."""
            },
            {
                "id": "rel-tarikats-and-minorities",
                "title": "5. Sufi Brotherhoods (*Tarikatlar*) & Historic Non-Muslim Confessions",
                "content": """The religious landscape encompasses traditional brotherhoods alongside historic non-Muslim confessions:
- **Sufi Orders (*Tarikatlar*) & Religious Communities (*Cemaatler*):** Formally prohibited by Law No. 677 in 1925, traditional Sufi brotherhoods persisted sociologically as charitable foundations, educational trusts, and business networks:
  - *Naqshbandi (*Nakşibendi*):* The most influential Sufi order, with historical offshoots including the İskenderpaşa, İsmailağa, and Menzil communities.
  - *Nur Movement:* Originating from the theological writings (*Risale-i Nur*) of Kurdish scholar Bediüzzaman Said Nursi (1877–1960), emphasizing Quranic defense against scientific materialism.
  - *Qadiri (*Kadiri*) & Mevlevi:* Orders rooted in the spiritual legacy of Abdul Qadir Gilani and Mevlana Rumi.
- **Historic Non-Muslim Religious Confessions:**
  - **Ecumenical Patriarchate of Constantinople (Fener):** The historical spiritual seat and *primus inter pares* of the Eastern Orthodox Church worldwide, led by Ecumenical Patriarch Bartholomew I.
  - **Armenian Patriarchate of Constantinople (Kumkapı):** Spiritual center of the Armenian Apostolic Church in Turkey, leading religious affairs for ~60,000 community members.
  - **Chief Rabbinate of Turkey (*Hahambaşılık*):** Leading the Sephardic and Ashkenazi Jewish communities, centered in Istanbul and Izmir.
  - **Syriac Churches:** Ancient Syriac Orthodox Church (centered at the Deyrulzafaran and Mor Gabriel monasteries in Mardin) and Syriac Catholic Church [LAUSANNE-1923]."""
            }
        ],
        "infographics": [
            {
                "type": "comparison-table",
                "id": "rel-denominations-matrix",
                "title": "Taxonomy of Religious Denominations & Confessions in Contemporary Turkey",
                "headers": ["Confession / Tradition", "Theological Affiliation", "Estimated Demographic Share", "Worship Place / Center", "Institutional Representation"],
                "rows": [
                    ["Sunni (Hanafi)", "Islamic (Hanafi Jurisprudence)", "~70–75% of Population", "Mosques (Cami)", "Presidency of Religious Affairs (Diyanet)"],
                    ["Sunni (Shafi'i)", "Islamic (Shafi'i Jurisprudence)", "~10–12% of Population", "Mosques (Cami)", "Presidency of Religious Affairs (Diyanet)"],
                    ["Alevi-Bektashi", "Anatolian Shia-Sufi Synthesis", "~10–15% of Population", "Cemevi (Assembly Houses)", "Alevi-Bektashi Directorate (Culture Ministry)"],
                    ["Armenian Apostolic", "Oriental Orthodox Christianity", "~50,000–60,000", "Surp Asdvadzadzin Patriarchal Church", "Armenian Patriarchate of Constantinople"],
                    ["Sephardic Judaism", "Rabbinic Judaism (Orthodox)", "~14,000–15,000", "Neve Shalom & Bet Israel Synagogues", "Chief Rabbinate of Turkey (Hahambaşılık)"],
                    ["Greek Orthodox (Rûm)", "Eastern Orthodox Christianity", "~2,000–3,000", "St. George Patriarchal Church (Fener)", "Ecumenical Patriarchate of Constantinople"],
                    ["Syriac Orthodox", "Oriental Orthodox (West Syriac)", "~25,000", "Mor Gabriel & Deyrulzafaran Monasteries", "Syriac Orthodox Metropolinate"]
                ]
            },
            {
                "type": "stat-grid",
                "id": "rel-stats-grid",
                "title": "Diyanet Apparatus & Religious Demographic Metrics",
                "data": [
                    {"label": "Diyanet Civil Servants", "value": "140,000+ Staff", "sub": "Imams, muftis, preachers, Quran teachers"},
                    {"label": "Mosques in Turkey", "value": "90,000+ Mosques", "sub": "Administered under Diyanet jurisdiction"},
                    {"label": "Sunni Islam Share", "value": "~80–85%", "sub": "Hanafi majority, Shafi'i southeast"},
                    {"label": "Alevi Community", "value": "~10–15%", "sub": "Cemevi ritual gatherings"},
                    {"label": "Ecumenical Seat", "value": "Fener, Istanbul", "sub": "Historic center of global Eastern Orthodoxy"},
                    {"label": "Constitutional Principle", "value": "Article 2 Laiklik", "sub": "French-derived active state oversight"}
                ]
            },
            {
                "type": "timeline",
                "id": "rel-milestones-timeline",
                "title": "Chronology of Secularization & Religious Institutional Policy in Turkey",
                "items": [
                    {"year": "1924", "event": "Ottoman Caliphate abolished (March 3); Presidency of Religious Affairs (Diyanet) created."},
                    {"year": "1925", "event": "Dervish lodges, Sufi shrines, and tarikat orders banned by Law No. 677."},
                    {"year": "1928", "event": "'Religion of the State is Islam' clause removed from the 1924 Constitution."},
                    {"year": "1937", "event": "The principle of Secularism (Laiklik) formally enshrined as an unamendable constitutional norm."},
                    {"year": "1982", "event": "Mandatory Religious Culture and Moral Knowledge (DKAB) classes instituted in schools."},
                    {"year": "2013", "event": "Headscarf ban in public institutions and universities legally abolished."},
                    {"year": "2020", "event": "Hagia Sophia (Ayasofya) reclassified from museum to mosque, reopening for Islamic prayer."},
                    {"year": "2022", "event": "Alevi-Bektashi Cultural and Cemevi Directorate established under Ministry of Culture."}
                ]
            }
        ]
    }

print("All expanded modules loaded.")
