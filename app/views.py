from django.shortcuts import render,HttpResponse
from .tasks import image_resize_task
from .models import mymodel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from app.tasks import image_resize_task

# Create your views here.


def upload(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            instance = mymodel.objects.create(image=image_file)
            if instance.image.width > 500 and instance.image.height > 500:
                image_resize_task.delay(instance.id)
                return HttpResponse("image resized successfully")     
        else:
            return render(request,'index.html')
                   
    else:
        return render(request,'index.html')
    

@receiver(pre_save, sender=mymodel)
def image_resizer(sender, instance, **kwargs):
    if instance.image and instance.image.width > 500 and instance.image.height > 500:
        image_resize_task.delay(instance.id)
