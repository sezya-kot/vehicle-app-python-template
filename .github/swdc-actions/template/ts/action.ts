import * as core from '@actions/core'

function getInput(name: string) {
    console.log("Hello " + name)
}

function setOutput() {
    const time = new Date();
    console.log("Logging time" + time.toTimeString())
    core.setOutput("time", time.toTimeString())
}

function exportVars() {
    core.exportVariable("HELLO", "hello")
}

getInput(core.getInput('who-to-greet'))
setOutput()
exportVars()
