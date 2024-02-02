from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import process_file


class File(models.Model):
    """
    Class describing the fields of the "File" object 
    in the database   
    """
    file = models.FileField(
        upload_to='files_media',
        verbose_name='Файл',
        help_text='Загрузите файл',
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время загрузки'
    )
    processed = models.BooleanField(
        default=False,
        verbose_name='Статус обработки файла'
    )

    def __str__(self):
        return f'Файл с ID {self.pk}'

    class Meta():
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


@receiver(post_save, sender=File)
def file_post_save(sender, instance, created, **kwargs):
    """
     A signal handler called after the File object is saved.
    
     When a new File object is created, it dispatches an asynchronous processing task
     (using Celery) to process the file using the process_file function.
    
     Options:
     - sender: The model class that initiated the signal (in this case, File).
     - instance: An instance of the File object that was saved.
     - created: Flag indicating whether the object has just been created.
     - **kwargs: Additional arguments passed by the signal.
    """
    if created:
        process_file.delay(instance.id)