# Webhooks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The index of the webhook. | [optional] 
**name** | **str** | The name of the webhook. | [optional] 
**method** | **str** | Method used in the webhook. | [optional] 
**url** | **str** | The url of the webhook. | [optional] 
**status** | **str** | The status of the webhook. | [optional] 
**data** | **bool** | If yes, send the content of what was done | [optional] 
**actions** | **list[str]** | The actions that triggers this webhook. | [optional] 
**collections** | **list[str]** |  | [optional] 
**headers** | **object** |  | [optional] 
**was_active_before_deprecation** | **bool** |  | [optional] 
**migrated_flow** | **OneOfWebhooksMigratedFlow** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

