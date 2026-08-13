from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .model import respon
from .models import NLPIndonesiaResponse, NLPIndonesiaResponseModel, TextMessage

DEFAULT_REPLY = 'Maaf, saya belum memahami pesan Anda. Coba tanyakan hal lain?'


def index(request):
    return render(request, 'index.html')


@require_POST
def submit(request):
    user_message = request.POST.get('user_message', '').strip()
    if not user_message:
        return JsonResponse({'error': 'Pesan tidak boleh kosong'}, status=400)

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key
    TextMessage.objects.create(message=user_message)
    bot_message = executebotscript(user_message, session_key)

    if bot_message:
        NLPIndonesiaResponse.objects.create(
            answer=bot_message[0],
            response_model=NLPIndonesiaResponseModel.objects.create(
                tag=bot_message[1],
                context_set=bot_message[2],
            ),
        )
        reply = bot_message[0]
        tag = bot_message[1]
    else:
        reply = DEFAULT_REPLY
        tag = 'unknown'

    return JsonResponse({
        'user_message': user_message,
        'bot_message': reply,
        'tag': tag,
    })


def executebotscript(message, userid='kunci115'):
    return respon.response(message, userid=userid)
