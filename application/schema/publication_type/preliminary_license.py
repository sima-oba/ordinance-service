from marshmallow import Schema, fields


class PreliminaryLicenseSchema(Schema):
    operation = fields.String(required=True, allow_none=True)
