from diagrams import Diagram, Cluster, Edge, Node
from diagrams.onprem.client import User
from diagrams.aws.network import Route53
from diagrams.aws.network import ElbApplicationLoadBalancer
from diagrams.aws.compute import EC2Instance
from diagrams.aws.database import RDS
from diagrams.aws.storage import SimpleStorageServiceS3

graph_attr = {
    "concentrate": "true",
    "splines": "spline",
}

with Diagram("System Architecture", filename="images/phase2/system_arch", show=False, graph_attr=graph_attr):
    
    users = User("Users\n(Browser)")

    dns = Route53("Route 53 \n(DNS)")

    alb = ElbApplicationLoadBalancer("Application Load Balancer \n(health checks, SSL termination)")

    with Cluster("Stateless AP nodes \n(Docker containers)", graph_attr={"margin": "30.0"}):
        app_nodes = [
            EC2Instance("EC2-1 \n(App)"),
            EC2Instance("EC2-2 \n(App)")]
        
    blank = Node("", shape="plaintext", height="0.0", width="0.0")

    rds = RDS("RDS MySQL Multi-AZ \n(primary + standby)")
    
    s3 = SimpleStorageServiceS3("S3 (images)")

    users >> Edge(label="HTTPS") >> dns >> Edge(headport="w", minlen="2") >> alb
    
    # Fan-out: ALB connects to both EC2 instances simultaneously
    alb >> Edge(headport="w", minlen="2") >> app_nodes

    # Fan-out/Fan-in: Both EC2 instances connect to both the DB and S3
    app_nodes - Edge(headport="w", minlen="1") - blank
    blank >> Edge(headport="w", minlen="2") >> [rds, s3]