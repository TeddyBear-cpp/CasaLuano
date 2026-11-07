import Lenis from 'lenis';

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let lenis = null;

const syncSmoothScroll = () => {
  if (reduceMotion.matches) {
    lenis?.destroy();
    lenis = null;
    return;
  }
  if (lenis) return;
  lenis = new Lenis({
    autoRaf: true,
    anchors: true,
    lerp: 0.12,
    syncTouch: false,
    stopInertiaOnNavigate: true,
  });
};

syncSmoothScroll();
reduceMotion.addEventListener?.('change', syncSmoothScroll);

const header = document.querySelector('.site-header');
const menuToggle = document.querySelector('.menu-toggle');

if (header) {
  const updateHeader = () => header.classList.toggle('is-scrolled', window.scrollY > 16);
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });
}

if (header && menuToggle) {
  const closeMenu = () => {
    header.classList.remove('menu-open');
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', 'Open navigation');
  };
  menuToggle.addEventListener('click', () => {
    const open = !header.classList.contains('menu-open');
    header.classList.toggle('menu-open', open);
    menuToggle.setAttribute('aria-expanded', String(open));
    menuToggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  });
  header.querySelectorAll('.nav-links a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') closeMenu();
  });
}

const reveals = [...document.querySelectorAll('.reveal, .intro-visual')];
if ('IntersectionObserver' in window && !reduceMotion.matches) {
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px 40px 0px' });
  reveals.forEach(element => revealObserver.observe(element));
  let revealFrame = 0;
  const revealPassedSections = () => {
    if (revealFrame) return;
    revealFrame = requestAnimationFrame(() => {
      revealFrame = 0;
      reveals.forEach(element => {
        if (element.classList.contains('in-view')) return;
        if (element.getBoundingClientRect().top < window.innerHeight * 0.9) {
          element.classList.add('in-view');
          revealObserver.unobserve(element);
        }
      });
    });
  };
  window.addEventListener('scroll', revealPassedSections, { passive: true });
  revealPassedSections();
} else {
  reveals.forEach(element => element.classList.add('in-view'));
}

document.querySelectorAll('[data-autoplay-video]').forEach(video => {
  const frame = video.closest('.film-frame');
  const control = frame?.querySelector('.video-control');
  let userPaused = false;
  let inView = true;
  video.muted = true;

  const setControl = paused => {
    if (!control) return;
    control.classList.toggle('is-paused', paused);
    control.setAttribute('aria-label', paused ? 'Play video' : 'Pause video');
    control.setAttribute('aria-pressed', String(!paused));
  };

  const syncPlayback = () => {
    if (reduceMotion.matches || userPaused || !inView || document.hidden) {
      video.pause();
      setControl(true);
      return;
    }
    video.play().then(() => setControl(false)).catch(() => setControl(true));
  };

  if (control) {
    control.addEventListener('click', () => {
      userPaused = !video.paused ? true : false;
      syncPlayback();
    });
  }

  if ('IntersectionObserver' in window) {
    const videoObserver = new IntersectionObserver(entries => {
      inView = entries[0]?.isIntersecting ?? false;
      syncPlayback();
    }, { threshold: 0.3 });
    videoObserver.observe(video);
  } else {
    syncPlayback();
  }
  document.addEventListener('visibilitychange', syncPlayback);
  reduceMotion.addEventListener?.('change', syncPlayback);
});

const wheels = [...document.querySelectorAll('[data-pottery-wheel]')];
for (const rotor of wheels) {
  let angle = 0;
  let lastPointerAngle = null;
  let dragging = false;

  const draw = () => {
    rotor.style.setProperty('--wheel-angle', `${angle}deg`);
    rotor.setAttribute('aria-valuenow', String(Math.round(((angle % 360) + 360) % 360)));
    rotor.setAttribute('aria-valuetext', `Turned ${Math.round(((angle % 360) + 360) % 360)} degrees`);
  };
  const pointerAngle = event => {
    const rect = rotor.getBoundingClientRect();
    const x = event.clientX - (rect.left + rect.width / 2);
    const y = event.clientY - (rect.top + rect.height / 2);
    return Math.atan2(y, x) * 180 / Math.PI;
  };
  const normalizeDelta = delta => ((delta + 540) % 360) - 180;

  rotor.addEventListener('pointerdown', event => {
    dragging = true;
    lastPointerAngle = pointerAngle(event);
    rotor.setPointerCapture(event.pointerId);
  });
  rotor.addEventListener('pointermove', event => {
    if (!dragging || lastPointerAngle === null) return;
    const next = pointerAngle(event);
    angle += normalizeDelta(next - lastPointerAngle);
    lastPointerAngle = next;
    draw();
  });
  const release = () => { dragging = false; lastPointerAngle = null; };
  rotor.addEventListener('pointerup', release);
  rotor.addEventListener('pointercancel', release);
  rotor.addEventListener('lostpointercapture', release);

  rotor.addEventListener('keydown', event => {
    if (event.key === 'ArrowRight' || event.key === 'ArrowUp') {
      event.preventDefault();
      angle += 20;
      draw();
    } else if (event.key === 'ArrowLeft' || event.key === 'ArrowDown') {
      event.preventDefault();
      angle -= 20;
      draw();
    } else if (event.key === 'Home') {
      event.preventDefault();
      angle = 0;
      draw();
    }
  });

  let lastScroll = window.scrollY;
  const spinOnScroll = () => {
    const current = window.scrollY;
    const delta = current - lastScroll;
    lastScroll = current;
    if (reduceMotion.matches || dragging || Math.abs(delta) > window.innerHeight * 1.5) return;
    const rect = rotor.getBoundingClientRect();
    if (rect.bottom < 0 || rect.top > window.innerHeight) return;
    angle += delta * 0.18;
    draw();
  };
  window.addEventListener('scroll', spinOnScroll, { passive: true });
  draw();
}
