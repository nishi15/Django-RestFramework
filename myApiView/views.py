from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.generics import get_object_or_404

from myApiView import serializer,models

# Create your views here.


class CustomerView(APIView):
    """An APIView demo app to handle all the Customerss"""

    def get(self,request,pk=None):
        if pk:
            customer = get_object_or_404(models.CustomerModel.objects.all(), pk=pk)
            serialized_data = serializer.CustomerSerializer(customer)
            return Response({"Customer": serialized_data.data})

        query = models.CustomerModel.objects.all()
        # return Response({"Customers":serialized_obj})
        return Response({"Customers":list(models.CustomerModel.objects.all().values("id", "email","pk","date_joined","customer_address","full_name"))})

    def post(self,request):
        serial = serializer.CustomerSerializer(data=request.data)

        if serial.is_valid(raise_exception=True):
            customer_saved = serial.save()
            customer_name = customer_saved.full_name
        return Response({"success":f"Customer {customer_name} is saved with us"})

    def delete(self,request,pk):
        customer = get_object_or_404(models.CustomerModel.objects.all(), pk=pk)
        customer.delete()
        return Response({"message": "Customer `{}` has been deleted.".format(customer.full_name)}, status=204)


    def put(self,request,pk):
            saved_customer = get_object_or_404(models.CustomerModel.objects.all(), pk=pk)
            data = request.data
            serialized_data = serializer.CustomerSerializer(instance=saved_customer, data=data, partial=True)
            if serialized_data.is_valid(raise_exception=True):
                customer = serialized_data.save()
            return Response({"success": "Customer '{}' updated successfully".format(customer)})



