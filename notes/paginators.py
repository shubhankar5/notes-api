from rest_framework.pagination import PageNumberPagination


class UserResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
    max_page_size = 100


class NoteResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 100