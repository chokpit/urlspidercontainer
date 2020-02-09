FROM centos:centos7
ENV URL_VAR=http://www.ynet.co.il
RUN export URL_VAR
COPY start_script.sh start_script.sh
COPY bs.py bs.py
COPY ./project_env ./project_env
RUN yum install -y pip3 python3

RUN chmod +x start_script.sh
ENTRYPOINT [ "./start_script.sh" ]
