from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import Django, React
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis

# The filename parameter defines where the image is saved. 
# We direct it straight to the images/ folder.
with Diagram("System Architecture", filename="images/system_architecture", show=False):
    
    client = User("Web Client")

    with Cluster("Frontend"):
        ui = React("React Interface")

    with Cluster("Backend Services"):
        proxy = Nginx("Reverse Proxy")
        api = Django("Django REST API")
        
        with Cluster("Data Layer"):
            db = PostgreSQL("PostgreSQL")
            cache = Redis("Redis Cache")

    # Define the communication flow
    client >> ui >> proxy >> api
    
    # The API reads/writes to both the DB and the Cache
    api >> db
    api >> cache
