from marshmallow import Schema, fields


class RectificationSchema(Schema):
    ordinance_number_rectified = fields.String(required=True)
