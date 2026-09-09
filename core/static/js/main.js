  document.getElementById('year').textContent = new Date().getFullYear();

  const panels = {
    disenador: {
      html: `<b>Diseño de interfaces y branding,</b> con obsesión por el detalle. UX, identidad visual y edición — formado en Diseño Integral, PENTA UC.`,
      chips: ['UI/UX','Branding','Adobe CC','Motion']
    },
    dev: {
      html: `<b>Del prototipo al backend real.</b> HTML, CSS, JS, Bootstrap y Django — sin miedo a mancharme las manos de código.`,
      chips: ['Django','Python','JavaScript','Bootstrap']
    }
  };

  const heroPhoto = document.querySelector('.id-photo img');
  if (heroPhoto) {
    const palette = ['var(--line)', 'var(--hot)', 'var(--yolk)', 'var(--sky)', 'var(--violet)', 'var(--lime)'];
    const randomColor = palette[Math.floor(Math.random() * palette.length)];
    heroPhoto.style.setProperty('--cover-bg', randomColor);
    heroPhoto.style.background = randomColor;
  }

  const buttons = document.querySelectorAll('.mode-toggle button');
  const panel = document.getElementById('modePanel');
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const data = panels[btn.dataset.mode];
      panel.innerHTML = `${data.html}<div class="chips">${data.chips.map(c => `<span class="chip">${c}</span>`).join('')}</div>`;
    });
  });

  // sticker cluster drifts loosely with the cursor within the hero stage (solo existe en home)
  const cluster = document.querySelector('.sticker-cluster');
  const stage = document.querySelector('.sticker-stage');
  let tx = 0, ty = 0, cx = 0, cy = 0;
  if (stage && cluster && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    stage.addEventListener('mousemove', (e) => {
      const r = stage.getBoundingClientRect();
      tx = (e.clientX - r.left - r.width/2) * 0.05;
      ty = (e.clientY - r.top - r.height/2) * 0.05;
    });
    stage.addEventListener('mouseleave', () => { tx = 0; ty = 0; });
    function raf(){
      cx += (tx - cx) * 0.06;
      cy += (ty - cy) * 0.06;
      cluster.style.transform = `translate(${cx}px, ${cy}px)`;
      requestAnimationFrame(raf);
    }
    raf();
  }

