from marshmallow import Schema, fields


class LicenseRevocationSchema(Schema):
    origin_ordinance = fields.String(required=True)
    revocation_type = fields.String(required=True)
    latitude = fields.Float(required=True, allow_none=True)
    longitude = fields.Float(missing=None, allow_none=True)
