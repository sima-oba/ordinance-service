from marshmallow import Schema, fields


class InstallationLicenseSchema(Schema):
    objective = fields.String(required=True, allow_none=True)
    location = fields.String(required=True, allow_none=True)
