from rest_framework import serializers
from .models import Candidatedirectory

class CandidatedirectorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Candidatedirectory
		fields ='__all__'

<<<<<<< HEAD
	def validate(self, data):
		email = data.get('email')
		contact_no_primary = data.get('contact_no_primary')

		# Check if an object with the same email or phone_number already exists in the database
		if self.instance:  # Check if an instance exists (i.e., we are updating)
			if email == self.instance.email:
				# Email remains unchanged, no need to check uniqueness
				pass
			elif Candidatedirectory.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
				raise serializers.ValidationError('This email is already in use.')

			if contact_no_primary == self.instance.contact_no_primary:
				# Phone number remains unchanged, no need to check uniqueness
				pass
			elif Candidatedirectory.objects.filter(contact_no_primary=contact_no_primary).exclude(pk=self.instance.pk).exists():
				raise serializers.ValidationError('This phone number is already in use.')
		else:
			if Candidatedirectory.objects.filter(email=email).exists():
				raise serializers.ValidationError('This email is already in use.')

			if Candidatedirectory.objects.filter(contact_no_primary=contact_no_primary).exists():
				raise serializers.ValidationError('This phone number is already in use.')

		return data
=======
	
>>>>>>> 45a149e707e986525b9f18fa71346e7dee879837
