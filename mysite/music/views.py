from django.http import HttpResponse
#from djangio
from .models import Album
from sendsms.message import SmsMessage


def index(request):
   # all_album = Album.objects.all()
  #  template = loader.get_template('music/index.html')
  #  context = {
      # 'all_album':all_album
  # }
    message = SmsMessage(body='lolcats make me hungry', from_phone='+918146417711', to=['+919780088660'])
    s  = message.send()


    return HttpResponse("jfsdngkdfkgb;dgth");