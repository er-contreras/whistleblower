from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .services import generate_incident_report

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def report_incident(request):
    victim_name = request.data.get('victim_name')
    classification = request.data.get('classification')

    if not victim_name or not classification:
        return Response(
            {"error": "Missing parameters"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        report_data = generate_incident_report(victim_name, classification)
        return Response(report_data, status=status.HTTP_200_OK)

    except Exception as e:
        error_msg = str(e)

        if "429" in error_msg:
            return Response({
                "error": "AI limit reached",
                "message": "Please wait a few seconds before try again"
            }, status=status.HTTP_429_TOO_MANY_REQUESTS)

        return Response(
            {"error": "Internal error when try to process the whistleblower", "details": error_msg},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
