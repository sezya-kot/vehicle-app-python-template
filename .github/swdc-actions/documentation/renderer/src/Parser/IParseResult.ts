import { TestArtifactSchemaEnum, TestArtifactTypeEnum } from "../TestArtifact/ITestArtifact";

export interface IParseResult {
    CommitHash: string;
    TestSuiteName: string;
    Type: TestArtifactTypeEnum;
    Schema: TestArtifactSchemaEnum;
    Result: any;
}
