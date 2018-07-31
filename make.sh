#!/bin/bash
cp /var/www/html/AnnotationTool/Images/.htaccess /var/www/html/AnnotationTool/Annotations/.htaccess
python3 /var/www/html/dcm-jpg.py /var/www/html/AnnotationTool/tmp_store /var/www/html/AnnotationTool/Images /var/www/html/AnnotationTool/Annotations > /var/log/dcm_log
make -C /var/www/html/AnnotationTool/
/etc/init.d/apache2 start

tail -f /dev/null
