// tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './**/templates/**/*.html', // Quét tất cả file .html trong thư mục templates của mọi app
      './**/templates/*.html',
  ],
  darkMode: 'class', // Enable dark mode with class strategy
  theme: {
    extend: {},
  },
  plugins: [],
}