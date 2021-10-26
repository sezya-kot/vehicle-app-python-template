import { binding, given, then, when } from "cucumber-tsflow";
import { should } from "chai";
import { IParser } from "../../../src/Parser/IParser";
import { IParseResult } from "../../../src/Parser/IParseResult";
import { CoberturaParser } from "../../../src/Parser/CoberturaParser";
import { TextParser } from "../../../src/Parser/TextParser";
import { ITestArtifact, TestArtifactSchemaEnum, TestArtifactTypeEnum } from "../../../src/TestArtifact/ITestArtifact";
import { TestArtifact } from "../../../src/TestArtifact/TestArtifact";
import { IPersistentStore } from "../../../src/IPersistentStore";
import { MockPersistentStore } from "../../MockPersistentStore";

@binding()
class CoberturaParserSteps {
  private _Should: Chai.Should;
  private _GivenPersistentStore?: IPersistentStore;
  private _GivenTestArtifact?: ITestArtifact;
  private _GivenParser?: IParser;
  private _ActionResult?: IParseResult;

  constructor() {
    this._Should = should();
    this._Should.exist(this._Should);
  }

  @given(/we mock the inbox/)
  public GivenWeMockTheInbox() {
    this._GivenPersistentStore = new MockPersistentStore();
  }

  @given(/we have a file with name '(.*)' and the following content in the inbox/)
  public GivenWeHaveAFileInTheInbox(Filename: string, Content: string) {
    this._GivenPersistentStore?.Save(Filename, Content);
  }

  @given(/we have a TestArtifact with CommitHash='(.*)' Type='(.*)' Schema='(.*)' and Container='(.*)'/)
  public GivenWeHaveATestArtifact(CommitHash: string, Type: string, Schema: string, Container: string) {
    const TypeEnumValue = TestArtifactTypeEnum[Type as keyof typeof TestArtifactTypeEnum];
    const SchemaEnumValue = TestArtifactSchemaEnum[Schema as keyof typeof TestArtifactSchemaEnum];
    this._GivenTestArtifact = new TestArtifact(CommitHash, TypeEnumValue, SchemaEnumValue, Container, this._GivenPersistentStore!);
  }

  @given(/we have a Cobertura parser/)
  public GivenWeHaveACoberturaParser() {
    this._GivenParser  = new CoberturaParser();
  }

  @given(/we have a Text parser/)
  public GivenWeHaveATextParser() {
    this._GivenParser  = new TextParser();
  }

  @when(/we call Parse/)
  public WhenWeCallRender(): void {
    this._ActionResult = this._GivenParser!.Parse(this._GivenTestArtifact!);
  }

  @then(/the TestSuiteName should be '(.*)'/)
  public ThenTheTestSuiteNameShouldBe(TestSuiteName: string): void {
    this._ActionResult?.TestSuiteName.should.equal(TestSuiteName);
  }

  @then(/the Result\.LineRate should be '(.*)'/)
  public ThenTheResultTestsShouldBe(LineRate: string): void {
    this._ActionResult?.Result["line-rate"].should.equal(LineRate);
  }

  @then(/the Result\.Errors should be '(.*)'/)
  public ThenTheResultErrorsShouldBe(Errors: string): void {
    this._ActionResult?.Result.Errors.should.equal(Errors);
  }

  @then(/the Result\.Failures should be '(.*)'/)
  public ThenTheResultFailuresShouldBe(Failures: string): void {
    this._ActionResult?.Result.Failures.should.equal(Failures);
  }

  @then(/the Result\.Overall should be '(.*)'/)
  public ThenTheResultOverallShouldBe(Overall: string): void {
    this._ActionResult?.Result.Overall.toString().should.equal(Overall);
  }

  @then(/the Result\.OriginalOutput should be the following content/)
  public OriginalOutput(Table: string): void {
    this._ActionResult?.Result.OriginalOutput.should.be.equal(Table);
  }
}

export = CoberturaParserSteps;
