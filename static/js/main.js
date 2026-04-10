/**
 * Ambika Mahavidyalaya – Main JavaScript
 * Features:
 *  - Navbar scroll effect
 *  - Mobile menu toggle
 *  - Language switcher (URL redirect)
 *  - Hero slider (via Swiper)
 *  - Lightbox gallery
 *  - Scroll-to-top
 *  - AOS-lite (scroll reveal)
 */

// ─────────────────────────────────────────────
// Navbar: add shadow on scroll
// ─────────────────────────────────────────────
const navbar = document.getElementById("main-nav");
window.addEventListener("scroll", () => {
  if (window.scrollY > 80) {
    navbar?.classList.add("scrolled", "bg-white/95", "shadow-sm");
    navbar?.classList.remove("bg-transparent", "py-6");
    navbar?.classList.add("py-4");
  } else {
    navbar?.classList.remove("scrolled", "bg-white/95", "shadow-sm", "py-4");
    navbar?.classList.add("bg-transparent", "py-6");
  }
});

// ─────────────────────────────────────────────
// Mobile Menu
// ─────────────────────────────────────────────
const menuBtn   = document.getElementById("menu-btn");
const mobileMenu = document.getElementById("mobile-menu");
const closeMenu = document.getElementById("close-menu");

menuBtn?.addEventListener("click", () => {
  mobileMenu?.classList.add("open");
  document.body.style.overflow = "hidden";
});

closeMenu?.addEventListener("click", closeMobileMenu);
mobileMenu?.addEventListener("click", (e) => {
  if (e.target === mobileMenu) closeMobileMenu();
});

function closeMobileMenu() {
  mobileMenu?.classList.remove("open");
  document.body.style.overflow = "";
}

// ─────────────────────────────────────────────
// Language Switcher
// ─────────────────────────────────────────────
document.querySelectorAll("[data-lang]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const lang = btn.dataset.lang;
    const currentPath = window.location.pathname;

    // Build new URL: swap language prefix
    // Pattern: /(en|gu)/... or /...
    let newPath;
    const langRegex = /^\/(en|gu)(\/.*)?$/;
    const match     = currentPath.match(langRegex);

    if (match) {
      newPath = `/${lang}${match[2] || "/"}`;
    } else {
      newPath = `/${lang}${currentPath}`;
    }

    // Store preference
    localStorage.setItem("preferred_lang", lang);
    window.location.href = newPath;
  });
});

// ─────────────────────────────────────────────
// Hero Slider (Swiper)
// ─────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  // 1. Hero / Header Swiper
  if (typeof Swiper !== "undefined" && document.querySelector(".header-swiper")) {
    new Swiper(".header-swiper", {
      loop: true,
      autoplay: { delay: 6000, disableOnInteraction: false },
      effect: "fade",
      fadeEffect: { crossFade: true },
      pagination: { el: ".swiper-pagination", clickable: true },
      speed: 1200,
    });
  }

  // 2. Testimonial Swiper
  if (typeof Swiper !== "undefined" && document.querySelector(".testimonial-swiper")) {
    new Swiper(".testimonial-swiper", {
      loop: true,
      spaceBetween: 30,
      autoplay: { delay: 4000 },
      pagination: { el: ".swiper-pagination", clickable: true },
      breakpoints: {
        640: { slidesPerView: 1 },
        1024: { slidesPerView: 1 }
      }
    });
  }

  // 3. Simple Image Swiper
  if (typeof Swiper !== "undefined" && document.querySelector(".image-swiper")) {
    new Swiper(".image-swiper", {
      loop: true,
      slidesPerView: 1,
      spaceBetween: 20,
      navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
      breakpoints: {
        768: { slidesPerView: 2 },
        1024: { slidesPerView: 3 }
      }
    });
  }
});

// ─────────────────────────────────────────────
// Lightbox Gallery
// ─────────────────────────────────────────────
const lightboxOverlay = document.getElementById("lightbox-overlay");
const lightboxImg     = document.getElementById("lightbox-img");
const lightboxCaption = document.getElementById("lightbox-caption");
const lightboxClose   = document.getElementById("lightbox-close");
const lightboxPrev    = document.getElementById("lightbox-prev");
const lightboxNext    = document.getElementById("lightbox-next");

let galleryItems = [];
let currentIndex = 0;

