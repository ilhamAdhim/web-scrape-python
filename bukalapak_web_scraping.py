from bs4 import BeautifulSoup 
import requests,time

print("Scraping data from Bukalapak.com : Laptop field (50 data in one page)")
print("This may take few seconds . . .\n")

page_list = [1,2,3,4]
page = page_list[0] - 1

for current_page in page_list:
	
	source = requests.get("https://www.bukalapak.com/c/komputer/laptop?page="+str(current_page)+"&search%5Bbrand_seller%5D=0&search%5Bcity%5D=&search%5Bcourier%5D=&search%5Bfilter_attr%5D%5Bkapasitas_memory%5D%5B%5D=%3E%3D8Gb&search%5Bfree_shipping_coverage%5D=&search%5Binstallment%5D=0&search%5Bnew%5D=1&search%5Bpremium_seller%5D=0&search%5Bprice_max%5D=11000000&search%5Bprice_min%5D=8000000&search%5Bprovince%5D=&search%5Brating_gte%5D=0&search%5Brating_lte%5D=5&search%5Btodays_deal%5D=0&search%5Btop_seller%5D=0&search%5Bused%5D=1&search%5Bwholesale%5D=0&utf8=%E2%9C%93").text

	soup = BeautifulSoup(source, "html.parser")
	package_containers = soup.findAll('ul',attrs={'class':'row-grid'})
	containers = soup.findAll('li', attrs={"class":"col-12--2"})
	page = page + 1
	print("Current page : " + str(page) + "\n")
	num = 0

	for each_section in package_containers:
		for container in containers:

			brand_name = soup.findAll('a',attrs={"class":"product__name line-clamp--2 js-tracker-product-link qa-list"})
			price_tag = soup.findAll('span',attrs={"class":"product-price__installment"})
			rating_tag = soup.findAll('a',attrs={"class":"user-feedback-summary"})
			city_tag = soup.findAll('div',attrs={"class":"user-city"})
			seller_tag = soup.findAll('h5',{'class':'user__name'})
			condition_tag = soup.findAll('span',attrs={"class":"product__condition"})	

			limit = len(brand_name)

			if (num < limit):
				brand = brand_name[num].text
				price = price_tag[num].text.strip()
				rating = rating_tag[num].text.strip()
				city = city_tag[num].text.strip()
				seller = seller_tag[num].text.strip()
				condition = condition_tag[num].text.strip()
				
				num = num+1	
		
				print("Product #" + str(num) + " by " + seller)
				print("Brand Name 			: " + brand)
				print("Price 				: " + price)
				print("Trustworthy level 		: " + rating)
				print("Sent from 			: " + city)
				print("Condition is 			: " + condition + "\n\n")

			else: 
				num = num
				print("Switching to next page . . . ")
				break