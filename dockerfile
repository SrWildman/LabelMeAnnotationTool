FROM php:7.0-apache
COPY src/ /var/www/html/
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN apt-get install apache2 php5 libapache2-mod-php5 libapache2-mod-perl2 perl-cgi libcgi-session-perl && \
  a2enmod include && \
  a2enmod rewrite && \
  a2enmod cgi 