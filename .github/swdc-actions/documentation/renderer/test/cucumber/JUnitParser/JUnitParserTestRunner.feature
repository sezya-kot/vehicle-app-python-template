Feature: Testing JUnit parser (integration test test runner schema)

    Feature Description

    @debug
    Scenario: parsing JUnit with single testsuite

        Given we mock the inbox
        And we have a file with name './junit.xml' and the following content in the inbox
            """
            <?xml version="1.0" ?>
            <testsuites disabled="0" errors="0" failures="0" tests="9" time="0.159">
            <testsuite disabled="0" errors="0" failures="0" name="testSuite-sdk-js" skipped="0" tests="9" time="0.065">
            <testcase name="echoString" time="0.008000"/>
            <testcase name="echoBoolean" time="0.006000"/>
            <testcase name="echoInteger" time="0.004000"/>
            <testcase name="echoDouble" time="0.006000"/>
            <testcase name="echoEmptyList" time="0.010000"/>
            <testcase name="echoIntegerList" time="0.004000"/>
            <testcase name="echoMixedList" time="0.006000"/>
            <testcase name="echoDeepList" time="0.006000"/>
            <testcase name="receiveEvent1ByMultipleTalents" time="0.015000"/>
            </testsuite>
            </testsuites>
            """
        And we have a TestArtifact with CommitHash='abc' Type='IntegrationTest' Schema='JUnit' and Container='.'
        And we have a JUnit parser

        When we call Parse

        Then the Result.Tests should be '9'
        And the Result.Errors should be '0'
        And the Result.Failures should be '0'
        And the array Result.TestSuite[0].name should be 'testSuite-sdk-js'
        And the array Result.TestSuite[0].tests should be '9'
        And the array Results.TestSuite[0].testcase should have the following items
            | Name                           |
            | echoString                     |
            | echoBoolean                    |
            | echoInteger                    |
            | echoDouble                     |
            | echoEmptyList                  |
            | echoIntegerList                |
            | echoMixedList                  |
            | echoDeepList                   |
            | receiveEvent1ByMultipleTalents |
        And the Result.OriginalOutput should be the following content
            """
            <?xml version="1.0" ?>
            <testsuites disabled="0" errors="0" failures="0" tests="9" time="0.159">
            <testsuite disabled="0" errors="0" failures="0" name="testSuite-sdk-js" skipped="0" tests="9" time="0.065">
            <testcase name="echoString" time="0.008000"/>
            <testcase name="echoBoolean" time="0.006000"/>
            <testcase name="echoInteger" time="0.004000"/>
            <testcase name="echoDouble" time="0.006000"/>
            <testcase name="echoEmptyList" time="0.010000"/>
            <testcase name="echoIntegerList" time="0.004000"/>
            <testcase name="echoMixedList" time="0.006000"/>
            <testcase name="echoDeepList" time="0.006000"/>
            <testcase name="receiveEvent1ByMultipleTalents" time="0.015000"/>
            </testsuite>
            </testsuites>
            """



    @debug
    Scenario: parsing JUnit with multiple testsuites

        Given we mock the inbox
        And we have a file with name './junit.xml' and the following content in the inbox
            """
            <?xml version="1.0" ?>
            <testsuites disabled="0" errors="0" failures="0" tests="25" time="0.159">
            <testsuite disabled="0" errors="0" failures="0" name="testSuite-sdk-py" skipped="0" tests="8" time="0.05799999999999999">
            <testcase name="echoString" time="0.009000"/>
            <testcase name="echoBoolean" time="0.011000"/>
            <testcase name="echoInteger" time="0.007000"/>
            <testcase name="echoDouble" time="0.007000"/>
            <testcase name="echoEmptyList" time="0.006000"/>
            <testcase name="echoIntegerList" time="0.006000"/>
            <testcase name="echoMixedList" time="0.006000"/>
            <testcase name="echoDeepList" time="0.006000"/>
            </testsuite>
            <testsuite disabled="0" errors="0" failures="0" name="testSuite-sdk-js" skipped="0" tests="9" time="0.065">
            <testcase name="echoString" time="0.008000"/>
            <testcase name="echoBoolean" time="0.006000"/>
            <testcase name="echoInteger" time="0.004000"/>
            <testcase name="echoDouble" time="0.006000"/>
            <testcase name="echoEmptyList" time="0.010000"/>
            <testcase name="echoIntegerList" time="0.004000"/>
            <testcase name="echoMixedList" time="0.006000"/>
            <testcase name="echoDeepList" time="0.006000"/>
            <testcase name="receiveEvent1ByMultipleTalents" time="0.015000"/>
            </testsuite>
            <testsuite disabled="0" errors="0" failures="0" name="testSuite-sdk-cpp" skipped="0" tests="8" time="0.036">
            <testcase name="echoBoolean" time="0.005000"/>
            <testcase name="echoDeepList" time="0.005000"/>
            <testcase name="echoDouble" time="0.005000"/>
            <testcase name="echoEmptyList" time="0.004000"/>
            <testcase name="echoInteger" time="0.003000"/>
            <testcase name="echoIntegerList" time="0.004000"/>
            <testcase name="echoMixedList" time="0.005000"/>
            <testcase name="echoString" time="0.005000"/>
            </testsuite>
            </testsuites>
            """
        And we have a TestArtifact with CommitHash='abc' Type='IntegrationTest' Schema='JUnit' and Container='.'
        And we have a JUnit parser

        When we call Parse

        Then the Result.Tests should be '25'
        And the Result.Errors should be '0'
        And the Result.Failures should be '0'
        And the array Result.TestSuite[0].name should be 'testSuite-sdk-py'
        And the array Result.TestSuite[0].tests should be '8'
        And the array Results.TestSuite[0].testcase should have the following items
            | Name            |
            | echoString      |
            | echoBoolean     |
            | echoInteger     |
            | echoDouble      |
            | echoEmptyList   |
            | echoIntegerList |
            | echoMixedList   |
            | echoDeepList    |
        And the array Result.TestSuite[1].name should be 'testSuite-sdk-js'
        And the array Result.TestSuite[1].tests should be '9'
        And the array Results.TestSuite[1].testcase should have the following items
            | Name                           |
            | echoString                     |
            | echoBoolean                    |
            | echoInteger                    |
            | echoDouble                     |
            | echoEmptyList                  |
            | echoIntegerList                |
            | echoMixedList                  |
            | echoDeepList                   |
            | receiveEvent1ByMultipleTalents |
        And the array Result.TestSuite[2].name should be 'testSuite-sdk-cpp'
        And the array Result.TestSuite[2].tests should be '8'
        And the array Results.TestSuite[2].testcase should have the following items
            | Name            |
            | echoBoolean     |
            | echoDeepList    |
            | echoDouble      |
            | echoEmptyList   |
            | echoInteger     |
            | echoIntegerList |
            | echoMixedList   |
            | echoString      |
        And the Result.OriginalOutput should be the following content
            """
            <?xml version="1.0" ?>
            <testsuites disabled="0" errors="0" failures="0" tests="25" time="0.159">
            <testsuite disabled="0" errors="0" failures="0" name="testSuite-sdk-py" skipped="0" tests="8" time="0.05799999999999999">
            <testcase name="echoString" time="0.009000"/>
            <testcase name="echoBoolean" time="0.011000"/>
            <testcase name="echoInteger" time="0.007000"/>
            <testcase name="echoDouble" time="0.007000"/>
            <testcase name="echoEmptyList" time="0.006000"/>
            <testcase name="echoIntegerList" time="0.006000"/>
            <testcase name="echoMixedList" time="0.006000"/>
            <testcase name="echoDeepList" time="0.006000"/>
            </testsuite>
            <testsuite disabled="0" errors="0" failures="0" name="testSuite-sdk-js" skipped="0" tests="9" time="0.065">
            <testcase name="echoString" time="0.008000"/>
            <testcase name="echoBoolean" time="0.006000"/>
            <testcase name="echoInteger" time="0.004000"/>
            <testcase name="echoDouble" time="0.006000"/>
            <testcase name="echoEmptyList" time="0.010000"/>
            <testcase name="echoIntegerList" time="0.004000"/>
            <testcase name="echoMixedList" time="0.006000"/>
            <testcase name="echoDeepList" time="0.006000"/>
            <testcase name="receiveEvent1ByMultipleTalents" time="0.015000"/>
            </testsuite>
            <testsuite disabled="0" errors="0" failures="0" name="testSuite-sdk-cpp" skipped="0" tests="8" time="0.036">
            <testcase name="echoBoolean" time="0.005000"/>
            <testcase name="echoDeepList" time="0.005000"/>
            <testcase name="echoDouble" time="0.005000"/>
            <testcase name="echoEmptyList" time="0.004000"/>
            <testcase name="echoInteger" time="0.003000"/>
            <testcase name="echoIntegerList" time="0.004000"/>
            <testcase name="echoMixedList" time="0.005000"/>
            <testcase name="echoString" time="0.005000"/>
            </testsuite>
            </testsuites>
            """



