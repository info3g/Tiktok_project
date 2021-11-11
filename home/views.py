from django.shortcuts import render
from home.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from home.models import Person
from home.models import Data
from home.models import AI_summery
from home.models import total_hits
from django.http import HttpResponse
import  time
import datetime
# driver = webdriver.Chrome('chromedriver.exe')
# driver.get("https://www.tiktok.com/@paaubookss")

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
			p = AI_summery.objects.create(total_calls ="1", Successful_calls="1",Response_time= datetime.datetime.now(),Timestamp=datetime.datetime.now())
			p = AI_summery(total_calls ="1", Successful_calls="1",Response_time= datetime.datetime.now(),Timestamp=datetime.datetime.now())
			p.save(force_insert=True)
			return HttpResponse("doneeeeeeeeeee")
			return Response({'userInfo':userInfo})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserVideo(APIView):
	def get(self, request, format=None):
		p = total_hits.objects.create(idd ="1", Successful_calls="1",number_calls="1")
		p = total_hits(idd ="1", Successful_calls="1",number_calls="1")
		p.save(force_insert=True)
		return HttpResponse("okayyyyyyyyyyyy done")
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


def homes(request):
	p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
	p = Person(first_name="Bruce", last_name="Springsteen")
	p.save(force_insert=True)
	return HttpResponse("done")

def test(request):
	t = Data.objects.create(user_name="sonu1233", password="123456677")
	t = Data(user_name="sonu1233", password="123456677")
	t.save(force_insert=True)
	return HttpResponse("successfull")
