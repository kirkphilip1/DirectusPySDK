# coding: utf-8

# flake8: noqa
"""
    Dynamic API Specification

    This is a dynamically generated API specification for all endpoints existing on the current project.  # noqa: E501

    OpenAPI spec version: 10.10.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.activity import Activity
from swagger_client.models.activity_comment_body import ActivityCommentBody
from swagger_client.models.any_offlows_body1_data import AnyOfflowsBody1Data
from swagger_client.models.any_ofoperations_body1_data import AnyOfoperationsBody1Data
from swagger_client.models.any_ofversions_body1_data import AnyOfversionsBody1Data
from swagger_client.models.auth_login_body import AuthLoginBody
from swagger_client.models.auth_logout_body import AuthLogoutBody
from swagger_client.models.auth_refresh_body import AuthRefreshBody
from swagger_client.models.bundle_name_body import BundleNameBody
from swagger_client.models.collection_id_body import CollectionIdBody
from swagger_client.models.collections import Collections
from swagger_client.models.collections_body import CollectionsBody
from swagger_client.models.collections_id_body import CollectionsIdBody
from swagger_client.models.collectionsid_meta import CollectionsidMeta
from swagger_client.models.comment_id_body import CommentIdBody
from swagger_client.models.diff import Diff
from swagger_client.models.diff_diff import DiffDiff
from swagger_client.models.diff_diff_collections import DiffDiffCollections
from swagger_client.models.diff_diff_fields import DiffDiffFields
from swagger_client.models.diff_diff_relations import DiffDiffRelations
from swagger_client.models.export_collection_body import ExportCollectionBody
from swagger_client.models.extensions import Extensions
from swagger_client.models.extensions_name_body import ExtensionsNameBody
from swagger_client.models.extensionsname_meta import ExtensionsnameMeta
from swagger_client.models.fields import Fields
from swagger_client.models.fields_collection_body import FieldsCollectionBody
from swagger_client.models.fieldscollection_meta import FieldscollectionMeta
from swagger_client.models.fieldscollection_schema import FieldscollectionSchema
from swagger_client.models.files import Files
from swagger_client.models.files_body import FilesBody
from swagger_client.models.files_body1 import FilesBody1
from swagger_client.models.files_id_body import FilesIdBody
from swagger_client.models.files_id_body1 import FilesIdBody1
from swagger_client.models.flows import Flows
from swagger_client.models.flows_body import FlowsBody
from swagger_client.models.flows_body1 import FlowsBody1
from swagger_client.models.flows_id_body import FlowsIdBody
from swagger_client.models.folders import Folders
from swagger_client.models.folders_body import FoldersBody
from swagger_client.models.folders_body1 import FoldersBody1
from swagger_client.models.folders_id_body import FoldersIdBody
from swagger_client.models.hash_generate_body import HashGenerateBody
from swagger_client.models.hash_verify_body import HashVerifyBody
from swagger_client.models.id import Id
from swagger_client.models.id1 import Id1
from swagger_client.models.id10 import Id10
from swagger_client.models.id11 import Id11
from swagger_client.models.id12 import Id12
from swagger_client.models.id13 import Id13
from swagger_client.models.id14 import Id14
from swagger_client.models.id15 import Id15
from swagger_client.models.id16 import Id16
from swagger_client.models.id17 import Id17
from swagger_client.models.id18 import Id18
from swagger_client.models.id19 import Id19
from swagger_client.models.id2 import Id2
from swagger_client.models.id20 import Id20
from swagger_client.models.id3 import Id3
from swagger_client.models.id4 import Id4
from swagger_client.models.id5 import Id5
from swagger_client.models.id6 import Id6
from swagger_client.models.id7 import Id7
from swagger_client.models.id8 import Id8
from swagger_client.models.id9 import Id9
from swagger_client.models.id_promote_body import IdPromoteBody
from swagger_client.models.import_collection_body import ImportCollectionBody
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response20010 import InlineResponse20010
from swagger_client.models.inline_response20011 import InlineResponse20011
from swagger_client.models.inline_response20012 import InlineResponse20012
from swagger_client.models.inline_response20013 import InlineResponse20013
from swagger_client.models.inline_response20014 import InlineResponse20014
from swagger_client.models.inline_response20015 import InlineResponse20015
from swagger_client.models.inline_response20016 import InlineResponse20016
from swagger_client.models.inline_response20017 import InlineResponse20017
from swagger_client.models.inline_response20018 import InlineResponse20018
from swagger_client.models.inline_response20019 import InlineResponse20019
from swagger_client.models.inline_response2001_data import InlineResponse2001Data
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response20020 import InlineResponse20020
from swagger_client.models.inline_response20021 import InlineResponse20021
from swagger_client.models.inline_response20022 import InlineResponse20022
from swagger_client.models.inline_response20023 import InlineResponse20023
from swagger_client.models.inline_response20024 import InlineResponse20024
from swagger_client.models.inline_response20025 import InlineResponse20025
from swagger_client.models.inline_response20026 import InlineResponse20026
from swagger_client.models.inline_response20027 import InlineResponse20027
from swagger_client.models.inline_response20028 import InlineResponse20028
from swagger_client.models.inline_response20029 import InlineResponse20029
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inline_response20030 import InlineResponse20030
from swagger_client.models.inline_response20031 import InlineResponse20031
from swagger_client.models.inline_response20032 import InlineResponse20032
from swagger_client.models.inline_response20033 import InlineResponse20033
from swagger_client.models.inline_response20034 import InlineResponse20034
from swagger_client.models.inline_response20035 import InlineResponse20035
from swagger_client.models.inline_response20036 import InlineResponse20036
from swagger_client.models.inline_response20037 import InlineResponse20037
from swagger_client.models.inline_response20038 import InlineResponse20038
from swagger_client.models.inline_response20039 import InlineResponse20039
from swagger_client.models.inline_response2003_data import InlineResponse2003Data
from swagger_client.models.inline_response2004 import InlineResponse2004
from swagger_client.models.inline_response20040 import InlineResponse20040
from swagger_client.models.inline_response20041 import InlineResponse20041
from swagger_client.models.inline_response20042 import InlineResponse20042
from swagger_client.models.inline_response20043 import InlineResponse20043
from swagger_client.models.inline_response20044 import InlineResponse20044
from swagger_client.models.inline_response20045 import InlineResponse20045
from swagger_client.models.inline_response20046 import InlineResponse20046
from swagger_client.models.inline_response20047 import InlineResponse20047
from swagger_client.models.inline_response20048 import InlineResponse20048
from swagger_client.models.inline_response20049 import InlineResponse20049
from swagger_client.models.inline_response2005 import InlineResponse2005
from swagger_client.models.inline_response20050 import InlineResponse20050
from swagger_client.models.inline_response20051 import InlineResponse20051
from swagger_client.models.inline_response20052 import InlineResponse20052
from swagger_client.models.inline_response20053 import InlineResponse20053
from swagger_client.models.inline_response20054 import InlineResponse20054
from swagger_client.models.inline_response20055 import InlineResponse20055
from swagger_client.models.inline_response20056 import InlineResponse20056
from swagger_client.models.inline_response20057 import InlineResponse20057
from swagger_client.models.inline_response20058 import InlineResponse20058
from swagger_client.models.inline_response20059 import InlineResponse20059
from swagger_client.models.inline_response2006 import InlineResponse2006
from swagger_client.models.inline_response20060 import InlineResponse20060
from swagger_client.models.inline_response20061 import InlineResponse20061
from swagger_client.models.inline_response20062 import InlineResponse20062
from swagger_client.models.inline_response20063 import InlineResponse20063
from swagger_client.models.inline_response20064 import InlineResponse20064
from swagger_client.models.inline_response20065 import InlineResponse20065
from swagger_client.models.inline_response20066 import InlineResponse20066
from swagger_client.models.inline_response20067 import InlineResponse20067
from swagger_client.models.inline_response20068 import InlineResponse20068
from swagger_client.models.inline_response20069 import InlineResponse20069
from swagger_client.models.inline_response2007 import InlineResponse2007
from swagger_client.models.inline_response20070 import InlineResponse20070
from swagger_client.models.inline_response2008 import InlineResponse2008
from swagger_client.models.inline_response2009 import InlineResponse2009
from swagger_client.models.inline_response200_data import InlineResponse200Data
from swagger_client.models.inline_response404 import InlineResponse404
from swagger_client.models.inline_response404_error import InlineResponse404Error
from swagger_client.models.invite_accept_body import InviteAcceptBody
from swagger_client.models.items_db_version import ItemsDBVersion
from swagger_client.models.items_db_version_body import ItemsDbVersionBody
from swagger_client.models.items_db_version_body1 import ItemsDbVersionBody1
from swagger_client.models.items_logs import ItemsLogs
from swagger_client.models.items_logs_body import ItemsLogsBody
from swagger_client.models.items_logs_body1 import ItemsLogsBody1
from swagger_client.models.items_purchased_songs import ItemsPurchasedSongs
from swagger_client.models.items_purchased_songs_body import ItemsPurchasedSongsBody
from swagger_client.models.items_purchased_songs_body1 import ItemsPurchasedSongsBody1
from swagger_client.models.items_scrape_config import ItemsScrapeConfig
from swagger_client.models.items_scrape_config_body import ItemsScrapeConfigBody
from swagger_client.models.items_scrape_config_body1 import ItemsScrapeConfigBody1
from swagger_client.models.items_scrape_hashes import ItemsScrapeHashes
from swagger_client.models.items_scrape_hashes_body import ItemsScrapeHashesBody
from swagger_client.models.items_scrape_hashes_body1 import ItemsScrapeHashesBody1
from swagger_client.models.items_session_data import ItemsSessionData
from swagger_client.models.items_session_data_body import ItemsSessionDataBody
from swagger_client.models.items_session_data_body1 import ItemsSessionDataBody1
from swagger_client.models.items_sources import ItemsSources
from swagger_client.models.items_sources_body import ItemsSourcesBody
from swagger_client.models.items_sources_body1 import ItemsSourcesBody1
from swagger_client.models.one_of_activity_collection import OneOfActivityCollection
from swagger_client.models.one_of_activity_ip import OneOfActivityIp
from swagger_client.models.one_of_activity_revisions_items import OneOfActivityRevisionsItems
from swagger_client.models.one_of_activity_user import OneOfActivityUser
from swagger_client.models.one_of_collections_group import OneOfCollectionsGroup
from swagger_client.models.one_of_fields_group import OneOfFieldsGroup
from swagger_client.models.one_of_files_folder import OneOfFilesFolder
from swagger_client.models.one_of_files_modified_by import OneOfFilesModifiedBy
from swagger_client.models.one_of_files_uploaded_by import OneOfFilesUploadedBy
from swagger_client.models.one_of_flows_operation import OneOfFlowsOperation
from swagger_client.models.one_of_flows_operations_items import OneOfFlowsOperationsItems
from swagger_client.models.one_of_flows_user_created import OneOfFlowsUserCreated
from swagger_client.models.one_of_folders_parent import OneOfFoldersParent
from swagger_client.models.one_of_items_purchased_songs_source_id import OneOfItemsPurchasedSongsSourceId
from swagger_client.models.one_of_items_session_data_source_id import OneOfItemsSessionDataSourceId
from swagger_client.models.one_of_operations_flow import OneOfOperationsFlow
from swagger_client.models.one_of_operations_reject import OneOfOperationsReject
from swagger_client.models.one_of_operations_resolve import OneOfOperationsResolve
from swagger_client.models.one_of_operations_user_created import OneOfOperationsUserCreated
from swagger_client.models.one_of_presets_collection import OneOfPresetsCollection
from swagger_client.models.one_of_presets_role import OneOfPresetsRole
from swagger_client.models.one_of_presets_user import OneOfPresetsUser
from swagger_client.models.one_of_revisions_activity import OneOfRevisionsActivity
from swagger_client.models.one_of_revisions_collection import OneOfRevisionsCollection
from swagger_client.models.one_of_revisions_version import OneOfRevisionsVersion
from swagger_client.models.one_of_roles_users_items import OneOfRolesUsersItems
from swagger_client.models.one_of_settings_public_favicon import OneOfSettingsPublicFavicon
from swagger_client.models.one_of_users_avatar import OneOfUsersAvatar
from swagger_client.models.one_of_users_role import OneOfUsersRole
from swagger_client.models.one_of_versions_collection import OneOfVersionsCollection
from swagger_client.models.one_of_versions_user_created import OneOfVersionsUserCreated
from swagger_client.models.one_of_versions_user_updated import OneOfVersionsUserUpdated
from swagger_client.models.one_of_webhooks_migrated_flow import OneOfWebhooksMigratedFlow
from swagger_client.models.one_offiles_id_body1_folder import OneOffilesIdBody1Folder
from swagger_client.models.one_offiles_id_body_folder import OneOffilesIdBodyFolder
from swagger_client.models.operations import Operations
from swagger_client.models.operations_body import OperationsBody
from swagger_client.models.operations_body1 import OperationsBody1
from swagger_client.models.operations_id_body import OperationsIdBody
from swagger_client.models.password_request_body import PasswordRequestBody
from swagger_client.models.password_reset_body import PasswordResetBody
from swagger_client.models.permissions import Permissions
from swagger_client.models.permissions_body import PermissionsBody
from swagger_client.models.permissions_body1 import PermissionsBody1
from swagger_client.models.permissions_id_body import PermissionsIdBody
from swagger_client.models.presets import Presets
from swagger_client.models.presets_body import PresetsBody
from swagger_client.models.presets_body1 import PresetsBody1
from swagger_client.models.presets_filters import PresetsFilters
from swagger_client.models.presets_id_body import PresetsIdBody
from swagger_client.models.presetsid_filters import PresetsidFilters
from swagger_client.models.query import Query
from swagger_client.models.relations import Relations
from swagger_client.models.relations_body import RelationsBody
from swagger_client.models.relations_id_body import RelationsIdBody
from swagger_client.models.revisions import Revisions
from swagger_client.models.roles import Roles
from swagger_client.models.roles_body import RolesBody
from swagger_client.models.roles_body1 import RolesBody1
from swagger_client.models.roles_id_body import RolesIdBody
from swagger_client.models.schema import Schema
from swagger_client.models.schema_apply_body import SchemaApplyBody
from swagger_client.models.schema_apply_body1 import SchemaApplyBody1
from swagger_client.models.schema_diff_body import SchemaDiffBody
from swagger_client.models.schema_diff_body1 import SchemaDiffBody1
from swagger_client.models.settings import Settings
from swagger_client.models.settings_arguments import SettingsArguments
from swagger_client.models.settings_public_background import SettingsPublicBackground
from swagger_client.models.settings_storage_asset_presets import SettingsStorageAssetPresets
from swagger_client.models.settings_transforms import SettingsTransforms
from swagger_client.models.sort_collection_body import SortCollectionBody
from swagger_client.models.track_page_body import TrackPageBody
from swagger_client.models.users import Users
from swagger_client.models.users_body import UsersBody
from swagger_client.models.users_invite_body import UsersInviteBody
from swagger_client.models.versions import Versions
from swagger_client.models.versions_body import VersionsBody
from swagger_client.models.versions_body1 import VersionsBody1
from swagger_client.models.versions_id_body import VersionsIdBody
from swagger_client.models.webhooks import Webhooks
from swagger_client.models.webhooks_body import WebhooksBody
from swagger_client.models.webhooks_body1 import WebhooksBody1
from swagger_client.models.webhooks_id_body import WebhooksIdBody
from swagger_client.models.x_metadata import XMetadata
