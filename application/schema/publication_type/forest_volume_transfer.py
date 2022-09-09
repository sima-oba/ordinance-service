from marshmallow import Schema, fields


class ForestVolumeTransferSchema(Schema):
    to_doc_number = fields.String(required=True)
