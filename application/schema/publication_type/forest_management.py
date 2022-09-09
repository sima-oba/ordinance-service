from marshmallow import Schema, fields


class ForestManagementSchema(Schema):
    area = fields.String(required=True, allow_none=True)
    latitude = fields.Float(required=True, allow_none=True)
    longitude = fields.Float(required=True, allow_none=True)
