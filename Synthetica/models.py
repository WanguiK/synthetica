from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.urls import reverse



class Project(models.Model):

    id = models.AutoField('Project ID:', primary_key=True)

    project_name = models.CharField('Project Name:', max_length=140, blank=False)

    description = models.TextField('Project Description:', max_length=1000, blank=False)

    records = models.IntegerField('No. Of Records:', default=1, blank=False, validators=[MinValueValidator(1), MaxValueValidator(5000)])

    class Meta:
        ordering = ['-id', 'project_name']

    def __str__(self):
        return f'{self.id} ({self.project_name})'

    def get_absolute_url(self):
        # return reverse('workspace')
        return reverse('generate', args=[str(self.id)])



class Generate(models.Model):
    id = models.AutoField('Generation ID', primary_key=True)

    project_id = models.ForeignKey(Project, 'Project ID', null=True)

    field_name = models.CharField('Field Name', max_length=100, blank=False, default='Field#')

    DATA_TYPES = (
        ('t', 'Short Text'),
        ('n', 'Numeric'),
        ('a', 'Alphanumeric'),
        ('lt', 'Long Text'),
        ('d', 'Date',),
        ('ti', 'Time'),
        ('dti', 'Date & Time')
    )

    data_type = models.CharField(
        'Data Type',
        max_length = 3,
        choices = DATA_TYPES,
        blank = True,
        default = 't',
    )
    options = models.TextField('Options', max_length=100, blank=True, default='car, shoe, tree')

    # def get_absolute_url(self):
    #     return reverse('generate', args=[str(self.id)])

    def __str__(self):
        return str(self.id)