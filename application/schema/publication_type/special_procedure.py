from marshmallow import Schema, fields


class SpecialProcedureSchema(Schema):
    authorization_number = fields.String(required=True)
