# Django-celery-rabbitmq-image_resizer


image resizer created with celery(worker) and rabbitmq(broker).
how the whole process works?

once user uploads a file it will check its resolution if it is above 500 then django signals sends notification to celery task to resize it 
