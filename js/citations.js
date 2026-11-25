/**
 * Citations Engine for Anatolia Academic Portal
 * Handles inline citation parsing, academic tooltips/popovers,
 * reference drawer, BibTeX, APA, and Chicago export generation.
 */

const CitationsEngine = {
  db: {},

  init(citationDatabase) {
    this.db = citationDatabase || {};
    this.setupModalListener();
  },

  // Replaces text bracket references like [TUIK-2024-POP] with interactive tags
  parseInlineCitations(text) {
    if (!text) return '';
    return text.replace(/\[([A-Z0-9\-_,\s]+)\]/g, (match, ids) => {
      const citeKeys = ids.split(',').map(s => s.trim());
      const badges = citeKeys.map(key => {
        const item = this.db[key];
        if (!item) return `<span class="cite-missing">[${key}]</span>`;
        return `<button type="button" class="cite-tag" data-cite-id="${key}" title="Click to view citation: ${item.author} (${item.year})">
          <svg class="icon-inline" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          <span class="cite-author">${this.formatShortCitation(item)}</span>
        </button>`;
      }).join(' ');
      return `<span class="citation-group">${badges}</span>`;
    });
  },

  formatShortCitation(item) {
    const authorShort = item.author.length > 22 ? item.author.split('(')[0].trim().substring(0, 18) + '...' : item.author;
    return `${authorShort}, ${item.year}`;
  },

  formatAPA(item) {
    let str = `${item.author} (${item.year}). *${item.title}*. ${item.publisher || ''}.`;
    if (item.doi) str += ` https://doi.org/${item.doi}`;
    else if (item.url) str += ` Available at: ${item.url}`;
    return str;
  },

  formatChicago(item) {
    let str = `${item.author}. "${item.title}." ${item.publisher || ''}, ${item.year}.`;
    if (item.url) str += ` ${item.url}.`;
    return str;
  },

  formatBibTeX(item) {
    const type = item.type === "Academic Monograph" ? "book" : (item.type === "Official Statistics" ? "misc" : "article");
    return `@${type}{${item.id},
  author    = {${item.author}},
  title     = {${item.title}},
  publisher = {${item.publisher || 'N/A'}},
  year      = {${item.year}},
  url       = {${item.url || ''}}${item.doi ? ',\n  doi       = {' + item.doi + '}' : ''}
}`;
  },

  openCitationModal(citeId) {
    const item = this.db[citeId];
    if (!item) return;

    const modal = document.getElementById('citation-modal');
    const container = document.getElementById('citation-modal-content');
    if (!modal || !container) return;

    const ui = (typeof MasterData !== 'undefined' && MasterData.getUI()) || {};

    const apa = this.formatAPA(item);
    const chicago = this.formatChicago(item);
    const bibtex = this.formatBibTeX(item);

    container.innerHTML = `
      <div class="modal-citation-header">
        <div class="citation-type-badge">${item.type || 'Primary Reference'}</div>
        <h3 class="modal-citation-title">${item.title}</h3>
        <p class="modal-citation-author"><strong>${ui.sourceAuthor || 'Source / Author'}:</strong> ${item.author} &bull; <strong>${ui.year || 'Year'}:</strong> ${item.year}</p>
        ${item.publisher ? `<p class="modal-citation-pub"><strong>${ui.publisher || 'Published By'}:</strong> ${item.publisher}</p>` : ''}
      </div>

      <div class="modal-citation-body">
        <div class="citation-tabs-nav">
          <button class="cite-tab-btn active" data-format="apa">APA 7th</button>
          <button class="cite-tab-btn" data-format="chicago">Chicago</button>
          <button class="cite-tab-btn" data-format="bibtex">BibTeX</button>
        </div>

        <div class="citation-format-display">
          <div id="cite-text-apa" class="cite-format-content active">
            <code>${apa}</code>
          </div>
          <div id="cite-text-chicago" class="cite-format-content">
            <code>${chicago}</code>
          </div>
          <div id="cite-text-bibtex" class="cite-format-content">
            <pre><code>${bibtex}</code></pre>
          </div>
        </div>

        <div class="citation-actions">
          <button class="btn btn-primary" id="btn-copy-citation">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            ${ui.copyCitation || 'Copy Citation'}
          </button>
          ${item.url ? `
            <a href="${item.url}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              ${ui.officialArchive || 'Official Archive &rarr;'}
            </a>
          ` : ''}
        </div>
      </div>
    `;

    // Tab switching inside modal
    const tabs = container.querySelectorAll('.cite-tab-btn');
    tabs.forEach(tab => {
      tab.addEventListener('click', (e) => {
        tabs.forEach(t => t.classList.remove('active'));
        container.querySelectorAll('.cite-format-content').forEach(c => c.classList.remove('active'));
        e.currentTarget.classList.add('active');
        const format = e.currentTarget.getAttribute('data-format');
        document.getElementById(`cite-text-${format}`).classList.add('active');
      });
    });

    // Copy to clipboard
    const copyBtn = document.getElementById('btn-copy-citation');
    copyBtn.addEventListener('click', () => {
      const activeContent = container.querySelector('.cite-format-content.active');
      const text = activeContent.innerText.trim();
      navigator.clipboard.writeText(text).then(() => {
        copyBtn.innerHTML = `
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
          ${ui.copied || 'Copied to Clipboard!'}
        `;
        setTimeout(() => {
          copyBtn.innerHTML = `
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            ${ui.copyCitation || 'Copy Citation'}
          `;
        }, 2200);
      });
    });

    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
  },

  setupModalListener() {
    // Document level delegation for cite buttons
    document.addEventListener('click', (e) => {
      const citeBtn = e.target.closest('.cite-tag');
      if (citeBtn) {
        const citeId = citeBtn.getAttribute('data-cite-id');
        this.openCitationModal(citeId);
      }

      // Close modal backdrop or close button
      if (e.target.matches('.modal-backdrop') || e.target.closest('.modal-close-btn')) {
        const modal = document.getElementById('citation-modal');
        if (modal) {
          modal.classList.remove('active');
          modal.setAttribute('aria-hidden', 'true');
        }
      }
    });

    // ESC key closes modal
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const modal = document.getElementById('citation-modal');
        if (modal && modal.classList.contains('active')) {
          modal.classList.remove('active');
          modal.setAttribute('aria-hidden', 'true');
        }
      }
    });
  },

  // Generates module-specific bibliography HTML
  renderModuleBibliography(moduleData) {
    const foundIds = new Set();
    const regex = /\[([A-Z0-9\-_,\s]+)\]/g;
    
    moduleData.sections.forEach(sec => {
      let m;
      while ((m = regex.exec(sec.content)) !== null) {
        m[1].split(',').forEach(id => foundIds.add(id.trim()));
      }
    });

    if (foundIds.size === 0) return '';

    const ui = (typeof MasterData !== 'undefined' && MasterData.getUI()) || {};

    let html = `
      <section class="module-bibliography" id="bibliography">
        <div class="bibliography-header">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          <h3>${ui.worksCited || 'Chapter Works Cited & Primary Sources'}</h3>
          <span class="biblio-count">${foundIds.size} ${ui.canonicalCitations || 'Canonical Citations'}</span>
        </div>
        <div class="bibliography-list">
    `;

    foundIds.forEach(id => {
      const item = this.db[id];
      if (item) {
        html += `
          <div class="biblio-entry" id="bib-${id}">
            <div class="biblio-badge">${item.type || 'Statute/Source'}</div>
            <div class="biblio-meta">
              <span class="biblio-author"><strong>${item.author}</strong> (${item.year}).</span>
              <span class="biblio-title"><em>${item.title}</em>.</span>
              <span class="biblio-publisher">${item.publisher || ''}.</span>
            </div>
            <div class="biblio-tools">
              <button class="btn btn-xs cite-tag" data-cite-id="${id}">${ui.getCitation || 'Cite / BibTeX'}</button>
              ${item.url ? `<a href="${item.url}" target="_blank" rel="noopener noreferrer" class="biblio-link">${ui.officialArchive || 'Official Archive &rarr;'}</a>` : ''}
            </div>
          </div>
        `;
      }
    });

    html += `
        </div>
      </section>
    `;

    return html;
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = CitationsEngine;
} else if (typeof window !== 'undefined') {
  window.CitationsEngine = CitationsEngine;
}
