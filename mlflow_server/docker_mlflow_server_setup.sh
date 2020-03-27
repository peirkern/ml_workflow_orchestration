docker build -t mlflow .
docker run -d -v ./filestore:/mlflow -p 5000:5000 mlflow