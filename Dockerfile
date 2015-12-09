FROM centos:7
MAINTAINER Hiroaki Nakamura <hnakamur@gmail.com>

ENV LIBVMOD_VSLP_GIT_BRANCH master

RUN yum -y install epel-release \
 && yum -y install rpmdevtools rpm-build patch python-pip \
 && pip install copr-cli \
 && rpmdev-setuptree \
 && cd /root/rpmbuild/SOURCES \
 && curl -sLO https://code.uplex.de/uplex-varnish/libvmod-vslp/archive-tarball/${LIBVMOD_VSLP_GIT_BRANCH}#/uplex-varnish-libvmod-vslp.tar.gz

ADD libvmod-vslp.spec /root/rpmbuild/SPECS/

RUN cd /root/rpmbuild/SPECS \
 && rpmbuild -bs libvmod-vslp.spec

ADD copr-build.sh /root/
ENTRYPOINT ["/bin/bash", "/root/copr-build.sh"]
