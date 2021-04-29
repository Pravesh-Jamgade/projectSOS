from help_api.models import *

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

import json

INVALID_POST_DATA = "Data insufficient to post"
VALID_POST_DATA = "Successfully posted"
# AddressModel
#1 get address of entity
#2 get contact of entity
#3 post address + contact

class AddressView(APIView):
    def get(self, request):
        data = {}
        return Response({'data':data, 'status':True})

#2 get entity names
#3 get entity choice

class EntityView():
    pass

# ToolsModel
#1 post tool_name, tool_from, tool_qty, tool _state
#2 get tool_from
#3 get tool_qty
#4 update/put tool_state

class ToolView():
    pass

# SOSModel
#1 post sos
#2 get sos_from
#3 put/update sos_state

class SOSView():
    pass

# Register
class RegisterEntityView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterEntitySerializer(data=data)
        if(not serializer.is_valid()):
            return Response({
                'status': False, 'message':INVALID_POST_DATA},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        entity = serializer.save()

        return Response({
            'status':True, 'message':VALID_POST_DATA}, 
            status=status.HTTP_200_OK
        )
    
    def get(self, request):
        data = []
        return Response({'status': True}, status=status.HTTP_200_OK)


# SortData 
#1 by SOS timestamp
#2 by SOS location and current location
#3 by tag requirement
class SortDataView():
    pass