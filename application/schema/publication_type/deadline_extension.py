from marshmallow import Schema, fields


class DeadlineExtensionSchema(Schema):
    extension = fields.String(required=True)
