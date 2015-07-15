#!/usr/bin/env node

var fs = require('fs')
  , path = require('path')
  , async = require('async')
  , cheerio = require('cheerio')
  , _ = require('lodash')
  , folder = path.resolve(process.argv[2] || '.');

fs.readdir(folder, function(err, filenames) {
  if (err) throw err;

  async.map(filenames, readFile, processPages);
});

function readFile(filename, callback) {
  fs.readFile(path.join(folder, filename), {encoding: 'utf8'}, function(err, fileData) {
    if (err) return callback(err);

    callback(null, fileData);
  });
}

function processPages(err, pages) {
  if (err) throw err;

  async.map(pages, scrapePage, logHrefs);
}

function scrapePage(page, callback) {
  var $ = cheerio.load(page);
  $('#main').each(function(i, html) {
    callback(null, _.pluck($(html).find('.file-icon'), 'attribs.href'));
  });
}

function logHrefs(err, hrefs) {
  if (err) throw err;

  _.forEach(_.flatten(hrefs), function(href) {
    console.log(href);
  });
}
