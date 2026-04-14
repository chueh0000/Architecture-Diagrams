from diagrams import Diagram
from diagrams.aws.network import APIGateway
from diagrams.aws.security import Cognito
from diagrams.aws.general import InternetAlt2
from diagrams.aws.general import Toolkit
from diagrams.aws.database import Database
from diagrams.generic.blank import Blank

with Diagram("Application Architecture", filename="images/phase3/application_arch", show=False):
    api = APIGateway("API Gateway\n(Kong/AWS)\nRate limiting, auth, routing, tenant ID")
    
    auth = Cognito("Auth Service\n- Login\n- Register\n- RBAC")
    asset = InternetAlt2("Asset Service\n- CRUD\n- Search\n- Assign")
    repair = Toolkit("Repair Request Service\n- Workflow\n- History\n- Images")
    
    user_db = Database("User DB\n(shared/own)")
    asset_db = Database("Asset DB\n(R/W + Redis)")
    repair_db = Database("Repair DB\n(R/W + Redis)")

    api >> [auth, asset, repair]
    
    auth >> user_db
    asset >> asset_db
    repair >> repair_db