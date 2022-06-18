from marshmallow import fields

from config.extensions import ma


class LinkSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    original_url = fields.URL()
    short_url = fields.String(dump_only=True)
    visits = fields.Integer(dump_only=True)
    one_use = fields.Boolean(required=False)
    date_created = fields.DateTime(required=False)


link_schema = LinkSchema()
links_schema = LinkSchema(many=True)
