# Install k3d
wget -q -O - https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash

# Install brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" < /dev/null

# (Optional) Install k9s
/home/linuxbrew/.linuxbrew/bin/brew install derailed/k9s/k9s
