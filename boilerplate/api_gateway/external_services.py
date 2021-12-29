import requests as api_request


class ExternalService:
    def __init__(self, base_url: str, endpoint: str) -> None:
        self.service_path = "/" + endpoint
        self.endpoint = base_url + '/api/' + endpoint
        self.swagger = base_url + "/swagger.json"


services = {
    'list_products': ExternalService(base_url="https://enigmatic-dusk-38395.herokuapp.com", endpoint="products"),
    'product_info': ExternalService(base_url="https://enigmatic-dusk-38395.herokuapp.com", endpoint="product/{product_id}/info"),
    'calculator': ExternalService(base_url="https://cryptic-wildwood-57466.herokuapp.com", endpoint="calculator")
}


def get_external_service_by_path(service_path: str):
    for service in services.values():
        if service_path == service.service_path:
            return service

    # Default case
    return services['calculator']


def get_swagger_paths(service: ExternalService):
    response = api_request.get(service.swagger)
    swagger_schema = response.json()
    swagger_path = swagger_schema["paths"][service.service_path]

    if service.service_path == services["list_products"].service_path:
        del swagger_path['post']

    return swagger_path
