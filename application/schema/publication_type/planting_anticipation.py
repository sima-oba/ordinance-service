from marshmallow import Schema, fields


class PlantingAnticipationSchema(Schema):
    crop = fields.String(missing=None)
    seeding_harverst = fields.String(missing=None)
    seeding_start = fields.DateTime(format='%Y-%m-%d', required=True)
    seeding_end = fields.DateTime(format='%Y-%m-%d', required=True)
    sanitary_void_harvest = fields.String(missing=None)
    sanitary_void_start = fields.DateTime(format='%Y-%m-%d', required=True)
    sanitary_void_end = fields.DateTime(format='%Y-%m-%d', required=True)
