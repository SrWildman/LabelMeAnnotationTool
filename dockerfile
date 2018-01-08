FROM php:7.0-apache
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY apache2.conf /etc/apache2/apache2.conf
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common  && apt-get update
RUN apt-get install -y --no-install-recommends libapache2-mod-perl2 && \
  a2enmod include && \
  a2enmod rewrite && \ 
  a2enmod cgi
RUN apt-get update && apt-get install -y --no-install-recommends libcgi-session-perl

CMD make -C /var/www/html/LabelMeAnnotationTool/make ; sleep infinity