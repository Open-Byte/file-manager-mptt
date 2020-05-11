from django.test import TestCase
from testapp.models import FileNodeTestModel
from django.contrib.auth  import  get_user_model 
from .factory import test_folder, test_sub_folder, test_file
from file_manager_mptt.exceptions.file_node_exception import FileNodeException
from file_manager_mptt.exceptions.errors import Errors
UserModel = get_user_model()

class FileMpttModelTest(TestCase):

    def setUp(self):
        self.test_user_1 = UserModel.objects.create(username="admin_1")
        self.test_user_2 = UserModel.objects.create(username="admin_2")
        self.folder_node = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1)
        self.sub_folder_node = FileNodeTestModel.objects.create(**test_sub_folder, parent=self.folder_node, owner=self.test_user_1)
        self.file_node = FileNodeTestModel.objects.create(**test_file, parent=self.folder_node, owner=self.test_user_2)


    def  test_save_folder_into_file_exception_message(self):
        
        with self.assertRaisesMessage(FileNodeException, Errors._FILE_CANNOT_HAVE_CHILDREN):
            file_node_test = FileNodeTestModel.objects.create(
                **test_file, owner=self.test_user_1, parent=self.file_node
            )
    
    
    def  test_update_folder_into_file_exception_message(self):
        
        with self.assertRaisesMessage(FileNodeException, Errors._FILE_CANNOT_HAVE_CHILDREN):
            file_node_test = FileNodeTestModel.objects.create(
                **test_file, owner=self.test_user_1
            )
            file_node_test.parent = self.file_node
            file_node_test.save()