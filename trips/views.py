from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TripSerializer

class TripView(APIView):
    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            trip = serializer.save()
            return Response({
                "message": "Trip created",
                "route": [
                    request.data['current_location'],
                    request.data['pickup_location'],
                    request.data['dropoff_location']
                ],
                "rests": [
                    {"name": "Rest Stop A", "lat": -1.5, "lng": 37.0},
                    {"name": "Fuel Stop B", "lat": -2.0, "lng": 36.8}
                ],
                "logs": [8, 4, 6]
            })
        return Response(serializer.errors, status=400)