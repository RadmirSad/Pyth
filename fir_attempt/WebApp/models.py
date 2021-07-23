from django.db import models

# Create your models here.


class Teacher(models.Model):
    FullName = models.CharField(verbose_name='ФИО преподавателя', max_length=50)


class Web(models.Model):
    Time = models.DateTimeField(verbose_name='Дата и время проведения вебинара')
    LOCATIONS = (
        (1, "Тульская"),
        (2, "Дом"),
        (3, "Питер"),
        (4, "Долгопрудный"),
        (5, "Сочи"),
        (6, "Новосибирск")
    )
    Location = models.IntegerField(verbose_name='Место проведения вебинара', choices=LOCATIONS, default=1)
    STATE = (
        (1, "Создан"),
        (2, "Сейчас идёт"),
        (3, "Закончен"),
        (4, "Отменён")
    )
    Status = models.IntegerField(verbose_name='Статус вебинара', choices=STATE, default=1)
    Teachers = models.ManyToManyField(Teacher)


class Course(models.Model):
    Name = models.CharField(verbose_name='Название курса', max_length=40)
    Webinars = models.ManyToManyField(Web, verbose_name='Вебинары данного курса')


class Cost(models.Model):
    Course_ID = models.ForeignKey(Course, verbose_name='ID курса', null=True, blank=True, on_delete=models.PROTECT)
    Teach_ID = models.ForeignKey(Teacher, verbose_name='ID преподавателя', null=True, blank=True, on_delete=models.PROTECT)
    CostInHour = models.FloatField(verbose_name='Стоимость вебинара')

