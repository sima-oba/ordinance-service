from marshmallow import Schema, fields


class LicenseRenewalSchema(Schema):
    renovation_type = fields.String(required=True)
    operation = fields.String(required=True)
