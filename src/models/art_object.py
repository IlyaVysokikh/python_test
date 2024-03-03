from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from src.enums.gender import Gender
from src.models.constituent import Constituent
from src.models.element import Element
from src.models.tag import Tag


class ArtObject(BaseModel):
    object_id: int = Field(..., alias="objectID")
    is_highlight: bool = Field(..., alias="isHighlight")
    accession_number: str = Field(..., alias="accessionNumber")
    accession_year: str = Field(..., alias="accessionYear")
    is_public_domain: bool = Field(..., alias="isPublicDomain")
    primary_image: Optional[str] = Field(..., alias="primaryImage")
    primary_image_small: Optional[str] = Field(..., alias="primaryImageSmall")
    additional_images: Optional[List[str]] = Field(..., alias="additionalImages")
    constituents: Optional[List[Constituent]] = Field(..., alias="constituents")
    department: str
    object_name: str = Field(..., alias="objectName")
    title: str
    culture: str
    period: str
    dynasty: str
    reign: str
    portfolio: str
    artist_role: str = Field(..., alias="artistRole")
    artist_prefix: str = Field(..., alias="artistPrefix")
    artist_display_name: str = Field(..., alias="artistDisplayName")
    artist_display_bio: str = Field(..., alias="artistDisplayBio")
    artist_suffix: str = Field(..., alias="artistSuffix")
    artist_alpha_sort: str = Field(..., alias="artistAlphaSort")
    artist_nationality: str = Field(..., alias="artistNationality")
    artist_begin_date: str = Field(..., alias="artistBeginDate")
    artist_end_date: str = Field(..., alias="artistEndDate")
    artist_gender: Optional[Gender] = Field(..., alias="artistGender")
    artist_wikidata_URL: Optional[str] = Field(..., alias="artistWikidata_URL")
    artist_ulan_URL: Optional[str] = Field(..., alias="artistULAN_URL")
    object_date: str = Field(..., alias="objectDate")
    object_begin_date: int = Field(..., alias="objectBeginDate")
    object_end_date: int = Field(..., alias="objectEndDate")
    medium: str
    dimensions: str
    measurements: Optional[List[Element]]
    credit_line: str = Field(..., alias="creditLine")
    geography_type: str = Field(..., alias="geographyType")
    city: str
    state: str
    county: str
    country: str
    region: str
    subregion: str
    locale: str
    locus: str
    excavation: str
    river: str
    classification: str
    rights_and_reproduction: str = Field(..., alias="rightsAndReproduction")
    link_resource: str = Field(..., alias="linkResource")
    metadata_date: datetime = Field(..., alias="metadataDate")
    repository: str
    object_url: str = Field(..., alias="objectURL")
    tags: Optional[List[Tag]]
    object_wikidata_URL: str = Field(..., alias="objectWikidata_URL")
    is_timeline_work: bool = Field(..., alias="isTimelineWork")
    gallery_number: str = Field(..., alias="GalleryNumber")
