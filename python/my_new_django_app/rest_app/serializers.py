from rest_framework import serializers
from rest_app.models import FancyCat

class FancyCatSerializer(serializers.ModelSerializer):

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError('Age cannot be less than 0')
        return value

    class Meta:
        model = FancyCat
        fields = ('id', 'date_added', 'name', 'age', 'is_active', 'description')