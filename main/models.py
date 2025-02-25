from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
class MainTexts(models.Model):
    firstBlockTitle=RichTextField('First Block Title',default='none')
    contact_link=models.CharField('Phone url',max_length=200)
    secondBlockTitle=RichTextField('Second Block Title',default='none')
    thirdBlockTitle=RichTextField('Third Block Title',default='none')
    consultations=RichTextField('Consultations',default='none')
    headerSlider=RichTextField('Header Slider Text',default='none')
    def __str__(self):
        return f'Main Texts'
    class Meta:
        verbose_name = 'Main Texts'
        verbose_name_plural = 'Main Texts Block'
class Specialty(models.Model):
    name=models.CharField('Title',max_length=200)
    desc=RichTextField('Description',default='none')
    date=models.DateTimeField('Date',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'
class HeaderSlider(models.Model):
    img=models.URLField('Image',default='')
    date=models.DateTimeField('Date',default=timezone.now)
    def __str__(self):
        return f'Header Slider Images {self.id}'
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Header Slider Images'