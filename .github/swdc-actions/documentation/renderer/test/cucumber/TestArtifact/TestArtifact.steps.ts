import { binding, then, when } from "cucumber-tsflow";
import { should } from "chai";
import { ITestArtifact, TestArtifactSchemaEnum, TestArtifactTypeEnum } from "../../../src/TestArtifact/ITestArtifact";
import { TestArtifact } from "../../../src/TestArtifact/TestArtifact";
import { MockPersistentStore } from "../../MockPersistentStore";

@binding()
class TestArtifactSteps {
    private _Should: Chai.Should;
    private _ActionResult?: ITestArtifact;

    constructor() {
        this._Should = should();
    }

    @when(/we create a TestArtifact with CommitHash='(.*)' Type='(.*)' Schema='(.*)' and Container='(.*)'/)
    public GivenWeHaveATestArtifact(CommitHash: string, Type: string, Schema: string, Container: string) {
        const TypeEnumValue = TestArtifactTypeEnum[Type as keyof typeof TestArtifactTypeEnum];
        const SchemaEnumValue = TestArtifactSchemaEnum[Schema as keyof typeof TestArtifactSchemaEnum];
        this._ActionResult = new TestArtifact(CommitHash, TypeEnumValue, SchemaEnumValue, Container, new MockPersistentStore());
    }

    @then(/the CommitHash should be '(.*)'/)
    public ThenTheCommitHashShouldBe(CommitHash: string): void {
      this._Should.exist(this._ActionResult?.CommitHash)
      this._ActionResult?.CommitHash.should.equal(CommitHash);
    }
  
    @then(/the Type should be '(.*)'/)
    public ThenTheTypeShouldBe(Type: string): void {
      this._Should.exist(this._ActionResult?.Type)
      this._ActionResult?.Type.should.equal(Type);
    }
  
    @then(/the Schema should be '(.*)'/)
    public ThenTheSchemaShouldBe(Schema: string): void {
      this._ActionResult?.Schema.should.equal(Schema);
    }

    @then(/the Container should be '(.*)'/)
    public ThenTheContainerShouldBe(Container: string): void {
      this._ActionResult?.Container.should.equal(Container);
    }    

    @then(/the PersistentStore should exist/)
    public ThenThePersistentStoreShouldNotBeNull(): void {
      this._Should.exist(this._ActionResult?.PersistentStore);
    }

}

export = TestArtifactSteps;