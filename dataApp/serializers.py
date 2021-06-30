from rest_framework import fields, serializers
from dataApp.models import Ticker
# from yahoofinancials import YahooFinancials


class TickerSerializer(serializers.Serializer):
    class Meta:
        model = Ticker
        fields = '__all__'
