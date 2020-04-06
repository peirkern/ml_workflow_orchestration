## ml_workflow_orchestration

# Prerequisites
- Docker Desktop 2.2.0.5
- Git & GitBash
- Anaconda

# Instructions
1. Setup local conda environmet with GitBash
```
cd local
./setup.sh
```
2. Setup AirFlow, MinIO, MLflow with Docker
```
./docker_setup_all.sh
```
3. run local\notebook\minio_create_bucket.ipynb
4. run local\notebook\model_pipeline.ipynb

# Urls (docker)
- AirFlow: http://192.168.99.100:8080/
- MLflow: http://192.168.99.100:5000/
- MinIO: http://192.168.99.100:9000/ (minioadmin/minioadmin)
