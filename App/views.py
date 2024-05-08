from django.shortcuts import render,HttpResponse
from .models import ContactPage
from .serializer import mySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io
# Create your views here.

class ContactAPI(APIView):
    serializer=mySerializer
    def post(self, request):
        print("request data is :", request.data)
        serializer_obj=mySerializer(data=request.data)
    # if request.method=="GET":
    #     form=ContactPage.objects.all()
    #     serializer=mySerializer(form, many=True)
    #     json_data=JSONRenderer().render(serializer.data)
    #     return HttpResponse(json_data, content_type='application/json')

        # if request.method == 'POST':
        #     json_data = request.body
        #     stream = io.BytesIO(json_data)
        #     pythondata = JSONParser().parse(stream)
        #     serializer = mySerializer(data= pythondata)
        if serializer_obj.is_valid():
              ContactPage.objects.create(
                            name=serializer_obj.data.get("name"),
                            email=serializer_obj.data.get("email"),
                            phone=serializer_obj.data.get("phone"),
                            company=serializer_obj.data.get("company"),
                            company_website=serializer_obj.data.get("company_website"),
                            services=serializer_obj.data.get("services"),
                            describe=serializer_obj.data.get("describe"),
                            term=serializer_obj.data.get("term") )
              msg = {'message': 'Data created'}
              return Response(msg)
        #     json_data= JSONRenderer().render(msg)
        #     return HttpResponse(json_data, content_type='application/json')
        # error_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(error_data, content_type='application/json')
    # if request.method == 'PUT':
    #     json_data=request.body
    #     stream= io.BytesIO(json_data)
    #     python_data=JSONParser().parse(stream)
    #     id=python_data.get('id')
    #     cnt=ContactPage.objects.get(id=id)
    #     serializer=mySerializer(cnt, data=python_data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         msg={'message':'data updated'}
    #         json_data=JSONRenderer().render(msg)
    #         return HttpResponse(json_data, content_type='application/json')
    #     error_data=JSONRenderer().render(serializer.errors)
    #     return HttpResponse(error_data, content_type='application/json')
    # if request.method=="DELETE":


