# Users

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the user. | [optional] 
**first_name** | **str** | First name of the user. | [optional] 
**last_name** | **str** | Last name of the user. | [optional] 
**email** | **str** | Unique email address for the user. | [optional] 
**password** | **str** | Password of the user. | [optional] 
**location** | **str** | The user&#x27;s location. | [optional] 
**title** | **str** | The user&#x27;s title. | [optional] 
**description** | **str** | The user&#x27;s description. | [optional] 
**tags** | **list[str]** | The user&#x27;s tags. | [optional] 
**avatar** | **OneOfUsersAvatar** | The user&#x27;s avatar. | [optional] 
**language** | **str** | The user&#x27;s language used in Directus. | [optional] 
**tfa_secret** | **str** | The 2FA secret string that&#x27;s used to generate one time passwords. | [optional] 
**status** | **str** | Status of the user. | [optional] 
**role** | **OneOfUsersRole** | Unique identifier of the role of this user. | [optional] 
**token** | **str** | Static token for the user. | [optional] 
**last_access** | **datetime** | When this user used the API last. | [optional] 
**last_page** | **str** | Last page that the user was on. | [optional] 
**provider** | **str** |  | [optional] 
**external_identifier** | **str** |  | [optional] 
**auth_data** | **object** |  | [optional] 
**email_notifications** | **bool** |  | [optional] 
**appearance** | **str** |  | [optional] 
**theme_dark** | **str** |  | [optional] 
**theme_light** | **str** |  | [optional] 
**theme_light_overrides** | **object** |  | [optional] 
**theme_dark_overrides** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

