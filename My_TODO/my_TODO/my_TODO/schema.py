import graphene
from graphene_django import DjangoObjectType
from mainapp.models import Project, TODO
from authapp.models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.UUID(required=True))
    user_by_email = graphene.Field(UserType, email=graphene.String(required=True))
    all_projects = graphene.List(ProjectType)
    project_by_id = graphene.Field(ProjectType, id=graphene.UUID(required=True))
    project_by_username = graphene.List(ProjectType, username=graphene.String(required=False))
    all_TODO = graphene.List(TODOType)
    TODO_by_id = graphene.Field(TODOType, id=graphene.Int(required=True))

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return None

    def resolve_user_by_email(self, info, email):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_project_by_id(self, info, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return None

    def resolve_project_by_username(self, info, username):
        projects = Project.objects.all()
        if username:
            projects = projects.filter(users_list__username=username)
        return projects

    def resolve_all_TODO(root, info):
        return TODO.objects.all()

    def resolve_TODO_by_id(self, info, id):
        try:
            return TODO.objects.get(id=id)
        except TODO.DoesNotExist:
            return None


class ProjectUpdate(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)
        status_complete = graphene.Boolean(required=True)
        id = graphene.UUID()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, project_name, status_complete, id):
        project = Project.objects.get(pk=id)
        project.project_name = project_name
        project.status_complete = status_complete
        project.save()
        return ProjectUpdate(project=project)


class Mutation(graphene.ObjectType):
    update_project = ProjectUpdate.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
