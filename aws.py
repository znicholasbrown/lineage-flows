import asyncio

from prefect import flow
from prefect._experimental.lineage import emit_external_resource_lineage

from resources import rds, shipyard

@flow
async def rds_to_shipyard():
    await emit_external_resource_lineage(
        upstream_resources=[rds],
        downstream_resources=[shipyard],
    )

if __name__ == "__main__":
    asyncio.run(rds_to_shipyard())