import graphene
from graphene_django import DjangoObjectType
from .models import Room


class RoomType(DjangoObjectType):

    user = graphene.Field("users.schema.UserType")

    class Meta:
        model = Room

# 룸타입을 정의하고


class RoomListResponse(graphene.ObjectType):

    arr = graphene.List(RoomType)
    total = graphene.Int()


class Query(object):

    rooms = graphene.Field(RoomListResponse, page=graphene.Int())

    def resolve_rooms(self, info, page=1):
        page_size = 5
        start = page_size * (page-1)
        end = page_size * (page)
        rooms = Room.objects.all()[start:end]
        total = Room.objects.count()
        return RoomListResponse(arr=rooms, total=total)

# 쿼리에서 리졸브 해준다
