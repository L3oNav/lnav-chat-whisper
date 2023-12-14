import os
from unittest import TestCase
from unittest.mock import patch
from app.settings import get_settings, Settings

class ModuleTestCase(TestCase):

    def setUp(self):
        os.environ["SECRET_KEY"] = "test-secret-key"
        os.environ["HOST"] = "test-host"
        os.environ["ENVIRONMENT"] = "test-environment"
        os.environ["OBJECT_STORAGE_ACCESS_KEY"] = "test-access-key"
        os.environ["OBJECT_STORAGE_SECRET_KEY"] = "test-secret-key"
        os.environ["OBJECT_STORAGE_ENDPOINT_PUBLIC"] = "test-public-endpoint"
        os.environ["OBJECT_STORAGE_ENDPOINT_PRIVATE"] = "test-private-endpoint"
        os.environ["OBJECT_STORAGE_REGION"] = "test-region"
        os.environ["POSTGRES_USER"] = "test-user"
        os.environ["POSTGRES_PASSWORD"] = "test-password"
        os.environ["POSTGRES_HOST"] = "test-host"
        os.environ["POSTGRES_DB"] = "test-db"

    def tearDown(self):
        del(os.environ["SECRET_KEY"])
        del(os.environ["HOST"])
        del(os.environ["ENVIRONMENT"])
        del(os.environ["OBJECT_STORAGE_ACCESS_KEY"])
        del(os.environ["OBJECT_STORAGE_SECRET_KEY"])
        del(os.environ["OBJECT_STORAGE_ENDPOINT_PUBLIC"])
        del(os.environ["OBJECT_STORAGE_ENDPOINT_PRIVATE"])
        del(os.environ["OBJECT_STORAGE_REGION"])
        del(os.environ["GOOGLE_ID_CLIENT"])
        del(os.environ["GOOGLE_SECRET_CLIENT"])
        del(os.environ["POSTGRES_USER"])
        del(os.environ["POSTGRES_PASSWORD"])
        del(os.environ["POSTGRES_HOST"])
        del(os.environ["POSTGRES_DB"])

    def test_get_settings_returns_valid_instance(self):
        settings = get_settings()
        self.assertIsInstance(settings, Settings)

    def test_app_name_is_set_correctly(self):
        settings = get_settings()
        self.assertEqual(settings.APP_NAME, "talkflow-spliter")

    def test_secret_key_is_set_correctly(self):
        settings = get_settings()
        self.assertEqual(settings.SECRET_KEY, "test-secret-key")

    def test_host_is_set_correctly(self):
        settings = get_settings()
        self.assertEqual(settings.HOST, "test-host")

    def test_environment_default_value_is_development(self):
        with patch.dict("os.environ", clear=True):
            settings = get_settings()
            self.assertEqual(settings.ENVIRONMENT, "development")

    def test_access_token_expire_minutes_is_set_correctly(self):
        settings = get_settings()
        self.assertTrue(isinstance(settings.access_token_expire_minutes, int))
        self.assertGreater(settings.access_token_expire_minutes, 0)

    def test_object_storage_access_key_is_set_correctly(self):
        settings = get_settings()
        self.assertEqual(settings.OBJECT_STORAGE_ACCESS_KEY, "test-access-key")

    def test_object_storage_secret_key_is_set_correctly(self):
        settings = get_settings()
        self.assertEqual(settings.OBJECT_STORAGE_SECRET_KEY, "test-secret-key")

    def test_object_storage_endpoint_public_is_set_correctly(self):
       settings = get_settings()
       self.assertEqual(settings.OBJECT_STORAGE_ENDPOINT_PUBLIC, "test-public-endpoint")

    def test_object_storage_endpoint_private_is_set_correctly(self):
       settings = get_settings()
       self.assertEqual(settings.OBJECT_STORAGE_ENDPOINT_PRIVATE, "test-private-endpoint")

    def test_object_storage_region_is_set_correctly(self):
       settings = get_settings()
       self.assertEqual(settings.OBJECT_STORAGE_REGION, "test-region")

    def test_google_id_client_is_set_correctly(self):
       settings = get_settings()
       self.assertEqual(settings.GOOGLE_ID_CLIENT, "test-id-client")

    def test_google_secret_client_is_set_correctly(self):
       settings = get_settings()
       self.assertEqual(settings.GOOGLE_SECRET_CLIENT, "test-secret-client")

    def test_postgres_user_is_set_correctly(self):
       settings = get_settings()
       self.assertEqual(settings.POSTGRES_USER, "test-user")

    def test_postgres_password_is_set_correctly(self):
        settings = get_settings()
        self.assertEqual(settings.POSTGRES_PASSWORD, "test-password")

    def test_postgres_host_is_set_correctly(self):
        settings = get_settings()
        self.assertEqual(settings.POSTGRES_HOST, "test-host")

    def test_postgres_db_is_set_correctly(self):
        settings = get_settings()
        self.assertEqual(settings.POSTGRES_DB, "test-db")
