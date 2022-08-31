const path = require('path')
function resolve (dir) {
  return path.join(__dirname, dir)
}

module.exports = {
  publicPath:'/',
  outputDir:'dist',
  assetsDir:'static',
  lintOnSave:false,
  productionSourceMap: false,
  devServer: {
    port: 8888,
    open: true,
    overlay: {
      warnings: false,
      errors: true
    },
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        ws: true,
      }
    }
    // disableHostCheck: true,
  },
  lintOnSave:false,
  transpileDependencies: ['vuetify'],
}
