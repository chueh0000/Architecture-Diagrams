from diagrams import Diagram, Cluster, Edge, Node
from diagrams.aws.general import Users
from diagrams.aws.network import Route53
from diagrams.aws.network import CloudFront
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.network import ElbApplicationLoadBalancer
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import ElasticKubernetesService
from diagrams.aws.database import RDSInstance
from diagrams.aws.database import ElasticacheForRedis
from diagrams.aws.analytics import ElasticsearchService

graph_attr = {
    "concentrate": "true",
    "splines": "spline",
}

with Diagram("System Architecture", filename="images/phase3/system_arch", show=False, graph_attr=graph_attr):
    users = Users("Users\n(Browser/Mobile)")
    route53 = Route53("Route 53")
    
    cloudfront = CloudFront("CloudFront\n(CDN)\nstatic + images")
    s3 = SimpleStorageServiceS3("S3 (images)")
    
    alb = ElbApplicationLoadBalancer("ALB")
    apigw = APIGateway("API GW / Kong")

    with Cluster("EKS Cluster"):
        auth = ElasticKubernetesService("Auth x2")
        asset = ElasticKubernetesService("Asset x3")
        repair = ElasticKubernetesService("Repair x3")
        eks_services = [auth, asset, repair]

    blank = Node("", shape="plaintext", height="0.0", width="0.0")

    rds_primary = RDSInstance("RDS Primary \n(write)")
    rds_replica = RDSInstance("RDS Read Replica")
    redis = ElasticacheForRedis("Redis ElastiCache \n(cache)")
    es = ElasticsearchService("Elasticsearch \n(search)")
    dbs = [rds_primary, rds_replica, redis, es]

    users >> route53
    route53 >> cloudfront >> s3
    route53 >> alb
    
    alb >> apigw
    alb >> eks_services
    apigw >> eks_services
    
    eks_services - Edge(headport="w", minlen="1") - blank
    blank >> Edge(headport="w", minlen="2") >> dbs