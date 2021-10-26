How to create typescript project locally:
npm init
tsc --init
npm i -g @vercel/ncc 

Local compile:
tsc action.ts -> this will create a action.js file 
ncc build action.js -o dist -> this will build node-modules and js into single file

Build:
./github/workflow/template-action.yml -> it build the action and calls template/ts/action.yml file
