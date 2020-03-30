#docker run --rm -it -p 21:21 -p 4559-4564:4559-4564 -e FTP_USER=ftp -e FTP_PASSWORD=ftp docker.io/panubo/vsftpd:latest
docker-compose -f docker-compose.yml up -d