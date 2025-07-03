from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer,TransactionSerializer
from rest_framework import authentication,permissions
from expense.models import Transaction

# Create your views here.

class SignUpView(APIView):
    def post(self,request,*args,**kwargs):

        serializer_instance=UserSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
class TransactionListCreateView(APIView):

    serializer_class=TransactionSerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        qs=Transaction.objects.filter(owner=request.user)

        serializer_instance=TransactionSerializer(qs,many=True)

        return Response(data=serializer_instance.data)





    

