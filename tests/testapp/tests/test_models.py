from django.test import TestCase
from testapp.models import FileNodeTestModel
from file_manager_mptt.utils.node_types import FILE, FOLDER
from django.contrib.auth  import  get_user_model 
from .factory import test_folder, test_sub_folder, test_file
UserModel = get_user_model()

class FileMpttModelTest(TestCase):

    def setUp(self):
        self.test_user_1 = UserModel.objects.create(username="admin_1")
        self.test_user_2 = UserModel.objects.create(username="admin_2")
        self.folder_node = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1)
        self.sub_folder_node = FileNodeTestModel.objects.create(**test_sub_folder, parent=self.folder_node, owner=self.test_user_1)
        self.file_node = FileNodeTestModel.objects.create(**test_file, parent=self.folder_node, owner=self.test_user_2)


    def test_utils_node_type(self):
        self.assertEqual(FILE, 200)
        self.assertEqual(FOLDER, 100)


    def test_field_match_in_model_file_node(self):
        self.assertEqual(self.file_node.label, 'File')
        self.assertEqual(self.file_node.name, 'test_file_node')
        self.assertEqual(self.file_node.type, FILE)
        

    def test_field_match_in_model_folder_node(self):
        self.assertEqual(self.folder_node.label, 'Folder')
        self.assertEqual(self.folder_node.name, 'test_folder_node')
        self.assertEqual(self.folder_node.type, FOLDER)
        

    def test_relationship_folder_file(self):
        self.assertEqual(self.folder_node.children.filter(type=FILE).all()[0], self.file_node)
        self.assertEqual(self.file_node.parent, self.folder_node)
    

    def test_relationship_sub_folder_folder(self):
        self.assertEqual(self.folder_node.children.filter(type=FOLDER).all()[0], self.sub_folder_node)
        self.assertEqual(self.sub_folder_node.parent, self.folder_node)
    

    def test_relationship_folder_children(self):
        self.assertEqual(self.folder_node.children.all().count(), 2)
