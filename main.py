from typing import Any
import composer2_airflow_rest_api
import functions_framework

# Replace with your Composer web server URL and DAG ID
WEB_SERVER_URL = "https://aac001cd64fd4a65b7d9cf7dc4045bec-dot-us-central1.composer.googleusercontent.com"
DAG_ID = "composer_sample_trigger_response_dag"

@functions_framework.cloud_event
def trigger_dag_gcf(cloud_event):
    """Triggered by a CloudEvent from GCS. Extracts file info and triggers a DAG."""
    data = cloud_event.data

    # Extract only serializable fields
    dag_conf = {
        "bucket": data.get("bucket"),
        "file_name": data.get("name"),
        "metageneration": data.get("metageneration"),
        "timeCreated": data.get("timeCreated"),
        "updated": data.get("updated")
    }

    print(f"Triggering DAG with conf: {dag_conf}")
    
    composer2_airflow_rest_api.trigger_dag(WEB_SERVER_URL, DAG_ID, dag_conf)
