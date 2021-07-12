from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models.LaunchpadModels import Launchpads
from api.serializer.LaunchpadSerializer import LaunchpadSerializer


@api_view(['GET'])
def getAllLaunchpad(request):
    pool = Launchpads.objects.filter(status='LIVE').order_by('-pk')
    serializer = LaunchpadSerializer(pool, many=True)
    return Response(serializer.data)
