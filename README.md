# 🚀 GCS to Composer DAG Trigger

This project sets up a **Cloud Function** that triggers an **Apache Airflow DAG in Cloud Composer 2** whenever a new file is uploaded to a **Google Cloud Storage (GCS) bucket**.

### 🔧 How It Works

- Listens to GCS object finalize events (file uploads)
- Extracts metadata like file name, bucket, and timestamps
- Calls the Composer 2 Airflow REST API to trigger a DAG

Useful for automating workflows based on new files in cloud storage.
