import pytest

from src.base.Response import Response
from src.models.art_objects_list import ArtObjectsList


@pytest.mark.parametrize(
    'param, search_string', [
        ('q', 'sunflowers')

])
def test_search(param, search_string, search_request):
    Response(search_request(param, search_string)).assert_status_code(200).validate(ArtObjectsList)
