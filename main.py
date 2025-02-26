from prefect import flow, task, tags
from resources import (
    mobile_application,
    heroku,
    aurora,
    sidekiq,
    fivetran,
    snowflake_ingest,
    snowflake_analytics,
    dbt,
    sendgrid,
)
from prefect._experimental.lineage import emit_external_resource_lineage
from asyncio import run

@flow(log_prints=True)
async def mobile_to_aurora_flow():
    await emit_external_resource_lineage(
        upstream_resources=[mobile_application],
        downstream_resources=[heroku],
    )
    
    await emit_external_resource_lineage(
        upstream_resources=[heroku],
        downstream_resources=[aurora],
    )

@flow(log_prints=True)
async def aurora_sidekiq_sync_flow():
    await emit_external_resource_lineage(
        upstream_resources=[aurora],
        downstream_resources=[sidekiq],
    )
    
    await emit_external_resource_lineage(
        upstream_resources=[sidekiq],
        downstream_resources=[aurora],
    )

@flow(log_prints=True)
async def aurora_to_snowflake():
    await emit_external_resource_lineage(
        upstream_resources=[aurora],
        downstream_resources=[fivetran],
    )
    
    await emit_external_resource_lineage(
        upstream_resources=[fivetran],
        downstream_resources=[snowflake_ingest],
    )

@flow(log_prints=True)
async def sendgrid_to_fivetran():
    await emit_external_resource_lineage(
        upstream_resources=[sendgrid],
        downstream_resources=[fivetran],
    )

@flow(log_prints=True)
async def snowflake_transform():
    with tags('january-2025'):
        print('Emitting lineage from snowflake_ingest to dbt')
        await emit_external_resource_lineage(
            # event_name="snowflake-transform",
            upstream_resources=[snowflake_ingest],
            downstream_resources=[dbt],
        )
        print('Emission complete')
        
        print('Emitting lineage from dbt to snowflake_analytics')
        await emit_external_resource_lineage(
            # event_name="snowflake-insert",
            upstream_resources=[dbt],
            downstream_resources=[snowflake_analytics],
        )
        print('Emission complete')



if __name__ == "__main__":
    # run(mobile_to_aurora_flow())
    # run(aurora_sidekiq_sync_flow())
    # run(aurora_to_snowflake())
    # run(sendgrid_to_fivetran())
    run(snowflake_transform())