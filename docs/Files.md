# Files

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the file. | [optional] 
**storage** | **str** | Where the file is stored. Either &#x60;local&#x60; for the local filesystem or the name of the storage adapter (for example &#x60;s3&#x60;). | [optional] 
**filename_disk** | **str** | Name of the file on disk. By default, Directus uses a random hash for the filename. | [optional] 
**filename_download** | **str** | How you want to the file to be named when it&#x27;s being downloaded. | [optional] 
**title** | **str** | Title for the file. Is extracted from the filename on upload, but can be edited by the user. | [optional] 
**type** | **str** | MIME type of the file. | [optional] 
**folder** | **OneOfFilesFolder** | Virtual folder where this file resides in. | [optional] 
**uploaded_by** | **OneOfFilesUploadedBy** | Who uploaded the file. | [optional] 
**uploaded_on** | **datetime** | When the file was uploaded. | [optional] 
**modified_by** | **OneOfFilesModifiedBy** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**charset** | **str** | Character set of the file. | [optional] 
**filesize** | **int** | Size of the file in bytes. | [optional] 
**width** | **int** | Width of the file in pixels. Only applies to images. | [optional] 
**height** | **int** | Height of the file in pixels. Only applies to images. | [optional] 
**duration** | **int** | Duration of the file in seconds. Only applies to audio and video. | [optional] 
**embed** | **str** | Where the file was embedded from. | [optional] 
**description** | **str** | Description for the file. | [optional] 
**location** | **str** | Where the file was created. Is automatically populated based on Exif data for images. | [optional] 
**tags** | **list[str]** | Tags for the file. Is automatically populated based on Exif data for images. | [optional] 
**metadata** | **object** | IPTC, Exif, and ICC metadata extracted from file | [optional] 
**focal_point_x** | **int** |  | [optional] 
**focal_point_y** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

