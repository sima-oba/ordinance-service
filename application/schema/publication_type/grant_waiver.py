from marshmallow import Schema, fields
from marshmallow.validate import Range


class GrantWaiverSchema(Schema):
    dismissal_process = fields.String(required=True, allow_none=True)
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
