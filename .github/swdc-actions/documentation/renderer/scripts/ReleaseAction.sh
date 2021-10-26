#!/bin/bash

echo "## installing prerequisites"
cd ..
npm install

echo "## creating test files"
./scripts/CreateTestFiles.sh

echo "## compiling typescript to javascript"
tsc --build --verbose .

echo "## creating index.js with ncc"
cd dist
npx ncc build ./src/action.js -o ncc

echo "## content of ncc folder"
ls ncc
