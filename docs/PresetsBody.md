# PresetsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** | What collection this collection preset is used for. | 
**title** | **str** | Name for the bookmark. If this is set, the collection preset will be considered to be a bookmark. | [optional] 
**role** | **str** | The unique identifier of a role in the platform. If user is null, this will be used to apply the collection preset or bookmark for all users in the role. | [optional] 
**search** | **str** | What the user searched for in search/filter in the header bar. | [optional] 
**filters** | [**list[PresetsFilters]**](PresetsFilters.md) |  | [optional] 
**layout** | **str** | Name of the view type that is used. | [optional] 
**layout_query** | **str** | Layout query that&#x27;s saved per layout type. Controls what data is fetched on load. These follow the same format as the JS SDK parameters. | [optional] 
**layout_options** | **str** | Options of the views. The properties in here are controlled by the layout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

