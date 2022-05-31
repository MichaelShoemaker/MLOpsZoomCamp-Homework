from mlflow.tracking import MlflowClient


MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"

from mlflow.entities import ViewType
client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

client.list_experiments()

runs = client.search_runs(
    experiment_ids='2',
    filter_string="metrics.rmse < 7",
    run_view_type=ViewType.ACTIVE_ONLY,
    max_results=5,
    order_by=["metrics.rmse ASC"]
)

for run in runs:
    print(run)