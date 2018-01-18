#!/bin/bash
cp /var/www/html/AnnotationTool/Images/.htaccess /var/www/html/AnnotationTool/Annotations/.htaccess
make -C /var/www/html/AnnotationTool/
/etc/init.d/apache2 start
tail -f /dev/null
