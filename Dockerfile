FROM centos:centos7
ENV URL_VAR=https://www.google.com
COPY start_script.sh start_script.sh
COPY ./project_env ./project_env
RUN yum install -y pip3 python3

#add aliases from file
COPY aliases.conf aliases.conf
ENV BASHRC_FILE_PATH=/root/.bashrc
ENV ALIASES_TO_ADD=/aliases.conf
RUN cat "$ALIASES_TO_ADD" >> "$BASHRC_FILE_PATH"

RUN export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
RUN chmod +x start_script.sh
ENTRYPOINT [ "./start_script.sh" ]
