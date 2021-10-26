import { IPersistentStore } from "../src/IPersistentStore";

export class MockPersistentStore implements IPersistentStore {
  private _Files: {Name: string, Content: string}[] = [];

  public GetFiles(Filter: string): string[] {
    const keys: string[] = [];
    this._Files.forEach((Entry: {Name: string, Content: string}) => {
      if (Entry.Name.endsWith(Filter)) {
        keys.push(Entry.Name);
      }
    })
    return keys;
  }

  public Load(Name: string): string {
    var Content: string = "";
    var Found: boolean = false;
    this._Files.forEach((Entry: {Name: string, Content: string}) => {
      if (Entry.Name  === Name) {
        Content = Entry.Content
        Found = true;
      }
    }) 
    if (!Found) {
      throw "Failed to find file '" + Name + "'"
    }
    return Content;
  }

  public Save(Name: string, Content: string): void {
    this._Files.push( {
      Name: Name,
      Content: Content
    });
  }

  public List(): string[] {
    let keys = [];
    for (var Key in this._Files.keys)
      keys.push(Key);
    return keys;
  }
}
