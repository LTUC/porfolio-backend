from rest_framework import serializers
from django.contrib.auth import get_user_model
from account.serializers import UserSerializer

from education.models import Degree, Education, Organization
class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    degree = DegreeSerializer(read_only = True)
    organization = OrgSerializer(read_only = True)

    user_id = serializers.PrimaryKeyRelatedField(queryset = get_user_model().objects.all(), source = "user", write_only=True)
    degree_id = serializers.PrimaryKeyRelatedField(queryset = Degree.objects.all(), source = "degree", write_only=True)
    organization_id = serializers.PrimaryKeyRelatedField(queryset = Organization.objects.all(), source = "organization", write_only=True)
    class Meta:
        model = Education
        fields = "__all__"