from marshmallow import Schema, fields


class LicenseCancellationSchema(Schema):
    origin_ordinance = fields.String(required=True)
