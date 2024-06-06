from rest_framework.generics import *

class GenericViewAPIViewSet(ListAPIView, RetrieveAPIView):
    pass


class GenericWriteAPIViewSet(CreateAPIView, UpdateAPIView):
    pass


class GenericReadWriteViewSet(CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView):
    pass
