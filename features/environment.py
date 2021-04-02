import logging
import allure
import time
import traceback
import os
import base64
import midhub_constants as mc
from utils.smart_driver import start_driver, driver_setup, cleanup_driver
from appium import webdriver
from behave.log_capture import capture
from utils.logger import logger


#Hooks
def before_all(context):
    driver_setup(context.config.userdata.get("appium_host", "unknown"),
                 context.config.userdata.get("appium_port", "unknown"),
                 context.config.userdata.get("appium_version", "unknown"),
                 context.config.userdata.get("automation_name", "unknown"),
                 context.config.userdata.get("platform_name", "unknown"),
                 context.config.userdata.get("test_name", "unknown"),
                 context.config.userdata.get("app_uri", "unknown"),
                 context.config.userdata.get("new_command_timeout", "unknown"))

def after_all(context):
    pass

def before_feature(context, feature):
    pass

def before_scenario(context, scenario):
    context.config.setup_logging()
    start_driver(context)
    if context.driver.capabilities.get('deviceApiLevel') > 26:
        context.driver.start_recording_screen()
    set_server(context, context.config.userdata.get("local_server_ip", None))

def after_scenario(context, scenario):
    if context.driver.capabilities.get('deviceApiLevel') > 26:
        video = context.driver.stop_recording_screen()

    if scenario.status == 'failed' or logger.soft_assert_fail:
        logger.soft_assert_fail = False
        # Attach screenshot
        allure.attach(context.driver.get_screenshot_as_png(), 
                        name = 'screenshot', attachment_type = allure.attachment_type.PNG)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        screenshots_dir = 'reports/screenshots'
        os.makedirs(screenshots_dir, exist_ok=True)
        screenshot_name =  os.path.join(screenshots_dir, 'screenshot' + timestr + ".png")
        context.driver.save_screenshot(screenshot_name)
        print("Screenshot: " + screenshot_name)
        
        # Attach video
        if context.driver.capabilities.get('deviceApiLevel') > 26:
            video_dir = 'reports/videos'
            os.makedirs(video_dir, exist_ok=True)
            timestr = time.strftime("%Y%m%d-%H%M%S")
            video_name = "screen_record" + timestr + ".mp4"
            video_full_name = os.path.join(video_dir, video_name)
            video_stream = base64.b64decode(video)
            with open(video_full_name, "wb") as fd:
                fd.write(video_stream)
            allure.attach(video_stream,
                        name = 'Video attach', 
                        attachment_type = allure.attachment_type.MP4)
            print("Video: " + video_full_name)

        # Attach logs
        allure.attach("Traceback: \n" + logger.logs) 
    logger.logs = ""
    cleanup_driver(context)

def after_feature(context, feature):
    pass

def before_step(context, step):
    pass

def after_step(context, step):
    if step.status == 'failed':
        # Attach traceback
        txt_tb = str(u"".join(traceback.format_tb(step.exc_traceback)))
        allure.attach("Traceback: \n" + txt_tb) 
        print(txt_tb)

def before_tag(context, tag):
    pass

def after_tag(context, tag):
    pass

def set_server(context, server_ip):
    context.tutorial_page.page_wait()
    context.base_page.open_right_menu()
    # Sometimes something interrupts animation
    if not context.right_menu_page.right_menu_opened():
        context.base_page.open_right_menu()
    menu_page = context.right_menu_page.page_wait()
    menu_page.tap_config()

    permission_alert = context.permission_alert.page_wait()
    permission_alert.tap_allow()
    configs_page = context.configs_page.page_wait()

    if server_ip is None:
        configs_page.tap_stage()
        toast_text = context.base_page.toast_text()
        assert toast_text == mc.RESTART_APP_TOAST

        context.driver.terminate_app(mc.BUNDLE_ID)
        context.driver.activate_app(mc.BUNDLE_ID)
    else:
        server_address = 'http://' + server_ip + ':10120'
        config_name = 'Test config'
        if configs_page.config_exists(config_name) == False:
            configs_page.tap_add()
            
            create_config_page = context.create_config_page.page_wait()
            create_config_page.enter_name(config_name)
            create_config_page.enter_url(server_address)
            create_config_page.tap_add()

            configs_page = context.configs_page.page_wait()
        configs_page.tap_config(config_name)

    context.driver.terminate_app(mc.BUNDLE_ID)
    context.driver.activate_app(mc.BUNDLE_ID)
