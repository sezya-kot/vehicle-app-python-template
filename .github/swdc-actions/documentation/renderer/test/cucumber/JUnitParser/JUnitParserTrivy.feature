Feature: Testing JUnit parser (trivy schema)

    Feature Description

    @debug
    Scenario: parsing single JUnit unit test in root

        Given we mock the inbox
        And we have a file with name './junit.xml' and the following content in the inbox
            """
            <?xml version="1.0" ?>
            <testsuites>
            <testsuite tests="0" failures="0" name="vapp-container-image-arch.tar (alpine 3.11.11)" errors="0" skipped="0" time="0">
            <properties>
            <property name="type" value="alpine"></property>
            </properties>
            </testsuite>
            </testsuites>
            """
        And we have a TestArtifact with CommitHash='j03094ur' Type='VulnerabilityScan' Schema='JUnit' and Container='.'
        And we have a JUnit parser

        When we call Parse

        Then the Result.Tests should be '0'
        And the Result.Errors should be '0'
        And the Result.Failures should be '0'
        And the array Result.TestSuite[0].name should be 'vapp-container-image-arch.tar (alpine 3.11.11)'
        And the array Result.TestSuite[0].tests should be '0'
        And the Result.OriginalOutput should be the following content
            """
            <?xml version="1.0" ?>
            <testsuites>
            <testsuite tests="0" failures="0" name="vapp-container-image-arch.tar (alpine 3.11.11)" errors="0" skipped="0" time="0">
            <properties>
            <property name="type" value="alpine"></property>
            </properties>
            </testsuite>
            </testsuites>
            """


