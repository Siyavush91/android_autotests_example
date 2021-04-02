from selenium.webdriver.common.by import By
from utils.base_page import BasePage

import midhub_constants as mc
import utils.asserts as asserts

class MyDocsPage(BasePage):
    documents_tab_container = (By.ID, 'accountDocumentsContainerTabLayout')
    ready_docs_tab          = (By.XPATH, f"//*[contains(@text, '{mc.READY_DOCS}')]")
    checking_docs_tab       = (By.XPATH, f"//*[contains(@text, '{mc.CHECKING_DOCS}')]")
    toolbar                 = (By.XPATH, "//*[(./@resource-id = 'ru.mobileup.midhub:id/toolbar')]/*[(./@class = 'android.widget.TextView')]")
    profile_button          = (By.ID, 'profileButton')
    search_button           = (By.ID, 'searchButton')
    qrcode_button           = (By.ID, 'qrButton')
    empty_state_tab         = (By.ID, 'emptyTextView')
    add_doc_button          = (By.ID, 'addDocumentButton')
    title_doc               = (By.ID, 'title')
    status_doc              = (By.ID, 'status')
    global_verification     = (By.ID, 'globalVerification')

    def page_wait(self):
        self.wait_element_displayed(self.documents_tab_container) 
        return self
    
    def verify_page(self):
        self.wait_elements_displayed([self.documents_tab_container, self.ready_docs_tab, self.checking_docs_tab])
        self.wait_elements_displayed([self.toolbar, self.profile_button, self.search_button, self.qrcode_button])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.toolbar)[0], mc.MY_DOCS_HEADER)

    def verify_empty_state(self, section_name):
        self.wait_elements_displayed([self.add_doc_button, self.empty_state_tab])
        asserts.soft_assert_equal(self.fetch_elements_name(*self.add_doc_button)[0], mc.ADD_DOC_BUTTON)
        if section_name == 'Ready':
            asserts.soft_assert_equal(self.fetch_elements_name(*self.empty_state_tab)[0], mc.EMPTY_READY_TAB)
        elif section_name == 'Checking':
            asserts.soft_assert_equal(self.fetch_elements_name(*self.empty_state_tab)[0], mc.EMPTY_CHECKING_TAB)
        else:
            raise('Unsupported status')

    def tap_checking_docs_tab(self):
        self.find_tapable_element(*self.checking_docs_tab).click()
        return

    def tap_ready_docs_tab(self):
        self.find_tapable_element(*self.ready_docs_tab).click()
        return

    def tap_add_doc_button(self):
        self.find_tapable_element(*self.add_doc_button).click()
        return

    def verify_doc_status(self, doc_name, status):
        # TODO: content-desc for verification_type
        self.wait_element_displayed(self.title_doc)
        locator = (By.XPATH, f"//*[contains(@text, '{doc_name}')]")
        asserts.assert_true(self.is_element_found(locator), 'Expected doc is not shown')
        if status == 'Pending':
            asserts.assert_equal(self.fetch_elements_name(*self.status_doc)[0], mc.PENDING_STATUS)
        elif status == 'Mining':
            asserts.assert_equal(self.fetch_elements_name(*self.status_doc)[0], mc.MINING_STATUS)
        elif status == 'Ready':
            self.wait_element_displayed(self.global_verification)
            asserts.assert_false(self.is_element_found(self.status_doc), 'Not expected status is shown')
        else:
            raise('Unsupported status')
        

    def open_doc(self, doc_name):
        doc_locator = self.locator_from_text(doc_name)
        self.find_tapable_element(*doc_locator).click()
        return
