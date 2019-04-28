import unittest
import xlrd
from geopy.geocoders import Nominatim



class TestGeo(unittest.TestCase):
	def test1(self):
		data =[]
		test_file=("/home/u1/test/Book.xlsx")
		workbook=xlrd.open_workbook(test_file)
		sheet=workbook.sheet_by_index(0)
		for rownum in range(sheet.nrows):
			row = sheet.row_values(rownum)
			for x in row:
				data.append(x)
		i = 0
		while i < len(data):
				geolocator = Nominatim(user_agent="c0mkom@yandex.ru")
				location = geolocator.geocode(data[i])
				latitude = str(location.latitude)
				longitude = str(location.longitude)
				coordinate = latitude + ", " + longitude
				try:
					self.assertEqual(data[i+1], coordinate)
					print("Correct "+data[i])
				except AssertionError as e:
					print("Test failed {}".format(e))
				i+=2
	def test2(self):
		data =[]
		test_file=("/home/u1/test/book1.xlsx")
		workbook=xlrd.open_workbook(test_file)
		sheet=workbook.sheet_by_index(0)
		for rownum in range(sheet.nrows):
			row = sheet.row_values(rownum)
			for x in row:
				data.append(x)
		i = 0
		while i < len(data):
			geolocator = Nominatim(user_agent="c0mkom@yandex.ru")
			location = geolocator.reverse(str(data[i+1]))
			address = str(location.address) 
			try:
				self.assertEqual(data[i], address)
				print("Correct "+ data[i])
			except AssertionError as e:
				print("Test failed {}".format(e))
			i+=2
if __name__ == '__main__':
	unittest.main()


			