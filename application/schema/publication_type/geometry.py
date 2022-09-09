from marshmallow import Schema, fields, validate
from marshmallow_geojson import GeometriesSchema


class GeometrySchema(Schema):
    id = fields.Integer(required=True)
    type = fields.Str(
        required=True,
        validate=validate.OneOf(['Feature'], error='Invalid feature type'),
    )
    geometry = fields.Nested(GeometriesSchema, required=True)
    properties = fields.Dict(required=True)


class GeometryCollectionSchema(Schema):
    type = fields.Str(
        required=True,
        validate=validate.OneOf(
            ['FeatureCollection'], error='Invalid feature collection type'
        ),
    )
    features = fields.List(fields.Nested(GeometrySchema), required=True)
