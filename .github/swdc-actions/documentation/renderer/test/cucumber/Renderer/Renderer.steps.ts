import { binding, given, then, when } from "cucumber-tsflow";
import { should } from "chai";
import { IParseResult } from "../../../src/Parser/IParseResult";
import { TestArtifactRenderer } from "../../../src/Renderer/TestArtifactRenderer";
import { TestArtifactSchemaEnum, TestArtifactTypeEnum } from "../../../src/TestArtifact/ITestArtifact";
import { ITemplateRepository } from "../../../src/TemplateRepository/ITemplateRepository";
import { IRenderer } from "../../../src/Renderer/IRenderer"

class MockTemplateRepository implements ITemplateRepository {
  private _Content: string;

  constructor(Content: string) {
    this._Content = Content;
  }

  GetTemplate(_Result: IParseResult): string {
    return this._Content;
  }
}


@binding()
class RendererSteps {
  private _Should: Chai.Should;
  private _ActionResult?: string;
  private _GivenTemplateRespository?: ITemplateRepository
  private _GivenTestResult?: IParseResult

  constructor() {
    this._Should = should();
    this._Should.exist(this._Should);
  }

  @given(/we mock the template repository with the template 'CodeCoverage-Cobertura\.md' and the following content/)
  public GivenWeMockTheTemplateRepository(Content: string) {
    this._GivenTemplateRespository = new MockTemplateRepository(Content);
  }

  @given(/we have a test result with schema '(.*)' of type '(.*)' and the following result/)
  public WeHaveATestResultWithSchema(Schema: string, Type: string, Content: any) {
    const TypeEnumValue = TestArtifactTypeEnum[Type as keyof typeof TestArtifactTypeEnum];
    const SchemaEnumValue = TestArtifactSchemaEnum[Schema as keyof typeof TestArtifactSchemaEnum];
    var TestResult: IParseResult;
    TestResult = {
      TestSuiteName: "some test suite",
      CommitHash: "someCommit",
      Schema: SchemaEnumValue,
      Type: TypeEnumValue,
      Result: JSON.parse(Content).Result
    };
    this._GivenTestResult = TestResult;
  }

  @when(/we call the Renderer/)
  public WhenWeCallTheRender(): void {
    var Renderer: IRenderer = new TestArtifactRenderer(this._GivenTemplateRespository!)
    this._ActionResult = Renderer.Render(this._GivenTestResult!)
  }

  @then(/the result should be/)
  public TheResultShouldBe(Content: string): void {
    this._ActionResult?.should.equal(Content);
  }
}

export = RendererSteps;
