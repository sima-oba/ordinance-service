from marshmallow import Schema, fields


class ICMBioInfractionNoticeSchema(Schema):
    geometry = fields.Dict(required=True)
    description = fields.String(required=True)
    infraction_type = fields.String(required=True)
    judging = fields.String(missing=None)
