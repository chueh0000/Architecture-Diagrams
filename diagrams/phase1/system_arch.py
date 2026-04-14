from diagrams import Diagram, Cluster, Edge
# from diagrams.aws.compute import EC2
from diagrams.aws.database import RDSMysqlInstance
from diagrams.onprem.network import Nginx
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.generic.storage import Storage

with Diagram("System Architecture", filename="images/phase1/system_arch", show=False):
    
    users = User("Users\n(Browser)")

    with Cluster("Single EC2 Instance", graph_attr={"margin": "50.0"}):
        proxy = Nginx("Nginx\n(reverse proxy + static files)")
        
        app = Server("App\n(API server)")

        db = RDSMysqlInstance("MySQL\n(single DB)")
        
        uploads = Storage("/uploads\n(local filesystem for images)")

    users >> Edge(label="HTTPS") >> proxy >> app >> db
    app >> uploads