/**
 * Main Application Orchestrator for Anatolia Academic Portal
 * Supports instant Trilingual Toggling (EN, TR, RU), Reading Modes,
 * Interactive Maps, Citations, and Global Semantic Search.
 */

const App = {
  activeModuleId: 'history',
  readingMode: 'article', // 'article' or 'briefing'
  theme: 'light',
  lang: 'en', // 'en', 'tr', or 'ru'

  init() {
    // 1. Init Language from localStorage or browser default
    const savedLang = localStorage.getItem('anatolia_lang') || 'en';
    this.lang = ['en', 'tr', 'ru'].includes(savedLang) ? savedLang : 'en';
    MasterData.init(this.lang);

    // 2. Initialize Citation Database
    CitationsEngine.init(MasterData.getData().citations);

    // 3. Build Search Index
    AcademicSearch.buildIndex(MasterData.getData());

    // 4. Update UI labels
    this.updateUILabels();

    // 5. Render Navigation Sidebar
    this.renderSidebar();

    // 6. Setup Event Listeners
    this.setupEvents();

    // 7. Initial Route Resolution
    this.handleRoute();

    // 8. Init Theme
    this.initTheme();
  },

  setLanguage(newLang) {
    if (!['en', 'tr', 'ru'].includes(newLang)) return;
    this.lang = newLang;
    localStorage.setItem('anatolia_lang', newLang);
    MasterData.init(newLang);

    // Update active button state
    document.querySelectorAll('.lang-btn').forEach(btn => {
      if (btn.getAttribute('data-lang') === newLang) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // Re-init engines with new localized data
    CitationsEngine.init(MasterData.getData().citations);
    AcademicSearch.buildIndex(MasterData.getData());

    // Update UI text strings
    this.updateUILabels();

    // Re-render sidebar & active view
    this.renderSidebar();
    this.handleRoute();
  },

  updateUILabels() {
    const ui = MasterData.getUI();
    const searchInput = document.getElementById('global-search-input');
    if (searchInput) searchInput.placeholder = ui.searchPlaceholder || "Search modules, treaties...";

    const brandTitle = document.getElementById('ui-brand-title');
    if (brandTitle) brandTitle.textContent = ui.siteTitle;

    const brandSub = document.getElementById('ui-brand-subtitle');
    if (brandSub) brandSub.textContent = ui.siteSubtitle;

    const citationsText = document.getElementById('ui-citations-text');
    if (citationsText) citationsText.textContent = ui.citationsRegistryBtn;

    const versionFooter = document.getElementById('ui-version-footer');
    if (versionFooter) versionFooter.textContent = ui.versionFooter;
  },

  renderSidebar() {
    const navList = document.getElementById('sidebar-nav-list');
    if (!navList) return;

    const ui = MasterData.getUI();
    const currentData = MasterData.getData();

    let html = `
      <div class="nav-section-title">${ui.coreModules || 'CORE RESEARCH MODULES (13)'}</div>
    `;

    currentData.modules.forEach(mod => {
      html += `
        <a href="#${mod.id}" class="nav-item ${mod.id === this.activeModuleId ? 'active' : ''}" data-mod-id="${mod.id}">
          <span class="nav-mod-num">${mod.number}</span>
          <span class="nav-mod-title">${mod.title}</span>
        </a>
      `;
    });

    html += `
      <div class="nav-section-title" style="margin-top: 1.5rem;">${ui.scholarlyTools || 'SCHOLARLY TOOLS'}</div>
      <a href="#master-bibliography" class="nav-item nav-tool-item" data-mod-id="master-bibliography">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
        <span>${ui.masterBibliography || 'Master Citation Registry'}</span>
      </a>
      <a href="#portal-methodology" class="nav-item nav-tool-item" data-mod-id="portal-methodology">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        <span>${ui.researchMethodology || 'Research Methodology'}</span>
      </a>
    `;

    navList.innerHTML = html;
  },

  handleRoute() {
    const hash = window.location.hash.replace('#', '') || 'history';
    const currentData = MasterData.getData();
    
    // Update active nav item
    document.querySelectorAll('#sidebar-nav-list .nav-item').forEach(el => {
      if (el.getAttribute('data-mod-id') === hash) {
        el.classList.add('active');
      } else {
        el.classList.remove('active');
      }
    });

    if (hash === 'master-bibliography') {
      this.renderMasterBibliography();
    } else if (hash === 'portal-methodology') {
      this.renderMethodology();
    } else {
      const mod = currentData.modules.find(m => m.id === hash);
      if (mod) {
        this.activeModuleId = mod.id;
        this.renderModule(mod);
      } else {
        this.activeModuleId = 'history';
        this.renderModule(currentData.modules[0]);
      }
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  renderModule(mod) {
    const container = document.getElementById('main-content-viewport');
    if (!container) return;

    const ui = MasterData.getUI();

    let html = `
      <article class="academic-module-article ${this.readingMode === 'briefing' ? 'mode-briefing' : 'mode-article'}">
        <!-- Module Header -->
        <header class="module-header">
          <div class="module-meta-bar">
            <span class="badge-module-num">${ui.moduleLabel || 'MODULE'} ${mod.number}</span>
            <span class="meta-separator">&bull;</span>
            <span class="reading-time-tag">${mod.readingTime}</span>
            <span class="meta-separator">&bull;</span>
            <span class="peer-reviewed-tag">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
              ${ui.badgeStandard || 'Academic Research Standard'}
            </span>
          </div>

          <h1 class="module-hero-title">${mod.title}</h1>
          <p class="module-hero-tagline">${mod.tagline}</p>

          <!-- Module Controls Bar -->
          <div class="module-controls">
            <div class="reading-mode-toggle">
              <button class="mode-btn ${this.readingMode === 'article' ? 'active' : ''}" id="mode-article-btn">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                ${ui.articleMode || 'Scholarly Article Mode'}
              </button>
              <button class="mode-btn ${this.readingMode === 'briefing' ? 'active' : ''}" id="mode-briefing-btn">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
                ${ui.briefingMode || 'Data & Visuals Briefing'}
              </button>
            </div>

            <div class="article-actions">
              <button class="action-btn" id="btn-print-chapter" title="Print or save as PDF">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
                ${ui.printBtn || 'Print / PDF'}
              </button>
            </div>
          </div>
        </header>

        <!-- Executive Summary Callout -->
        <div class="executive-summary-card">
          <div class="summary-badge">${ui.execBrief || 'EXECUTIVE RESEARCH BRIEF'}</div>
          <p>${mod.summary}</p>
        </div>

        <!-- Custom Visualizations / Maps / Infographics depending on module -->
        <div class="module-visualizations-wrapper">
    `;

    // Special custom interactive widgets per module
    if (mod.id === 'geography') {
      html += Visualizations.renderRegionalMap();
      html += Visualizations.renderFaultLinesMap();
    } else if (mod.id === 'energy') {
      html += Visualizations.renderEnergyChart();
    }

    // Standard infographic components attached to module data
    if (mod.infographics && mod.infographics.length > 0) {
      mod.infographics.forEach(info => {
        if (info.type === 'timeline') {
          html += Visualizations.renderTimeline(info);
        } else if (info.type === 'stat-grid') {
          html += Visualizations.renderStatGrid(info);
        } else if (info.type === 'comparison-table') {
          html += Visualizations.renderTable(info);
        } else if (info.type === 'organogram') {
          html += Visualizations.renderOrganogram(info);
        }
      });
    }

    html += `
        </div>

        <!-- Scholarly Narrative Sections -->
        <div class="module-narrative-body">
    `;

    mod.sections.forEach(sec => {
      html += `
        <section class="chapter-section" id="${sec.id}">
          <h2 class="section-title">${sec.title}</h2>
          <div class="section-prose">
            ${this.formatProse(sec.content)}
          </div>
        </section>
      `;
    });

    html += `
        </div>

        <!-- Chapter Works Cited & Bibliography -->
        ${CitationsEngine.renderModuleBibliography(mod)}

        <!-- Chapter Footer Navigation -->
        ${this.renderChapterNav(mod)}
      </article>
    `;

    container.innerHTML = html;

    // Attach module specific interactions
    if (mod.id === 'geography') {
      Visualizations.initMapEvents();
    }

    // Attach mode toggle buttons
    document.getElementById('mode-article-btn')?.addEventListener('click', () => {
      this.setReadingMode('article');
    });
    document.getElementById('mode-briefing-btn')?.addEventListener('click', () => {
      this.setReadingMode('briefing');
    });

    // Print button
    document.getElementById('btn-print-chapter')?.addEventListener('click', () => {
      window.print();
    });
  },

  formatProse(rawContent) {
    if (!rawContent) return '';
    // 1. Process inline citations
    const withCitations = CitationsEngine.parseInlineCitations(rawContent);

    // 2. Format paragraphs and markdown bullet points
    const lines = withCitations.split('\n');
    let formatted = '';
    let inList = false;

    lines.forEach(line => {
      const trimmed = line.trim();
      if (!trimmed) {
        if (inList) {
          formatted += '</ul>';
          inList = false;
        }
        return;
      }

      if (trimmed.startsWith('- ')) {
        if (!inList) {
          formatted += '<ul class="scholarly-bullet-list">';
          inList = true;
        }
        formatted += `<li>${this.formatMarkdownBold(trimmed.substring(2))}</li>`;
      } else {
        if (inList) {
          formatted += '</ul>';
          inList = false;
        }
        formatted += `<p class="prose-paragraph">${this.formatMarkdownBold(trimmed)}</p>`;
      }
    });

    if (inList) formatted += '</ul>';
    return formatted;
  },

  formatMarkdownBold(text) {
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>');
  },

  renderChapterNav(currentMod) {
    const currentData = MasterData.getData();
    const idx = currentData.modules.findIndex(m => m.id === currentMod.id);
    const prev = idx > 0 ? currentData.modules[idx - 1] : null;
    const next = idx < currentData.modules.length - 1 ? currentData.modules[idx + 1] : null;
    const ui = MasterData.getUI();

    return `
      <div class="chapter-pagination">
        ${prev ? `
          <a href="#${prev.id}" class="chapter-nav-btn prev">
            <span class="nav-direction">&larr; ${ui.prevModule || 'Previous Module'}</span>
            <span class="nav-target-name">${prev.number}. ${prev.title}</span>
          </a>
        ` : '<div></div>'}
        
        ${next ? `
          <a href="#${next.id}" class="chapter-nav-btn next">
            <span class="nav-direction">${ui.nextModule || 'Next Module'} &rarr;</span>
            <span class="nav-target-name">${next.number}. ${next.title}</span>
          </a>
        ` : '<div></div>'}
      </div>
    `;
  },

  setReadingMode(mode) {
    this.readingMode = mode;
    const article = document.querySelector('.academic-module-article');
    if (!article) return;

    if (mode === 'briefing') {
      article.classList.remove('mode-article');
      article.classList.add('mode-briefing');
      document.getElementById('mode-briefing-btn')?.classList.add('active');
      document.getElementById('mode-article-btn')?.classList.remove('active');
    } else {
      article.classList.remove('mode-briefing');
      article.classList.add('mode-article');
      document.getElementById('mode-article-btn')?.classList.add('active');
      document.getElementById('mode-briefing-btn')?.classList.remove('active');
    }
  },

  renderMasterBibliography() {
    const container = document.getElementById('main-content-viewport');
    if (!container) return;

    const currentData = MasterData.getData();
    const ui = MasterData.getUI();
    const cites = Object.values(currentData.citations);

    let html = `
      <div class="academic-module-article">
        <header class="module-header">
          <div class="module-meta-bar">
            <span class="badge-module-num">${ui.scholarlyTools || 'SCHOLARLY APPARATUS'}</span>
            <span class="meta-separator">&bull;</span>
            <span class="reading-time-tag">${cites.length} ${ui.sourcesCountSuffix || 'Primary Legal & Empirical Sources'}</span>
          </div>
          <h1 class="module-hero-title">${ui.masterBibliography || 'Master Citation Registry'}</h1>
          <p class="module-hero-tagline">${ui.biblioTagline || 'Canonical statutory acts, international boundary treaties, statistical databases, and academic monographs.'}</p>
        </header>

        <div class="master-biblio-filter-bar">
          <div class="search-box-wrap">
            <input type="text" id="biblio-search-input" class="search-input" placeholder="${ui.filterCitationsPlaceholder || 'Filter citations by author, treaty name, year...'}">
          </div>
          <button class="btn btn-primary" id="btn-export-all-bibtex">${ui.exportBibtexBtn || 'Export Full BibTeX (.bib)'}</button>
        </div>

        <div class="master-biblio-grid" id="master-biblio-list">
    `;

    cites.forEach(item => {
      html += `
        <div class="biblio-card" data-search="${item.author.toLowerCase()} ${item.title.toLowerCase()} ${item.publisher ? item.publisher.toLowerCase() : ''}">
          <div class="card-top">
            <span class="citation-type-badge">${item.type}</span>
            <span class="citation-year">${item.year}</span>
          </div>
          <h4 class="biblio-card-title">${item.title}</h4>
          <p class="biblio-card-author"><strong>${ui.sourceAuthor || 'Source / Author'}:</strong> ${item.author}</p>
          ${item.publisher ? `<p class="biblio-card-pub"><strong>${ui.publisher || 'Published By'}:</strong> ${item.publisher}</p>` : ''}
          <div class="biblio-card-footer">
            <button class="btn btn-xs cite-tag" data-cite-id="${item.id}">${ui.getCitation || 'Cite / BibTeX'}</button>
            ${item.url ? `<a href="${item.url}" target="_blank" rel="noopener noreferrer" class="biblio-link">${ui.officialArchive || 'Official Portal &rarr;'}</a>` : ''}
          </div>
        </div>
      `;
    });

    html += `
        </div>
      </div>
    `;

    container.innerHTML = html;

    // Filter listener
    const filterInput = document.getElementById('biblio-search-input');
    filterInput?.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      document.querySelectorAll('#master-biblio-list .biblio-card').forEach(card => {
        const text = card.getAttribute('data-search');
        if (!q || text.includes(q)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });

    // Export all BibTeX
    document.getElementById('btn-export-all-bibtex')?.addEventListener('click', () => {
      const fullBib = cites.map(c => CitationsEngine.formatBibTeX(c)).join('\n\n');
      const blob = new Blob([fullBib], { type: 'text/plain;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'anatolia-academic-citations.bib';
      a.click();
      URL.revokeObjectURL(url);
    });
  },

  renderMethodology() {
    const container = document.getElementById('main-content-viewport');
    if (!container) return;

    const lang = (typeof MasterData !== 'undefined' && MasterData.currentLang) || 'en';
    const ui = MasterData.getUI();

    const methData = {
      en: {
        badge: "ACADEMIC STANDARDS",
        tag: "Methodology & Research Protocol",
        title: "Academic Sourcing & Research Methodology",
        tagline: "Epistemological framework, statutory verification standards, and empirical data integrity.",
        s1Title: "1. Primary Source Hierarchy & Verification Protocol",
        s1Intro: "To guarantee the highest scholarly credibility for students and academic researchers, all information presented in this portal strictly complies with four methodological criteria:",
        bullets: [
          "<strong>Statutory & Constitutional Law:</strong> Sourced directly from the Official Gazette of the Republic of Turkey (<em>T.C. Resmî Gazete</em>), the Grand National Assembly (TBMM) legislative records, and Constitutional Court (<em>AYM</em>) jurisprudence databases.",
          "<strong>Diplomatic & International Boundaries:</strong> Grounded in verified multilateral and bilateral treaty instruments deposited with the United Nations and League of Nations Treaty Series (notably the 1921 Moscow and Kars Treaties, 1923 Lausanne Treaty, and 1936 Montreux Convention).",
          "<strong>Empirical & Macroeconomic Statistics:</strong> Sourced exclusively from official institutional regulators including TÜİK (Turkish Statistical Institute), TCMB (Central Bank), BDDK (Banking Regulation Agency), EPDK (Energy Market Regulatory Authority), alongside cross-verified international datasets from the World Bank, IMF, IEA, and SIPRI.",
          "<strong>Historiographical Objectivity:</strong> Historical trajectories (such as civil-military dynamics, military coups, and ethnic demographics) are treated using rigorous peer-reviewed scholarship (such as Erik-Jan Zürcher's canonical <em>Turkey: A Modern History</em>) and human rights archive documentation."
        ],
        s2Title: "2. Citation & Dataset Export Protocol",
        s2Text: "Every statistical figure, institutional organogram, and historical treaty carries clickable inline citation badges. Students and researchers can click any badge to inspect bibliographic metadata, format citations in APA 7th, Chicago, or BibTeX format, or export datasets for academic reproduction."
      },
      tr: {
        badge: "AKADEMİK STANDARTLAR",
        tag: "Metodoloji ve Araştırma Protokolü",
        title: "Akademik Kaynak Gösterme ve Araştırma Metodolojisi",
        tagline: "Epistemolojik çerçeve, mevzuat doğrulama standartları ve ampirik veri bütünlüğü.",
        s1Title: "1. Birincil Kaynak Hiyerarşisi ve Doğrulama Protokolü",
        s1Intro: "Lisans, lisansüstü öğrencileri ve araştırmacılar için en yüksek akademik güvenilirliği sağlamak amacıyla portalımızdaki tüm bilgiler dört temel metodolojik kurala titizlikle uyar:",
        bullets: [
          "<strong>Mevzuat ve Anayasa Hukuku:</strong> Doğrudan T.C. Resmî Gazete, Türkiye Büyük Millet Meclisi (TBMM) kanun tutanakları ve Anayasa Mahkemesi (AYM) içtihat veri tabanlarından alınmıştır.",
          "<strong>Diplomatik ve Uluslararası Sınırlar:</strong> Birleşmiş Milletler ve Milletler Cemiyeti arşivlerinde tescilli çok taraflı ve iki taraflı antlaşma metinlerine (1921 Moskova ve Kars Antlaşmaları, 1923 Lozan Barış Antlaşması, 1936 Montrö Boğazlar Sözleşmesi) dayandırılmıştır.",
          "<strong>Ampirik ve Makroekonomik İstatistikler:</strong> TÜİK, TCMB, BDDK, EPDK gibi resmi ulusal düzenleyici otoritelerin yanı sıra Dünya Bankası, IMF, IEA ve SIPRI veri tabanlarıyla çapraz doğrulanmıştır.",
          "<strong>Tarihsel Nesnellik:</strong> Sivil-asker ilişkileri, askeri darbeler ve etnik demografi gibi hassas konular Erik-Jan Zürcher gibi uluslararası alanda kabul görmüş hakemli akademik monografiler ve insan hakları arşivleri ışığında tarafsızlıkla ele alınmıştır."
        ],
        s2Title: "2. Atıf ve Veri Dışa Aktarma Protokolü",
        s2Text: "Her istatistiki veri, kurumsal teşkilat şeması ve tarihi antlaşma tıklanabilir kanonik atıf etiketleri taşır. Araştırmacılar herhangi bir etikete tıklayarak bibliyografik künyeyi inceleyebilir, APA 7th, Chicago veya BibTeX formatlarında kopyalayabilir veya akademik çalışmalarında kullanmak üzere indirebilir."
      },
      ru: {
        badge: "АКАДЕМИЧЕСКИЕ СТАНДАРТЫ",
        tag: "Методология и исследовательский протокол",
        title: "Академические стандарты и методология исследований",
        tagline: "Эпистемологическая рамка, верификация нормативно-правовых актов и эмпирическая достоверность данных.",
        s1Title: "1. Иерархия первоисточников и протокол верификации",
        s1Intro: "В целях обеспечения академической достоверности для студентов, аспирантов и ученых все материалы портала строго соответствуют четырем методологическим критериям:",
        bullets: [
          "<strong>Законодательство и конституционное право:</strong> первоисточниками выступают публикации в Официальном вестнике Турецкой Республики (<em>T.C. Resmî Gazete</em>), протоколы законодательных актов ВНСТ (TBMM) и прецеденты Конституционного суда (<em>AYM</em>).",
          "<strong>Дипломатия и международные границы:</strong> опираются на аутентичные тексты международных договоров, депонированных в Лиге Наций и ООН (Московский и Карсский договоры 1921 г., Лозаннский мирный договор 1923 г., Конвенция Монтрё 1936 г.).",
          "<strong>Эмпирические и макроэкономические показатели:</strong> используются исключительно официальные данные национальных регуляторов (TÜİK, TCMB, BDDK, EPDK) в сопоставлении с базами данных Всемирного банка, МВФ, МЭА (IEA) и СИПРИ (SIPRI).",
          "<strong>Историографическая объективность:</strong> сложные историко-политические процессы (военные перевороты, курдский вопрос, демографические трансформации) излагаются на основе признанных академических монографий (Эрик-Ян Цюрхер «Турция: Новая история») и компаративного анализа."
        ],
        s2Title: "2. Протокол цитирования и экспорта данных",
        s2Text: "Каждый факт, статистическая метрика и схема снабжены кликабельными каноническими ссылками. Доступно цитирование в международных форматах APA 7th, Chicago и BibTeX для включения в научные статьи и диссертации."
      }
    };

    const cur = methData[lang] || methData.en;

    container.innerHTML = `
      <div class="academic-module-article">
        <header class="module-header">
          <div class="module-meta-bar">
            <span class="badge-module-num">${cur.badge}</span>
            <span class="meta-separator">&bull;</span>
            <span class="reading-time-tag">${cur.tag}</span>
          </div>
          <h1 class="module-hero-title">${cur.title}</h1>
          <p class="module-hero-tagline">${cur.tagline}</p>
        </header>

        <div class="chapter-section">
          <h2 class="section-title">${cur.s1Title}</h2>
          <div class="section-prose">
            <p class="prose-paragraph">${cur.s1Intro}</p>
            <ul class="scholarly-bullet-list">
              ${cur.bullets.map(b => `<li>${b}</li>`).join('')}
            </ul>
          </div>
        </div>

        <div class="chapter-section">
          <h2 class="section-title">${cur.s2Title}</h2>
          <div class="section-prose">
            <p class="prose-paragraph">${cur.s2Text}</p>
          </div>
        </div>
      </div>
    `;
  },

  setupEvents() {
    // Hash change routing
    window.addEventListener('hashchange', () => this.handleRoute());

    // Language switcher buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const targetLang = e.currentTarget.getAttribute('data-lang');
        this.setLanguage(targetLang);
      });
    });

    // Global Search functionality
    const searchInput = document.getElementById('global-search-input');
    const searchDropdown = document.getElementById('search-results-dropdown');
    const ui = MasterData.getUI();

    if (searchInput && searchDropdown) {
      searchInput.addEventListener('input', (e) => {
        const query = e.target.value;
        const ui = MasterData.getUI();
        if (!query || query.trim().length < 2) {
          searchDropdown.classList.remove('active');
          searchDropdown.innerHTML = '';
          return;
        }

        const results = AcademicSearch.search(query);
        if (results.length === 0) {
          searchDropdown.innerHTML = `
            <div class="search-no-results">${ui.noSearchResults || 'No academic sections or citations matching'} "${query}"</div>
          `;
          searchDropdown.classList.add('active');
          return;
        }

        let html = '';
        results.forEach(res => {
          html += `
            <a href="#${res.moduleId}" class="search-result-item" data-mod="${res.moduleId}">
              <div class="search-res-top">
                <span class="search-res-type">${res.type}</span>
                <span class="search-res-mod">${res.moduleNumber ? (ui.moduleLabel || 'Module') + ' ' + res.moduleNumber : ''}</span>
              </div>
              <div class="search-res-heading">${res.heading}</div>
              <div class="search-res-snippet">${res.snippet}</div>
            </a>
          `;
        });

        searchDropdown.innerHTML = html;
        searchDropdown.classList.add('active');
      });

      // Close search when clicking outside
      document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
          searchDropdown.classList.remove('active');
        }
      });

      // Click on search item closes dropdown
      searchDropdown.addEventListener('click', (e) => {
        const item = e.target.closest('.search-result-item');
        if (item) {
          searchDropdown.classList.remove('active');
          searchInput.value = '';
        }
      });
    }

    // Theme toggle
    const themeBtn = document.getElementById('theme-toggle-btn');
    themeBtn?.addEventListener('click', () => {
      this.toggleTheme();
    });

    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-toggle');
    const sidebar = document.getElementById('app-sidebar');
    mobileMenuBtn?.addEventListener('click', () => {
      sidebar?.classList.toggle('mobile-open');
    });

    // Close mobile menu on nav click
    document.getElementById('sidebar-nav-list')?.addEventListener('click', (e) => {
      if (e.target.closest('.nav-item')) {
        sidebar?.classList.remove('mobile-open');
      }
    });
  },

  initTheme() {
    const saved = localStorage.getItem('anatolia_theme') || 'light';
    this.setTheme(saved);
  },

  toggleTheme() {
    const newTheme = this.theme === 'light' ? 'dark' : 'light';
    this.setTheme(newTheme);
  },

  setTheme(theme) {
    this.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('anatolia_theme', theme);
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) {
      if (theme === 'dark') {
        themeBtn.innerHTML = `
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
        `;
      } else {
        themeBtn.innerHTML = `
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        `;
      }
    }
  }
};

// Auto-run on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
