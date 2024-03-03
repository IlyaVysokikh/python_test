from src.base.Response import Response

from src.models.art_objects_list import ArtObjectsList


def test_getting_total_and_objects_ids(get_total_and_objects_ids):
    Response(get_total_and_objects_ids).assert_status_code(200).validate(ArtObjectsList)

