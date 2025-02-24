from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Parámetro para enviar el número de elementos por página
    max_page_size = 100  # Límite máximo de elementos por página

    def get_page_size(self, request):
        if self.page_size_query_param:
            try:
                # Intenta obtener el valor de `page_size` desde los parámetros de la solicitud
                page_size = int(request.query_params[self.page_size_query_param])
                if page_size > 0:
                    return min(page_size, self.max_page_size)  # Asegúrate de no exceder el límite máximo
            except (KeyError, ValueError):
                pass
        # Si no se proporciona `page_size`, usa el valor por defecto
        return self.page_size