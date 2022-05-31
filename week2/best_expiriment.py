import mlflow
from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient
EXPERIMENT_NAME = "random-forest-best-models"
mlflow.set_tracking_uri("http://127.0.0.1:5000")
client=MlflowClient()
experiment = client.get_experiment_by_name(EXPERIMENT_NAME)
best_run = client.search_runs(experiment_ids='2', 
filter_string="metrics.rmse < 7", 
run_view_type=ViewType.ACTIVE_ONLY, 
max_results=5, 
order_by=["metrics.rmse ASC"])
#mlflow.register_model(model_uri=f"runs:/fae98c63de534f10995217dd3272221b/model",name="nyc-taxi-rand-forest")
print(best_run)