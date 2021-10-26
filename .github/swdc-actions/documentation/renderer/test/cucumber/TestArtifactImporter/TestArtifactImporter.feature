Feature: TestArtifactImporter

  Feature Description

  Scenario: Import

    Given we mock the inbox
    And we have a file with name './TestArtifact.json' and the following content in the inbox
      """
      {
        "Type": "UnitTest",
        "Schema": "JUnit",
        "CommitHash": "piop32459ajf097435"
      }
      """
    And we have a file with name '2/TestArtifact.json' and the following content in the inbox
      """
      {
        "Type": "IntegrationTest",
        "Schema": "Text",
        "CommitHash": "piehf203pj"
      }
      """

    When we call GetTestArtifacts

    Then it should return '2' objects
    And the Type of the first object should be 'UnitTest'
    And the Schema of the first object should be 'JUnit'
    And the Container of the first object should be '.'
    And the CommitHash of the first object should be 'piop32459ajf097435'

    And the Type of the second object should be 'IntegrationTest'
    And the Schema of the second object should be 'Text'
    And the Container of the second object should be '2'
    And the CommitHash of the second object should be 'piehf203pj'