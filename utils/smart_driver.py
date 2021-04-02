import os

from appium import webdriver
# from behave.tag_matcher import ActiveTagMatcher, setup_active_tag_values

CWD = os.getcwd()

__driver_configs = {}

def driver_setup(host, port, appium_version, automation_name, platform_name, test_name, app_uri, new_command_timeout):
    __driver_configs['host'] = host
    __driver_configs['port'] = port
    __driver_configs['appium_version'] = appium_version
    __driver_configs['automation_name'] = automation_name
    __driver_configs['platform_name'] = platform_name
    __driver_configs['test_name'] = test_name
    __driver_configs['app_uri'] = os.path.abspath(app_uri)
    __driver_configs['new_command_timeout'] = new_command_timeout

def start_driver(context):
    try:
        context.driver = webdriver.Remote(
        command_executor='http://%s:%s/wd/hub' % (__driver_configs.get('host'),__driver_configs.get('port')),
        desired_capabilities={
            'platformName': __driver_configs.get('platform_name'),
            'automationName': __driver_configs.get('automation_name'),
            'app': __driver_configs.get('app_uri'),
            'new_command_timeout': __driver_configs.get('new_command_timeout')
        })

        context.platform = __driver_configs.get('platform_name')
        if  context.platform == 'Android':
            from pages.android.tutorial_page import TutorialPage
            from pages.android.start_page import StartPage
            from pages.android.pin_code_page import PinCodePage
            from pages.android.right_menu_page import RightMenuPage
            from pages.android.permission_alert import PermissionAlert
            from pages.android.configs_page import ConfigsPage
            from pages.android.wallet_info_page import WalletInfoPage
            from pages.android.main_page import MainPage
            from pages.android.wallet_page import WalletPage
            from pages.android.top_up_info_page import TopUpInfoPage
            from pages.android.create_config_page import CreateConfigPage
            from pages.android.add_doc_page import AddDocPage
            from pages.android.my_docs_page import MyDocsPage
            from pages.android.choose_domain_page import ChooseDomainPage
            from pages.android.add_doc_form_page import AddDocFormPage
            from pages.android.field_page import FieldPage
            from pages.android.camera_page import CameraPage
            from pages.android.request_in_progress_page import RequestInProgress
            from pages.android.chrome_start_page import ChromeStartPage
            from pages.android.verification_type_page import VerificationTypePage
            from pages.android.verification_details_page import VerificationDetailsPage
            from utils.base_page import BasePage
        else:
            raise RuntimeError('Unrecognized platform: {}'.format(context.platform))
        context.tutorial_page = TutorialPage(context.driver)
        context.start_page = StartPage(context.driver)
        context.pin_code_page = PinCodePage(context.driver)
        context.right_menu_page = RightMenuPage(context.driver)
        context.permission_alert = PermissionAlert(context.driver)
        context.configs_page = ConfigsPage(context.driver)
        context.base_page = BasePage(context.driver)
        context.wallet_info_page = WalletInfoPage(context.driver)
        context.main_page = MainPage(context.driver)
        context.wallet_page = WalletPage(context.driver)
        context.top_up_info_page = TopUpInfoPage(context.driver)
        context.create_config_page = CreateConfigPage(context.driver)
        context.add_doc_page = AddDocPage(context.driver)
        context.my_docs_page = MyDocsPage(context.driver)
        context.choose_domain_page = ChooseDomainPage(context.driver)
        context.add_doc_form_page = AddDocFormPage(context.driver)
        context.field_page = FieldPage(context.driver)
        context.camera_page = CameraPage(context.driver)
        context.request_in_progress_page = RequestInProgress(context.driver)
        context.chrome_start_page = ChromeStartPage(context.driver)
        context.verification_type_page = VerificationTypePage(context.driver)
        context.verification_details_page = VerificationDetailsPage(context.driver)
    except Exception as e:
        raise e

def cleanup_driver(context):
    context.driver.quit()
