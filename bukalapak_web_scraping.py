from bs4 import BeautifulSoup 
import requests,time

print("Mining data from Bukalapak.com")
print("This may take few seconds . . .\n")


source = requests.get("https://www.bukalapak.com/c/komputer/laptop?utf8=%E2%9C%93&search%5Bfilter_attr%5D%5Bkapasitas_memory%5D%5B%5D=%3E%3D8Gb&search%5Bnew%5D=0&search%5Bnew%5D=1&search%5Bused%5D=0&search%5Bused%5D=1&search%5Bfree_shipping_coverage%5D=&search%5Bprovince%5D=&search%5Bcity%5D=&search%5Bcourier%5D=&search%5Bprice_min%5D=8000000&search%5Bprice_max%5D=11000000&search%5Brating_gte%5D=0&search%5Brating_lte%5D=5&search%5Btodays_deal%5D=0&search%5Binstallment%5D=0&search%5Bwholesale%5D=0&search%5Btop_seller%5D=0&search%5Bpremium_seller%5D=0&search%5Bbrand_seller%5D=0").text

soup = BeautifulSoup(source, "html.parser")

containers = soup.findAll('li', attrs={"class":"product--sem col-12--2"})

num = 0
for container in containers:

	brand_name = soup.findAll('a',attrs={"class":"product__name line-clamp--2 js-tracker-product-link qa-list"})
	brand = brand_name[num].text

	price_tag = soup.findAll('span',attrs={"class":"product-price__installment"})
	price = price_tag[num].text.strip()

	rating_tag = soup.findAll('a',attrs={"class":"user-feedback-summary"})
	rating = rating_tag[num].text.strip()

	city_tag = soup.findAll('div',attrs={"class":"user-city"})
	city = city_tag[num].text.strip()

	condition = soup.findAll('span',attrs={"class":"product__condition product__condition--used"})

	num = num+1

	print("Product #" + str(num))
	print("Brand Name 			: " + brand)
	print("Price 				: " + price)
	print("Trustworthy level 		: " + rating)
	print("Sent from 			: " + city)

	if(condition == "Baru"):
		condition = "New"
		print("Condition is 			: " + condition + "\n\n")
	else:
		condition = "Used"
		print("Condition is 			: " + condition + "\n\n")

