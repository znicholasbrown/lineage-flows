from typing import Dict

def create_resource(resource_type: str, name: str, role: str) -> Dict[str, str]:
    return {
        "prefect.resource.id": f"{resource_type}://{name.lower().replace(' ', '_')}",
        "prefect.resource.role": role,
        "prefect.resource.name": name
    }

# Frontend and Application Resources
k8s_frontend = create_resource("k8s", "Frontend Cluster", "application_hosting")
k8s_backend = create_resource("k8s", "Backend Cluster", "application_hosting")
k8s_monitoring = create_resource("k8s", "Monitoring Cluster", "system_monitoring")

# Data Storage Resources
mongodb_main = create_resource("mongodb", "Main Database", "data_storage")
redis_cache = create_resource("redis", "Cache Layer", "caching")
pgsql_analytics = create_resource("pgsql", "Analytics DB", "data_storage")

# Cloud Resources
s3_storage = create_resource("s3", "Object Storage", "data_storage")
gcp_services = create_resource("gcp", "Cloud Services", "cloud_platform")

# Data Pipeline Resources
snowflake_warehouse = create_resource("snowflake", "Data Warehouse", "data_processing")
dbt_transforms = create_resource("dbt", "Data Transforms", "data_transformation")
fivetran_etl = create_resource("fivetran", "Data Pipeline", "data_integration")

# Monitoring and Communication
sendgrid_notifications = create_resource("sendgrid", "Email Service", "notifications")
prometheus = create_resource("k8s", "Prometheus", "monitoring")
grafana = create_resource("k8s", "Grafana", "visualization")

mobile_application = {
    "prefect.resource.id": "app://mobile.clif.com",
    "prefect.resource.role": "application",
    "prefect.resource.name": "Clif Mobile App"
}

heroku = {
    "prefect.resource.id": "heroku://production",
    "prefect.resource.role": "application_deployment",
    "prefect.resource.name": "Heroku Production"
}

aurora = {
    "prefect.resource.id": "aurora://production",
    "prefect.resource.role": "database",
    "prefect.resource.name": "Aurora Production"
}

shipyard = {
    "prefect.resource.id": "shipyard://production",
    "prefect.resource.role": "application_deployment",
    "prefect.resource.name": "Shipyard Production"
}

sidekiq = {
    "prefect.resource.id": "sidekiq://queue",
    "prefect.resource.role": "queue",
    "prefect.resource.name": "Sidekiq Queue"
}

fivetran = {
    "prefect.resource.id": "fivetran://production",
    "prefect.resource.role": "data_pipeline",
    "prefect.resource.name": "Fivetran Production"
}

snowflake_ingest = {
    "prefect.resource.id": "snowflake://ingest",
    "prefect.resource.role": "database",
    "prefect.resource.name": "Snowflake Ingest"
}

snowflake_analytics = {
    "prefect.resource.id": "snowflake://analytics",
    "prefect.resource.role": "database",
    "prefect.resource.name": "Snowflake Analytics"
}

dbt = {
    "prefect.resource.id": "dbt://transform",
    "prefect.resource.role": "data_pipeline",
    "prefect.resource.name": "DBT Transform"
}

rds = {
    "prefect.resource.id": "rds://production",
    "prefect.resource.role": "database",
    "prefect.resource.name": "RDS Production"
}

sendgrid = {
    "prefect.resource.id": "sendgrid://production",
    "prefect.resource.role": "email",
    "prefect.resource.name": "Sendgrid"
}

REDSHIFT_TABLE_A = {"prefect.resource.id": "redshift://my_database/my_schema/table_a", "prefect.resource.name": "Raw Customers", "prefect.resource.role": "table"}
REDSHIFT_TABLE_B = {"prefect.resource.id": "redshift://my_database/my_schema/table_b", "prefect.resource.name": "Regions", "prefect.resource.role": "table"}
REDSHIFT_TABLE_C = {"prefect.resource.id": "redshift://my_database/my_schema/table_c", "prefect.resource.name": "Raw Orders", "prefect.resource.role": "table"}
REDSHIFT_TABLE_D = {"prefect.resource.id": "redshift://my_database/my_schema/table_d", "prefect.resource.name": "Item Popularity", "prefect.resource.role": "table"}

DATABRICKS_TABLE_A = {"prefect.resource.id": "databricks://my_database/my_schema/table_a", "prefect.resource.name": "Customers by Region", "prefect.resource.role": "table"}
DATABRICKS_TABLE_B = {"prefect.resource.id": "databricks://my_database/my_schema/table_b", "prefect.resource.name": "Orders of Popular Items", "prefect.resource.role": "table"}
DATABRICKS_TABLE_C = {"prefect.resource.id": "databricks://my_database/my_schema/table_c", "prefect.resource.name": "Top Customer of Popular Items by Region", "prefect.resource.role": "table"}