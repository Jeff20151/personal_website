const igemShell = document.querySelector(".igem-shell");
if (igemShell) {
  const langButtons = igemShell.querySelectorAll(".lang-btn");
  const root = document.documentElement;
  const defaultLang = igemShell.dataset.lang || "zh";
  const savedLang = localStorage.getItem("igem-lang");

  setLanguage(savedLang || defaultLang, false);

  langButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      setLanguage(btn.dataset.lang, true);
    });
  });

  function setLanguage(lang, persist) {
    root.setAttribute("data-lang", lang);
    igemShell.setAttribute("data-lang", lang);
    langButtons.forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.lang === lang);
    });
    if (persist) {
      localStorage.setItem("igem-lang", lang);
    }
  }

  // Enable smooth hash scrolling within the iGEM page
  igemShell.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (event) => {
      const targetId = anchor.getAttribute("href");
      if (!targetId || targetId === "#") return;
      const el = igemShell.querySelector(targetId);
      if (!el) return;
      event.preventDefault();
      el.scrollIntoView({ behavior: "smooth" });
    });
  });
}
