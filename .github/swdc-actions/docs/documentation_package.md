# Release Documentation Package Action

The action `documentation/package` copies all files from sourcePath to the packagePath under a subfolder name.
It also adds a metadata file to the folder containing name, type and format of the artifacts. 

**Location**
documentation/package

**Inputs**
|Name|Required|Description|Example values|
|-|-|-------------------|---------------|
|name|true|arbitrary name for the artifact|Unit Test Results Talent X|
|type|true|type of the artifact|UnitTest, IntegrationTest, ContainerScan, ...
|format|true|format of the files|junit, ...
|sourcePath|true|folder where the action retrieves the raw result files|
|packagePath|true|target path where the results are copied to |



