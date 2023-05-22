from kubernetes import client, config

# load kubernetes configuration
config.load_kube_config()

# Create a kubernetes API client
api_client = client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="cloud-monitoring"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "cloud-monitoring"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "cloud-monitoring"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="cloud_monitoring",
                        image="227512099407.dkr.ecr.ap-south-1.amazonaws.com/cloud_monitoring:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# create the deployment
app_instance = client.AppsV1Api(api_client)
app_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="cloud-monitoring"),
    spec=client.V1ServiceSpec(
        selector={"app": "cloud-monitoring"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)