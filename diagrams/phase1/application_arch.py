from diagrams import Diagram
from diagrams.generic.blank import Blank

with Diagram("Application Architecture", filename="images/phase1/application_arch", show=False):
    
    stack_structure = (
        "Frontend (SPA) \\nReact / Vue / Next.js"
        "|"
        "{ Backend (Monolith) | { Auth Module | Asset Module | Repair Module | Image Upload | Search Module } }"
        "|"
        "ORM / Data Access Layer"
        "|"
        "MySQL (Single DB)"
    )
    
    Blank(stack_structure, 
          shape="Mrecord",
          fontsize="16", 
          fontname="Courier",
          fixedsize="false",
          margin="0.2")