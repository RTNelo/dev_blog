#!/usr/local/bin/python
#conding: utf-8
#author: He.Kang@dev-engine.com


from Handler.home import HomeHandler
from Handler.dback import DbackHandler
from Handler.wback import WbackHandler
from Handler.diary import DiaryListHandler,\
                          DiaryDetailHandler,\
                          DiaryLoadHandler, DiaryRssHandler
from Handler.admin import AdminHandler, LoginHandler, LogoutHandler, AdminDiaryListHandler,\
                          AdminSettingsHandler, AdminCommentHandler,DiaryAddHandler,\
                          DiaryDelHandler, DiaryUpdateHandler, DiarySetDateHandler
                              
from Handler.comment import CommentAddHandler, CommentDelHandler,\
                            CommentReplyHandler

urls = [
    (r'/', HomeHandler),
    (r'/dback', DbackHandler),
    (r'/wback', WbackHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/feed', DiaryRssHandler),

    (r'/diary/add', DiaryAddHandler),
    (r'/diary/load', DiaryLoadHandler),
    (r'/diary/detail/([0-9]+)', DiaryDetailHandler),
    (r'/diary/list/([0-9]+)', DiaryListHandler),

    (r'/admin', AdminHandler),
    (r'/admin/all-post/([0-9]+)', AdminDiaryListHandler),
    (r'/admin/settings', AdminSettingsHandler),
    (r'/admin/diary/edit/([0-9]+)', DiaryUpdateHandler),
    (r'/admin/diary/del/([0-9]+)', DiaryDelHandler),
    (r'/admin/diary/set-date', DiarySetDateHandler),
    (r'/admin/comments/all-comment/([0-9]+)', AdminCommentHandler),
    (r'/admin/comment/del', CommentDelHandler),
    (r'/admin/comment/reply', CommentReplyHandler),

    (r'/comment/add', CommentAddHandler),
]
