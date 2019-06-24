#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ykdl.util.html import get_content
from ykdl.util.match import match1, matchall

import json

from .acbase import AcBase


class AcVideo(AcBase):

    name = u'ACfun 弹幕视频网'

    def get_page_info(self, html):
        pageInfo = json.loads(match1(html, u'(?:pageInfo|videoInfo) = ({.+?})</script>'))
        videoList = pageInfo['videoList']
        videoInfo = pageInfo.get('currentVideoInfo') or videoList[pageInfo['P']]
        title = pageInfo['title']
        sub_title = videoInfo['title']
        artist = pageInfo.get('username') or pageInfo['name']
        sourceVid = videoInfo['id']
        if sub_title not in ('noTitle', 'Part1') or len(videoList) > 1:
            title = u'{} - {}'.format(title, sub_title)

        return title, artist, sourceVid

    def get_path_list(self):
        html = get_content(self.url)
        videos = matchall(html, ['href="(/v/[a-zA-Z0-9_]+)" title="'])
        return videos

site = AcVideo()