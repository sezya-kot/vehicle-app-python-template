#!/bin/bash

# mkdir hugo/data/menu
echo "---" > ./hugo/data/menu/main.yaml
printf "header:\n  - name: GitHub\n    ref: https://github.com/SoftwareDefinedVehicle/vehicle-app-python-template\n    icon: gdoc_github\n    external: true\n" >> ./hugo/data/menu/main.yaml

echo "---" > ./hugo/data/menu/more.yaml
printf 'more:\n  - name: Releases\n    ref: "https://github.com/SoftwareDefinedVehicle/vehicle-app-python-template/releases"\n    external: true\n    icon: "gdoc_download"\n  - name: "View Source"\n    ref: "https://github.com/SoftwareDefinedVehicle/vehicle-app-python-template/tree/@tag"\n    external: true\n    icon: "gdoc_github"\n' >> ./hugo/data/menu/more.yaml


# mkdir hugo/layouts/shortcode
echo $'{{$pbFile := .Get 0}}\n{{ if strings.HasSuffix $pbFile ".html" }}\n<iframe src="{{ with .Page.Resources.GetMatch $pbFile }}{{ .RelPermalink }}{{ end }}" frameborder="0" seamless style="width:100%;height:1000px;" onload="this.style.height=(this.contentDocument.body.scrollHeight + 40) + \'px\';"></iframe>\n{{ else if strings.HasSuffix $pbFile ".md" }}\n{{ with .Page.Resources.GetMatch $pbFile }}{{ .RawContent | safeHTML }}{{ end }}\n{{ end }}' > ./hugo/layouts/shortcodes/include-pb-resource.html