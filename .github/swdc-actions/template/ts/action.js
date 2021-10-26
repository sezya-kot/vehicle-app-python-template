"use strict";
exports.__esModule = true;
var core = require("@actions/core");
function getInput(name) {
    console.log("Hello " + name);
}
function setOutput() {
    var time = new Date();
    console.log("Logging time" + time.toTimeString());
    core.setOutput("time", time.toTimeString());
}
function exportVars() {
    core.exportVariable("HELLO", "hello");
}
getInput(core.getInput('who-to-greet'));
setOutput();
exportVars();
