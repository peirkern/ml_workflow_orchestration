conda env create -f environment.yml
source activate mlworkflow

mkdir -p notebook

export MLFLOW_S3_ENDPOINT_URL=http://192.168.99.100:9000
export AWS_ACCESS_KEY_ID=minioadmin
export AWS_SECRET_ACCESS_KEY=minioadmin
export MLFLOW_URL=http://192.168.99.100:5000/

cd notebook
jupyter notebook