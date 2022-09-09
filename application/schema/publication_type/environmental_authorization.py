from marshmallow import Schema, fields


class EnvironmentalAuthorizationSchema(Schema):
    observation = fields.String(required=True)
