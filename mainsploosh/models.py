from django.db import models

class Class(models.Model):
    class_id = models.CharField(max_length=10)
    section  = models.CharField(max_length=10)
    def __str__(self):
        return self.class_id + '-' + completeSection(str(self.section))

class ClassCategory(models.Model):
    category_name = models.CharField('Name of the category as appears on PennIntouch', max_length=30)
    ok_classes = models.ManyToManyField(Class, verbose_name='List of classes that satisfy the class requirement')
    def __str__(self):
        return self.category_name

class Degree(models.Model):
    major = models.CharField('Major', max_length=50, default = 'Undeclared')
    degreeType = models.CharField('Type of degree', max_length=50, default = '')
    school = models.CharField('School', max_length=50, default = '')
    class_categories = models.ManyToManyField(ClassCategory, verbose_name="List of class category requirements")
    def __str__(self):
        return self.degreeType + ' in ' + self.major

def completeSection(s):
    if len(s) == 1:
        return '00' + s
    elif len(s) == 2:
        return '0' + s
    else:
        return s
