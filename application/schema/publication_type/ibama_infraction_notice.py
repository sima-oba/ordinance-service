from marshmallow import Schema, fields


class IbamaInfractionNoticeSchema(Schema):
    amount = fields.Float(required=True)
    status = fields.String(required=True)
    sanctions = fields.String(required=True)
    city = fields.String(required=True)
    infraction = fields.String(required=True)
