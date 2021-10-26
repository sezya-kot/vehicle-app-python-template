Feature: TestArtifact

    Feature Description

    @debug
    Scenario: constructor

        When we create a TestArtifact with CommitHash='abc' Type='UnitTest' Schema='JUnit' and Container='/'

        Then the CommitHash should be 'abc'
        And the Type should be 'UnitTest'
        And the Schema should be 'JUnit'
        And the Container should be '/'
        And the PersistentStore should exist