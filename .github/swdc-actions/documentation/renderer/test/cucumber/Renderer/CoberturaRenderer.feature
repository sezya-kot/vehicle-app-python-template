Feature: Testing code coverage result rendering

    @debug
    Scenario: Code Coverage result rendering

        Given we mock the template repository with the template 'CodeCoverage-Cobertura.md' and the following content
            """
            # Code Coverage Test

            the code coverage is {{Result.line-rate}}
            """
        And we have a test result with schema 'Cobertura' of type 'CodeCoverage' and the following result
            """
            {
                "Result": {
                    "line-rate": "0.5387"
                }
            }
            """

        When we call the Renderer

        Then the result should be
            """
            # Code Coverage Test

            the code coverage is 0.5387
            """
