from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 50
    max_page_size = 500
    page_size_query_param = 'page_size'