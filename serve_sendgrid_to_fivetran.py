from main import sendgrid_to_fivetran
    
if __name__ == "__main__":
    sendgrid_to_fivetran.serve(
        name="sendgrid-to-fivetran-production",
        tags=["lineage", "deploy-fivetran"],
    )