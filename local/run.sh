source activate mlworkflow

export MLFLOW_S3_ENDPOINT_URL=http://host.docker.internal:9000
export AWS_ACCESS_KEY_ID=minioadmin
export AWS_SECRET_ACCESS_KEY=minioadmin
export MLFLOW_URL=http://host.docker.internal:5000/

cd notebook
jupyter notebook