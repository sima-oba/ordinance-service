from marshmallow import Schema, fields


class ImplantationLicenseSchema(Schema):
    area = fields.Float(missing=None)
    prod_volume = fields.Float(missing=None)
