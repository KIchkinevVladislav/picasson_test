from django.db import models


class File (models.Model):
    """
    Class describing the fields of the "File" object 
    in the database   
    """
    file = models.FileField(
        upload_to='files_media',
        verbose_name='Файл'        
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время загрузки'
    )
    processed = models.BooleanField(
        default=False,
        verbose_name='Статус обработки файла'
    )

    class Meta():
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'