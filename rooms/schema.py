import graphene
from .queries import resolve_room, resolve_rooms
from .types import RoomType, RoomListResponse


class Query(object):

    rooms = graphene.Field(
        RoomListResponse, page=graphene.Int(), resolver=resolve_rooms
    )
    room = graphene.Field(
        RoomType, id=graphene.Int(required=True), resolver=resolve_room
    )

# 쿼리에서 리졸브 해준다
