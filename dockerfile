FROM php:7.0-apache
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY apache2.conf /etc/apache2/apache2.conf
COPY make.sh /
RUN chmod +x /make.sh
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common
ENV PERL5LIB=".:${PERL5LIB}"
RUN apt-get install -y --no-install-recommends libapache2-mod-perl2 && \
  a2enmod include && \
  a2enmod rewrite && \ 
  a2enmod cgi
RUN apt-get install -y --no-install-recommends libcgi-session-perl
RUN apt-get install -y python3-pip python3-pil
RUN pip3 install pydicom numpy


CMD /make.sh