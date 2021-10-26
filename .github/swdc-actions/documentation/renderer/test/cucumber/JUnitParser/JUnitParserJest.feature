Feature: Testing JUnit parser (junit schema)

    Feature Description

    @debug
    Scenario: parsing single JUnit unit test in root

        Given we mock the inbox
        And we have a file with name './junit.xml' and the following content in the inbox
            """
            <?xml version="1.0" encoding="UTF-8"?>
            <testsuites name="jest tests" tests="1" failures="0" errors="0" time="2.677">
            <testsuite name="Echo talent" errors="0" failures="0" skipped="0" timestamp="2021-06-16T09:27:01" time="1.805" tests="1">
            <testcase classname="Echo talent does echo string value" name="Echo talent does echo string value" time="0.001"></testcase>
            </testsuite>
            </testsuites>
            """
        And we have a TestArtifact with CommitHash='abc' Type='UnitTest' Schema='JUnit' and Container='.'
        And we have a JUnit parser

        When we call Parse

        And the TestSuiteName should be 'jest tests'
        And the Result.Tests should be '1'
        And the Result.Errors should be '0'
        And the Result.Failures should be '0'
        And the Result.OriginalOutput should be the following content
            """
            <?xml version="1.0" encoding="UTF-8"?>
            <testsuites name="jest tests" tests="1" failures="0" errors="0" time="2.677">
            <testsuite name="Echo talent" errors="0" failures="0" skipped="0" timestamp="2021-06-16T09:27:01" time="1.805" tests="1">
            <testcase classname="Echo talent does echo string value" name="Echo talent does echo string value" time="0.001"></testcase>
            </testsuite>
            </testsuites>
            """



    Scenario: parsing single JUnit unit test in folder

        Given we mock the inbox
        And we have a file with name '/folder/junit.xml' and the following content in the inbox
            """
            <?xml version="1.0" encoding="UTF-8"?>
            <testsuites name="jest tests" tests="2" failures="0" errors="0" time="2.677">
            <testsuite name="Echo talent" errors="0" failures="0" skipped="0" timestamp="2021-06-16T09:27:01" time="1.805" tests="1">
            <testcase classname="Echo talent does echo string value" name="Echo talent does echo string value" time="0.001"></testcase>
            </testsuite>
            </testsuites>
            """
        And we have a TestArtifact with CommitHash='abc' Type='UnitTest' Schema='JUnit' and Container='/folder'
        And we have a JUnit parser

        When we call Parse

        And the TestSuiteName should be 'jest tests'
        And the Result.Tests should be '2'
        And the Result.Errors should be '0'
        And the Result.Failures should be '0'
        And the Result.OriginalOutput should be the following content
            """
            <?xml version="1.0" encoding="UTF-8"?>
            <testsuites name="jest tests" tests="2" failures="0" errors="0" time="2.677">
            <testsuite name="Echo talent" errors="0" failures="0" skipped="0" timestamp="2021-06-16T09:27:01" time="1.805" tests="1">
            <testcase classname="Echo talent does echo string value" name="Echo talent does echo string value" time="0.001"></testcase>
            </testsuite>
            </testsuites>
            """


    Scenario: Failed unit test
        Given we mock the inbox
        And we have a file with name '/folder/junit.xml' and the following content in the inbox
            """
            <?xml version="1.0" encoding="UTF-8"?>
            <testsuites name="jest tests" tests="5" failures="1" errors="0" time="3.565">
            <testsuite name="Echo talent" errors="0" failures="1" skipped="0" timestamp="2021-09-06T14:53:37" time="0.803" tests="5">
            <testcase classname="Echo talent does echo string value" name="Echo talent does echo string value" time="0.004">
            <failure>Error: expect(received).toBe(expected) // Object.is equality

            Expected: &quot;failed&quot;
            Received: &quot;asdasddsadasd&quot;
            at Object.&lt;anonymous&gt; (/workspaces/swdc-iotea-talent-template-nodejs-dev/test/unit-tests/myEchoTalent/myEchoTalent.test.js:24:28)
            at processTicksAndRejections (internal/process/task_queues.js:95:5)</failure>
            </testcase>
            <testcase classname="Echo talent does echo array of strings" name="Echo talent does echo array of strings" time="0">
            </testcase>
            <testcase classname="Echo talent does echo number value" name="Echo talent does echo number value" time="0">
            </testcase>
            <testcase classname="Echo talent does echo array of numbers" name="Echo talent does echo array of numbers" time="0">
            </testcase>
            <testcase classname="Echo talent does echo array of mixed numbers and strings" name="Echo talent does echo array of mixed numbers and strings" time="0">
            </testcase>
            </testsuite>
            </testsuites>
            """
        And we have a TestArtifact with CommitHash='453wef223' Type='UnitTest' Schema='JUnit' and Container='/folder'
        And we have a JUnit parser

        When we call Parse

        And the TestSuiteName should be 'jest tests'
        And the Result.Tests should be '5'
        And the Result.Errors should be '0'
        And the Result.Failures should be '1'

        And the array Results.TestSuite[0].testcase should have the following items
            | Name                                                     | Passed |
            | Echo talent does echo string value                       | false  |
            | Echo talent does echo array of strings                   | true   |
            | Echo talent does echo number value                       | true   |
            | Echo talent does echo array of numbers                   | true   |
            | Echo talent does echo array of mixed numbers and strings | true   |
        And the test case Results.TestSuite[0].testcase[0].failure should be the following
            """
            Error: expect(received).toBe(expected) // Object.is equality

            Expected: "failed"
            Received: "asdasddsadasd"
            at Object.<anonymous> (/workspaces/swdc-iotea-talent-template-nodejs-dev/test/unit-tests/myEchoTalent/myEchoTalent.test.js:24:28)
            at processTicksAndRejections (internal/process/task_queues.js:95:5)
            """
