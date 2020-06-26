#!/usr/bin/env python
# coding: utf-8




from splinter import Browser 
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time



def init_browser():

    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)






def scrape():
    browser = init_browser()
   

    url ='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(3)
    html= browser.html
    soup = bs(html, 'html.parser')

    article_location= soup.find('div', class_="list_text")
    news_p= article_location.find('div',class_='article_teaser_body').text.strip()
    news_title=article_location.find('div',class_='content_title').text
    print(news_title)
    print(news_p)
    



    mars_url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_url)
    time.sleep(3)
    html= browser.html
    soup = bs(html, 'html.parser')





    featured_image= soup.find('a', class_="button fancybox")['data-fancybox-href']

    featured_image_url= (f'https://www.jpl.nasa.gov{featured_image}')
    


    



    weather_url= 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    time.sleep(3)
    html= browser.html
    soup = bs(html, 'html.parser')




    tweet= soup.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')

    mars_weather= tweet.find('span',class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0").text
    print(mars_weather)
    
    facts_url= 'https://space-facts.com/mars/'
    fact_tables= pd.read_html(facts_url)
    print(fact_tables)
    

    comparison= fact_tables[1]

    comparison.set_index('Mars - Earth Comparison')
    html_comp= comparison.to_html(index = False)
    html_comp.replace('\n','')
    print(html_comp)
    print(comparison)
    

    overview= fact_tables[0]
    ov= overview.rename(columns= {0: "Observation", 1 : "Statistics"})
    ov.set_index("Observation")
    html_ov= ov.to_html(index= False)
    html_ov.replace('\n','')
    print(html_ov)
    print(ov)
  
    Moons = ['Cerberus', 'Schiaparelli', 'Syrtis Major', 'Valles Marineris']
    hemisphere_image_urls= []
    
    for i in Moons:
        hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemis_url)
        browser.click_link_by_partial_text(i)
        html = browser.html
        soup = bs(html, 'html.parser')
        i_image_url = soup.find('img', class_ = 'wide-image')['src']
        i_image = (f'https://astrogeology.usgs.gov/{i_image_url}')
        hemisphere_image_urls.append({'Moon': f'{i} Hemisphere', 'img_url': i_image})
        print(i_image)
    
    
    df= pd.DataFrame(hemisphere_image_urls)
    print(df)
    mars = {'News_Title' : news_title, 'News_Paragraph' : news_p, 'Mars_Photo' : featured_image_url, 'Mars_Weather' : mars_weather, 'Mars_Overview' : html_ov, 'Moon_Photos' : hemisphere_image_urls,"Comparison": html_comp}

    return mars






# In[ ]:




