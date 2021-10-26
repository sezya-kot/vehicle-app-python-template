clear
./node_modules/.bin/cucumber-js test/cucumber/TestArtifact/**/*.feature --require test/cucumber/TestArtifact/**/*.ts
./node_modules/.bin/cucumber-js test/cucumber/TestArtifactImporter/**/*.feature --require test/cucumber/TestArtifactImporter/**/*.ts
./node_modules/.bin/cucumber-js test/cucumber/CoberturaParser/**/*.feature --require test/cucumber/CoberturaParser/**/*.ts
./node_modules/.bin/cucumber-js test/cucumber/JUnitParser/**/*.feature --require test/cucumber/JUnitParser/**/*.ts
./node_modules/.bin/cucumber-js test/cucumber/TextParser/**/*.feature --require test/cucumber/TextParser/**/*.ts
./node_modules/.bin/cucumber-js test/cucumber/Renderer/**/*.feature --require test/cucumber/Renderer/**/*.ts