// cucumber.js
let common = [
    '--require-module ts-node/register',    // Load TypeScript module
    '--publish-quiet',
    '--format cucumber-console-formatter'
  ].join(' ');
  
  module.exports = {
    default: common
  };