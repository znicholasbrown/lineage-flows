from prefect import flow
from prefect._experimental.lineage import emit_external_resource_lineage

@flow(name="simple")
async def simple():
   await emit_external_resource_lineage(
        upstream_resources=[
            {
                "prefect.resource.id": "api://simple",
                "prefect.resource.role": "api",
                "prefect.resource.name": "Simple API"
            }
        ],
        downstream_resources=[
           {
                "prefect.resource.id": "app://simple",
                "prefect.resource.role": "application",
                "prefect.resource.name": "Simple App"
            }
        ]
    )

if __name__ == "__main__":  
    simple.from_source(
        source="https://github.com/znicholasbrown/lineage-flows.git",
        entrypoint="simple.py:simple",
    ).deploy(
        name="simple",
        work_pool_name="default",
        image="simple",
        push=False,
        job_variables={}
    )