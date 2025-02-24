from pydantic import BaseModel, model_serializer

class Product(BaseModel):
    name: str
    short_description: str | None
    description: str | None
    images: list[str] | None
    attributes: dict

    @model_serializer
    def serialize_model(self):
        base_json = {
            'Name': self.name,
            'Short description': self.short_description if self.short_description else "",
            'Description': self.description if self.description else "",
            'Images': ", ".join(self.images) if self.images else "",
        }
        attributes_json = {}
        for i, (key, value) in enumerate(self.attributes.items()):
            attributes_json.update({f"Attribute {i + 1} name": key, f"Attribute {i + 1} value": value, f"Attribute {i + 1} visible": 1, f"Attribute {i + 1} global": 1})
        return {**base_json, **attributes_json}