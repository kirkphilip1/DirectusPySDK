# Relations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the relation. | [optional] 
**many_collection** | **str** | Collection that has the field that holds the foreign key. | [optional] 
**many_field** | **str** | Foreign key. Field that holds the primary key of the related collection. | [optional] 
**one_collection** | **str** | Collection on the _one_ side of the relationship. | [optional] 
**one_field** | **str** | Alias column that serves as the _one_ side of the relationship. | [optional] 
**one_collection_field** | **str** |  | [optional] 
**one_allowed_collections** | **list[str]** |  | [optional] 
**junction_field** | **str** | Field on the junction table that holds the many field of the related relation. | [optional] 
**sort_field** | **str** |  | [optional] 
**one_deselect_action** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

