from dataApp import serializers
from dataApp.models import Ticker
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dataApp.serializers import TickerSerializer
from yahoofinancials import YahooFinancials

# funtion to pull data from api


def pullNsave(ticker, st_date, end_date):
    yahoo_financials = YahooFinancials(ticker)
    a = yahoo_financials.get_historical_price_data(
        st_date, end_date, "daily")
    lst = a[ticker]['prices']
    for i in lst:
        serializer = TickerSerializer(data={"name": ticker,
                                            "date": i['formatted_date'], "open_val": i['open'], "high_val": i['high'], "low_val": i['low'], "close_val": i['close']})
        if serializer.is_valid():
            serializer.save


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/ticker-list/',
        'Detail': '/tikcer-detail/<str:pk>',
        'Create': '/ticker-create/',
        'Update': '/ticker-update/<str:pk>',
        'Delete': '/ticker-delete/<str:pk>'}

    return Response(api_urls)


@api_view(['GET'])
def tickerList(request):
    ticker = Ticker.objects.all()
    serializer = TickerSerializer(ticker, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tickerDetail(request, pk):
    ticker = Ticker.objects.get(id=pk)
    serializer = TickerSerializer(ticker, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def tickerCreate(request):

    pullNsave(request.data['ticker'],
              request.data['st_date'], request.data['end_date'])
    return Response('Data Saved !!')


@api_view(['POST'])
def tickerUpdate(request, pk):
    ticker = Ticker.objects.get(id=pk)
    serializer = TickerSerializer(instance=ticker, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def tickerDelete(request, pk):
    ticker = Ticker.objects.get(id=pk)
    ticker.delete()
    return Response('Deleted !')
