FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY html /usr/share/nginx/site/html
COPY css /usr/share/nginx/site/css
COPY js /usr/share/nginx/site/js

EXPOSE 80

