FROM centos:centos7
ENV URL_VAR=https://www.google.com
COPY start_script.sh start_script.sh
COPY ./project_env ./project_env
RUN yum install -y pip3 python3
RUN chmod +x start_script.sh
ENTRYPOINT [ "./start_script.sh" ]
