# PermissionsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** | What collection this permission applies to. | [optional] 
**comment** | **str** | If the user can post comments. | [optional] 
**create** | **str** | If the user can create items. | [optional] 
**delete** | **str** | If the user can update items. | [optional] 
**explain** | **str** | If the user is required to leave a comment explaining what was changed. | [optional] 
**read** | **str** | If the user can read items. | [optional] 
**role** | **int** | Unique identifier of the role this permission applies to. | [optional] 
**read_field_blacklist** | **list[str]** | Explicitly denies read access for specific fields. | [optional] 
**status** | **str** | What status this permission applies to. | [optional] 
**status_blacklist** | **list[str]** | Explicitly denies specific statuses to be used. | [optional] 
**update** | **str** | If the user can update items. | [optional] 
**write_field_blacklist** | **list[str]** | Explicitly denies write access for specific fields. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

