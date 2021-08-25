def delay():
    time.sleep(random.radiant(1, 3))


tesla_url = 'https://www.tesla.com/'
tesla_logo = "//a[@aria-label='Tesla Logo']//*[local-name()='svg']"

# tesla_logo = "//header/h1[1]/a[1]/*[1]"
Model_S = "//a[@href='/models'][contains(.,'Model S')]"
side_menu = '//*[@id="tds-consumer-global-header"]/dialog/ol/li[2]//a["@href"]'
Model_3 = "//a[@href='/model3'][contains(.,'Model 3')]"
Model_X = "//a[@href='/modelx'][contains(.,'Model X')]"
Model_Y = "//a[@href='/modely'][contains(.,'Model Y')]"
Solar_Roof = "//a[@href='/solarroof'][contains(.,'Solar Roof')]"
Solar_Panels = "//a[@href='/solarpanels'][contains(.,'Solar Panels')]"
Shop = '//a[@href="https://shop.tesla.com/us/en.html?tesref=true"][contains(.,"Shop")]'
Account = "//a[@href='/teslaaccount'][contains(.,'Account')]"

logo_S = "(//h1[contains(.,'Model S')])[1]"
btn_Custom_Order = "(//a[contains(@title,'Custom Order')])[1]"
logo_Y = "(//h1[contains(.,'Model Y')])[1]"
btn_Existing_Inventory = "(//a[contains(.,'Existing Inventory')])[2]"
logo_3 = "(//h1[contains(.,'Model 3')])[1]"
logo_X = "(//h1[contains(.,'Model X')])[1]"
logo_Solar_Panels = "(//h1[contains(.,'Solar Panels')])[1]"
btn_Order_Now = "(//a[@href='/solarroof/design'])[1]"
logo_Solar_Roof = "(//h1[contains(.,'Solar Roof')])[1]"
btn_Learn_More = "(//a[@href='/solarroof'])[2]"
logo_Accessories = "(//h1[contains(.,'Accessories')])[1]"
btn_Shop_Now = "(//a[@href='/shop?tesref=true'])[1]"
About = "(//a[@href='/shop?tesref=true'])[1]"
# About = "//a[contains(text(),'Tesla © 2021')]"
Legal = "//a[contains(.,'Privacy & Legal')]"
Contact = "//a[@href='/contact']"
Career = "//a[@href='/careers']"
News = "//a[@href='/blog']"
Engage = "//a[@href='https://engage.tesla.com/']"
Locations = "//a[contains(.,'Locations')]"

job_search_url = "https://www.tesla.com/careers/search/"
search_name = "//label[@class='tds-form-item-label'][contains(.,'Search')]"
# search_field = "//input[@id='_uaUPfDGTO']"
search_field = '//*[@class="tds-text-input"]'
job_cat_nm = "//*[@class='tds-form-item-label'][contains(.,'Job Category')]"
job_cat_field = '//*[@name="/department"]'
job_cat = "//option[contains(text(),'Engineering & Information Technology')]"
region_name = "//label[contains(.,'Region')]"
region_field = '//*[@name="/region"]'
region = "//option[contains(text(),'North America')]"
location_name = "//label[contains(.,'Location')]"
location_field = "//select[contains(@name,'/country')]"
location = "//option[contains(text(),'United States of America')]"
state_name = "//label[contains(.,'State')]"
state_field = "//select[@name='/state']"
state = "//option[contains(text(),'Florida')]"
city_name = "//label[contains(.,'City')]"
city_field = "//select[@name='/location']"
city = "//option[contains(.,'Miami')]"
reset_filters = "//button[contains(.,'Reset Filters')]"
