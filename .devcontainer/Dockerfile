FROM ubuntu:20.04
# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="false"
# [Option] Enable non-root Docker access in container
ARG ENABLE_NONROOT_DOCKER="true"
# [Option] Use the OSS Moby Engine instead of the licensed Docker Engine
ARG USE_MOBY="true"

# Install needed packages and setup non-root user. Use a separate RUN statement to add your
# own dependencies. A user of "automatic" attempts to reuse an user ID if one already exists.
ARG USERNAME=automatic
ARG USER_UID=1000
ARG USER_GID=$USER_UID

COPY library-scripts/*.sh /tmp/library-scripts/
RUN /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" 2>&1 | tee -a /usr/local/share/common-debian.log
RUN /bin/bash /tmp/library-scripts/docker-in-docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "${USERNAME}" "${USE_MOBY}" 2>&1 | tee -a /usr/local/share/docker-in-docker-debian.log

COPY sdv/ /tmp/sdv/
RUN /bin/bash /tmp/sdv/set-container.sh 2>&1 | tee -a /usr/local/share/set-container.log
RUN /bin/bash /tmp/sdv/add-powershell.sh 2>&1 | tee -a /usr/local/share/add-powershell.log
RUN /bin/bash /tmp/sdv/add-dapr.sh 2>&1 | tee -a /usr/local/share/add-dapr.log
RUN /bin/bash /tmp/sdv/add-nodejs.sh 2>&1 | tee -a /usr/local/share/add-nodejs.log
RUN /bin/bash /tmp/sdv/add-python.sh 2>&1 | tee -a /usr/local/share/add-python.log

# Add daprd to the path for the VS Code Dapr extension.
ENV PATH=$PATH:/home/vscode/.dapr/bin

VOLUME [ "/var/lib/docker" ]

# Setting the ENTRYPOINT to docker-init.sh will start up the Docker Engine
# inside the container "overrideCommand": false is set in devcontainer.json.
# The script will also execute CMD if you need to alter startup behaviors.
ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]
CMD [ "sleep", "infinity" ]
