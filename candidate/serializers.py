from typing import override
from candidate.models import Candidate
from rest_framework import serializers

class CandidateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(read_only=True,)
    class Meta:
        model = Candidate
        fields = (
        "status",
        "name",
        "phone",
        "email",
        "dob",
        "major",
        "work_experience",
        'file',
        'cv'
    )
        validators = []
    
    @override
    def save(self,path:str, **kwargs):
        self.validated_data['cv'] = path
        return super().save(**kwargs)


