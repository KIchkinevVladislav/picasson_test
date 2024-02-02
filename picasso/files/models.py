from django.db import models


class File (models.Model):
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