from marshmallow import Schema, fields


class OwnershipTransferSchema(Schema):
    transfer_type = fields.String(missing=None)
    to_doc_number = fields.String(required=True)
