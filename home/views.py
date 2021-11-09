from django.shortcuts import render
from home.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import  time
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.tiktok.com/@paaubookss")

def homepage(request):
	return render(request,'table.html')

class UserInfoList(APIView):
	def get(self, request, format=None):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():	
			user = serializer.data['username']
			print(user)
			if '@' in user:
				driver.get("https://www.tiktok.com/"+str(user))
			else:
				users = '@'+str(user)
				print(users)
				driver.get("https://www.tiktok.com/"+str(users))
			driver.get("https://www.tiktok.com/@paaubookss")
			import  time
			time.sleep(15)
			bs_data = driver.page_source
			soup = bs(bs_data, "html.parser")
			data_all = soup.find("script", attrs={"id": "__NEXT_DATA__"})
			data=str(data_all).replace('<script crossorigin="anonymous" id="__NEXT_DATA__" nonce="" type="application/json">','').replace('</script>','')    
			import json
			res = json.loads(data)
			print(res)
			userInfo = res['props']['pageProps']['userInfo']
			print({'userInfo':userInfo})
			return Response({'userInfo':userInfo})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserVideo(APIView):
	def get(self, request, format=None):
		serializer = VideoSerializer(data=request.data)
		if serializer.is_valid():	
			user = serializer.data['userid']
			print(user)
			countss = serializer.data['counts']
			if '@' in user:
				driver.get("https://www.tiktok.com/"+str(user))
			else:
				users = '@'+str(user)
				driver.get("https://www.tiktok.com/"+str(users))
			import  time
			time.sleep(10)
			bs_data = driver.page_source
			soup = bs(bs_data, "html.parser")
			data_all = soup.find("script", attrs={"id": "__NEXT_DATA__"})
			data=str(data_all).replace('<script crossorigin="anonymous" id="__NEXT_DATA__" nonce="" type="application/json">','').replace('</script>','')    
			import json
			res = json.loads(data)
			itemList = res['props']['pageProps']['items']
			# print({'itemList':itemList})
			import time
			page_source = []
			time.sleep(20)
			data=driver.find_elements_by_xpath('//*[@class="jsx-1906445185 video-feed-item-wrapper"]')
			print(data,"dataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

			for i in data:
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(3)
				links = i.get_attribute('href')
				print(links,"llllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
				if len(page_source) <= int(countss):
					page_source.append(links)
				else:
					break       
				
			return Response({'itemList':itemList,'images':page_source})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)