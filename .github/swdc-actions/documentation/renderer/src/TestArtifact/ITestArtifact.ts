import { IPersistentStore } from "../IPersistentStore";

export enum TestArtifactTypeEnum {
    Undefined = "Undefined",
    UnitTest = "UnitTest",
    IntegrationTest = "IntegrationTest",
    PerformanceTest = "PerformanceTest",
    VulnerabilityScan = "VulnerabilityScan",
    CodeCoverage = "CodeCoverage"
}

export enum TestArtifactSchemaEnum {
    Undefined = "Undefined",
    XUnit = "XUnit",
    JUnit = "JUnit",
    Cobertura = "Cobertura",
    Text = "Text"
}

export interface ITestArtifact {
    CommitHash: string;
    Type: TestArtifactTypeEnum;
    Schema: TestArtifactSchemaEnum;
    Container: string;
    PersistentStore: IPersistentStore;
    Load(Name: string): string;
}
