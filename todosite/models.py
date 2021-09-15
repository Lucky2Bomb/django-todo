from django.db import models

# Todo model
# id            Int
# title         Varchar(150)
# is_finished   Boolean (default:false)
# show_checked  Boolean (default:true)

# Task model
# id            Int
# title         Varchar(150)
# is_checked    Boolean (default:false)
# todo          Int (fk -> Todo, nullable = false, cascade)

class Todo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    is_finished = models.BooleanField(default=False, verbose_name='Выполнено')
    show_checked = models.BooleanField(
        default=True, verbose_name='Показывать выполненные')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'список дел'
        verbose_name_plural = 'списки дел'


class Task(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    is_checked = models.BooleanField(default=False, verbose_name='Выполнено')

    todo = models.ForeignKey(
        'Todo', on_delete=models.CASCADE, null=False, verbose_name='Название списка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'задача списка дел'
        verbose_name_plural = 'задачи списков дел'
