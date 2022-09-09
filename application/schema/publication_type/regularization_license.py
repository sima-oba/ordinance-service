from marshmallow import Schema, fields


class RegularizationLicenseSchema(Schema):
    latitude = fields.Float(required=True, allow_none=True)
    longitude = fields.Float(required=True, allow_none=True)
    operation = fields.String(required=True, allow_none=True)
