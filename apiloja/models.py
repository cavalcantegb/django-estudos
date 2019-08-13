from django.db import models

# Create your models here.
class Peca(models.Model):
    isnPeca = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return "{} - {}".format(self.isnPeca, self.descricao)
    
class Marca(models.Model):
    isnMarca = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.descricao

class Processador(models.Model):
    isnProcessador = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, null=False)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=False)
    
    def __str__(self):
        return self.descricao

class PlacaMae(models.Model):
    isnPlacaMae = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, null=False)
    marca_processador = models.ForeignKey(Marca, on_delete=models.PROTECT, null=False)
    slots_memoria = models.PositiveIntegerField(default=2, null=False)
    total_memoria = models.PositiveIntegerField(default=0 ,null=False)
    video_integrado = models.BooleanField(default=False, null=False)
    
    def __str__(self):
        return "{} - {}".format(self.descricao, self.marca_processador)
    
class TamanhoMemoria(models.Model):
    isnTamanhoMemoria = models.AutoField(primary_key=True)
    tamanho = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return "{} GB".format(self.tamanho)

class MemoriaRam(models.Model):
    isnMemoriaRam = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=False,default="")
    tamanho = models.ForeignKey(TamanhoMemoria, on_delete=models.PROTECT, null=False)
    
    def __str__(self):
        return "{} - {}".format(self.marca, self.tamanho)
    
class PlacaVideo(models.Model):
    isnPlacaVideo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}".format(self.descricao)
    
class Maquina(models.Model):
    isnMaquina = models.AutoField(primary_key=True)
    processador = models.ForeignKey(Processador, on_delete=models.PROTECT, null=False)
    placa_mae = models.ForeignKey(PlacaMae, on_delete=models.PROTECT, null=False)
    placa_video = models.ForeignKey(PlacaVideo, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return "Maquina - {}".format(self.isnMaquina)
    
    @property
    def placa_mae_descricao(self):
        return self.placa_mae.descricao
      
    @property
    def processador_descricao(self):
        return self.processador.descricao
    
    @property
    def placa_video_descricao(self):
        return self.placa_video.descricao
    
    @property
    def valida_placa_video(self):
        placa_video_valida = True
        if self.placa_mae.video_integrado == False and self.placa_video is None:
            placa_video_valida = False
        return placa_video_valida

    @property
    def valida_processador(self):
        processador_valido = False
        if self.placa_mae.marca_processador == self.processador.marca:
            processador_valido = True
        return processador_valido
    
#class PedidoCabecalho(models.Model):
#    isnPedidoCabecalho = models.AutoField(primary_key=True)
    
#class PedidoItem(models.Model):
#    isnPedidoItem =  models.AutoField(primary_key=True)
#    isnTipoItem = models.ForeignKey(Peca, on_delete=models.PROTECT, null=False)
#    isnItem = models.IntegerField(null=False)
#    isnPedidoCabecalho =  models.ForeignKey(PedidoCabecalho, on_delete=models.PROTECT, null=False)