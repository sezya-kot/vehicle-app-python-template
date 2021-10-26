# How to create typescript project locally

```bash
npm init
tsc --init
npm i -g @vercel/ncc 
```

Local compile:

```bash
# this will create a action.js file 
tsc action.ts 

# this will build node-modules and js into single file
ncc build action.js -o dist
```

Build:

```bash
# it build the action and calls template/ts/action.yml file
./github/workflow/template-action.yml 
```
