import pytest

from pages.main_page import MainPage
from locators.locators import MainPageLocators, FooterLocators, BasePageLocators, PartnersLocators
from test_data.urls import MainPageUrls, SuitsUrls, FooterImageUrls
from test_data.all_links import Links
from test_data.main_page_data import *


class TestMainPage:
    URLs = SuitsUrls.URLs

    def test_example_search_city(self, driver, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.search_city('Almaty')

    def test_tc_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.search_city("Paris")
        main_page.choose_1st_option(wait)
        main_page.switch_to_c_temp()
        main_page.check_8_lines_are_displayed()

    def test_tc_021_01_01_visibility_of_agriculture_analytics_link(self, driver, open_and_load_main_page, wait):
        main_page = MainPage(driver)
        main_page.element_is_displayed(MainPageLocators.AGRICULTURE_ANALYTICS_TITLE_LOCATOR, wait)

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_01_03_verify_footer_presence_in_the_dom_tree_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        footer_common_kit = page.find_element(MainPageLocators.FOOTER_COMMON_KIT)
        page.check_element_is_present_in_the_dom_tree(footer_common_kit)

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_02_verify_display_of_product_collections_module_on_pages(self, driver,
                                                                                open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_product_collections_section_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_03_verify_display_of_subscription_section_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_subscription_section_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_04_verify_display_of_company_section_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_company_section_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_05_verify_display_of_technologies_section_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_technologies_section_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_06_verify_display_of_terms_and_conditions_section_on_pages(self, driver, open_and_load_main_page,
                                                                                  URL):
        page = MainPage(driver, link=URL)
        page.check_terms_and_conditions_section_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_07_verify_display_of_single_links_section_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_single_links_section_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_08_verify_display_of_download_openweather_app_section_on_pages \
                    (self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_download_openweather_app_section_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_02_09_verify_display_of_social_media_section_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_social_media_section_is_visible()

    def test_tc_003_03_03_historical_weather_data_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_historical_weather_data_link_is_visible()

    def test_tc_003_03_04_verify_weather_dashboard_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_is_visible()

    def test_tc_003_03_05_verify_weather_dashboard_link_clickability(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_is_clickable()

    def test_tc_003_03_07_verify_current_and_forecast_apis_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_current_and_forecast_apis_link_is_visible()

    def test_tc_003_03_08_verify_historical_weather_data_link_clickability(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_historical_weather_data_link_is_clickable()

    def test_tc_003_03_10_verify_weather_maps_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_maps_link_is_visible()

    def test_tc_003_03_11_verify_widgets_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_widgets_link_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_05_04_verify_display_of_pricing_link_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_pricing_link_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_05_05_verify_clickability_of_pricing_link_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_pricing_link_is_clickable()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_05_06_verify_display_of_subscribe_for_free_link_on_pages(self, driver, open_and_load_main_page,
                                                                             URL):
        page = MainPage(driver, link=URL)
        page.check_subscribe_for_free_link_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_05_07_verify_clickability_of_subscribe_for_free_link_on_pages(self, driver, open_and_load_main_page,
                                                                                  URL):
        page = MainPage(driver, link=URL)
        page.check_subscribe_for_free_link_is_clickable()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_05_08_verify_display_of_faq_link_on_pages(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_faq_link_is_visible()

    def test_tc_003_05_09_verify_clickability_of_faq_link_on_pages(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_faq_link_is_clickable()

    def test_tc_003_06_02_verify_terms_and_conditions_module_title_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_terms_and_conditions_module_title_visibility()

    def test_tc_003_06_03_verify_website_terms_and_conditions_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_website_terms_and_conditions_link_visibility()

    def test_tc_003_06_04_verify_clickability_of_website_terms_and_conditions_link(self, driver,
                                                                                   open_and_load_main_page):
        page = MainPage(driver)
        page.check_website_terms_and_conditions_link_is_clickable()

    def test_tc_003_06_05_verify_terms_and_conditions_of_sale_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_terms_and_conditions_of_sale_link_visibility()

    def test_tc_003_06_06_verify_clickability_of_terms_and_conditions_of_sale_link(self, driver,
                                                                                   open_and_load_main_page):
        page = MainPage(driver)
        page.check_terms_and_conditions_of_sale_link_is_clickable()

    def test_tc_003_06_07_verify_privacy_policy_link_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_privacy_policy_link_visibility()

    def test_tc_003_06_08_verify_clickability_of_privacy_policy_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_privacy_policy_link_is_clickable()

    def test_tc_003_07_02_verify_company_module_title_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_company_module_title_visibility()

    def test_tc_003_07_03_verify_text_of_company_module_title(self, driver, open_and_load_main_page, wait):
        page = MainPage(driver)
        page.check_text_of_company_module_title("Company")

    def test_tc_003_07_04_verify_company_module_text_visibility(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_company_module_text_visibility()

    def test_tc_003_07_05_verify_content_of_company_module_text(self, driver, open_and_load_main_page, wait):
        page = MainPage(driver)
        page.check_content_of_company_module_text("OpenWeather is a team of IT experts and data scientists that has "
                                                  "been practising deep weather data science. For each point on the "
                                                  "globe, OpenWeather provides historical, current and forecasted "
                                                  "weather data via light-speed APIs. Headquarters in London, UK.")

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_08_05_about_us_link_is_visible_on_each_page_specified_in_data(self, driver,
                                                                                  open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_about_us_link_is_visible()

    @pytest.mark.parametrize('URL', URLs)
    def test_tc_003_08_06_verify_about_us_link_clickability(self, driver, open_and_load_main_page, URL):
        page = MainPage(driver, link=URL)
        page.check_about_us_link_is_clickable()

    def test_tc_003_09_01_verify_title_presence_in_download_openweather_app_module(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_title_is_present_in_download_openweather_app_module()

    def test_tc_003_09_06_verify_text_of_download_openweather_app_module_title(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_text_of_download_openweather_app_module_title("Download OpenWeather app")

    def test_tc_003_09_07_verify_image_presence_in_download_on_the_app_store_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        download_on_the_app_store_image = page.find_element(MainPageLocators.DOWNLOAD_ON_THE_APP_STORE_IMAGE)
        page.check_image_is_present_in_the_element(download_on_the_app_store_image)

    def test_tc_003_09_08_verify_image_visibility_in_download_on_the_app_store_link(self, driver,
                                                                                    open_and_load_main_page):
        page = MainPage(driver)
        download_on_the_app_store_image = page.find_element(MainPageLocators.DOWNLOAD_ON_THE_APP_STORE_IMAGE)
        page.go_to_element(download_on_the_app_store_image)
        page.check_element_image_is_visible(download_on_the_app_store_image)

    def test_tc_003_09_09_verify_image_correctness_in_download_on_the_app_store_link(self, driver,
                                                                                     open_and_load_main_page):
        page = MainPage(driver)
        download_on_the_app_store_image = page.find_element(MainPageLocators.DOWNLOAD_ON_THE_APP_STORE_IMAGE)
        download_on_the_app_store_image_url = FooterImageUrls.DOWNLOAD_ON_THE_APP_STORE_IMAGE_URL
        page.check_image_is_correct_in_the_element(download_on_the_app_store_image, download_on_the_app_store_image_url)

    def test_tc_003_09_10_verify_image_presence_in_get_it_on_google_play_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        get_it_on_google_play_image = page.find_element(MainPageLocators.GET_IT_ON_GOOGLE_PLAY_IMAGE)
        page.check_image_is_present_in_the_element(get_it_on_google_play_image)

    def test_tc_003_09_11_verify_image_visibility_in_get_it_on_google_play_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        get_it_on_google_play_image = page.find_element(MainPageLocators.GET_IT_ON_GOOGLE_PLAY_IMAGE)
        page.go_to_element(get_it_on_google_play_image)
        page.check_element_image_is_visible(get_it_on_google_play_image)

    def test_tc_003_09_12_verify_image_correctness_in_get_it_on_google_play_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        get_it_on_google_play_image = page.find_element(MainPageLocators.GET_IT_ON_GOOGLE_PLAY_IMAGE)
        get_it_on_google_play_image_url = FooterImageUrls.GET_IT_ON_GOOGLE_PLAY_IMAGE_URL
        page.check_image_is_correct_in_the_element(get_it_on_google_play_image, get_it_on_google_play_image_url)

    def test_tc_003_10_11_verify_display_of_facebook_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_facebook_link_visibility()

    def test_tc_003_10_12_verify_clickability_of_facebook_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_facebook_link_clickaility()

    def test_tc_003_10_13_verify_image_presence_in_facebook_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        facebook_image = page.find_element(MainPageLocators.FACEBOOK_IMAGE)
        page.check_image_is_present_in_the_element(facebook_image)

    def test_tc_003_10_14_verify_image_visibility_in_facebook_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        facebook_image = page.find_element(MainPageLocators.FACEBOOK_IMAGE)
        page.go_to_element(facebook_image)
        page.check_element_image_is_visible(facebook_image)

    def test_tc_003_10_15_verify_image_correctness_in_facebook_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        facebook_image = page.find_element(MainPageLocators.FACEBOOK_IMAGE)
        facebook_image_url = FooterImageUrls.FACEBOOK_IMAGE_URL
        page.check_image_is_correct_in_the_element(facebook_image, facebook_image_url)

    def test_tc_003_10_16_verify_display_of_twitter_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_twitter_link_visibility()

    def test_tc_003_10_17_verify_clickability_of_twitter_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_twitter_link_clickaility()

    def test_tc_003_10_18_verify_image_presence_in_twitter_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        twitter_image = page.find_element(MainPageLocators.TWITTER_IMAGE)
        page.check_image_is_present_in_the_element(twitter_image)

    def test_tc_003_10_19_verify_image_visibility_in_twitter_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        twitter_image = page.find_element(MainPageLocators.TWITTER_IMAGE)
        page.go_to_element(twitter_image)
        page.check_element_image_is_visible(twitter_image)

    def test_tc_003_10_20_verify_image_correctness_in_twitter_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        twitter_image = page.find_element(MainPageLocators.TWITTER_IMAGE)
        twitter_image_url = FooterImageUrls.TWITTER_IMAGE_URL
        page.check_image_is_correct_in_the_element(twitter_image, twitter_image_url)

    def test_tc_003_10_21_verify_display_of_telegram_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_telegram_link_visibility()

    def test_tc_003_10_22_verify_clickability_of_telegram_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_telegram_link_clickaility()

    def test_tc_003_10_23_verify_image_presence_in_telegram_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        telegram_image = page.find_element(MainPageLocators.TELEGRAM_IMAGE)
        page.check_image_is_present_in_the_element(telegram_image)

    def test_tc_003_10_24_verify_image_visibility_in_telegram_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        telegram_image = page.find_element(MainPageLocators.TELEGRAM_IMAGE)
        page.go_to_element(telegram_image)
        page.check_element_image_is_visible(telegram_image)

    def test_tc_003_10_25_verify_image_correctness_in_telegram_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        telegram_image = page.find_element(MainPageLocators.TELEGRAM_IMAGE)
        telegram_image_url = FooterImageUrls.TELEGRAM_IMAGE_URL
        page.check_image_is_correct_in_the_element(telegram_image, telegram_image_url)

    def test_tc_003_10_26_verify_image_presence_in_linkedin_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        linkedin_image = page.find_element(MainPageLocators.LINKEDIN_IMAGE)
        page.check_image_is_present_in_the_element(linkedin_image)

    def test_tc_003_10_27_verify_image_visibility_in_linkedin_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        linkedin_image = page.find_element(MainPageLocators.LINKEDIN_IMAGE)
        page.go_to_element(linkedin_image)
        page.check_element_image_is_visible(linkedin_image)

    def test_tc_003_10_28_verify_image_correctness_in_linkedin_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        linkedin_image = page.find_element(MainPageLocators.LINKEDIN_IMAGE)
        linkedin_image_url = FooterImageUrls.LINKEDIN_IMAGE_URL
        page.check_image_is_correct_in_the_element(linkedin_image, linkedin_image_url)

    def test_tc_003_10_29_verify_image_presence_in_medium_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        medium_image = page.find_element(MainPageLocators.MEDIUM_IMAGE)
        page.check_image_is_present_in_the_element(medium_image)

    def test_tc_003_10_30_verify_image_visibility_in_medium_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        medium_image = page.find_element(MainPageLocators.MEDIUM_IMAGE)
        page.go_to_element(medium_image)
        page.check_element_image_is_visible(medium_image)

    def test_tc_003_10_31_verify_image_correctness_in_medium_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        medium_image = page.find_element(MainPageLocators.MEDIUM_IMAGE)
        medium_image_url = FooterImageUrls.MEDIUM_IMAGE_URL
        page.check_image_is_correct_in_the_element(medium_image, medium_image_url)

    def test_tc_003_10_32_verify_image_presence_in_github_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        github_image = page.find_element(MainPageLocators.GITHUB_IMAGE)
        page.check_image_is_present_in_the_element(github_image)

    def test_tc_003_10_33_verify_image_visibility_in_github_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        github_image = page.find_element(MainPageLocators.GITHUB_IMAGE)
        page.go_to_element(github_image)
        page.check_element_image_is_visible(github_image)

    def test_tc_003_10_34_verify_image_correctness_in_github_brand_link(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        github_image = page.find_element(MainPageLocators.GITHUB_IMAGE)
        github_image_url = FooterImageUrls.GITHUB_IMAGE_URL
        page.check_image_is_correct_in_the_element(github_image, github_image_url)

    def test_tc_003_10_35_verify_image_presence_in_the_rmets_element(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        rmets_image = page.find_element(MainPageLocators.RMETS_IMAGE)
        page.check_image_is_present_in_the_element(rmets_image)

    def test_tc_003_12_01_check_historical_weather_data_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_historical_weather_data_link_functionality()

    def test_tc_003_12_02_verify_weather_data_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_dashboard_link_functionality()

    def test_tc_003_12_03_verify_weather_maps_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_weather_maps_link_functionality()

    def test_tc_003_12_08_verify_our_technology_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_our_technology_link_functionality()

    def test_tc_003_12_16_verify_accuracy_and_quality_of_weather_data_link_functionality \
                    (self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_accuracy_and_quality_of_weather_data_link_functionality()

    def test_tc_003_12_17_verify_connect_your_weather_station_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_connect_your_weather_station_link_functionality()

    @pytest.mark.skip('Build failed')
    def test_tc_003_12_18_verify_how_to_start_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_how_to_start_link_functionality()

    def test_tc_003_12_19_verify_subscribe_for_free_link_functionality_for_unauthorized_user \
                    (self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_subscribe_for_free_link_functionality()

    def test_tc_003_12_20_verify_blog_link_functionality(self, driver, open_and_load_main_page, wait):
        page = MainPage(driver)
        expected_link = Links.URL_BLOG_WEATHER
        page.check_blog_link_functionality(expected_link)

    def test_tc_003_12_21_verify_openweather_for_business_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        expected_link = Links.URL_OPENWEATHER_FOR_BUSINESS
        page.check_openweather_for_business_link_functionality(expected_link)

    def test_TC_003_13_01_verify_cookies_management_module_is_visible(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_manage_cookies_link_is_visible()

    def test_TC_003_14_02_manage_cookies_link_functionality(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_manage_cookies_link_is_functionality()

    @pytest.mark.skip('Build failed')
    def test_TC_001_02_01_verify_temperature_switched_on_metric_system(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.checking_the_temperature_system_switching("°C")

    @pytest.mark.skip('Build failed')
    def test_TC_001_02_02_verify_temperature_switched_on_imperial_system(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.checking_the_temperature_system_switching("°F")

    def test_TC_001_02_03_verify_temperature_metric_button_displayed_clickable(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_temperature_button_displayed_clickable("°C")

    def test_TC_001_02_04_verify_temperature_imperial_button_displayed_clickable(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_temperature_button_displayed_clickable("°F")

    @pytest.mark.skip('Build failed')
    def test_TC_001_05_01_verify_the_current_date_and_time(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_the_current_date_and_time()

    @pytest.mark.skip('Build failed')
    def test_TC_001_05_02_verify_current_location(self, driver, open_and_load_main_page, wait):
        page = MainPage(driver)
        page.verify_current_location(wait)

    @pytest.mark.skip('Build failed')
    def test_tc_001_01_01_verify_city_name_displayed_by_zip(self, driver, wait, open_and_load_main_page):
        page = MainPage(driver)
        page.check_city_name_displayed_by_zip(wait)

    def test_tc_001_01_02_main_page_search_city_dropdown_options_valid_value(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_dropdown_options()

    def test_tc_001_02_04_01_switch_toggle_buttons(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_buttons_displayed_and_enabled()

    def test_tc_001_04_03_verify_in_day_list_first_element_day_by_week(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.check_day()

    def test_tc_001_04_04_verify_in_day_list_first_element_month(self, driver, open_and_load_main_page):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_months()

    def test_tc_001_04_05_verify_in_day_list_first_element_number_day(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_in_day_list_first_element_number_day()

    def test_tc_001_04_06_verify_in_day_list_days_of_the_week(self, driver, open_and_load_main_page):
        page = MainPage(driver)
        page.verify_in_day_list_days_of_the_week()

    def test_tc_001_04_07_verify_day_list_elements_numbers_days(self, driver, wait, open_and_load_main_page):
        page = MainPage(driver)
        page.check_in_day_list_numbers_days(driver)

    def test_tc_003_09_01_the_module_title_display(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_module_title_download_openweather_app()

    def test_tc_003_09_02_app_store_brand_link_display(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_app_store_brand_link_display()

    def test_tc_003_09_03_app_store_brand_link_clickable(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_app_store_brand_link_clickable()

    def test_tc_003_09_04_google_play_brand_link_clickable(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_google_play_brand_link_clickable()

    def test_tc_003_09_04_google_play_brand_link_display(self, driver):
        page = MainPage(driver, Links.URL_MAIN_PAGE)
        page.open_page()
        page.check_google_play_brand_link_display()

    def test_TC_001_05_04_verify_description_weather_for_current_location(self, driver, open_and_load_main_page, wait):
        actual_weather = MainPage(driver)
        actual_weather.check_description_weather_block('Feels like')

    def test_TC_001_01_08_dropdown_list_contain_city_temperature(self, driver, open_and_load_main_page, wait):
        search_result = MainPage(driver)
        search_result.dropdown_contain_city_temperature()

    class TestFooterLinksFunctionality:
        @pytest.mark.skip('Build failed')
        def test_TC_003_12_04_current_and_forecast_apis_functionality(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.check_current_and_forecast_apis_functionality()

        def test_TC_003_12_06_verify_privacy_policy_is_opened_after_click(self, driver, wait, open_and_load_main_page):
            main_page = MainPage(driver)
            main_page.verify_privacy_policy_is_opened_after_click(driver, wait)

        def test_TC_003_12_07_about_us_link_leads_to_correct_page(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.about_us_link_leads_to_correct_page()

        def test_TC_003_12_11_link_Google_Play_leads_to_correct_page_in_GP(self, driver, open_and_load_main_page, wait):
            google_link = MainPage(driver)
            google_link.check_leads_link_Googl_Play()

    class TestFooterLinksclickability:
        def test_TC_003_03_02_verify_clickability_current_and_forecast_apis(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.verify_clickability_current_and_forecast_apis()

        def test_tc_003_03_06_verify_widgets_clickability(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_widgets_clickability()

    class TestHowToStartLink:
        def test_tc_003_05_02_verify_how_to_start_visibility(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_how_to_start_visibility()

        def test_tc_003_05_03_verify_how_to_start_link_is_clickable(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_how_to_start_link_is_clickable()

        def test_tc_002_03_10_01_how_to_start_link_leads_to_correct_page(self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            main_page.check_how_to_start_link_opens_opens_correct_page(wait, Links.HOW_TO_START_URL)
            main_page.check_correct_header_is_displayed("How to start using professional collections")

    class TestHeaderPage:
        def test_tc_002_02_07_placeholder_is_displayed_in_search_field(self, driver, open_and_load_main_page):
            main_page = MainPage(driver)
            main_page.check_placeholder_text_is_visible("Weather in your city")

        def test_tc_002_02_09_placeholder_disappears_if_symbol_is_typed_in_search_field(
                self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            main_page.check_placeholder_disappears("a", "value")

        def test_tc_002_03_23_faq_link_is_visible_and_clickable(self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            main_page.click_support_link()
            main_page.faq_submenu_should_be_visible(wait=wait)

        def test_tc_002_03_09_01_faq_link_leads_to_correct_page(self, driver, open_and_load_main_page, wait):
            main_page = MainPage(driver)
            main_page.check_faq_link_opens_opens_correct_page(wait, Links.FAQ_URL)
            main_page.check_correct_header_is_displayed("Frequently Asked Questions")

        def test_TC_002_03_22_partners_link_is_visible_and_clickable(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.link_visible_and_clickable(BasePageLocators.PARTNERS_LINK)

        def test_TC_002_03_21_partners_link_leads_to_page_with_correct_header(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.link_leads_to_page_with_correct_header(BasePageLocators.PARTNERS_LINK,
                                                        PartnersLocators.PARTNERS_PAGE_HEADING)

        def test_TC_002_03_07_marketplace_link_redirects_to_valid_page(self, driver, open_and_load_main_page):
            main_page = MainPage(driver)
            main_page.verify_marketplace_link_redirects_to_valid_page()

        @pytest.mark.parametrize('page', data["pages"])
        def test_TC_002_01_03_Logo_is_visible(self, driver, page):
            main_page = MainPage(driver, f'{Links.URL_MAIN_PAGE}{page}')
            main_page.open_page()
            main_page.check_logo_is_visible()

    class TestMainPageFooter:
        link_product_collections = MainPageUrls.PRODUCT_COLLECTION_LINKS

        def test_tc_003_12_12_widgets_link_functionality(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            expected_link = "https://openweathermap.org/widgets-constructor"
            page.click_footer_product_collections_widgets(expected_link)

        @pytest.mark.parametrize("link_product_collection", link_product_collections)
        def test_tc_003_12_24_verify_product_collections_module_all_link_functionality(self, driver,
                                                                                       open_and_load_main_page, wait,
                                                                                       link_product_collection):
            page = MainPage(driver)
            expected_link = link_product_collection
            link_number = self.link_product_collections.index(expected_link)
            page.click_footer_product_collections_all_widgets(expected_link, link_number)

        @pytest.mark.parametrize('page', data["pages"])
        def test_TC_003_01_01_verify_footer_is_visible_from_all_pages_specified_in_data(self, driver, page):
            footer = MainPage(driver, f'{Links.URL_MAIN_PAGE}{page}')
            footer.open_page()
            footer_actual_result = footer.find_element(FooterLocators.FOOTER_WEBSITE)
            footer.go_to_element(footer_actual_result)
            footer.check_footer_website_is_displayed(footer_actual_result)

        @pytest.mark.parametrize('page', data["pages"])
        def test_TC_003_01_02_verify_copyright_is_visible_from_all_pages_specified_in_data(self, driver, page):
            footer = MainPage(driver, f'{Links.URL_MAIN_PAGE}{page}')
            footer.open_page()
            copyright_actual_result = footer.find_element(FooterLocators.FOOTER_COPYRIGHT)
            footer.go_to_element(copyright_actual_result)
            footer.check_copyright_is_displayed(copyright_actual_result)

        def test_TC_003_08_02_ask_a_question_link_is_visible(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.element_is_visible(MainPageLocators.ASK_A_QUESTION_LINK)

        def test_TC_003_08_03_ask_a_question_link_is_clickable(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.element_is_clickable(MainPageLocators.ASK_A_QUESTION_LINK)

        def test_TC_003_12_05_ask_a_question_link_leads_to_correct_page(self, driver, open_and_load_main_page):
            page = MainPage(driver)
            page.scroll_down_the_page()
            page.check_link_in_new_window(MainPageLocators.ASK_A_QUESTION_LINK, MainPageUrls.ASK_A_QUESTION_PAGE)

        @pytest.mark.parametrize('page', data["pages"])
        def test_TC_003_03_01_Product_Collections_title_is_visible(self, driver, page):
            footer = MainPage(driver, f'{Links.URL_MAIN_PAGE}{page}')
            footer.open_page()
            footer.check_product_collections_module_title_is_visible()

    class TestMainPageHourlyForecast:
        def test_tc_001_08_04_verify_chart_is_present(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.verify_chart_weather_is_present()

    def test_tc_001_017_01_visibility_of_nwp_block(self, driver):
        page = MainPage(driver, MainPageUrls.QUALITY_INFO_PAGE)
        page.open_page()
        page.element_is_visible(MainPageLocators.NWP_MODEL)

    class TestMainPageGraphicAndWeather:
        def test_tc_001_08_01_graphic_hourly_forecast_is_displayed(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.graphic_hourly_forecast_is_displayed(wait=wait)

        def test_tc_001_08_02_weather_items_are_displayed(self, driver, open_and_load_main_page, wait):
            page = MainPage(driver)
            page.weather_items_are_displayed(wait=wait)
