from marshmallow import Schema,fields

class ExportResultsSchema(Schema):
    """Export Results Schema """
    file_name=fields.Str(required=True)
    file_type=fields.Str(required=True,validate=lambda x:x in ['csv','excel'])