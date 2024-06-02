import logging

import connexion
import six

from swagger_server import util

playlist_count = 0


def playlists_get():  # noqa: E501
    """Получить все плейлисты

     # noqa: E501


    :rtype: None
    """

    global playlist_count
    return playlist_count


def playlists_playlist_id_delete(playlist_id):  # noqa: E501
    """Удалить плейлист по ID

     # noqa: E501

    :param playlist_id: ID of the playlist
    :type playlist_id: int

    :rtype: None
    """
    #return 'do some magic!'
    global playlist_count
    # Ваша логика удаления плейлиста по ID здесь
    # Например, удаление записи из базы данных
    playlist_count -= 1
    return 'Playlist deleted successfully', 204


def playlists_playlist_id_get(playlist_id):  # noqa: E501
    """Получить плейлист по ID

     # noqa: E501

    :param playlist_id: ID of the playlist
    :type playlist_id: int

    :rtype: None
    """
    return 'do some magic!'


def playlists_playlist_id_put(playlist_id):  # noqa: E501
    """Обновить плейлист по ID

     # noqa: E501

    :param playlist_id: ID of the playlist
    :type playlist_id: int

    :rtype: None
    """
    return 'do some magic!'


def playlists_playlist_id_tracks_get(playlist_id):  # noqa: E501
    """Получить все треки в плейлисте

     # noqa: E501

    :param playlist_id: ID of the playlist
    :type playlist_id: int

    :rtype: None
    """
    return 'do some magic!'


def playlists_playlist_id_tracks_post(playlist_id):  # noqa: E501
    """Добавить новый трек в плейлист

     # noqa: E501

    :param playlist_id: ID of the playlist
    :type playlist_id: int

    :rtype: None
    """
    return 'do some magic!'


def playlists_playlist_id_tracks_track_id_delete(playlist_id, track_id):  # noqa: E501
    """Удалить трек по ID

     # noqa: E501

    :param playlist_id: ID of the playlist
    :type playlist_id: int
    :param track_id: ID of the track
    :type track_id: int

    :rtype: None
    """
    return 'do some magic!'


def playlists_playlist_id_tracks_track_id_get(playlist_id, track_id):  # noqa: E501
    """Получить трек по ID

     # noqa: E501

    :param playlist_id: ID of the playlist
    :type playlist_id: int
    :param track_id: ID of the track
    :type track_id: int

    :rtype: None
    """
    return 'do some magic!'


def playlists_playlist_id_tracks_track_id_put(playlist_id, track_id):  # noqa: E501
    """Обновить трек по ID

     # noqa: E501

    :param playlist_id: ID of the playlist
    :type playlist_id: int
    :param track_id: ID of the track
    :type track_id: int

    :rtype: None
    """
    return 'do some magic!'


def playlists_post():  # noqa: E501
    """Создать новый плейлист

     # noqa: E501


    :rtype: None
    """
    # return 'do some magic!'`1
    logging.info("Added new playlist")
    global playlist_count
    # Ваша логика создания плейлиста здесь
    # Например, создание записи в базе данных
    playlist_count += 1
    return 'Playlist created successfully', 201
