'use strict';

var path = require('path')
var webpack = require('webpack')

var ROOT = process.cwd();
var SRC = path.join(ROOT, 'demo');
var LIBRARY_NAME = 'other-library'
var BUILD_PATH = path.join(ROOT, 'lib');
var environment = 'development';

module.exports = {
  mode: 'development',
  module: {
    rules: [
      {
        test: /\.json$/,
        loader: 'json-loader'
      },
      {
        test: /\.jsx?$/,
        include: [SRC],
        /*
         * Use require.resolve to get a deterministic path
         * and avoid webpack's magick loader resolution
         */
        use: [
          {
            loader: 'babel-loader'
          }
        ]
      }
    ],
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify(environment)
      }
    })
  ],
  entry: {
    bundle: [path.join(SRC, 'index.js')],
  },
  devServer: {
    contentBase: SRC
  },
  output: {
    // library: LIBRARY_NAME,
    // libraryTarget: 'umd', // Could be 'umd'
    path: BUILD_PATH,
    pathinfo: true,
    publicPath: '/lib/', // For loading from webpack dev server
    filename: '[name].js'
  }
}
