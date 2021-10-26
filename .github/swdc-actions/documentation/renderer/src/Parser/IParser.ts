import { ITestArtifact } from "../TestArtifact/ITestArtifact";
import { IParseResult } from "./IParseResult";

export interface IParser {
    Parse(TestArtifact: ITestArtifact): IParseResult;
}
