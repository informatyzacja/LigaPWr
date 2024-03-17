FROM nginx

RUN rm -f /etc/nginx/conf.d/default.conf

COPY conf.d/ /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf

COPY html/ /etc/nginx/html/
COPY letsencrypt/ /etc/nginx/letsencrypt/
