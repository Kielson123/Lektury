/**
 * Vademecum Kontekstów Maturalnych - Logika Aplikacji (JavaScript)
 * Obsługa filtrowania, wyszukiwania, schowka, ulubionych i trybu powtórkowego
 */

document.addEventListener('DOMContentLoaded', () => {
  // Stan aplikacji
  const state = {
    searchQuery: '',
    selectedCategory: 'all',
    selectedEpoka: 'all',
    selectedContextType: 'all',
    showFavoritesOnly: false,
    favorites: JSON.parse(localStorage.getItem('matura_lektury_favs') || '[]'),
    theme: localStorage.getItem('matura_theme') || 'light'
  };

  // Elementy DOM
  const elements = {
    cardsContainer: document.getElementById('cardsContainer'),
    emptyState: document.getElementById('emptyState'),
    searchInput: document.getElementById('searchInput'),
    btnClearSearch: document.getElementById('btnClearSearch'),
    categoryPills: document.querySelectorAll('.category-pills .pill-btn'),
    epokaFilter: document.getElementById('epokaFilter'),
    contextTypeFilter: document.getElementById('contextTypeFilter'),
    btnToggleFavorites: document.getElementById('btnToggleFavorites'),
    btnResetFilters: document.getElementById('btnResetFilters'),
    activeCountText: document.getElementById('activeCountText'),
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    themeIcon: document.getElementById('themeIcon'),
    btnOpenGuide: document.getElementById('btnOpenGuide'),
    guideModal: document.getElementById('guideModal'),
    btnCloseGuide: document.getElementById('btnCloseGuide'),
    btnRandomizer: document.getElementById('btnRandomizer'),
    flashcardModal: document.getElementById('flashcardModal'),
    btnCloseFlashcard: document.getElementById('btnCloseFlashcard'),
    btnNextRandom: document.getElementById('btnNextRandom'),
    btnRevealFlashcard: document.getElementById('btnRevealFlashcard'),
    flashcardBody: document.getElementById('flashcardBody'),
    toastContainer: document.getElementById('toastContainer')
  };

  // Inicjalizacja motywu
  initTheme();

  // Inicjalizacja danych i renderowanie
  renderCards();
  updateCategoryCounts();

  // ==========================================
  // Obsługa zdarzeń (Event Listeners)
  // ==========================================

  // Wyszukiwarka
  elements.searchInput.addEventListener('input', (e) => {
    state.searchQuery = e.target.value.trim().toLowerCase();
    renderCards();
  });

  elements.btnClearSearch.addEventListener('click', () => {
    elements.searchInput.value = '';
    state.searchQuery = '';
    elements.searchInput.focus();
    renderCards();
  });

  // Filtry kategorii (Zakres podstawowy / SP / Dodatkowe)
  elements.categoryPills.forEach(pill => {
    pill.addEventListener('click', () => {
      elements.categoryPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      state.selectedCategory = pill.dataset.category;
      renderCards();
    });
  });

  // Filtr epoki
  elements.epokaFilter.addEventListener('change', (e) => {
    state.selectedEpoka = e.target.value;
    renderCards();
  });

  // Filtr typu kontekstu
  elements.contextTypeFilter.addEventListener('change', (e) => {
    state.selectedContextType = e.target.value;
    renderCards();
  });

  // Przełącznik ulubionych
  elements.btnToggleFavorites.addEventListener('click', () => {
    state.showFavoritesOnly = !state.showFavoritesOnly;
    elements.btnToggleFavorites.classList.toggle('active', state.showFavoritesOnly);
    elements.btnToggleFavorites.classList.toggle('btn-primary', state.showFavoritesOnly);
    elements.btnToggleFavorites.classList.toggle('btn-secondary', !state.showFavoritesOnly);
    renderCards();
    showToast(state.showFavoritesOnly ? 'Wyświetlam tylko zapisane do powtórki' : 'Wyświetlam wszystkie lektury');
  });

  // Reset filtrów
  elements.btnResetFilters.addEventListener('click', resetFilters);

  // Zmiana motywu (Dark / Light)
  elements.themeToggleBtn.addEventListener('click', toggleTheme);

  // Modal: Przewodnik CKE
  elements.btnOpenGuide.addEventListener('click', () => openModal(elements.guideModal));
  elements.btnCloseGuide.addEventListener('click', () => closeModal(elements.guideModal));

  // Modal: Losowarka / Tryb Fiszki
  elements.btnRandomizer.addEventListener('click', openRandomizerModal);
  elements.btnCloseFlashcard.addEventListener('click', () => closeModal(elements.flashcardModal));
  elements.btnNextRandom.addEventListener('click', loadRandomCardIntoModal);
  elements.btnRevealFlashcard.addEventListener('click', revealFlashcard);

  // Zamykanie modali po kliknięciu w tło
  [elements.guideModal, elements.flashcardModal].forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal(modal);
    });
  });

  // Klawisz Escape zamyka modale
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeModal(elements.guideModal);
      closeModal(elements.flashcardModal);
    }
  });

  // Delegacja zdarzeń wewnątrz kontenera kart (Kopiowanie, Ulubione, Kliknięcie w motyw)
  elements.cardsContainer.addEventListener('click', (e) => {
    // 1. Dodaj / Usuń z ulubionych
    const favBtn = e.target.closest('.btn-fav');
    if (favBtn) {
      const id = favBtn.dataset.id;
      toggleFavorite(id, favBtn);
      return;
    }

    // 2. Kopiuj całą lekturę do notatek
    const copyCardBtn = e.target.closest('.btn-copy-card');
    if (copyCardBtn) {
      const id = copyCardBtn.dataset.id;
      copyLekturaMarkdown(id);
      return;
    }

    // 3. Kopiuj pojedynczy kontekst
    const copyContextBtn = e.target.closest('.btn-copy-context');
    if (copyContextBtn) {
      const textToCopy = copyContextBtn.dataset.copyText;
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast('📋 Skopiowano kontekst do schowka!');
      });
      return;
    }

    // 4. Kliknięcie w motyw literacki (szybkie wyszukanie)
    const motifTag = e.target.closest('.motif-tag');
    if (motifTag) {
      const motif = motifTag.dataset.motif;
      elements.searchInput.value = motif;
      state.searchQuery = motif.toLowerCase();
      renderCards();
      window.scrollTo({ top: elements.searchInput.offsetTop - 80, behavior: 'smooth' });
      showToast(`Filtruję po motywie: "${motif}"`);
      return;
    }
  });

  // ==========================================
  // Funkcje renderujące i filtrujące
  // ==========================================

  function getFilteredLektury() {
    return LEKTURY_DATA.filter(item => {
      // Filtr kategorii
      if (state.selectedCategory !== 'all' && item.kategoria !== state.selectedCategory) {
        return false;
      }

      // Filtr epoki
      if (state.selectedEpoka !== 'all' && item.epoka !== state.selectedEpoka) {
        return false;
      }

      // Filtr ulubionych
      if (state.showFavoritesOnly && !state.favorites.includes(item.id)) {
        return false;
      }

      // Filtr typu kontekstu
      if (state.selectedContextType !== 'all') {
        const hasContextType = item.konteksty.some(k => 
          k.typ.toLowerCase().includes(state.selectedContextType.toLowerCase())
        );
        if (!hasContextType) return false;
      }

      // Wyszukiwanie tekstowe
      if (state.searchQuery) {
        const query = state.searchQuery;
        const matchesTitle = item.tytul.toLowerCase().includes(query);
        const matchesAuthor = item.autor.toLowerCase().includes(query);
        const matchesGenre = item.gatunek.toLowerCase().includes(query);
        const matchesSynteza = item.synteza.toLowerCase().includes(query);
        const matchesMotif = item.motywy.some(m => m.toLowerCase().includes(query));
        const matchesContext = item.konteksty.some(k => 
          k.tytul.toLowerCase().includes(query) ||
          (k.zrodloZewnetrzne && k.zrodloZewnetrzne.toLowerCase().includes(query)) ||
          k.opis.toLowerCase().includes(query) ||
          k.funkcja.toLowerCase().includes(query) ||
          k.typ.toLowerCase().includes(query)
        );
        const matchesTopics = item.tematyMaturalne.some(t => t.toLowerCase().includes(query));

        if (!matchesTitle && !matchesAuthor && !matchesGenre && !matchesSynteza && !matchesMotif && !matchesContext && !matchesTopics) {
          return false;
        }
      }

      return true;
    });
  }

  function renderCards() {
    const filtered = getFilteredLektury();

    // Licznik
    elements.activeCountText.textContent = `Wyświetlam ${filtered.length} z ${LEKTURY_DATA.length} lektur`;

    if (filtered.length === 0) {
      elements.cardsContainer.innerHTML = '';
      elements.emptyState.style.display = 'block';
      return;
    }

    elements.emptyState.style.display = 'none';

    const html = filtered.map(item => {
      const isFav = state.favorites.includes(item.id);
      
      return `
        <article class="lektura-card" id="card-${item.id}">
          <div class="card-header">
            <div class="card-title-group">
              <div class="badge-row">
                <span class="badge badge-${item.kategoria}">${item.kategoriaNazwa}</span>
                <span class="badge badge-epoka">🏛️ ${item.epoka}</span>
              </div>
              <h2 class="card-title">${escapeHTML(item.tytul)}</h2>
              <div class="card-author">✍️ ${escapeHTML(item.autor)}</div>
            </div>
            <div class="card-actions-top">
              <button class="btn-fav ${isFav ? 'active' : ''}" data-id="${item.id}" title="${isFav ? 'Usuń z powtórek' : 'Dodaj do powtórek'}">
                ${isFav ? '★' : '☆'}
              </button>
              <button class="btn-copy-card" data-id="${item.id}" title="Kopiuj lekturę i konteksty do notatek">
                📋
              </button>
            </div>
          </div>

          <div class="card-overview">
            <div class="overview-genre">📖 Gatunek: ${escapeHTML(item.gatunek)}</div>
            <p class="overview-synteza">${escapeHTML(item.synteza)}</p>
          </div>

          <div class="motifs-container">
            <span class="motif-label">Kluczowe motywy:</span>
            ${item.motywy.map(motif => `
              <span class="motif-tag" data-motif="${escapeHTML(motif)}">#${escapeHTML(motif)}</span>
            `).join('')}
          </div>

          <div class="contexts-section-title">
            <span>🎯 3 Konteksty Interpretacyjne do Matury</span>
            <span style="font-size: 0.8rem; font-weight: normal; color: var(--text-muted);">Gotowe argumenty do wypracowania</span>
          </div>

          <div class="contexts-grid">
            ${item.konteksty.map((kontekst, index) => {
              const fullContextMarkdown = `**${escapeHTML(item.tytul)} - Kontekst ${index + 1}: ${escapeHTML(kontekst.tytul)} (${kontekst.typ})**\n- **Wiedza zewnętrzna:** ${kontekst.zrodloZewnetrzne}\n- **Opis:** ${kontekst.opis}\n- **Funkcja na maturze:** ${kontekst.funkcja}`;
              return `
                <div class="context-box">
                  <div class="context-header">
                    <span class="context-num">Kontekst ${index + 1} / 3</span>
                    <span class="context-type-badge">${escapeHTML(kontekst.typ)}</span>
                  </div>
                  <h3 class="context-title">${escapeHTML(kontekst.tytul)}</h3>
                  <div class="context-external-source">
                    <span class="source-icon">🏛️</span>
                    <div class="source-content">
                      <span class="source-label">Wiedza zewnętrzna wobec dzieła:</span>
                      <span class="source-text">${escapeHTML(kontekst.zrodloZewnetrzne)}</span>
                    </div>
                  </div>
                  <p class="context-desc">${escapeHTML(kontekst.opis)}</p>
                  <div class="context-function-box">
                    <div class="function-label">🎯 Sfunkcjonalizowanie na maturze:</div>
                    <div>${escapeHTML(kontekst.funkcja)}</div>
                  </div>
                  <button class="btn-copy-context" data-copy-text="${escapeAttribute(fullContextMarkdown)}" title="Kopiuj ten kontekst">
                    📄 Kopiuj kontekst
                  </button>
                </div>
              `;
            }).join('')}
          </div>

          <div class="card-matura-topics">
            <div class="topics-title">💡 Przykładowe tematy wypracowań i pytania maturalne:</div>
            <ul class="topics-list">
              ${item.tematyMaturalne.map(topic => `
                <li class="topic-item">${escapeHTML(topic)}</li>
              `).join('')}
            </ul>
          </div>
        </article>
      `;
    }).join('');

    elements.cardsContainer.innerHTML = html;
  }

  function updateCategoryCounts() {
    const totalCount = LEKTURY_DATA.length;
    const podstawowyCount = LEKTURY_DATA.filter(i => i.kategoria === 'podstawowy').length;
    const spCount = LEKTURY_DATA.filter(i => i.kategoria === 'podstawowa-szkola').length;
    const dodatkoweCount = LEKTURY_DATA.filter(i => i.kategoria === 'dodatkowy').length;

    const countAll = document.getElementById('countAll');
    const countPodstawowy = document.getElementById('countPodstawowy');
    const countSP = document.getElementById('countSP');
    const countDodatkowe = document.getElementById('countDodatkowe');

    if (countAll) countAll.textContent = totalCount;
    if (countPodstawowy) countPodstawowy.textContent = podstawowyCount;
    if (countSP) countSP.textContent = spCount;
    if (countDodatkowe) countDodatkowe.textContent = dodatkoweCount;
  }

  function resetFilters() {
    elements.searchInput.value = '';
    state.searchQuery = '';
    state.selectedCategory = 'all';
    state.selectedEpoka = 'all';
    state.selectedContextType = 'all';
    state.showFavoritesOnly = false;

    elements.categoryPills.forEach(p => p.classList.remove('active'));
    elements.categoryPills[0].classList.add('active');
    elements.epokaFilter.value = 'all';
    elements.contextTypeFilter.value = 'all';
    elements.btnToggleFavorites.classList.remove('active', 'btn-primary');
    elements.btnToggleFavorites.classList.add('btn-secondary');

    renderCards();
    showToast('🔄 Zresetowano wszystkie filtry');
  }

  // ==========================================
  // Zarządzanie Ulubionymi
  // ==========================================

  function toggleFavorite(id, btnElement) {
    const index = state.favorites.indexOf(id);
    if (index === -1) {
      state.favorites.push(id);
      btnElement.classList.add('active');
      btnElement.innerHTML = '★';
      btnElement.title = 'Usuń z powtórek';
      showToast('⭐ Dodano lekturę do powtórek!');
    } else {
      state.favorites.splice(index, 1);
      btnElement.classList.remove('active');
      btnElement.innerHTML = '☆';
      btnElement.title = 'Dodaj do powtórek';
      showToast('Usunięto z powtórek');
      if (state.showFavoritesOnly) {
        renderCards();
      }
    }
    localStorage.setItem('matura_lektury_favs', JSON.stringify(state.favorites));
  }

  // ==========================================
  // Kopiowanie do schowka
  // ==========================================

  function copyLekturaMarkdown(id) {
    const item = LEKTURY_DATA.find(l => l.id === id);
    if (!item) return;

    let md = `# ${item.tytul}\n`;
    md += `**Autor:** ${item.autor} | **Epoka:** ${item.epoka} | **Gatunek:** ${item.gatunek}\n`;
    md += `**Kategoria CKE:** ${item.kategoriaNazwa}\n\n`;
    md += `## Problematyka:\n${item.synteza}\n\n`;
    md += `## 3 Konteksty interpretacyjne:\n\n`;

    item.konteksty.forEach((k, idx) => {
      md += `### ${idx + 1}. [${k.typ}] ${k.tytul}\n`;
      md += `- **Wiedza zewnętrzna:** ${k.zrodloZewnetrzne}\n`;
      md += `- **Opis:** ${k.opis}\n`;
      md += `> **Sfunkcjonalizowanie na maturze:** ${k.funkcja}\n\n`;
    });

    md += `## Przykładowe tematy maturalne:\n`;
    item.tematyMaturalne.forEach(t => {
      md += `- ${t}\n`;
    });

    navigator.clipboard.writeText(md).then(() => {
      showToast(`📋 Skopiowano cały zestaw kontekstów dla: ${item.tytul}`);
    });
  }

  // ==========================================
  // Tryb Fiszki / Randomizer
  // ==========================================

  let currentRandomItem = null;

  function openRandomizerModal() {
    loadRandomCardIntoModal();
    openModal(elements.flashcardModal);
  }

  function loadRandomCardIntoModal() {
    const pool = state.showFavoritesOnly && state.favorites.length > 0
      ? LEKTURY_DATA.filter(l => state.favorites.includes(l.id))
      : LEKTURY_DATA;

    const randomIndex = Math.floor(Math.random() * pool.length);
    currentRandomItem = pool[randomIndex];

    elements.btnRevealFlashcard.style.display = 'inline-flex';
    elements.btnNextRandom.textContent = '🎲 Losuj inną';

    elements.flashcardBody.innerHTML = `
      <div class="flashcard-cover" id="flashcardCover">
        <span class="badge badge-${currentRandomItem.kategoria}" style="margin-bottom: 0.5rem; display: inline-block;">${currentRandomItem.kategoriaNazwa}</span>
        <div style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 0.25rem;">🏛️ Epoka: ${currentRandomItem.epoka}</div>
        <h2 style="font-family: var(--font-serif); font-size: 1.6rem; color: var(--text-main); margin-bottom: 0.25rem;">${escapeHTML(currentRandomItem.tytul)}</h2>
        <div style="font-size: 1.1rem; font-weight: 600; color: var(--primary); margin-bottom: 1rem;">✍️ ${escapeHTML(currentRandomItem.autor)}</div>
        
        <div style="font-size: 0.9rem; color: var(--text-soft); max-width: 500px; margin: 0 auto 1.5rem; line-height: 1.5;">
          ${escapeHTML(currentRandomItem.synteza)}
        </div>

        <div class="flashcard-prompt">
          🧠 Sprawdź się! Jakie 3 konteksty dopasujesz do tej lektury?
        </div>
      </div>

      <div class="flashcard-content" id="flashcardRevealed">
        <div class="contexts-section-title" style="margin-bottom: 1rem;">
          <span>🎯 Sprawdź 3 konteksty:</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          ${currentRandomItem.konteksty.map((k, idx) => `
            <div class="context-box">
              <div class="context-header">
                <span class="context-num">Kontekst ${idx + 1} / 3</span>
                <span class="context-type-badge">${escapeHTML(k.typ)}</span>
              </div>
              <h4 class="context-title">${escapeHTML(k.tytul)}</h4>
              <div class="context-external-source">
                <span class="source-icon">🏛️</span>
                <div class="source-content">
                  <span class="source-label">Wiedza zewnętrzna wobec dzieła:</span>
                  <span class="source-text">${escapeHTML(k.zrodloZewnetrzne)}</span>
                </div>
              </div>
              <p class="context-desc">${escapeHTML(k.opis)}</p>
              <div class="context-function-box">
                <div class="function-label">🎯 Sfunkcjonalizowanie na maturze:</div>
                <div>${escapeHTML(k.funkcja)}</div>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  function revealFlashcard() {
    const revealedEl = document.getElementById('flashcardRevealed');
    if (revealedEl) {
      revealedEl.classList.add('revealed');
      elements.btnRevealFlashcard.style.display = 'none';
      elements.btnNextRandom.textContent = '🎲 Następna lektura';
    }
  }

  // ==========================================
  // Modale pomocnicze
  // ==========================================

  function openModal(modalEl) {
    modalEl.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal(modalEl) {
    modalEl.classList.remove('active');
    document.body.style.overflow = '';
  }

  // ==========================================
  // Motyw (Dark / Light)
  // ==========================================

  function initTheme() {
    document.documentElement.setAttribute('data-theme', state.theme);
    updateThemeIcon();
  }

  function toggleTheme() {
    state.theme = state.theme === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', state.theme);
    localStorage.setItem('matura_theme', state.theme);
    updateThemeIcon();
    showToast(state.theme === 'dark' ? '🌙 Włączono tryb ciemny' : '☀️ Włączono tryb jasny');
  }

  function updateThemeIcon() {
    if (elements.themeIcon) {
      elements.themeIcon.textContent = state.theme === 'dark' ? '☀️' : '🌙';
    }
  }

  // ==========================================
  // Powiadomienia Toast
  // ==========================================

  function showToast(message) {
    if (!elements.toastContainer) return;
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    elements.toastContainer.appendChild(toast);

    setTimeout(() => {
      toast.remove();
    }, 3000);
  }

  // ==========================================
  // Narzędzia sanityzacji tekstu
  // ==========================================

  function escapeHTML(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function escapeAttribute(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
});
