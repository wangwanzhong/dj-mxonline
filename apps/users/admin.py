import xadmin

from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin:
    list_display = ('email', 'code', 'send_type', 'send_time')
    search_fields = ('email', 'code', 'send_type')
    list_filter = ('email', 'send_type', 'send_time')


class BannerAdmin:
    list_display = ('title', 'image', 'url', 'index', 'add_time')
    search_fields = ('title', 'image', 'url', 'index', 'add_time')
    list_filter = ('title', 'image', 'url', 'index', 'add_time')


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
