from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def result(request):
    djtext = request.POST.get('number', 'default')
    selecttype = request.POST.get('selecttype', 'off')

    decimal = 0
    if selecttype == 'binary' and djtext != '':
        decimal = int(djtext, 2)
        octal = oct(decimal)
        hexa = hex(decimal)
        params = {'type1' : 'Decimal','value1':decimal,'type2':'Octal','value2':octal,'type3':'Hexa Decimal','value3':hexa}
        return render(request, 'result.html', params)
    elif selecttype == 'octal' and djtext != '':
        decimal = str(int(djtext, 8))
        binary = bin(int(decimal))
        hexa = hex(int(decimal))
        params = {'type1': 'Decimal', 'value1': decimal, 'type2': 'Binary', 'value2': binary, 'type3': 'Hexa Decimal',
                  'value3': hexa}
        return render(request, 'result.html', params)
    elif selecttype == 'decimal' and djtext != '':
        octal = oct(int(djtext))
        binary = bin(int(djtext))
        hexa = hex(int(djtext))
        params = {'type1': 'Octal', 'value1': octal, 'type2': 'Binary', 'value2': binary, 'type3': 'Hexa Decimal',
                  'value3': hexa}
        return render(request, 'result.html', params)
    elif selecttype == 'hexa' and djtext != '':
        decimal = str(int(djtext, 16))
        binary = bin(int(decimal))
        octal = oct(int(decimal))
        params = {'type1': 'Decimal', 'value1': decimal, 'type2': 'Binary', 'value2': binary, 'type3': 'Octal',
                  'value3': octal}
        return render(request, 'result.html', params)
    else:
        return HttpResponse('Error')