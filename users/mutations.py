import graphene
from .models import User


class CreateAccountMutation(graphene.Mutation):

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, email, password, first_name=None, last_name=None):
        try:
            User.objects.get(email=email)
            return CreateAccountMutation(ok=False, error="User already exists")
        except User.DoesNotExist:
            try:
                User.objects.create_user(email, email, password)
                # https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user
                # create_user 헬프 함수에대해 위 링크를 참조하자
                return CreateAccountMutation(ok=True)
            except Exception:
                return CreateAccountMutation(error="Can't create user.", ok=False)
