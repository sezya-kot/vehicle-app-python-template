Feature: Testing code coverage result rendering

    @debug
    Scenario: Code Coverage result rendering

        Given we mock the template repository with the template 'CodeCoverage-Cobertura.md' and the following content
            """
            Code coverage is {{Result.line-rate}}
            """
        And we have the following test result
            | Schema    | Type         | Result                                  |
            | Cobertura | CodeCoverage | { "Result": { "line-rate": "0.5387" } } |

        When we call the Renderer

        Then the result should be
            """
            Code coverage is 0.5387
            """
