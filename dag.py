from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

# Config
PROJECT_ID = "mounika2295"
DATASET = "Student_123"
TABLE = "Teacher1234"
BUCKET = "nani2"
SOURCE_FILE = "mk.csv"

default_args = {
    "start_date"(2026)
}
with DAG(
    dag_id="gcs_to_bq_schedule",
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    load_data = GCSToBigQueryOperator(
        task_id="load_gcs_to_bq",
        bucket=BUCKET,
        source_objects=[SOURCE_FILE],
        destination_project_dataset_table=f"{mounika2295}.{Student_123}.{Teacher1234}",
        source_format="CSV",
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",  # or WRITE_APPEND
        autodetect=True,
    )

    load_data