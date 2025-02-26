from prefect import flow, get_run_logger

@flow(name="simple")
async def simple():
    logger = get_run_logger()
    logger.info("This is a simple test of managed execution.")

if __name__ == "__main__":  
    simple.from_source(
        source="https://github.com/znicholasbrown/lineage-flows.git",
        entrypoint="simple.py:simple",
    ).deploy(
        name="simple",
        work_pool_name="default",
        job_variables={},
        image='prefecthq/prefect:3-latest'
    )