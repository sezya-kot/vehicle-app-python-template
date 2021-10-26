import { IParseResult } from "../Parser/IParseResult";

export interface ITemplateRepository {
    GetTemplate(Result: IParseResult): string;
}
