from django.http import HttpResponse
from joycasino.lib.core import core

def index(request):
    username = request.GET.get('user', 'Name')
    try:
        money = int(request.GET.get('money', 0))
        bet = int(request.GET.get('bet', 0))
    except:
        raise Exception("money&bet must have numeric value")
    message = core.addBet(username, money, bet)
    return HttpResponse(message)