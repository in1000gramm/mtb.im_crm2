import uuid
from django.db import models
from PIL import Image

# Create your models here.
class Client(models.Model):
    c_name = models.CharField('Имя', max_length=100)
    c_surname = models.CharField('Фамилия', max_length=100)
    c_phone = models.CharField('Телефон', max_length=100, blank=True)
    c_email = models.EmailField('E-mail', max_length=100, blank=True)
    c_birthday = models.DateField('День рождения', null=True, blank=True)
    c_image = models.ImageField('Добавить фото', default='clients_pics/default.jpg', upload_to='clients_pics')
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)

    # Override the save method of the model
    def save(self):
        super().save()
        img = Image.open(self.c_image.path)  # Open image
        # resize image
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)  # Resize image
            img.save(self.c_image.path)  # Save it again and override the larger image


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.c_surname, self.c_name)

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'Клиенты'