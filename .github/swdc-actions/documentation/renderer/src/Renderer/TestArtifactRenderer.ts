import * as handlebars from "handlebars";
import { ITemplateRepository } from "../TemplateRepository/ITemplateRepository";
import { IParseResult } from "../Parser/IParseResult";
import { IRenderer } from "./IRenderer";

export class TestArtifactRenderer implements IRenderer {
    private _TemplateRepository: ITemplateRepository;

    constructor(TemplateRepository: ITemplateRepository) {
        this._TemplateRepository = TemplateRepository;
     }

    public Render(Result: IParseResult): string {
        try {
            
            const TemplateSource = this._TemplateRepository.GetTemplate(Result);
            const template = handlebars.compile(TemplateSource, { strict: true });
            
            const result = template(Result);

            console.log(result);
            return result;
        } catch (e) {
            console.log(`failed to create documentation with error: ${e}`);
            throw e;
        }
    }
}
