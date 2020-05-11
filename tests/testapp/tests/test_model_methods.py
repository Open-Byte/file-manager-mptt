from django.test import TestCase
from testapp.models import FileNodeTestModel
from file_manager_mptt.utils.node_types import FILE, FOLDER
from django.contrib.auth  import  get_user_model 
from .factory import test_folder, test_sub_folder, test_file
from random import choices
UserModel = get_user_model()

class FileMpttModelTest(TestCase):

    ## SetUp Zone
    def setUp(self):
        self.test_user_1 = UserModel.objects.create(username="admin_1")
        

    def _setup_files_or_folder_for_folder(self, type=False, quantity=10):
        type_list = [FOLDER, FILE] if not type else [type]
        folder_files_list = [
            FileNodeTestModel.objects.create(**{
                    "label": f"{index}", 
                    "name": f"{node_type}-{index}",
                    "type": node_type
                    },
                    owner=self.test_user_1
            ) for node_type, index in zip(choices(type_list, k=quantity), range(quantity))
        ]

        return folder_files_list

    def _add_children_to_folder(self, folder, children_type=False):

        file_or_folder_list = self._setup_files_or_folder_for_folder(type=children_type)
        for file in file_or_folder_list: 
            file.parent = folder
            file.save()

        return file_or_folder_list

    ## Testing Zone
    def test_get_file_from_folder(self):

        folder_node = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1)
        file_list = self._add_children_to_folder(folder_node, FILE)
        children = folder_node.get_children(type=FILE).order_by('created_date')

        self.assertEqual(len(file_list), len(children))

        for child, file in zip(children, file_list):
            self.assertEqual(child, file)
    

    def test_get_sub_folders_from_folder(self):

        folder_node = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1)
        folder_list = self._add_children_to_folder(folder_node, FOLDER)
        children = folder_node.get_children(type=FOLDER).order_by('created_date')

        self.assertEqual(len(folder_list), len(children))

        for child, folder in zip(children, folder_list):
            self.assertEqual(child, folder)


    def test_get_children_from_folder(self):

        folder_node = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1)
        folder_file_list = self._add_children_to_folder(folder_node)
        children = folder_node.get_children().order_by('created_date')

        self.assertEqual(len(folder_file_list), len(children))

        for child, folder_file in zip(children, folder_file_list):
            self.assertEqual(child, folder_file)
    

    def test_slug_generator_create_record(self):

        folder_node = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1)
        folder_node_slug_duplicate = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1, slug=folder_node.slug)

        self.assertNotEqual(folder_node.slug, folder_node_slug_duplicate.slug)


    def test_duplicated_slug_update_record_exception(self):

        with self.assertRaises(Exception):
            folder_node = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1)
            folder_node_slug_duplicate = FileNodeTestModel.objects.create(**test_folder, owner=self.test_user_1)
            folder_node_slug_duplicate.slug = folder_node.slug
            folder_node_slug_duplicate.save()

        
        

        
        
    