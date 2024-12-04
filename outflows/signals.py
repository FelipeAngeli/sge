from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow
from services.notify import Notify


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()

@receiver(post_save, sender=Outflow)
def send_outflow_event(sender, instance, **kwargs):
    notify = Notify()
    
    data = {
        'event_type': 'outflow',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'product': str(instance.product),
        'quantity': instance.quantity,
    }
    notify.send_event(data)