// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//     transpileDependencies: true
// }, )
module.exports = {
    // publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
    configureWebpack: {
        // other webpack options to merge in ...
    },
    // devServer Options don't belong into `configureWebpack`
    publicPath: '/',

    devServer: {
        host: "0.0.0.0",
        port: 8080,
        hot: true,
        // disableHostCheck: true,
    }
};