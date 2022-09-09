from marshmallow import Schema, fields


class DemolitionPenaltySchema(Schema):
    infringement_date = fields.DateTime(format='%Y-%m-%d', required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
