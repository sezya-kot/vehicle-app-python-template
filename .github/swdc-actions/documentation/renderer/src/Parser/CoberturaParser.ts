import { ITestArtifact } from "../TestArtifact/ITestArtifact";
import { IParser } from "./IParser";
import { IParseResult } from "./IParseResult";
import * as xml2js from "xml2js"

export class CoberturaParser implements IParser {
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

        const TestOutput = Artifact.Load("cobertura-coverage.xml");
        console.log(TestOutput)
        if (TestOutput === null) {
            throw ("Failed to load cobertura-coverage.xml")
        }
        parser.parseString(TestOutput, function (err: any, result: any) {
            if (err) {
                throw "Failed to parse XML with error: " + err;
            }
            TestResult.Result = {
                "line-rate": result.coverage["line-rate"],
                OriginalOutput: TestOutput
            };
        });

        return TestResult;
    }
}
