# FieldscollectionSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field. | [optional] 
**table** | **str** | The collection of the field. | [optional] 
**type** | **str** | The type of the field. | [optional] 
**default_value** | **str** | The default value of the field. | [optional] 
**max_length** | **int** | The max length of the field. | [optional] 
**is_nullable** | **bool** | If the field is nullable. | [optional] 
**is_primary_key** | **bool** | If the field is primary key. | [optional] 
**has_auto_increment** | **bool** | If the field has auto increment. | [optional] 
**foreign_key_column** | **str** | Related column from the foreign key constraint. | [optional] 
**foreign_key_table** | **str** | Related table from the foreign key constraint. | [optional] 
**comment** | **str** | Comment as saved in the database. | [optional] 
**schema** | **str** | Database schema (pg only). | [optional] 
**foreign_key_schema** | **str** | Related schema from the foreign key constraint (pg only). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

