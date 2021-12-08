#!/bin/bash
hugo new site hugo

cp ./README.md ./hugo/content/_index.md

mkdir ./hugo/content/documentation
cp ./README.md ./hugo/content/documentation/_index.md
sed -i '1d' hugo/content/documentation/_index.md
sed -i '1s/^/---\ntitle: "VehicleApp using Python"\ndraft: false\n---\n/' hugo/content/documentation/_index.md

mkdir ./hugo/content/reports
mkdir ./hugo/content/reports/code-coverage
mkdir ./hugo/content/reports/integration-test
mkdir ./hugo/content/reports/unit-test
mkdir ./hugo/content/reports/vulnerability-scan-client
mkdir ./hugo/content/reports/vulnerability-scan-vehicleapi

echo $'---\ntitle: "Code Coverage Test"\n---\n{{% include-pb-resource "code_coverage_report.md" %}}' > ./hugo/content/reports/code-coverage/index.md
echo $'---\ntitle: "Integration Test Results"\n---\n{{% include-pb-resource "integration_test_report.md" %}}\n## Rendered Html Reports\n[Link to report](integration-test/integration-test.html)\n{{% include-pb-resource "integration-test.html" %}}\n' > ./hugo/content/reports/integration-test/index.md
echo $'---\ntitle: "Unit Test Results"\n---\n{{% include-pb-resource "unit_test_report.md" %}}## Rendered Html Reports\n[Link to report](unit-test/unit-test.html)\n{{% include-pb-resource "unit-test.html" %}}\n' > ./hugo/content/reports/unit-test/index.md
echo $'---\ntitle: "Vulnerability Scan Results"\n---\n{{% include-pb-resource "vulnerability_scan_report.md" %}}\n## Rendered Html Reports\n[Link to report](vulnerability-scan-client/vulnerability-scan.html)\n{{% include-pb-resource "vulnerability-scan.html" %}}\n' > ./hugo/content/reports/vulnerability-scan-client/index.md
echo $'---\ntitle: "Vulnerability Scan Results"\n---\n{{% include-pb-resource "vulnerability_scan_report.md" %}}\n## Rendered Html Reports\n[Link to report](vulnerability-scan-vehicleapi/vulnerability-scan.html)\n{{% include-pb-resource "vulnerability-scan.html" %}}\n' > ./hugo/content/reports/vulnerability-scan-vehicleapi/index.md

mkdir ./hugo/config
mkdir ./hugo/config/_default
mkdir ./hugo/config/pages

echo $'languageCode = "en-us"\ntitle = "Release Documentation - @tag"\n\nbaseURL = "http://example.org/"\n\n# Keep uglyURLs for now, as this provides the best out of the box support for rendering markdown images in VSCode preview and Hugo\n# Link: https://gohugo.io/content-management/urls/#ugly-urls\nuglyURLs = "true"\n\nenableGitInfo = true\n\ntheme = "hugo-geekdoc"\n\n# Geekdoc required configuration\npygmentsUseClasses = true\npygmentsCodeFences = true\ndisablePathToLower = true\n\n[markup]\ndefaultMarkdownHandler = "goldmark"\n\n[markup.goldmark.renderer]\nunsafe = true\n\n[markup.tableOfContents]\n    ordered= false\n    startLevel= 1\n    endLevel= 3\n\n[params]\ngeekdocRepo = "https://github.com/SoftwareDefinedVehicle/vehicle-app-python-template"\ngeekdocEditPath = "edit/main/hugo/content"\ngeekdocCollapseSection = true\n' > ./hugo/config/_default/config.toml
echo $'# Hugo-Geekdoc Theme Config\n\nbaseURL = "https://fantastic-fiesta-da4ab8e5.pages.github.io/"\n\ntheme = "hugo-geekdoc"\n\nenableGitInfo = false\n\npluralizeListTitles = false\npygmentsUseClasses = true\n\n[markup]\n  defaultMarkdownHandler = "goldmark"\n\n[markup.highlight]\n    anchorLineNos = false\n    codeFences = true\n    guessSyntax = false\n    hl_Lines = ""\n    lineAnchors = ""\n    lineNoStart = 1\n    lineNos = true\n    lineNumbersInTable = true\n    noClasses = false\n    style = "paraiso-dark"\n    tabWidth = 4\n\n[markup.tableOfContents]\n    endLevel = 3\n    ordered = false\n    startLevel = 1\n\n[markup.goldmark.extensions]\n    typographer = true\n\n[markup.goldmark.renderer]\n    unsafe = true\n\n# Disable geekdoc default theme settings\n[params]\ngeekdocRepo = ""\ngeekdocEditPath = ""\n# disable non-working search when serving from local file system\ngeekdocSearch = false\n' > ./hugo/config/pages/config.toml

mkdir hugo/data/menu
echo "---" > ./hugo/data/menu/extra.yaml
printf "header:\n  - name: GitHub\n    ref: https://github.com/SoftwareDefinedVehicle/vehicle-app-python-template\n    icon: gdoc_github\n    external: true\n" >> ./hugo/data/menu/extra.yaml

echo "---" > ./hugo/data/menu/more.yaml
printf 'more:\n  - name: Releases\n    ref: "https://github.com/SoftwareDefinedVehicle/vehicle-app-python-template/releases"\n    external: true\n    icon: "gdoc_download"\n  - name: "View Source"\n    ref: "https://github.com/SoftwareDefinedVehicle/vehicle-app-python-template/tree/@tag"\n    external: true\n    icon: "gdoc_github"\n' >> ./hugo/data/menu/more.yaml

mkdir hugo/layouts/shortcodes
echo $'{{$pbFile := .Get 0}}\n{{ if strings.HasSuffix $pbFile ".html" }}\n<iframe src="{{ with .Page.Resources.GetMatch $pbFile }}{{ .RelPermalink }}{{ end }}" frameborder="0" seamless style="width:100%;height:1000px;" onload="this.style.height=(this.contentDocument.body.scrollHeight + 40) + \'px\';"></iframe>\n{{ else if strings.HasSuffix $pbFile ".md" }}\n{{ with .Page.Resources.GetMatch $pbFile }}{{ .RawContent | safeHTML }}{{ end }}\n{{ end }}' > ./hugo/layouts/shortcodes/include-pb-resource.html