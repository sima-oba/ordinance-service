from marshmallow import Schema, fields


class OperationLicenseSchema(Schema):
    operation = fields.String(missing=None)
