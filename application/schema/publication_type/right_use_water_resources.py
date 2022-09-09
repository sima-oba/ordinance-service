from marshmallow import Schema, fields
from marshmallow.validate import Range


class RightUseWaterResourcesSchema(Schema):
    flow = fields.String(required=True)
    capture = fields.String(required=True, allow_none=True)
    area = fields.String(required=True, allow_none=True)
    latitude = fields.Float(
        validates=Range(min=-90, max=90),
        required=True,
        allow_none=True
    )
    longitude = fields.Float(
        validates=Range(min=-180, max=180),
        required=True,
        allow_none=True
    )
