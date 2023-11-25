from django.shortcuts import render
from .models import AnnouncedPuResults, PollingUnit, Lga
from django.db.models import Sum
from .forms import PartyPollingResultForm

# Create your views here.

def ListPollingResult(request):
    polling_result = PollingUnit.objects.all().exclude(announced_polling__isnull = True)
    return render(request,'list_polling_result.html', context={'polling_result':polling_result})


def GetPollingResult(request, polling_id):
    polling_unit = PollingUnit.objects.get(uniqueid=polling_id)
    polling_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=polling_unit)
    print(polling_result[0].result_id)
    return render(request,'get_polling_result.html', context={'polling_result':polling_result,'polling_unit':polling_unit })


def ListLgas(request):
    lgas = Lga.objects.all()
    return render(request,'list_lga.html', context={'lgas':lgas})


def GetTotalLgaResult(request):
    lga_id = request.POST['lga']
    lga = Lga.objects.get(lga_id=lga_id)
    polling_unit = PollingUnit.objects.filter(lga_id=lga_id).exclude(announced_polling__isnull = True)
    print(polling_unit)

    context = {
        'total' : AnnouncedPuResults.objects.filter(polling_unit_uniqueid__in=polling_unit).aggregate(Sum("party_score")),
        'lga':lga

    }
    # print(context['polling_result']['party_score__sum'])
    return render(request,'get_total_lga_res.html', context)


def PartyPollingResult(request):
    form = PartyPollingResultForm()
    if request.method == 'POST':
        form = PartyPollingResultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'party_polling_result.html', context={'form':form})

