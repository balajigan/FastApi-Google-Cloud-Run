
from pydantic import BaseModel
from typing import Optional
from typing import Union

class CloudRun(BaseModel):
    resource_type: str
    project_id: str
    service_name: str
    location: str
    image: str
    generate_revision_name: Optional[bool] = True
    container_command: Optional[list[str]] = None
    service_labels: Optional[dict[str, str]] = None
    service_annotations: Optional[dict[str, str]] = None
    template_annotations: Optional[dict[str, str]] = None

    template_labels: Optional[dict[str, str]] = None
    argument: Optional[list[str]] = None
    max_scale_instances: Optional[int] = 2
    min_scale_instances: Optional[int] = 0
    env_vars: Optional[list[dict[str,str]]] = [{"environment":"Dev", "ci-number":"12345"}]

    limits: Optional[dict[str, str]] = None
    requests: Optional[dict[str, str]] = None
    ports: Optional[list[dict[str,Union[str,int]]]]
