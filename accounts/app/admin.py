from import_export import resources
from ..models import MyUser

class UserResource(resources.ModelResource):

    class Meta:
        model = MyUser
        fields = ('username', 'birthday', 'rand_int',)