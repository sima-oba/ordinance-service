from marshmallow import Schema, fields


class OwnerNameChangeSchema(Schema):
    from_name = fields.String(required=True)
    to_name = fields.String(required=True)
