import { ITemplateRepository } from "./ITemplateRepository";
import { IParseResult } from "../Parser/IParseResult";
import { IPersistentStore } from "../IPersistentStore";
import { LinuxFileSystemPersistentStore } from "../LinuxFileSystemPersistentStore";

export class TemplateRepository implements ITemplateRepository {
    private _PersistentStore: IPersistentStore;

    constructor(TemplateFolder: string) {
        this._PersistentStore = new LinuxFileSystemPersistentStore(TemplateFolder)
     }

    public GetTemplate(Result: IParseResult): string {
        const TemplateFilename = Result.Type.toString() + "-" + Result.Schema.toString() + ".md";
        const source = this._PersistentStore.Load(TemplateFilename)
        return source;
    }
}
