from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from education.models import Degree, Organization, Education
from education.serializers import DegreeSerializer, OrgSerializer, EducationSerializer
from utils.permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly
# Create your views here.
class DegreeListCreateView(ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    

class DegreeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

class OrgListCreateView(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer

class OrgRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

class EducationListCreateView(ListCreateAPIView):
    
    serializer_class = EducationSerializer

    def get_queryset(self):
        queryset = Education.objects.all()
        user_id = self.request.query_params.get('user')
        if user_id is not None:
            queryset = Education.objects.filter(user__id = user_id)
        return queryset

class EducationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsOwnerOrReadOnly,)