from django.contrib import admin
from .models import TextMessage
from .models import NLPIndonesiaResponse
from .models import NLPIndonesiaResponseModel

admin.site.register(TextMessage)
admin.site.register(NLPIndonesiaResponse)
admin.site.register(NLPIndonesiaResponseModel)