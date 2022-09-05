from django.urls import path

from education.views import DegreeListCreateView, DegreeRetrieveUpdateDestroyView, OrgListCreateView, OrgRetrieveUpdateDestroyView, EducationListCreateView, EducationRetrieveUpdateDestroyView

urlpatterns = [
    path("degree/", DegreeListCreateView.as_view(), name="degree_list"),
    path("degree/<int:pk>/", DegreeRetrieveUpdateDestroyView.as_view(), name="degree_detail"),
    path("org/", OrgListCreateView.as_view(), name="degree_list"),
    path("org/<int:pk>/", OrgRetrieveUpdateDestroyView.as_view(), name="degree_detail"),
    path("", EducationListCreateView.as_view(), name="education_list"),
    path("<int:pk>/", EducationRetrieveUpdateDestroyView.as_view(), name="education_detail"),
]