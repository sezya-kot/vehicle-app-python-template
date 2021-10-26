import * as fs from "fs";
import { IPersistentStore } from "./IPersistentStore";
import * as path from "path";

export class LinuxFileSystemPersistentStore implements IPersistentStore {
    private _BasePath;

    constructor(BasePath: string) {
        // this._BasePath = path.resolve(__dirname, BasePath);
        this._BasePath = BasePath;
    }

    public GetFiles(Filter: string): string[] {
        var FileList: string[] = [];
        var FilteredFiles: string[] = [];

        console.log("Scanning folder '" + this._BasePath + "' with filter '" + Filter + "'")
        var RootFileList = fs.readdirSync(this._BasePath);

        RootFileList.forEach((Entry: string) => {
            var EntryFilename = path.join(this._BasePath, Entry);
            if (fs.statSync(EntryFilename).isDirectory()) {
                var SubfolderName = Entry;
                var SubfolderFileList = fs.readdirSync(EntryFilename);
                SubfolderFileList.forEach((Entry: string) => {
                    FileList.push(path.join(SubfolderName, Entry))
                })
            } else {
                FileList.push(Entry);
            }
        })

        FileList.forEach((File: string) => {
            if (path.basename(File) === Filter) {
                console.log("Found " + File)
                FilteredFiles.push(File);
            }
        })
        console.log("Found " + FilteredFiles.length + " file(s)")
        return FilteredFiles;
    }

    public Load(Name: string): string {
        const Filename = path.join(this._BasePath, Name);
        const Data: string = fs.readFileSync(Filename, { encoding: 'utf8', flag: 'r' });
        return Data;
    }

    public Save(Name: string, Data: string): void {
        const Filename = path.join(this._BasePath, Name);
        fs.mkdirSync(this._BasePath, { recursive: true });
        fs.writeFileSync(Filename, Data);
        console.log(`File written to ${Filename}`);
    }

    public List(Path: string): string[] {
        return fs.readdirSync(Path);
    }
}
