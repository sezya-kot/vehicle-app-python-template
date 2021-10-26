import { ITestArtifact } from "../TestArtifact/ITestArtifact";

export interface ITestArtifactImporter {
    GetTestArtifacts(): ITestArtifact[];
}
