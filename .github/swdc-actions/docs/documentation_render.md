# Release Documentation Render Action

The action `documentation/render` reads all input packages from the `inboxPath` and renders it as markdown to `outboxPath`. Available templates are stored in `templatePath`. 

**Location**
documentation/render

**Inputs**
|Name|Required|Description|Example values|
|-|-|-------------------|---------------|
|inboxPath|false|path containing the packaged input files for the release documentation  ||
|outboxPath|false|output path for the rendered release documentation |
|templatePath|false|path to the templates used for release documentation generation|./.github/swdc-actions/documentation/renderer/templates



