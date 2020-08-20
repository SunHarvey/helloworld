FROM centos:7
MAINTAINER SunHarvey
ENV USER centos
ENV APP_HOME /home/$USER/apps/

RUN yum install wget -y && \
 rm -rf  /etc/yum.repos.d/* && \
 wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo && \
 wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo && \
 yum install python36 python36-devel python3-pip git -y && \
 yum clean all  && \
 useradd -m  -s /bin/bash $USER && \
 mkdir /home/$USER/apps/ -p && \
 chown centos.centos -R /home/$USER/apps/ && \
 mkdir ~/.pip && \
 echo "[global]" > ~/.pip/pip.conf && \
 echo "index-url = https://mirrors.aliyun.com/pypi/simple/" >> ~/.pip/pip.conf && \
 echo "[install]" >> ~/.pip/pip.conf && \
 echo "trusted-host=mirrors.aliyun.com" >> ~/.pip/pip.conf  && \
 echo "[list]" >> ~/.pip/pip.conf && \
 echo "format=columns" >> ~/.pip/pip.conf && \
 pip3 install django==2.0 && \
 cd $APP_HOME && git clone https://github.com/SunHarvey/helloworld.git

USER centos
WORKDIR /home/$USER/apps/helloworld/

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]