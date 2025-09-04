from django.db import models

class Program(models.Model):
    sn = models.IntegerField(verbose_name="SN", unique=True)
    university_name = models.CharField(max_length=255, verbose_name="University Name")
    type_of_institution = models.CharField(max_length=100, verbose_name="Type of institution")
    location = models.CharField(max_length=255, verbose_name="Location")
    program_name = models.CharField(max_length=255, verbose_name="Program Name")
    degree = models.CharField(max_length=100, verbose_name="Degree")
    duration = models.CharField(max_length=50, verbose_name="Duration")
    instruction_language = models.CharField(max_length=50, verbose_name="Instruction Language")
    tuition_fee = models.CharField(max_length=100, verbose_name="Tuition Fee")
    semester_contribution = models.CharField(max_length=100, verbose_name="Semester contribution (Approx. per semester)")
    deadline = models.CharField(max_length=100, verbose_name="Deadline")
    beginning = models.CharField(max_length=100, verbose_name="Beginning")
    admission_restricted = models.CharField(max_length=50, verbose_name="Admission Restricted?")
    academic_requirements = models.TextField(verbose_name="Academic Requirements")
    ects = models.CharField(max_length=50, verbose_name="ECTS")
    grade_threshold = models.CharField(max_length=50, verbose_name="Grade Threshold")
    language_requirement = models.TextField(verbose_name="Language Requirement")
    link_for_detailed_info = models.URLField(verbose_name="Link for detailed info", blank=True)
    data_source = models.CharField(max_length=255, verbose_name="Data Source", blank=True)
    application_channel = models.CharField(max_length=255, verbose_name="Application Channel", blank=True)
    added_by = models.CharField(max_length=100, verbose_name="Added by", blank=True)

    def __str__(self):
        return f"{self.program_name} at {self.university_name}"