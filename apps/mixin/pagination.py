from rest_framework.pagination import PageNumberPagination


class HumanPag(PageNumberPagination):
    # Сколько объектов показывать на одной странице
    page_size = 3

    # Можно менять размер страницы через ?page_size=...
    page_query_param = 'page_size'

    # Но не больше 20 объектов за запрос
    max_page_size = 20
