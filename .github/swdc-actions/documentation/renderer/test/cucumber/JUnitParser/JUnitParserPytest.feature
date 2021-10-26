Feature: Testing JUnit parser (pytest schema)

    Feature Description

    @debug
    Scenario: parsing single JUnit unit test in root

        Given we mock the inbox
        And we have a file with name './junit.xml' and the following content in the inbox
            """
            <?xml version="1.0" encoding="utf-8"?>
            <testsuites>
            <testsuite name="pytest" errors="0" failures="0" skipped="0" tests="8" time="0.151" timestamp="2021-08-31T16:32:10.211936" hostname="fv-az129-202">
            <testcase classname="test.test_rules.TestRules" name="test_save" time="0.065" />
            <testcase classname="test.test_rules.TestRules" name="test_append_single_rule" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_invalid_exclude_on" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_stringify_value_type" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_get_type_feature" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_extract_segment_from_type_selector" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_invalid_type_selector" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_op_constraint_save" time="0.001" />
            </testsuite>
            </testsuites>
            """
        And we have a TestArtifact with CommitHash='abc' Type='UnitTest' Schema='JUnit' and Container='.'
        And we have a JUnit parser

        When we call Parse

        Then the Result.Tests should be '8'
        And the Result.Errors should be '0'
        And the Result.Failures should be '0'
        And the array Result.TestSuite[0].name should be 'pytest'
        And the array Result.TestSuite[0].tests should be '8'
        And the array Results.TestSuite[0].testcase should have the following items
            | Name                                    |
            | test_save                               |
            | test_append_single_rule                 |
            | test_invalid_exclude_on                 |
            | test_stringify_value_type               |
            | test_get_type_feature                   |
            | test_extract_segment_from_type_selector |
            | test_invalid_type_selector              |
            | test_op_constraint_save                 |
        And the Result.OriginalOutput should be the following content
            """
            <?xml version="1.0" encoding="utf-8"?>
            <testsuites>
            <testsuite name="pytest" errors="0" failures="0" skipped="0" tests="8" time="0.151" timestamp="2021-08-31T16:32:10.211936" hostname="fv-az129-202">
            <testcase classname="test.test_rules.TestRules" name="test_save" time="0.065" />
            <testcase classname="test.test_rules.TestRules" name="test_append_single_rule" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_invalid_exclude_on" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_stringify_value_type" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_get_type_feature" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_extract_segment_from_type_selector" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_invalid_type_selector" time="0.001" />
            <testcase classname="test.test_rules.TestRules" name="test_op_constraint_save" time="0.001" />
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
