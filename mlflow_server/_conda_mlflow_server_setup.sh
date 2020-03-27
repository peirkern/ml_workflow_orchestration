conda env create -f environment.yml
source activate mlflow_server
mlflow server --backend-store-uri ./mnt/backend_store_uri --default-artifact-root ./mnt/artifact_root --host 0.0.0.0