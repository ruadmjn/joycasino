import types
from joycasino.models import *
from django.db import Error, transaction

class core:

    @classmethod
    def addBet(cls, userName, allMoney, jackPart=0):
        if not isinstance(allMoney, int) or not isinstance(jackPart, int):
            raise Exception("money must have integer type")
        else:
            #temporary hard set parameter
            gameId = 1
            transactionInfo = ""


            try:
                with transaction.atomic():
                    userBalance = UserInfo.objects.get_or_create(
                        name=userName,
                        defaults={'name': userName}
                    )[0].balance + allMoney

                    jackpot = Bank.objects.get_or_create(
                        id=gameId,
                        defaults={'id': 1, 'jackpot': 0}
                    )[0].jackpot
                    if userBalance > jackPart:
                        UserInfo.objects.filter(name=userName).update(balance=userBalance-jackPart)
                        Bank.objects.filter(id=gameId).update(jackpot=jackpot+jackPart)
                        transactionInfo = "transaction OK"
                    else:
                        transactionInfo = "you dont have enough money"
            except Error:
                #here can be "raise Exception('transaction falls')"
                transactionInfo = "transaction falls"
        return transactionInfo