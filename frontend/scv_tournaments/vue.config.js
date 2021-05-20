/**
 * @type {string}
 */
let apiHost;
//Use enviroment variable for docker setup, localhost for local dev
if (process.env.API_HOST) {
    apiHost = process.env.API_HOST
} else {
    apiHost = 'localhost'
}

module.exports = {
    devServer: {
        proxy: {
            "^/backend": {
                target: 'http://' + apiHost + ':8000',
                changeOrigin: true,
                logLevel: "debug",
                pathRewrite: {"^/backend": "/"}
            }
        }
    }
};