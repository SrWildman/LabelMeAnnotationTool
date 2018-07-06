#!/bin/bash
cp /var/www/html/AnnotationTool/Images/.htaccess /var/www/html/AnnotationTool/Annotations/.htaccess
make -C /var/www/html/AnnotationTool/
/etc/init.d/apache2 start
# python3 /var/www/html/dcm-jpg.py /var/www/html/AnnotationTool/Images
tail -f /dev/null
