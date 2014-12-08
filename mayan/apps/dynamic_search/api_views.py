from __future__ import absolute_import

from rest_framework import generics
from rest_framework.exceptions import ParseError

from rest_api.filters import MayanObjectPermissionsFilter

from .classes import SearchModel
from .models import RecentSearch
from .serializers import RecentSearchSerializer, SearchSerializer


class APIRecentSearchListView(generics.ListAPIView):
    """
    Returns a list of all the recent searches.
    """

    serializer_class = RecentSearchSerializer
    queryset = RecentSearch.objects.all()

    # TODO: Add filter_backend so that users can only see their own entries


class APIRecentSearchView(generics.RetrieveDestroyAPIView):
    """
    Returns the selected recent search details.
    """

    serializer_class = RecentSearchSerializer
    queryset = RecentSearch.objects.all()

    # TODO: Add filter_backend so that users can only see their own entries


class APISearchView(generics.ListAPIView):
    """
    Perform a search operaton
    q -- Term that will be used for the search.
    """

    filter_backends = (MayanObjectPermissionsFilter,)

    # Placeholder serializer to avoid errors with Django REST swagger
    serializer_class = SearchSerializer

    def get_queryset(self):
        document_search = SearchModel.get('documents.Document')
        self.serializer_class = document_search.serializer
        self.mayan_object_permissions = {'GET': [document_search.permission]}

        try:
            if 'q' in self.request.GET:
                # Simple query
                query_string = self.request.GET.get('q', u'').strip()
                queryset, ids, timedelta = document_search.simple_search(query_string)
            else:
                # Advanced search
                queryset, ids, timedelta = document_search.advanced_search(self.request.GET)
        except Exception as exception:
            raise ParseError(unicode(exception))

        RecentSearch.objects.add_query_for_user(self.request.user, self.request.GET, len(ids))

        return queryset