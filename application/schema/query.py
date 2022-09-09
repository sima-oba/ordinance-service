from marshmallow import Schema, fields


class OrdinanceQuery(Schema):
    start_date = fields.DateTime(missing=None)
    end_date = fields.DateTime(missing=None)
