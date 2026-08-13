from django.db import models


class NLPIndonesiaResponseModel(models.Model):
    tag = models.CharField(max_length=100)
    context_set = models.CharField(max_length=100)


class TextMessage(models.Model):
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.message[0:5]


class NLPIndonesiaResponse(models.Model):
    answer = models.CharField(max_length=250)
    response_model = models.ForeignKey(NLPIndonesiaResponseModel, on_delete = models.CASCADE)
