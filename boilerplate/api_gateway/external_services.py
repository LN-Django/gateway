class ExternalService:
    def __init__(self, base_url: str, endpoint: str) -> None:
        self.endpoint = base_url + '/api/' + endpoint
        self.swagger = base_url + "/swagger.json"


services = {
    'list_products': ExternalService("", ""),
    'product_info': ExternalService("", ""),
    'calculator': ExternalService(base_url="https://cryptic-wildwood-57466.herokuapp.com", endpoint="calculator")
}
