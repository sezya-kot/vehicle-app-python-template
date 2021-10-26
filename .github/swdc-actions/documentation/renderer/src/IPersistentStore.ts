export interface IPersistentStore {
  GetFiles(Filter: string): string[];
  Load(Name: string): string;
  Save(Name: string, Data: string): void;
  List(Path: string): string[];
}
