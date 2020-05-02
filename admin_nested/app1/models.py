from django.db import models


class Campus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE,
                               related_name='school',
                               default=None, null=True)

    def __str__(self):
        return f"{self.name} - {self.campus.name}"


class Grade(models.Model):
    """
    1st standard, 2nd standard, 1st year, 2nd year etc
    Each school or college will have a standard
    """
    school = models.ForeignKey(School, on_delete=models.CASCADE,
                               related_name='grade',
                               default=None, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    """
    Every standard (1st std, 2nd std or 1st year,
    2nd year will have multiple subjects
    """
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,
                              related_name='subject')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default=None
                                   , null=True, blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    Every subject has multiple lessons
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                related_name='lesson')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default=None
                                   , null=True, blank=True)

    def __str__(self):
        return self.name
