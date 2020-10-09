from django.db import models


class Employee(models.Model):

    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)

    designation = models.CharField(max_length=100)

    salary = models.IntegerField(null=False)

    # date of joining
    doj = models.CharField(null=False, max_length=10)

    # date of birth
    dob = models.CharField(null=False, max_length=10)

    class Meta:

        ordering = ["-dob"]

    def __str__(self):

        return self.name

    @classmethod
    def records(cls, list_of_records):

        for record in list_of_records:

            if not Employee.objects.filter(id=record.get("id")).exist():

                new_employee = cls.objects.create(**record)
            
            else:

                print(f"Id:{record.get('id')} is already exist.")
        