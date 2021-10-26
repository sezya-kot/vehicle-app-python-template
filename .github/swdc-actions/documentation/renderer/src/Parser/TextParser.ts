import { ITestArtifact } from "../TestArtifact/ITestArtifact";
import { IParser } from "./IParser";
import { IParseResult } from "./IParseResult";

export class TextParser implements IParser {
    public Parse(Artifact: ITestArtifact): IParseResult {
        var TestResult: IParseResult;
        TestResult = {
            CommitHash: Artifact.CommitHash,
            Schema: Artifact.Schema,
            Type: Artifact.Type,
            TestSuiteName: "",
            Result: undefined
        };

        const TestOutput = Artifact.Load("output.log");
        TestResult.Result = { 
            OriginalOutput: TestOutput
        }
        return TestResult;
    }
}
