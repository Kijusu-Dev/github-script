from selenium import webdriver


def ViewsData(driver):
	driver.get(f"https://komarev.com/ghpvc/?username={username}")
	views = int(
		driver.find_element_by_css_selector(
			"svg > g:nth-child(4) > text:nth-child(4)"
			).get_attribute("innerHTML")
		)
	return views

def FollowData(driver):
	driver.get(f"https://www.github.com/{username}")
	try:
		follow = driver.find_element_by_css_selector(
			"span.text-bold.color-text-primary"
			)
	except:
		return "Not Found"

	if follow:
		return follow.text
	else:
		return "Not Found"

def BioData(driver):
	driver.get(f"https://github.com/{username}")
	try:
		k = driver.find_element_by_css_selector(
		"div.p-note.user-profile-bio.mb-3.js-user-profile-bio.f4"
		)

		bio = k.find_element_by_css_selector(
			"div"
			)
	except:
		return "Not Found"

	if bio:
		return bio.text
	else:
		return "Not Found"

def LocationData(driver):
	try:
		k = driver.find_element_by_css_selector("div.js-profile-editable-area.d-flex.flex-column.d-md-block")
		location = k.find_element_by_css_selector(
			"span.p-label"
			)
	except:
		return "Not Found"
	if location:
		return location.text
	else:
		return "Not Found"


username = input("Username > ")
driver = webdriver.Chrome(executable_path="chromedriver.exe")
ViewsDD = ViewsData(driver)
FollowDD = FollowData(driver)
BioDD = BioData(driver)
LocaDD = LocationData(driver)

def DisplayEvent():

	driver.quit()

	print(f"Username : {username}")
	print(f"Bio : {BioDD}")
	print(f"Location : {LocaDD}")

	if ViewsDD <= 1:
		print(f"Profils view : {ViewsDD} view")
	else:
		print(f"Profils views : {ViewsDD} views")
	print(f"Followers : {FollowDD}")

	print(f"Links profile : https://github.com/{username}")

DisplayEvent()
