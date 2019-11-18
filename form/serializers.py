from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
  class Meta:
    model = Form
    fields = ('id', 'firstName', 'lastName', 'telephone', 'Collage', 'Electronic_design', 'DreamArt','Print_no_edit', 'size_of_picture', 'completed')
