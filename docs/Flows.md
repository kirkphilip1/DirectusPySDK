# Flows

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the flow. | [optional] 
**name** | **str** | The name of the flow. | [optional] 
**icon** | **str** | Icon displayed in the Admin App for the flow. | [optional] 
**color** | **str** | Color of the icon displayed in the Admin App for the flow. | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** | Current status of the flow. | [optional] [default to 'active']
**trigger** | **str** | Type of trigger for the flow. One of &#x60;hook&#x60;, &#x60;webhook&#x60;, &#x60;operation&#x60;, &#x60;schedule&#x60;, &#x60;manual&#x60;. | [optional] 
**accountability** | **str** | The permission used during the flow. One of &#x60;$public&#x60;, &#x60;$trigger&#x60;, &#x60;$full&#x60;, or UUID of a role. | [optional] 
**options** | **object** | Options of the selected trigger for the flow. | [optional] 
**operation** | **OneOfFlowsOperation** | UUID of the operation connected to the trigger in the flow. | [optional] 
**date_created** | **datetime** | Timestamp in ISO8601 when the flow was created. | [optional] 
**user_created** | **OneOfFlowsUserCreated** | The user who created the flow. | [optional] 
**operations** | **list[OneOfFlowsOperationsItems]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

