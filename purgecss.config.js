module.exports = {
    content: [
      './**/templates/**/*.html', // Include all templates across all apps
      './**/static/**/*.js',      // Include all JavaScript files across all apps
      './**/*.py',                // Include Python files to catch inline CSS in strings
    ],
    css: ['./**/static/**/*.css'], // Include all CSS files in the static folders
    output: './cleaned-css/',      // Output cleaned CSS to a dedicated directory
    safelist: {                    // Optional: Define classes or selectors to exclude from purging
      standard: ['active', 'open', 'nav-item'], 
    },
  };
  