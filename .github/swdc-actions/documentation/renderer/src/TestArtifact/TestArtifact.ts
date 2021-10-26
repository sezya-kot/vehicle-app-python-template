import { IPersistentStore } from "../IPersistentStore";
import { ITestArtifact, TestArtifactTypeEnum, TestArtifactSchemaEnum } from "./ITestArtifact";

export class TestArtifact implements ITestArtifact {
    public CommitHash: string;
    public Type: TestArtifactTypeEnum;
    public Schema: TestArtifactSchemaEnum;
    public Container: string;
    readonly PersistentStore: IPersistentStore;
    
    constructor(CommitHash: string, Type: TestArtifactTypeEnum, Schema: TestArtifactSchemaEnum,  Container: string, PersistentStore: IPersistentStore) {
        this.CommitHash = CommitHash;
        this.Type = Type;
        this.Schema = Schema;
        this.Container = Container;
        this.PersistentStore = PersistentStore;
    }

    public Load(Name: string): string {
        return this.PersistentStore.Load(this.Container + "/" + Name);
    }
}
