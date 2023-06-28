FROM ubuntu:22.04
RUN apt-get update 
RUN apt-get install -y nginx

COPY src/html/index.html /var/www/html/index.nginx-debian.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]