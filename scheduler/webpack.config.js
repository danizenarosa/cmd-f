const path = require('path')
const webpack = require('webpack')

module.exports = {

    entry: {
      main: path.resolve(__dirname, 'src/App.jsx'),
    },
    mode: 'development',
    output: {
      path: path.resolve(__dirname, '../main/'),
      filename: '[name].js',
    },
    "scripts" : {
        "dev": "webpack --watch --config webpack.config.js"
    },
    plugins: [
      // Don't output new files if there is an error
      new webpack.NoEmitOnErrorsPlugin(),
    ],
    // Where find modules that can be imported (eg. React) 
    resolve: {
      extensions: ['*', '.js', '.jsx'],
      modules: [
          path.resolve(__dirname, 'src'),
          path.resolve(__dirname, 'node_modules'),
      ],
    },
  }