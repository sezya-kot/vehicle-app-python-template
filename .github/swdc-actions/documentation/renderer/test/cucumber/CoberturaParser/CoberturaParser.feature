Feature: Testing cobertura parser

    Feature Description

    @debug
    Scenario: parsing single cobertura code coverage file in root

        Given we mock the inbox
        And we have a file with name './cobertura-coverage.xml' and the following content in the inbox
            """
            <?xml version="1.0" ?>
            <!DOCTYPE coverage SYSTEM "http://cobertura.sourceforge.net/xml/coverage-04.dtd">
            <coverage lines-valid="13" lines-covered="9" line-rate="0.6923" branches-valid="0" branches-covered="0" branch-rate="1" timestamp="1628771291660" complexity="0" version="0.1">
            <sources>
            <source>/workspaces/swdc-iotea-talent-template-nodejs-dev</source>
            </sources>
            <packages>
            <class name="myEchoTalent.js" filename="src/myEchoTalent.js" line-rate="0.6923" branch-rate="1">
            <lines>
            <line number="1" hits="1" branch="false"/>
            <line number="9" hits="1" branch="false"/>
            <line number="13" hits="1" branch="false"/>
            <line number="17" hits="1" branch="false"/>
            <line number="20" hits="1" branch="false"/>
            <line number="24" hits="1" branch="false"/>
            <line number="34" hits="0" branch="false"/>
            <line number="40" hits="0" branch="false"/>
            <line number="42" hits="0" branch="false"/>
            <line number="44" hits="0" branch="false"/>
            <line number="48" hits="5" branch="false"/>
            <line number="49" hits="5" branch="false"/>
            <line number="54" hits="1" branch="false"/>
            </lines>
            </class>
            </packages>
            </coverage>
            """
        And we have a TestArtifact with CommitHash='abc' Type='CodeCoverage' Schema='Cobertura' and Container='.'
        And we have a Cobertura parser

        When we call Parse

        Then the Result.LineRate should be '0.6923'
