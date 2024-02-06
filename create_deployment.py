# Make your code schedulable

from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/edwardosindo/prefect-tutorial.git",
        entrypoint="prefect_tutorial.py:repo_info",

    ).deploy(
        name="my-first-deployment",
        work_pool_name="edward-managed-pool",
        cron="0 1 * * * ",
    )

