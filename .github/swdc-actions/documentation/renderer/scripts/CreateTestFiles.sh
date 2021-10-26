# ------------------- unit test ------------------------------------
mkdir -p ./inbox
cat >./inbox/JUnit.xml <<EOL
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="jest tests" tests="1" failures="0" errors="0" time="2.677">
    <testsuite name="Echo talent" errors="0" failures="0" skipped="0" timestamp="2021-06-16T09:27:01" time="1.805" tests="1">
        <testcase classname="Echo talent does echo string value" name="Echo talent does echo string value" time="0.001"></testcase>
    </testsuite>
</testsuites>
EOL

mkdir -p ./inbox
cat >./inbox/TestArtifact.json <<EOL
{
    "CommitHash": "oizu354087uzpe",
    "Type": "UnitTest",
    "Schema": "JUnit"
}
EOL

# ------------------- integration test ------------------------------------
mkdir -p ./inbox/IntegrationTest
cat >./inbox/IntegrationTest/output.log <<EOL
Start Integration Tests
Get Tests for myechotalent-inttest-js
Prepare myechotalent-inttest-js
Running myechotalent-inttest-js
[1/1] Running Test: echoString
- Result: OK (10ms)
Result of myechotalent-inttest-js is true
Overall test result is true
EOL

mkdir -p ./inbox/IntegrationTest
cat >./inbox/IntegrationTest/TestArtifact.json <<EOL
{
    "CommitHash": "7534u0747poiu",
    "Type": "IntegrationTest",
    "Schema": "Text"
}
EOL

# ------------------- vulnerability scan ------------------------------------
mkdir -p ./inbox/VulnerabilityScan
cat >./inbox/VulnerabilityScan/JUnit.xml <<EOL
<?xml version="1.0" encoding="UTF-8"?>
<testsuites name="Vulnerability Scan" tests="532" failures="0" errors="0" time="2.677">
    <testsuite name="Virus Scan" errors="0" failures="0" skipped="0" timestamp="2021-06-21T06:12:39" time="19.265" tests="1">
        <testcase classname="Virus A" name="some name" time="0.001"></testcase>
    </testsuite>
</testsuites>
EOL

mkdir -p ./inbox/VulnerabilityScan
cat >./inbox/VulnerabilityScan/TestArtifact.json <<EOL
{
    "CommitHash": "0j34097543uj0975",
    "Type": "VulnerabilityScan",
    "Schema": "JUnit"
}
EOL



mkdir -p ./outbox