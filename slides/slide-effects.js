(function () {
  let audioContext = null;

  function getAudioContext() {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return null;
    if (!audioContext) audioContext = new AudioContext();
    return audioContext;
  }

  function noiseBurst(ctx, start, duration, volume, frequency) {
    const sampleRate = ctx.sampleRate;
    const buffer = ctx.createBuffer(1, Math.max(1, sampleRate * duration), sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < data.length; i += 1) {
      data[i] = (Math.random() * 2 - 1) * (1 - i / data.length);
    }

    const source = ctx.createBufferSource();
    const filter = ctx.createBiquadFilter();
    const gain = ctx.createGain();

    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(frequency, start);
    filter.Q.setValueAtTime(0.8, start);
    gain.gain.setValueAtTime(volume, start);
    gain.gain.exponentialRampToValueAtTime(0.001, start + duration);

    source.buffer = buffer;
    source.connect(filter);
    filter.connect(gain);
    gain.connect(ctx.destination);
    source.start(start);
    source.stop(start + duration);
  }

  function tone(ctx, start, duration, volume, frequency, type) {
    const oscillator = ctx.createOscillator();
    const gain = ctx.createGain();

    oscillator.type = type;
    oscillator.frequency.setValueAtTime(frequency, start);
    oscillator.frequency.exponentialRampToValueAtTime(frequency * 0.58, start + duration);
    gain.gain.setValueAtTime(volume, start);
    gain.gain.exponentialRampToValueAtTime(0.001, start + duration);

    oscillator.connect(gain);
    gain.connect(ctx.destination);
    oscillator.start(start);
    oscillator.stop(start + duration);
  }

  function playSfx(kind) {
    const ctx = getAudioContext();
    if (!ctx) return;

    ctx.resume().then(() => {
      const now = ctx.currentTime;
      if (kind === 'none') return;

      if (kind === 'boing') {
        tone(ctx, now, 0.16, 0.12, 420, 'triangle');
        tone(ctx, now + 0.07, 0.12, 0.08, 620, 'sine');
        return;
      }

      noiseBurst(ctx, now, 0.045, 0.18, 1800);
      tone(ctx, now + 0.015, 0.09, 0.11, 140, 'square');
    }).catch(() => {});
  }

  function playForFragment(fragment) {
    if (!fragment) return;
    if (fragment.dataset && fragment.dataset.sfx) {
      playSfx(fragment.dataset.sfx);
      return;
    }

    const target = fragment.querySelector('[data-sfx]');
    if (target && target.dataset) {
      playSfx(target.dataset.sfx);
    }
  }

  function register() {
    if (!window.Reveal || !Reveal.on) {
      window.setTimeout(register, 100);
      return;
    }

    Reveal.on('fragmentshown', function (event) {
      playForFragment(event.fragment);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', register);
  } else {
    register();
  }
}());
