from rest_framework.permissions import BasePermission


class GenrePermissionClass(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTION', 'HEAD']:
            return request.user.has_perm('genres.view_genre')

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE': 
            return request.user.has_perm('genres.delete_genre')
        
        return False
    