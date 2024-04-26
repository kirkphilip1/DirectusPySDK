# Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the setting. | [optional] 
**project_name** | **str** | The name of the project. | [optional] 
**project_url** | **str** | The url of the project. | [optional] 
**project_color** | **str** | The brand color of the project. | [optional] 
**project_logo** | **str** | The logo of the project. | [optional] 
**public_foreground** | **str** | The foreground of the project. | [optional] 
**public_background** | [**SettingsPublicBackground**](SettingsPublicBackground.md) |  | [optional] 
**public_note** | **str** | Note rendered on the public pages of the app. | [optional] 
**auth_login_attempts** | **int** | Allowed authentication login attempts before the user&#x27;s status is set to blocked. | [optional] 
**auth_password_policy** | **str** | Authentication password policy. | [optional] 
**storage_asset_transform** | **str** | What transformations are allowed in the assets endpoint. | [optional] 
**storage_asset_presets** | [**list[SettingsStorageAssetPresets]**](SettingsStorageAssetPresets.md) | Array of allowed | [optional] 
**custom_css** | **str** |  | [optional] 
**storage_default_folder** | **str** | Default folder to place files | [optional] 
**basemaps** | **object** |  | [optional] 
**mapbox_key** | **str** |  | [optional] 
**module_bar** | **object** |  | [optional] 
**project_descriptor** | **str** |  | [optional] 
**default_language** | **str** |  | [optional] 
**custom_aspect_ratios** | **object** |  | [optional] 
**public_favicon** | **OneOfSettingsPublicFavicon** | $t:field_options.directus_settings.project_favicon_note | [optional] 
**default_appearance** | **str** |  | [optional] 
**default_theme_light** | **str** |  | [optional] 
**theme_light_overrides** | **object** |  | [optional] 
**default_theme_dark** | **str** |  | [optional] 
**theme_dark_overrides** | **object** |  | [optional] 
**report_error_url** | **str** |  | [optional] 
**report_bug_url** | **str** |  | [optional] 
**report_feature_url** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

