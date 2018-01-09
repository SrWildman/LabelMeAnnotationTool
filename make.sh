#!/bin/bash
make -C /var/www/html/AnnotationTool/
/etc/init.d/apache2 start
tail -f /dev/null
