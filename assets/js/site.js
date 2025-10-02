document.addEventListener("DOMContentLoaded", () => {
  const carousels = Array.from(document.querySelectorAll("[data-carousel]"));
  carousels.forEach(initCarousel);
});

function initCarousel(carousel) {
  const ring = carousel.querySelector(".orbit-ring");
  const cards = Array.from(carousel.querySelectorAll(".orbit-card"));
  if (!ring || cards.length === 0) return;

  let index = 0;
  let autoRotateId;
  let radius = parseInt(carousel.dataset.radius || 400, 10);

  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const updateRadius = () => {
    const width = window.innerWidth;
    if (width < 640) {
      radius = 160;
    } else if (width < 980) {
      radius = 260;
    } else {
      radius = parseInt(carousel.dataset.radius || 400, 10);
    }
  };

  const render = () => {
    const step = 360 / cards.length;
    cards.forEach((card, i) => {
      const angle = step * (i - index);
      const transform = `rotateY(${angle}deg) translateZ(${radius}px)`;
      card.style.transform = transform;
      card.style.zIndex = `${cards.length - Math.abs(Math.round(angle / step))}`;
      card.classList.toggle("is-active", i === index);
      card.style.opacity = Math.abs(angle) > 150 ? 0 : Math.abs(angle) > 90 ? 0.25 : 1;
    });
  };

  const next = () => {
    index = (index + 1) % cards.length;
    render();
  };

  const prev = () => {
    index = (index - 1 + cards.length) % cards.length;
    render();
  };

  const startAuto = () => {
    if (prefersReduced) return;
    stopAuto();
    autoRotateId = window.setInterval(next, 6000);
  };

  const stopAuto = () => {
    if (autoRotateId) {
      window.clearInterval(autoRotateId);
      autoRotateId = undefined;
    }
  };

  carousel.querySelectorAll("[data-action='next']").forEach((btn) => btn.addEventListener("click", () => {
    stopAuto();
    next();
    startAuto();
  }));

  carousel.querySelectorAll("[data-action='prev']").forEach((btn) => btn.addEventListener("click", () => {
    stopAuto();
    prev();
    startAuto();
  }));

  cards.forEach((card, i) => {
    card.addEventListener("click", (event) => {
      if (i !== index) {
        event.preventDefault();
        index = i;
        render();
      }
    });

    card.addEventListener("mouseenter", () => {
      stopAuto();
      index = i;
      render();
    });

    card.addEventListener("mouseleave", () => {
      startAuto();
    });
  });

  carousel.addEventListener("mouseenter", stopAuto);
  carousel.addEventListener("mouseleave", startAuto);
  window.addEventListener("resize", () => {
    updateRadius();
    render();
  });

  updateRadius();
  render();
  startAuto();
}
