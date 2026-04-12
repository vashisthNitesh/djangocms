/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/*.py',
    './static/js/**/*.js',
    './ambika/**/*.py',
    './static/src/input.css',
  ],
  theme: {
    extend: {
      colors: {
        slate: { // Oxford Navy Blue / Prestige Palette
          50: '#F7F9FC', // Off-white, extremely clean
          100: '#E8ECF2',
          200: '#CDD5E1',
          300: '#A3B4C9',
          400: '#738BA9',
          500: '#4D6B8C',
          600: '#375373',
          700: '#28415B',
          800: '#1C2E42',
          900: '#0F1A28', // Deep Oxford Blue
        },
        accent: { // Royal Gold / Saffron
          50: '#FDFBF4',
          100: '#FAF5DF',
          200: '#F2E5B1',
          300: '#E7CF7B',
          400: '#DBB14B',
          500: '#C98D26', // Perfect classic Royal Gold/Saffron
          600: '#B06F1D',
          700: '#8C521A',
          800: '#704219',
          900: '#5A3718',
        },
      },
      fontFamily: {
        'sans': ['"Inter"', '"Noto Sans Gujarati"', 'sans-serif'],
        'display': ['"Lora"', '"Playfair Display"', 'serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.8s ease-in-out',
        'slide-up': 'slideUp 0.8s ease-out',
        'slide-down': 'slideDown 0.8s ease-out',
        'drift-1': 'drift1 40s ease-in-out infinite',
        'drift-2': 'drift2 45s ease-in-out infinite',
        'drift-3': 'drift3 50s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: { '0%': { opacity: 0 }, '100%': { opacity: 1 } },
        slideUp: { '0%': { opacity: 0, transform: 'translateY(40px)' }, '100%': { opacity: 1, transform: 'translateY(0)' } },
        slideDown: { '0%': { opacity: 0, transform: 'translateY(-40px)' }, '100%': { opacity: 1, transform: 'translateY(0)' } },
        drift1: {
          '0%, 100%': { transform: 'translate(0px, 0px) rotate(0deg)' },
          '33%': { transform: 'translate(150px, -150px) rotate(8deg)' },
          '66%': { transform: 'translate(-50px, 100px) rotate(-4deg)' },
        },
        drift2: {
          '0%, 100%': { transform: 'translate(0px, 0px) rotate(0deg)' },
          '33%': { transform: 'translate(-200px, -50px) rotate(-10deg)' },
          '66%': { transform: 'translate(100px, -150px) rotate(5deg)' },
        },
        drift3: {
          '0%, 100%': { transform: 'translate(0px, 0px) rotate(0deg)' },
          '33%': { transform: 'translate(100px, 200px) rotate(15deg)' },
          '66%': { transform: 'translate(-150px, 50px) rotate(-5deg)' },
        }
      },
      boxShadow: {
        'premium': '0 20px 40px -15px rgba(15, 23, 42, 0.1)',
      }
    },
  },
  plugins: [],
}
