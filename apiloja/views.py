from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import MaquinaSerializer

# Create your views here.
# blogs = Blog.objects.filter(author=author).values_list('id', flat=True)
class APILojaView(APIView):

    def get(self, request):
        maquinas = Maquina.objects.all()
        serializer = MaquinaSerializer(maquinas, many=True)
        return Response({"maquinas":serializer.data},status=status.HTTP_200_OK)
    
    def post(self, request):
        maquina_data = request.data.get('maquina')
        serializer = MaquinaSerializer(data=maquina_data)
        fail_message = ""
        if serializer.is_valid(raise_exception=True):
            isnProcessador = serializer.data['processador']
            isnPlacaMae = serializer.data['placa_mae']
            isnPlacaVideo = serializer.data['placa_video']
            
            processador = Processador.objects.get(pk=isnProcessador)
            placa_mae = PlacaMae.objects.get(pk=isnPlacaMae)
            placa_video = None
            if isnPlacaVideo is not None:
                placa_video = PlacaVideo.objects.get(pk=isnPlacaVideo)

            maquina = Maquina(processador=processador, placa_mae=placa_mae, placa_video=placa_video)        

            if maquina.valida_placa_video and maquina.valida_processador:
                maquina.save()
                return Response({"success": "{} created successfully".format(maquina)})
            else:
                if maquina.valida_processador == False:
                    fail_message = "Placa Mae {} não suporta processador {}. ".format(placa_mae.descricao, processador.marca)
                if maquina.valida_placa_video == False:
                    fail_message += "Não foi selecionado nenhuma placa de vídeo para o computador."
        else:
            fail_message = "Dados não são validos."           
        
        return Response({"fail": fail_message})
