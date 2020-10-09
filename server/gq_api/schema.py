import graphene

from graphene_django.types import DjangoObjectType

from items.models import Employee


class EmployeeType(DjangoObjectType):

    id = graphene.Int()

    name = graphene.String()

    designation = graphene.String()

    salary = graphene.Int()

    doj = graphene.String()

    dob = graphene.String()


    class Meta:

        model = Employee

    def resolve_id(self, info):

        return self.id
    
    def resolve_name(self, info):

        return self.name

    def resolve_designation(self, info):

        return self.designation

    def resolve_salary(self, info):

        return self.salary

    def resolve_doj(self, info):

        return self.doj

    def resolve_dob(self, info):

        return self.dob


class Query(graphene.ObjectType):

    employee_list = graphene.List(EmployeeType)

    def resolve_employee_list(self, info, *_):

        return Employee.objects.all().only("name", "dob")


schema = graphene.Schema(query=Query)