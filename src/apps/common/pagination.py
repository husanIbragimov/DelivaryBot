from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    """
    Obyektlarni ``GET`` qilishda sahifalarga bo'lish uchun asosiy pagionation class
    """
    page_size_query_param = 'size'
    page_size = 5

    def get_paginated_response(self, data):
        if self.get_page_size(self.request) == 0:
            return Response({
                'results': data
            })
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'page_size': self.get_page_size(self.request),
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'page_items': len(self.page),
            'total': self.page.paginator.count,
            'results': data
        })
