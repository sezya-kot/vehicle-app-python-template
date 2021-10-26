import { IParseResult } from "../Parser/IParseResult";

export interface IRenderer {
    Render(Result: IParseResult): string;
}
