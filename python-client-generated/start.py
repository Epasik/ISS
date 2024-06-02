from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
#api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
configuration = swagger_client.Configuration()
configuration.host = '192.168.1.102:8080'
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.PlaylistsApi(api_client=api_client)

# body = swagger_client.PlaylistsApi()
#
# try:
#     # Получить все плейлисты
#     resp = api_instance.playlists_get(body)
#
# except ApiException as e:
#     print("Exception when calling PlaylistsApi->playlists_get: %s\n" % e)

# create an instance of the API class
#api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 51 # int | ID of the playlist

try:
    # Удалить плейлист по ID
    resp = api_instance.playlists_playlist_id_delete(playlist_id)
    pprint(resp)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_delete: %s\n" % e)

# create an instance of the API class

playlist_id = 56 # int | ID of the playlist

try:
    # Получить плейлист по ID
    api_instance.playlists_playlist_id_get(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_get: %s\n" % e)

# create an instance of the API class

playlist_id = 56 # int | ID of the playlist

try:
    # Обновить плейлист по ID
    api_instance.playlists_playlist_id_put(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_put: %s\n" % e)

# create an instance of the API class

playlist_id = 56 # int | ID of the playlist

try:
    # Получить все треки в плейлисте
    api_instance.playlists_playlist_id_tracks_get(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_get: %s\n" % e)

# create an instance of the API class

playlist_id = 56 # int | ID of the playlist

try:
    # Добавить новый трек в плейлист
    api_instance.playlists_playlist_id_tracks_post(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_post: %s\n" % e)

# create an instance of the API class

playlist_id = 56 # int | ID of the playlist
track_id = 56 # int | ID of the track

try:
    # Удалить трек по ID
    api_instance.playlists_playlist_id_tracks_track_id_delete(playlist_id, track_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_track_id_delete: %s\n" % e)

# create an instance of the API class

playlist_id = 56 # int | ID of the playlist
track_id = 56 # int | ID of the track

try:
    # Получить трек по ID
    api_instance.playlists_playlist_id_tracks_track_id_get(playlist_id, track_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_track_id_get: %s\n" % e)

# create an instance of the API class

playlist_id = 56 # int | ID of the playlist
track_id = 56 # int | ID of the track

try:
    # Обновить трек по ID
    api_instance.playlists_playlist_id_tracks_track_id_put(playlist_id, track_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_playlist_id_tracks_track_id_put: %s\n" % e)

# create an instance of the API class


try:
    # Создать новый плейлист
    api_instance.playlists_post()
except ApiException as e:
    print("Exception when calling PlaylistsApi->playlists_post: %s\n" % e)