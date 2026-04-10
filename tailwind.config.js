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
        slate: { // Re-mapped to traditional warm/Parchment/Maroon theme
          50: '#FDFCFB',
          100: '#F9F6F0',
          200: '#EFE7D6',
          300: '#E1CFB1',
          400: '#CDB185',
          500: '#B8925A',
          600: '#9C7446',
          700: '#7D5135',
          800: '#4A2A22',
          900: '#2A1313', // Deep traditional maroon
        },
        accent: {
          50: '#FFFBEB',
          100: '#FEF3C7',
          200: '#FDE68A',
          300: '#FCD34D',
          400: '#FBBF24',
          500: '#F59E0B',
          600: '#D97706',
          700: '#B45309',
          800: '#92400E',
          900: '#78350F',
        },
      },
      fontFamily: {
        'sans': ['"Inter"', '"Noto Sans Gujarati"', 'sans-serif'],
        'display': ['"Outfit"', 'sans-serif'],
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
