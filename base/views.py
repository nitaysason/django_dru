from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Drugs
from rest_framework import serializers

class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = '__all__'



@api_view(['GET','POST','DELETE','PUT','PATCH'])
def drugs_view(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_drugs=Drugs.objects.get(id=id)
                return Response (DrugsSerializer(temp_drugs,many=False).data)
            except Drugs.DoesNotExist:
                return Response ("not found")
        all_Drugss=DrugsSerializer(Drugs.objects.all(),many=True).data
        return Response (  all_Drugss)
    if req.method =='POST':
        drugs_serializer = DrugsSerializer(data=req.data)
        if drugs_serializer.is_valid():
            drugs_serializer.save()
            return Response ("post...")
        else:
            return Response (DrugsSerializer.errors)
    if req.method =='DELETE':
        try:
             temp_drugs=Drugs.objects.get(id=id)
        except Drugs.DoesNotExist:
            return Response ("not found")    
       
        temp_drugs.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
             temp_drugs=Drugs.objects.get(id=id)
        except Drugs.DoesNotExist:
            return Response ("not found")
       
        ser = DrugsSerializer(data=req.data)
        old_drugs = Drugs.objects.get(id=id)
        res = ser.update(old_drugs, req.data)
        return Response('upd')   

