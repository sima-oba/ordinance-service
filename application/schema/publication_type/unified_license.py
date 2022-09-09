from marshmallow import Schema, fields


class UnifiedLicenseSchema(Schema):
    operation = fields.String(required=True, allow_none=True)
