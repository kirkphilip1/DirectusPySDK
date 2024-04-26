# Permissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the permission. | [optional] 
**role** | **str** | Unique identifier of the role this permission applies to. | [optional] 
**collection** | **str** | What collection this permission applies to. | [optional] 
**action** | **str** | What action this permission applies to. | [optional] 
**permissions** | **object** | JSON structure containing the permissions checks for this permission. | [optional] 
**validation** | **object** | JSON structure containing the validation checks for this permission. | [optional] 
**presets** | **object** | JSON structure containing the preset value for created/updated items. | [optional] 
**fields** | **list[str]** | CSV of fields that the user is allowed to interact with. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

