import { ITestArtifact } from "../TestArtifact/ITestArtifact";
import { IParser } from "./IParser";
import { IParseResult } from "./IParseResult";
import * as xml2js from "xml2js"

export class JUnitParser implements IParser {
    public Parse(Artifact: ITestArtifact): IParseResult {
        var TestResult: IParseResult;
        TestResult = {
            CommitHash: Artifact.CommitHash,
            Schema: Artifact.Schema,
            Type: Artifact.Type,
            TestSuiteName: "",
            Result: undefined
        };

        const parser = new xml2js.Parser({ mergeAttrs: true, explicitArray: false });

        const TestOutput = Artifact.Load("junit.xml");
        console.log(TestOutput)
        if (TestOutput === null) {
            throw ("Failed to load junit.xml")
        }
        parser.parseString(TestOutput, function (err: any, result: any) {
            if (err) {
                throw "Failed to parse XML with error: " + err;
            }
            
            var TestSuitesArray
            if (Array.isArray(result.testsuites.testsuite)) {
                TestSuitesArray = result.testsuites.testsuite
            } else {
                TestSuitesArray = [ result.testsuites.testsuite ]
            }

            if (result.testsuites.tests !== undefined) {
                TestResult.TestSuiteName = result.testsuites.name;
                TestResult.Result = {
                    Errors: result.testsuites.errors,
                    Failures: result.testsuites.failures,
                    Tests: result.testsuites.tests,
                    Timestamp: result.testsuites.testsuite.timestamp,
                    TestSuite: TestSuitesArray
                };
            }
            if (result.testsuites.tests === undefined) {
                TestResult.TestSuiteName = result.testsuites.name;
                TestResult.Result = {
                    Errors: result.testsuites.testsuite.errors,
                    Failures: result.testsuites.testsuite.failures,
                    Tests: result.testsuites.testsuite.tests,
                    Timestamp: result.testsuites.testsuite.timestamp,
                    TestSuite: TestSuitesArray
                };
            }            
        });

        TestResult.Result.OriginalOutput = TestOutput;
        return TestResult;
    }
}
