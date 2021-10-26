import { ITestArtifact, TestArtifactSchemaEnum, TestArtifactTypeEnum } from "../TestArtifact/ITestArtifact";
import { IParser } from "./IParser";
import { IParserFactory } from "./IParserFactory";

export class ParserFactory implements IParserFactory {
    private _Parsers: Map<string, IParser> = new Map();
    constructor() { }
    public RegisterParser(Type: TestArtifactTypeEnum, Schema: TestArtifactSchemaEnum, Parser: IParser): void {
        const Key = Type.toString() + "-" + Schema.toString();
        console.log("Registering parser for: " + Key);
        this._Parsers.set(Key, Parser);
    }

    public GetParser(TestArtifact: ITestArtifact): IParser {
        const Key = TestArtifact.Type.toString() + "-" + TestArtifact.Schema.toString();
        var Parser: IParser;
        if (this._Parsers.has(Key)) {
            console.log("Found parser with key '${Key}'")
            Parser = this._Parsers.get(Key)!;
        } else {
            throw "Failed to find parser with key: " + Key;
        }
        return Parser;
    }
}
