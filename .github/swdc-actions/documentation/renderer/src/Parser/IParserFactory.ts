import { ITestArtifact, TestArtifactSchemaEnum, TestArtifactTypeEnum } from "../TestArtifact/ITestArtifact";
import { IParser } from "./IParser";

export interface IParserFactory {
    RegisterParser(Type: TestArtifactTypeEnum, Schema: TestArtifactSchemaEnum, Parser: IParser): void;
    GetParser(TestArtifact: ITestArtifact): IParser;
}
