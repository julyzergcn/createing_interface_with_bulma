module.exports = {
  plugins: [
    require('googlefonts-inliner')({
      localPath: './dist/fonts',
      webPath: '/static/fonts'
    }),
  ],
};
