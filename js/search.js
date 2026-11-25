/**
 * Academic Search & Indexing Engine for Anatolia Academic
 * Indexes all 13 modules, section headings, paragraphs, institutions, and citations
 * to provide instant keyword search with contextual previews.
 */

const AcademicSearch = {
  index: [],

  buildIndex(academicData) {
    this.index = [];
    academicData.modules.forEach(mod => {
      // Index module overview
      this.index.push({
        moduleId: mod.id,
        sectionId: mod.id,
        moduleNumber: mod.number,
        moduleTitle: mod.title,
        heading: mod.title,
        text: mod.summary + " " + mod.tagline,
        type: "Module Overview"
      });

      // Index individual sections
      mod.sections.forEach(sec => {
        this.index.push({
          moduleId: mod.id,
          sectionId: sec.id,
          moduleNumber: mod.number,
          moduleTitle: mod.title,
          heading: sec.title,
          text: sec.content,
          type: "Chapter Section"
        });
      });
    });

    // Also index citations
    Object.values(academicData.citations).forEach(cite => {
      this.index.push({
        moduleId: "citations-master",
        sectionId: cite.id,
        moduleNumber: "SRC",
        moduleTitle: "Citation Registry",
        heading: `${cite.author} (${cite.year}) - ${cite.title}`,
        text: `${cite.title} ${cite.publisher || ''} ${cite.type || ''}`,
        type: "Primary Source / Law"
      });
    });
  },

  search(query, maxResults = 8) {
    if (!query || query.trim().length < 2) return [];
    const q = query.toLowerCase().trim();
    const tokens = q.split(/\s+/).filter(t => t.length > 0);

    const scores = [];

    this.index.forEach(item => {
      let score = 0;
      const headingLower = item.heading.toLowerCase();
      const textLower = item.text.toLowerCase();
      const titleLower = item.moduleTitle.toLowerCase();

      // Check whole query match
      if (headingLower.includes(q)) score += 50;
      if (titleLower.includes(q)) score += 30;
      if (textLower.includes(q)) score += 15;

      // Token matches
      tokens.forEach(tok => {
        if (headingLower.includes(tok)) score += 15;
        if (textLower.includes(tok)) score += 5;
      });

      if (score > 0) {
        // Find snippet
        let snippet = "";
        const idx = textLower.indexOf(tokens[0] || q);
        if (idx !== -1) {
          const start = Math.max(0, idx - 45);
          const end = Math.min(item.text.length, idx + 110);
          snippet = (start > 0 ? "..." : "") + item.text.substring(start, end).replace(/\n/g, ' ') + (end < item.text.length ? "..." : "");
        } else {
          snippet = item.text.substring(0, 130).replace(/\n/g, ' ') + "...";
        }

        scores.push({
          ...item,
          score,
          snippet
        });
      }
    });

    return scores.sort((a, b) => b.score - a.score).slice(0, maxResults);
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = AcademicSearch;
} else if (typeof window !== 'undefined') {
  window.AcademicSearch = AcademicSearch;
}
