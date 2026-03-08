from django.shortcuts import render
from .models import*

# Create your views here.
def recepie(request):
    # so frontend sai backened mai data lanay kai liya hum ye use krty hai
    if request.method=="Post":
        data=request.post
        # for files
        recepie_image=request.Files.get("recepie_image")
        recepie_name=data.get("recepie_name")
        recepie_quantity=data.get("recepie_quantity")
        Recepie.objects.create(
            recepie_name=recepie_name,
            recepie_quantity=recepie_quantity,
            recepie_image=recepie_image)
        print(recepie_name)
        print(recepie_quantity)
        print(recepie_image)
    return render(request,"recepie.html")
#aur agr hamy is data ko save krna hai
