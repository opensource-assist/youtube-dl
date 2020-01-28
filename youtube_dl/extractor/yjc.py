# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import (
    int_or_none,
    unified_strdate,
)


class JpopsukiIE(InfoExtractor):
    IE_NAME = 'yjc.ir'
    https://www.yjc.ir/fa/news/7226827/
    _VALID_URL = r'https?://(?:www\.)yjc\.ir/fa/news/(?P<id>\S+/.)'

    _TEST = {
        'url': 'https://www.yjc.ir/fa/news/7226827/%D8%A8%D9%87%D8%AA-%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7%DB%8C%DB%8C%E2%80%8C%D9%87%D8%A7-%D8%A7%D8%B2-%D8%B3%D9%82%D9%88%D8%B7-%D9%87%D9%88%D8%A7%D9%BE%DB%8C%D9%85%D8%A7%DB%8C-e-11a-%D9%81%DB%8C%D9%84%D9%85',
        #'md5': '88018c0c1a9b1387940e90ec9e7e198e',
        'info_dict': {
            'id': '7226827',
            'ext': 'mp4',
            'title': '11283514_648.mp4',
            #'thumbnail': '',
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)

        webpage = self._download_webpage(url, video_id)

        video_url = 'https://www.yjc.ir' + self._html_search_regex(
            r'<source href="(.mp4)" type', webpage, 'video url')

        video_title = self._og_search_title(webpage)
        description = self._og_search_description(webpage)
        thumbnail = self._og_search_thumbnail(webpage)
        uploader = self._html_search_regex(
            r'<li>from: <a href="/user/view/user/(.*?)/uid/',
            webpage, 'video uploader', fatal=False)
        uploader_id = self._html_search_regex(
            r'<li>from: <a href="/user/view/user/\S*?/uid/(\d*)',
            webpage, 'video uploader_id', fatal=False)
        upload_date = unified_strdate(self._html_search_regex(
            r'<li>uploaded: (.*?)</li>', webpage, 'video upload_date',
            fatal=False))
        view_count_str = self._html_search_regex(
            r'<li>Hits: ([0-9]+?)</li>', webpage, 'video view_count',
            fatal=False)
        comment_count_str = self._html_search_regex(
            r'<h2>([0-9]+?) comments</h2>', webpage, 'video comment_count',
            fatal=False)

        return {
            'id': video_id,
            'url': video_url,
            'title': video_title,
            'description': description,
            'upload_date': upload_date,
        }
