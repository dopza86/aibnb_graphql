import graphene
from .models import Room
from .types import RoomType, RoomListResponse


class Query(object):

    rooms = graphene.Field(RoomListResponse, page=graphene.Int())
    room = graphene.Field(RoomType, id=graphene.Int(required=True))
    # required=True 필수값 지정

    def resolve_rooms(self, info, page=1):
        if page < 1:
            page = 1
        page_size = 5
        start = page_size * (page-1)
        end = page_size * (page)
        rooms = Room.objects.all()[start:end]
        total = Room.objects.count()
        return RoomListResponse(arr=rooms, total=total)

    def resolve_room(self, info, id):
        try:
            return Room.objects.get(id=id)
        except Room.DoesNotExist:
            return None

# 쿼리에서 리졸브 해준다
