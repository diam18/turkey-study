/**
 * Master Data Coordinator for Anatolia Academic Portal
 * Dynamically routes to EN, TR, or RU datasets based on user language selection.
 */

const MasterData = {
  currentLang: 'en',

  init(lang) {
    this.currentLang = lang || 'en';
  },

  getData() {
    if (this.currentLang === 'tr' && typeof ACADEMIC_DATA_TR !== 'undefined') {
      return ACADEMIC_DATA_TR;
    } else if (this.currentLang === 'ru' && typeof ACADEMIC_DATA_RU !== 'undefined') {
      return ACADEMIC_DATA_RU;
    }
    // Default to EN
    return typeof ACADEMIC_DATA_EN !== 'undefined' ? ACADEMIC_DATA_EN : (typeof ACADEMIC_DATA !== 'undefined' ? ACADEMIC_DATA : {});
  },

  getUI() {
    if (typeof UI_TRANSLATIONS !== 'undefined') {
      return UI_TRANSLATIONS[this.currentLang] || UI_TRANSLATIONS.en;
    }
    return {};
  }
};

// Global backward compatibility
var ACADEMIC_DATA = MasterData.getData();

if (typeof module !== 'undefined' && module.exports) {
  module.exports = MasterData;
} else if (typeof window !== 'undefined') {
  window.MasterData = MasterData;
}
