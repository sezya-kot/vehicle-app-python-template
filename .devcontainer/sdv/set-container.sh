#!/usr/bin/env bash
echo
echo "#######################################################"
echo "### Checking successful container configuration"
echo "#######################################################"

echo "## checking if docker-init.sh was created by docker-in-docker-debian.sh" 
if [ -f "/usr/local/share/docker-init.sh" ]; then
    echo "## /usr/local/share/docker-init.sh already exists. Fallback docker-init.sh does not need to be created." 
else 
    echo "## WARNING: failed to find docker-init.sh. Creating fallback docker-init.sh." 
    echo 'exec "$@"' > /usr/local/share/docker-init.sh
    chmod +x /usr/local/share/docker-init.sh
    sleep 5
fi

echo "## checking if user 'vscode' was created by common-debian.sh" 
if id -u vscode > /dev/null 2>&1; then
    echo "## found existing user 'vscode'"
else
    echo "## WARNING: failed to find user 'vscode'. Adding user 'vscode' directly as a fallback"
    useradd vscode --password vscode -m 
    usermod -aG sudo vscode
    sleep 5
fi

exit 0