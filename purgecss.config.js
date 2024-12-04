module.exports = {
    content: [
      './**/templates/**/*.html',
      './**/static/**/*.js',    
      './**/*.py',                
    ],
    css: ['./**/static/**/*.css'], 
    output: './cleaned-css/',     
    safelist: {                  
      standard: ['active', 'open', 'nav-item'], 
    },
  };