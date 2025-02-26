from main import aurora_to_snowflake

if __name__ == "__main__":
    aurora_to_snowflake.serve(
        name="aurora-to-snowflake-production",
        tags=["lineage"],
    )