import boto3
from src.slack import send_adjust_size

clusterName = os.environ["clusterName"]
serviceName = os.environ["slackToken"]
client = boto3.client("ecs")


def scale_out(event, context):
    desiredCount = 8
    response = client.update_service(
        cluster=clusterName,
        service=serviceName,
        desiredCount=desiredCount,
    )
    if response:
        send_adjust_size(serviceName, desiredCount, "scaleOut")


def scale_in(event, context):
    desiredCount = 4
    response = client.update_service(
        cluster=clusterName,
        service=serviceName,
        desiredCount=desiredCount,
    )

    if response:
        send_adjust_size(serviceName, desiredCount, "scaleIn")
