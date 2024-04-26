# Operations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the operation. | [optional] 
**name** | **str** | The name of the operation. | [optional] 
**key** | **str** | Key for the operation. Must be unique within a given flow. | [optional] 
**type** | **str** | Type of operation. One of &#x60;log&#x60;, &#x60;mail&#x60;, &#x60;notification&#x60;, &#x60;create&#x60;, &#x60;read&#x60;, &#x60;request&#x60;, &#x60;sleep&#x60;, &#x60;transform&#x60;, &#x60;trigger&#x60;, &#x60;condition&#x60;, or any type of custom operation extensions. | [optional] 
**position_x** | **int** | Position of the operation on the X axis within the flow workspace. | [optional] 
**position_y** | **int** | Position of the operation on the Y axis within the flow workspace. | [optional] 
**options** | **object** | Options depending on the type of the operation. | [optional] 
**resolve** | **OneOfOperationsResolve** | The operation triggered when the current operation succeeds (or &#x60;then&#x60; logic of a condition operation). | [optional] 
**reject** | **OneOfOperationsReject** | The operation triggered when the current operation fails (or &#x60;otherwise&#x60; logic of a condition operation). | [optional] 
**flow** | **OneOfOperationsFlow** |  | [optional] 
**date_created** | **datetime** | Timestamp in ISO8601 when the operation was created. | [optional] 
**user_created** | **OneOfOperationsUserCreated** | The user who created the operation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

