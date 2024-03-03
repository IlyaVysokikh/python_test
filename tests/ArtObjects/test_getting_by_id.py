from src.base.Response import Response

from src.models.art_object import ArtObject


def test_getting_existing_art_object_by_id(get_existing_art_object_by_id):
    Response(get_existing_art_object_by_id).assert_status_code(200).validate(ArtObject)


def test_getting_nonexisting_art_object_by_id(get_nonexisting_art_object_by_id):
    Response(get_nonexisting_art_object_by_id).assert_status_code(404)