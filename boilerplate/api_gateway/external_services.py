

class ExternalService:
    def __init__(self, base_url: str, endpoint: str) -> None:
        self.endpoint = base_url + '/api/' + endpoint
        self.swagger = base_url + "/swagger.json"


services = {
    'list_products': ExternalService(base_url="https://enigmatic-dusk-38395.herokuapp.com", endpoint="products"),
    'product_info': ExternalService(base_url="https://enigmatic-dusk-38395.herokuapp.com", endpoint="product/<product_id>/info"),
    'calculator': ExternalService(base_url="https://cryptic-wildwood-57466.herokuapp.com", endpoint="calculator")
}
