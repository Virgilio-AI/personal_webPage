from django.contrib import admin
from .models import Blog

# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
# 	readonly_fieds = ('created_at','updated_at')
# 	search_fields = ('name','description')
# 	list_display = ('name','created_at')
# class ArticleAdmin(admin.ModelAdmin):
# 	readonly_fieds = ('user','created_at','updated_at')
# 	search_fields = ('title','content','user__username','categories__name')
# 	list_display = ('title','user','public','created_at')
# 	list_filter = ('public','user__username','categories__name')



# 	def save_model(self,request,obj,form,change):
# 		if not obj.user_id:
# 			obj.user_id = request.user.id
# 		obj.save()



# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Article,ArticleAdmin)
admin.site.register(Blog)



# python manage.py makemigrations
# python manage.py sqlmigrate Blog 0001
# python manage.py migrate




