FROM centos:latest

RUN yum install wget -y

RUN wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

RUN rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

RUN yum install jenkins -y

RUN yum install java-11-openjdk.x86_64 -y

Run yum install sudo -y

RUN echo -e "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

EXPOSE 8080

RUN yum install net-tools -y

RUN mkdir /home/mycode/

COPY mail.py   /home/mycode/

COPY docker.repo  /etc/yum.repos.d/
#RUN yum install /sbin/service -y

RUN yum install python36 -y

RUN yum install git -y

RUN yum install docker-ce --nobest -y

#USER jenkins
#ENV USER jenkins

CMD java -jar /usr/lib/jenkins/jenkins.war

#CMD /etc/rc.d/init.d/jenkins start -DFORGROUND