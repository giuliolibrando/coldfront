from django.urls import path

import core.djangoapps.publication.views as publication_views

urlpatterns = [
    path('publication-search/<int:project_pk>/', publication_views.PublicationSearchView.as_view(), name='publication-search'),
    path('publication-search-result/<int:project_pk>/', publication_views.PublicationSearchResultView.as_view(), name='publication-search-result'),
    path('add-publication/<int:project_pk>/', publication_views.PublicationAddView.as_view(), name='add-publication'),
    path('project/<int:project_pk>/delete-publications/', publication_views.PublicationDeletePublicationsView.as_view(), name='publication-delete-publications'),

]
