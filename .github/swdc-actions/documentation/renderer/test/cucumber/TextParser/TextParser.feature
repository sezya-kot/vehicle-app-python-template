Feature: Testing text parser

    Feature Description

    @debug
    Scenario: parsing single log file output in root

        Given we mock the inbox
        And we have a file with name './output.log' and the following content in the inbox
            """
            Start Integration Tests
            Get Tests for myechotalent-inttest-js
            Prepare myechotalent-inttest-js
            Running myechotalent-inttest-js
            [1/1] Running Test: echoString
            - Result: OK (10ms)
            Result of myechotalent-inttest-js is true
            Overall test result is true
            """
        And we have a TestArtifact with CommitHash='abc' Type='IntegrationTest' Schema='Text' and Container='.'
        And we have a Text parser

        When we call Parse

        And the Result.OriginalOutput should be the following content
            """
            Start Integration Tests
            Get Tests for myechotalent-inttest-js
            Prepare myechotalent-inttest-js
            Running myechotalent-inttest-js
            [1/1] Running Test: echoString
            - Result: OK (10ms)
            Result of myechotalent-inttest-js is true
            Overall test result is true
            """