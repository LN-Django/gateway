class ExternalService:
    def __init__(self, endpoint: str, swagger: str) -> None:
        self.endpoint = endpoint
        self.swagger = swagger


services = {
    'list_products': ExternalService("", ""),
    'product_info': ExternalService("", ""),
    'calculator': ExternalService("", "")
}
