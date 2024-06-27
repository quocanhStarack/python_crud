from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import status, generics

from candidate.serializers import CandidateSerializer
from candidate.models import Candidate
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from config.firebase_config import FirebaseConfig
from uploader.firebase_uploader import FirebaseUploader

# Create your views here.

class CandidateDetailView(generics.RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer = CandidateSerializer
    
class CandidateListView(ListCreateAPIView):
    model = Candidate
    serializer_class = CandidateSerializer

    def get_queryset(self):
        queryset = Candidate.objects.all()
        # queryset =queryset.prefetch_related('cv')
        return queryset

    def create(self, request, *args, **kwargs):
        my_data = request.data
        file = my_data["file"]
        serializer = CandidateSerializer(
            data=my_data,
        )

        firebase_uploader = FirebaseUploader(config=FirebaseConfig.firebaseConfig)
        uploader = firebase_uploader.uploadFile(my_data["file"])

        if serializer.is_valid():
            serializer.save(uploader)

            return JsonResponse(
                {"message": "Create a new Candidate successful!"},
                status=status.HTTP_201_CREATED,
            )
        print(serializer.data)
        print(serializer.errors)
        return JsonResponse(
            {"message": "Create a new Candidate unsuccessful!"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CandidateUpdateAndDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    model = Candidate
    serializer_class = CandidateSerializer

    def put(self, request, *args, **kwargs):
        candidate = get_object_or_404(Candidate, id=kwargs.get("pk"))
        serializer = CandidateSerializer(candidate, data=request.data)
        data = request.data
        file = data["file"]
        serializer = CandidateSerializer(
            data=data,
        )

        firebase_uploader = FirebaseUploader(config=FirebaseConfig.firebaseConfig)
        uploader = firebase_uploader.uploadFile(data["file"])

        if serializer.is_valid():
            serializer.save(uploader)

            return JsonResponse(
                {"message": "Update Candidate successful!"}, status=status.HTTP_200_OK
            )

        return JsonResponse(
            {"message": "Update Candidate unsuccessful!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def delete(self, request, *args, **kwargs):
        candidate = get_object_or_404(Candidate, id=kwargs.get('pk'))
        candidate.delete()

        return JsonResponse({
            'message': 'Delete Candidate successful!'
        }, status=status.HTTP_200_OK)
