from django.contrib import admin

from Hands2HopeApp.models import ComplaintsTable, FeedbackTable, LoginTable, UserTable

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(ComplaintsTable)
admin.site.register(FeedbackTable)