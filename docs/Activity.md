# Activity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the object. | [optional] 
**action** | **str** | Action that was performed. | [optional] 
**user** | **OneOfActivityUser** | The user who performed this action. | [optional] 
**timestamp** | **datetime** | When the action happened. | [optional] 
**ip** | **OneOfActivityIp** | The IP address of the user at the time the action took place. | [optional] 
**user_agent** | **str** | User agent string of the browser the user used when the action took place. | [optional] 
**collection** | **OneOfActivityCollection** | Collection identifier in which the item resides. | [optional] 
**item** | **str** | Unique identifier for the item the action applied to. This is always a string, even for integer primary keys. | [optional] 
**comment** | **str** | User comment. This will store the comments that show up in the right sidebar of the item edit page in the admin app. | [optional] 
**origin** | **str** | Origin of the request when the action took place. | [optional] 
**revisions** | **list[OneOfActivityRevisionsItems]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

