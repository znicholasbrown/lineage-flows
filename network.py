from prefect import flow
from prefect._experimental.lineage import emit_external_resource_lineage
from resources import (
    k8s_frontend,
    k8s_backend,
    k8s_monitoring,
    mongodb_main,
    redis_cache,
    pgsql_analytics,
    s3_storage,
    gcp_services,
    snowflake_warehouse,
    dbt_transforms,
    fivetran_etl,
    sendgrid_notifications,
    prometheus,
    grafana
)

@flow(name="frontend_backend_flow", log_prints=True)
async def frontend_backend_flow():
    """Simulates the relationship between frontend and backend services"""
    await emit_external_resource_lineage(
        upstream_resources=[k8s_frontend],
        downstream_resources=[k8s_backend, redis_cache]
    )

@flow(name="backend_data_flow", log_prints=True)
async def backend_data_flow():
    """Simulates the data flow from backend services to storage"""
    await emit_external_resource_lineage(
        upstream_resources=[k8s_backend],
        downstream_resources=[mongodb_main, redis_cache, s3_storage]
    )

@flow(name="monitoring_flow", log_prints=True)
async def monitoring_flow():
    """Simulates the monitoring stack relationships"""
    await emit_external_resource_lineage(
        upstream_resources=[k8s_frontend, k8s_backend, mongodb_main],
        downstream_resources=[prometheus]
    )
    await emit_external_resource_lineage(
        upstream_resources=[prometheus],
        downstream_resources=[grafana, sendgrid_notifications]
    )

@flow(name="data_pipeline_flow", log_prints=True)
async def data_pipeline_flow():
    """Simulates the data warehouse pipeline"""
    await emit_external_resource_lineage(
        upstream_resources=[mongodb_main, pgsql_analytics],
        downstream_resources=[fivetran_etl]
    )
    await emit_external_resource_lineage(
        upstream_resources=[fivetran_etl],
        downstream_resources=[snowflake_warehouse]
    )
    await emit_external_resource_lineage(
        upstream_resources=[snowflake_warehouse],
        downstream_resources=[dbt_transforms]
    )

@flow(name="cloud_services_flow", log_prints=True)
async def cloud_services_flow():
    """Simulates cloud service integrations"""
    await emit_external_resource_lineage(
        upstream_resources=[k8s_backend, k8s_monitoring],
        downstream_resources=[gcp_services]
    )
    await emit_external_resource_lineage(
        upstream_resources=[gcp_services],
        downstream_resources=[s3_storage]
    )

@flow(name="k8s_network_simulation")
async def k8s_network_simulation():
    """Main flow that runs all network simulation flows"""
    await frontend_backend_flow()
    await backend_data_flow()
    await monitoring_flow()
    await data_pipeline_flow()
    await cloud_services_flow()

if __name__ == "__main__":
    # from asyncio import run
    # run(k8s_network_simulation())

    k8s_network_simulation.from_source(
        source="https://github.com/znicholasbrown/lineage-flows.git",
        entrypoint="network.py:k8s_network_simulation",
    ).deploy(
        name="k8s-network-simulation",
        work_pool_name="test",
        image='prefecthq/prefect:3-latest',
        job_variables={"env": {"PREFECT_EXPERIMENTS_LINEAGE_EVENTS_ENABLED": "true"}},
    )