document.querySelectorAll(".gallery-item").forEach((item, idx) => {
  item.addEventListener("click", () => openLightbox(idx));
  galleryItems.push({
    src:     item.dataset.src || item.querySelector("img")?.src,
    caption: item.dataset.caption || "",
  });
});

function openLightbox(idx) {
  currentIndex = idx;
  updateLightbox();
  lightboxOverlay?.classList.add("active");
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  lightboxOverlay?.classList.remove("active");
  document.body.style.overflow = "";
}

function updateLightbox() {
  const item = galleryItems[currentIndex];
  if (lightboxImg)     lightboxImg.src = item.src;
  if (lightboxCaption) lightboxCaption.textContent = item.caption;
}

lightboxClose?.addEventListener("click", closeLightbox);
lightboxOverlay?.addEventListener("click", (e) => {
  if (e.target === lightboxOverlay) closeLightbox();
});

lightboxPrev?.addEventListener("click", () => {
  currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length;
  updateLightbox();
});

lightboxNext?.addEventListener("click", () => {
  currentIndex = (currentIndex + 1) % galleryItems.length;
  updateLightbox();
});

// Keyboard navigation
document.addEventListener("keydown", (e) => {
  if (!lightboxOverlay?.classList.contains("active")) return;
  if (e.key === "Escape")      closeLightbox();
  if (e.key === "ArrowLeft")   { currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length; updateLightbox(); }
  if (e.key === "ArrowRight")  { currentIndex = (currentIndex + 1) % galleryItems.length; updateLightbox(); }
});

// ─────────────────────────────────────────────
// Gallery filter tabs
// ─────────────────────────────────────────────
document.querySelectorAll("[data-filter]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const filter = btn.dataset.filter;

    document.querySelectorAll("[data-filter]").forEach((b) => {
      b.classList.remove("active", "bg-saffron-500", "text-white");
      b.classList.add("border-saffron-300", "text-saffron-700");
    });
    btn.classList.add("active", "bg-saffron-500", "text-white");
    btn.classList.remove("border-saffron-300", "text-saffron-700");

    document.querySelectorAll(".gallery-item").forEach((item) => {
      if (filter === "all" || item.dataset.category === filter) {
        item.style.display = "";
        item.classList.add("animate-fade-in");
      } else {
        item.style.display = "none";
      }
    });
  });
});



// ─────────────────────────────────────────────
// Simple "AOS" scroll reveal
// ─────────────────────────────────────────────
const revealElements = document.querySelectorAll("[data-aos]");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("aos-animate");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1, rootMargin: "0px 0px -40px 0px" }
);

revealElements.forEach((el) => observer.observe(el));

// ─────────────────────────────────────────────
// Interactive Om Particle Background
// ─────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("om-particles");
  if (container) {
    const particleCount = 40;
    // We mix some drifting animations
    const animations = ["animate-drift-1", "animate-drift-2", "animate-drift-3", "animate-float-slow", "animate-float-slower"];
    
    for (let i = 0; i < particleCount; i++) {
      const om = document.createElement("div");
      om.textContent = "ॐ";
      
      // Select a random drifting animation
      const r_anim = animations[Math.floor(Math.random() * animations.length)];
      
      // Base tailwind classes for an ultra-premium spiritual aesthetic
      // Adding a slight blur that snaps into focus, a golden base color instead of grey, and a radiant glow on hover
      om.className = `absolute text-2xl md:text-4xl font-serif text-accent-500/20 ${r_anim} pointer-events-auto transition-all duration-1000 ease-out hover:text-accent-400 hover:opacity-100 hover:scale-[2.5] hover:-translate-y-6 hover:-rotate-12 cursor-default select-none blur-[1px] hover:blur-none drop-shadow-sm hover:drop-shadow-[0_0_25px_rgba(245,158,11,0.8)] filter`;
      
      // Scatter them randomly across viewport dimensions (they'll drift from these starting spots)
      om.style.top = Math.random() * 100 + "%";
      om.style.left = Math.random() * 100 + "%";
      om.style.animationDelay = (Math.random() * 15) + "s";
      
      container.appendChild(om);
    }
  }
});

// ─────────────────────────────────────────────
// Contact form – character counter
// ─────────────────────────────────────────────
const msgTextarea = document.getElementById("id_message");
if (msgTextarea) {
  msgTextarea.addEventListener("input", () => {
    const counter = document.getElementById("msg-counter");
    if (counter) counter.textContent = msgTextarea.value.length;
  });
}
