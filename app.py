from bs4 import BeautifulSoup
import csv

with open('data/3DX19s0p.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

reviews = soup.find_all('div', class_='shopee-product-rating')
print(f"Found {len(reviews)} review elements")


review_list = []
if reviews:
    for review in reviews:
        for item in review:
            # print(item)
            # date  
            name_tag = item.find('div', class_='shopee-product-rating__author-name')
            name = name_tag.get_text().strip() if name_tag else ''
            if name == '':
                    name_tag = item.find('a', class_='shopee-product-rating__author-name')
                    name = name_tag.get_text().strip() if name_tag else ''


            date_tag = item.find('div', class_='shopee-product-rating__time')
            date = date_tag.get_text().strip() if date_tag else ''

           
             
            review_tag = item.find('div', attrs={"style": "margin-top: 0.75rem;"})
            review = review_tag.get_text().strip() if review_tag else ''
            if review == '':            
                review_tag = item.find('div', attrs={"style": "position: relative; box-sizing: border-box; margin: 15px 0px; font-size: 14px; line-height: 20px; color: rgba(0, 0, 0, 0.87); word-break: break-word; white-space: pre-wrap;"})
                review = review_tag.get_text().strip() if review_tag else ''
            cleaned_review = review.replace("\n", " ")
            
            rereview_tag = item.find('div', class_='shopee-product-rating__content')
            rereview = rereview_tag.get_text().strip() if rereview_tag else ''
            cleaned_rereview = rereview.replace("\n", " ")

            print("------START------")
            print("name: ",name)
            print("date: ",date)
            print("review: ", review)
            print("re-review: ", rereview)
            print("------E N D------")

            if not name == '' or not date == '' or not review == '':
                review_list.append([name, date, cleaned_review, cleaned_rereview])
else:
    print("No reviews found")




with open('out.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Date', 'Review', 'Rereview'])
    writer.writerows(review_list)