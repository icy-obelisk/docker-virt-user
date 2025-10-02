FROM ubuntu:24.04

ARG USER_NAME

RUN --mount=type=secret,id=password,env=USER_PASSWORD \
    apt update && apt upgrade -y && \
    apt install -y openssh-server sudo curl bash-completion command-not-found nano && \
    apt update && apt clean && apt autoremove --purge -y && \
    useradd -ms /bin/bash ${USER_NAME} && \
    usermod -aG sudo ${USER_NAME} && \
    echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    echo "${USER_NAME}:${USER_PASSWORD}" | chpasswd
COPY .bash_profile /home/${USER_NAME}/
COPY setup-miniforge.sh /home/${USER_NAME}/

USER ${USER_NAME}
WORKDIR /home/${USER_NAME}/
RUN ./setup-miniforge.sh

SHELL ["/bin/bash", "-l", "-c"]
ENTRYPOINT sudo service ssh restart && /bin/bash
