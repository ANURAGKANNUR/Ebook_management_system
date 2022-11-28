from rest_framework import permissions

class CreatedUseronly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.createdby == request.user

class ReviewUseronly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

            return obj.review_user==request.user




