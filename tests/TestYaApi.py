
from YandexAPI.YaApi import YaUpCreate, TOKEN


class TestYaApi:
    @staticmethod
    def setup() -> None:
        print('SetUp --> Work')

    @staticmethod
    def teardown() -> None:
        print('TearDown --> Work')

    def test_create_folder(self):
        assert YaUpCreate(TOKEN).create_folder('test_folder') == 201

    def test_delete_folder(self):
        assert YaUpCreate(TOKEN).delete_folder('test_folder') == 204
