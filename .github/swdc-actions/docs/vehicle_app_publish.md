# VehicleApp Publish Action

The action `vapp/publish` publishes a VehicleApp container image to the OTA system. This includes the following steps:

- Retrieve pre-built container image with `commit` and `vappName` from `sourceRegistry` and upload it to `targetRegistry` optionaly with `tagAsLatest` set to true which will result in additional tagging with "latest".
- Retrieve an OAuth Bearer Token with `clientId`, `clientSecret`, `grantType`and `scope` from `azureUrl`.
- Send PUT-Request to `otaUrl` containing link VAPP name, version and link to uploaded container image.

**Prequisites**
Login to `sourceRegistry` and `targetRegistry` need to be performed before invoking the action.

**Location**
vapp/install

**Inputs**
|Name|Required|Description|Default values|
|-|-|-------------------|---------------|
|commit|true|Commit hash to retrieve the image from ghcr  ||
|vappVersion|true|VAPP version which will be published to OTA |
|vappName|true|VAPP name which will be publish to OTA'
|sourceRegistry|true|Registry where source image is located
|targetRegistry|true|Target Registry where the container image will be pushed|
|tagAsLatest|false|Set to `true` will result in additional tagging with "latest" in the container registry. Note: has nothing to do with actual released version as sent to OTA system. |
otaUrl|true|Metadata endpoint of the OTA system|
clientId|true|OAuth clientId
clientSecret|true|OAuth client secret|
azureUrl|false|OAuth endpoint|https://login.microsoftonline.com/0ae51e19-07c8-4e4b-bb6d-648ee58410f4/oauth2/v2.0/token
grantType|false| OAuth grant type| client_credentials
scope|false|OAuth scope  |api://3ceb092f-44af-49e8-ba3f-b33f387073b8/.default



