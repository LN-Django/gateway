from .external_services import get_external_service_by_path, get_swagger_paths
from drf_yasg.generators import OpenAPISchemaGenerator
from typing import OrderedDict


class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_paths_object(self, paths):
        return_obj = super().get_paths_object(paths)
        return_dict = {}
        for path, index in return_obj.items():
            swagger_response = get_swagger_paths(
                get_external_service_by_path(path))

            return_dict[path] = swagger_response

        return OrderedDict(return_dict)
