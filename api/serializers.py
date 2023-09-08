from rest_framework import serializers
from .models import Candidatedirectory

class CandidatedirectorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Candidatedirectory
		fields ='__all__'

	