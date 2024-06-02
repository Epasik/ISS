# swagger_client.PlaylistsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlists_get**](PlaylistsApi.md#playlists_get) | **GET** /playlists | Получить все плейлисты
[**playlists_playlist_id_delete**](PlaylistsApi.md#playlists_playlist_id_delete) | **DELETE** /playlists/{playlistId} | Удалить плейлист по ID
[**playlists_playlist_id_get**](PlaylistsApi.md#playlists_playlist_id_get) | **GET** /playlists/{playlistId} | Получить плейлист по ID
[**playlists_playlist_id_put**](PlaylistsApi.md#playlists_playlist_id_put) | **PUT** /playlists/{playlistId} | Обновить плейлист по ID
[**playlists_playlist_id_tracks_get**](PlaylistsApi.md#playlists_playlist_id_tracks_get) | **GET** /playlists/{playlistId}/tracks | Получить все треки в плейлисте
[**playlists_playlist_id_tracks_post**](PlaylistsApi.md#playlists_playlist_id_tracks_post) | **POST** /playlists/{playlistId}/tracks | Добавить новый трек в плейлист
[**playlists_playlist_id_tracks_track_id_delete**](PlaylistsApi.md#playlists_playlist_id_tracks_track_id_delete) | **DELETE** /playlists/{playlistId}/tracks/{trackId} | Удалить трек по ID
[**playlists_playlist_id_tracks_track_id_get**](PlaylistsApi.md#playlists_playlist_id_tracks_track_id_get) | **GET** /playlists/{playlistId}/tracks/{trackId} | Получить трек по ID
[**playlists_playlist_id_tracks_track_id_put**](PlaylistsApi.md#playlists_playlist_id_tracks_track_id_put) | **PUT** /playlists/{playlistId}/tracks/{trackId} | Обновить трек по ID
[**playlists_post**](PlaylistsApi.md#playlists_post) | **POST** /playlists | Создать новый плейлист

# **playlists_get**
> playlists_get()

Получить все плейлисты

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()

try:
    # Получить все плейлисты
    api_instance.playlists_get()
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_playlist_id_delete**
> playlists_playlist_id_delete(playlist_id)

Удалить плейлист по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()
playlist_id = 56 # int | ID of the playlist

try:
    # Удалить плейлист по ID
    api_instance.playlists_playlist_id_delete(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| ID of the playlist | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_playlist_id_get**
> playlists_playlist_id_get(playlist_id)

Получить плейлист по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()
playlist_id = 56 # int | ID of the playlist

try:
    # Получить плейлист по ID
    api_instance.playlists_playlist_id_get(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| ID of the playlist | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_playlist_id_put**
> playlists_playlist_id_put(playlist_id)

Обновить плейлист по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()
playlist_id = 56 # int | ID of the playlist

try:
    # Обновить плейлист по ID
    api_instance.playlists_playlist_id_put(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| ID of the playlist | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_playlist_id_tracks_get**
> playlists_playlist_id_tracks_get(playlist_id)

Получить все треки в плейлисте

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()
playlist_id = 56 # int | ID of the playlist

try:
    # Получить все треки в плейлисте
    api_instance.playlists_playlist_id_tracks_get(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| ID of the playlist | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_playlist_id_tracks_post**
> playlists_playlist_id_tracks_post(playlist_id)

Добавить новый трек в плейлист

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()
playlist_id = 56 # int | ID of the playlist

try:
    # Добавить новый трек в плейлист
    api_instance.playlists_playlist_id_tracks_post(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| ID of the playlist | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_playlist_id_tracks_track_id_delete**
> playlists_playlist_id_tracks_track_id_delete(playlist_id, track_id)

Удалить трек по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()
playlist_id = 56 # int | ID of the playlist
track_id = 56 # int | ID of the track

try:
    # Удалить трек по ID
    api_instance.playlists_playlist_id_tracks_track_id_delete(playlist_id, track_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_track_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| ID of the playlist | 
 **track_id** | **int**| ID of the track | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_playlist_id_tracks_track_id_get**
> playlists_playlist_id_tracks_track_id_get(playlist_id, track_id)

Получить трек по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()
playlist_id = 56 # int | ID of the playlist
track_id = 56 # int | ID of the track

try:
    # Получить трек по ID
    api_instance.playlists_playlist_id_tracks_track_id_get(playlist_id, track_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_track_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| ID of the playlist | 
 **track_id** | **int**| ID of the track | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_playlist_id_tracks_track_id_put**
> playlists_playlist_id_tracks_track_id_put(playlist_id, track_id)

Обновить трек по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()
playlist_id = 56 # int | ID of the playlist
track_id = 56 # int | ID of the track

try:
    # Обновить трек по ID
    api_instance.playlists_playlist_id_tracks_track_id_put(playlist_id, track_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_track_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| ID of the playlist | 
 **track_id** | **int**| ID of the track | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_post**
> playlists_post()

Создать новый плейлист

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlaylistsApi()

try:
    # Создать новый плейлист
    api_instance.playlists_post()
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

