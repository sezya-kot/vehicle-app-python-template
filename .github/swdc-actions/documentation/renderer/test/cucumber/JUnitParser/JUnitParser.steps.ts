import { binding, given, then, when } from "cucumber-tsflow";
import { should } from "chai";
import { IParser } from "../../../src/Parser/IParser";
import { IParseResult } from "../../../src/Parser/IParseResult";
import { JUnitParser } from "../../../src/Parser/JUnitParser";
import { ITestArtifact, TestArtifactSchemaEnum, TestArtifactTypeEnum } from "../../../src/TestArtifact/ITestArtifact";
import { TestArtifact } from "../../../src/TestArtifact/TestArtifact";
import { IPersistentStore } from "../../../src/IPersistentStore";
import { MockPersistentStore } from "../../MockPersistentStore";

@binding()
class JUnitSteps {
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

  @given(/we have a JUnit parser/)
  public GivenWeHaveAJUnitParser() {
    this._GivenParser  = new JUnitParser();
  }

  @when(/we call Parse/)
  public WhenWeCallRender(): void {
    this._ActionResult = this._GivenParser!.Parse(this._GivenTestArtifact!);
  }

  @then(/the array Result\.TestSuite\[(.*)\]\.name should be '(.*)'/)
  public TheArrayResultTestSuite0NameShouldbe(Index: number, Value: string): void {
    const TestSuite = this._ActionResult?.Result.TestSuite[Index]
    TestSuite.name.should.equal(Value)
  }

  @then(/the array Result\.TestSuite\[(.*)\]\.tests should be '(.*)'/)
  public TheArrayResultTestSuite0TestShouldBe(Index: number, Value: string): void {
    const TestSuite = this._ActionResult?.Result.TestSuite[Index]
    TestSuite.tests.should.equal(Value)
  }

  @then(/the array Results\.TestSuite\[(.*)\]\.testcase should have the following items/)
  public TheArrayResultTestSuite0TestcaseShouldHaveTheFollowingItems(Index: number, ExpectedValues: any): void {

    var Testcase = new Map()
    const TestSuite = this._ActionResult?.Result.TestSuite[Index]
    for (var CurrentTestCase = 0; CurrentTestCase < TestSuite.testcase.length; CurrentTestCase++) {
      const Name = TestSuite.testcase[CurrentTestCase].name
      Testcase.set(Name, TestSuite.testcase[CurrentTestCase])
    }

    for (var row = 1; row < ExpectedValues.rawTable.length; row++) {
      const ExpectedName = ExpectedValues.rawTable[row][0]
      Testcase.get(ExpectedName).name.should.equal(ExpectedName)
    };
  }

  @then(/the test case Results.TestSuite\[0\]\.testcase\[0\]\.failure should be the following/)
  public AndTheTestCaseResultsTestSuite0Testcase0FailureShouldBeTheFollowing(ExpectedValue: string): void {
    const ValueWithoutWhitespace = this._ActionResult?.Result.TestSuite[0].testcase[0].failure.replace(/\s+/g, ' ').trim()
    const ExpectedWithoutWhitespace = ExpectedValue.replace(/\s+/g, ' ').trim()
    ValueWithoutWhitespace.should.equal(ExpectedWithoutWhitespace)
  }

  @then(/the TestSuiteName should be '(.*)'/)
  public ThenTheTestSuiteNameShouldBe(TestSuiteName: string): void {
    this._ActionResult?.TestSuiteName.should.equal(TestSuiteName);
  }

  @then(/the Result\.Tests should be '(.*)'/)
  public ThenTheResultTestsShouldBe(Tests: string): void {
    this._ActionResult?.Result.Tests.should.equal(Tests);
  }

  @then(/the Result\.Errors should be '(.*)'/)
  public ThenTheResultErrorsShouldBe(Errors: string): void {
    this._ActionResult?.Result.Errors.should.equal(Errors);
  }

  @then(/the Result\.Failures should be '(.*)'/)
  public ThenTheResultFailuresShouldBe(Failures: string): void {
    this._ActionResult?.Result.Failures.should.equal(Failures);
  }

  @then(/the Result\.OriginalOutput should be the following content/)
  public OriginalOutput(Table: string): void {
    this._ActionResult?.Result.OriginalOutput.should.be.equal(Table);
  }
}

export = JUnitSteps;
