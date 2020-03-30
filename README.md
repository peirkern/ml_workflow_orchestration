## ml_workflow_orchestration

# Instructions
1. Setup local conda environmet (notebook execution)
```
cd local
./setup.sh
```
2. Setup AirFlow
```
cd airflow
./setup.sh
```
3. Setup MinIO (~S3)
```
. cd minio
./setup.sh
```
4. Setup MLflow
```
cd mlflow
./setup.sh
```
5. run local\notebook\minio_create_bucket.ipynb
6. run local\notebook\model_pipeline.ipynb

# Urls (docker)
- AirFlow: http://192.168.99.100:8080/
- MLflow: http://192.168.99.100:5000/
- MinIO: http://192.168.99.100:9000/ (minioadmin/minioadmin)