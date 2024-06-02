# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPlaylistsController(BaseTestCase):
    """PlaylistsController integration test stubs"""

    def test_playlists_get(self):
        """Test case for playlists_get

        Получить все плейлисты
        """
        response = self.client.open(
            '/playlists',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_playlist_id_delete(self):
        """Test case for playlists_playlist_id_delete

        Удалить плейлист по ID
        """
        response = self.client.open(
            '/playlists/{playlistId}'.format(playlist_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_playlist_id_get(self):
        """Test case for playlists_playlist_id_get

        Получить плейлист по ID
        """
        response = self.client.open(
            '/playlists/{playlistId}'.format(playlist_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_playlist_id_put(self):
        """Test case for playlists_playlist_id_put

        Обновить плейлист по ID
        """
        response = self.client.open(
            '/playlists/{playlistId}'.format(playlist_id=56),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_playlist_id_tracks_get(self):
        """Test case for playlists_playlist_id_tracks_get

        Получить все треки в плейлисте
        """
        response = self.client.open(
            '/playlists/{playlistId}/tracks'.format(playlist_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_playlist_id_tracks_post(self):
        """Test case for playlists_playlist_id_tracks_post

        Добавить новый трек в плейлист
        """
        response = self.client.open(
            '/playlists/{playlistId}/tracks'.format(playlist_id=56),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_playlist_id_tracks_track_id_delete(self):
        """Test case for playlists_playlist_id_tracks_track_id_delete

        Удалить трек по ID
        """
        response = self.client.open(
            '/playlists/{playlistId}/tracks/{trackId}'.format(playlist_id=56, track_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_playlist_id_tracks_track_id_get(self):
        """Test case for playlists_playlist_id_tracks_track_id_get

        Получить трек по ID
        """
        response = self.client.open(
            '/playlists/{playlistId}/tracks/{trackId}'.format(playlist_id=56, track_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_playlist_id_tracks_track_id_put(self):
        """Test case for playlists_playlist_id_tracks_track_id_put

        Обновить трек по ID
        """
        response = self.client.open(
            '/playlists/{playlistId}/tracks/{trackId}'.format(playlist_id=56, track_id=56),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playlists_post(self):
        """Test case for playlists_post

        Создать новый плейлист
        """
        response = self.client.open(
            '/playlists',
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
