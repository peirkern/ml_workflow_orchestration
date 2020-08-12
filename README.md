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
4. run local\notebook\download_data.ipynb
5. run local\notebook\model_pipeline.ipynb

# Urls (docker)
- AirFlow: http://host.docker.internal:8080/
- MLflow: http://host.docker.internal:5000/
- MinIO: http://host.docker.internal:9000/ (minioadmin/minioadmin)
