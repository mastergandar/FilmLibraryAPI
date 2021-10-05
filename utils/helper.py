from django.contrib.contenttypes.models import ContentType


def get_content_object(content_type_model: str, object_id: int):
    try:
        ct = ContentType.objects.get(model=content_type_model)
    except ContentType.DoesNotExist:
        raise ValueError("Specified content_type does not exist")
    ct_class = ct.model_class()
    try:
        content_object = ct_class.objects.get(pk=object_id)
    except Exception:
        raise ValueError("Content not found")
    return content_object


def get_content_type(obj) -> str:
    ct = ContentType.objects.get_for_model(obj)
    return ct.model
