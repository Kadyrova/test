import unittest
import xlrd
from geopy.geocoders import Nominatim

data_c =[]
test_file=("./Book.xlsx")
workbook=xlrd.open_workbook(test_file)
sheet=workbook.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    for x in row:
        data_c.append(x)

data_a =[]
test_file=("./book1.xlsx")
workbook=xlrd.open_workbook(test_file)
sheet=workbook.sheet_by_index(0)
for rownum in range(sheet.nrows):
	row = sheet.row_values(rownum)
	for x in row:
		data_a.append(x)


class TestGeo(unittest.TestCase):

	geolocator = Nominatim(user_agent="c0mk0m@yandex.ru")


	def test1_1(self):
		location = self.geolocator.geocode(str(data_c[0]))
		latitude = str(location.latitude)
		longitude = str(location.longitude)
		coordinate = latitude + ", " + longitude
		self.assertEqual(data_c[1], coordinate)


	def test1_2(self):
		location = self.geolocator.geocode(str(data_c[2]))
		latitude = str(location.latitude)
		longitude = str(location.longitude)
		coordinate = latitude + ", " + longitude
		self.assertEqual(data_c[3], coordinate)


	def test1_3(self):
		location = self.geolocator.geocode(str(data_c[4]))
		latitude = str(location.latitude)
		longitude = str(location.longitude)
		coordinate = latitude + ", " + longitude
		self.assertEqual(data_c[5], coordinate)


	def test1_4(self):
		location = self.geolocator.geocode(str(data_c[6]))
		with self.assertRaises(AttributeError):
			location.latitude


	def test1_5(self):
		location = self.geolocator.geocode(str(data_c[7]))
		with self.assertRaises(AttributeError):
			location.latitude

	def test1_6(self):
		location = self.geolocator.geocode(str(data_c[8]))
		with self.assertRaises(AttributeError):
			location.latitude


	def test1_7(self):
		location = self.geolocator.geocode(str(data_c[9]))
		with self.assertRaises(AttributeError):
			location.latitude


	def test1_8(self):
		location = self.geolocator.geocode(str(int(data_c[10])))
		with self.assertRaises(AttributeError):
			location.latitude

	def test1_9(self):
		location = self.geolocator.geocode(str(data_c[11]))
		with self.assertRaises(AttributeError):
			location.latitude


	def test1_10(self):
		location = self.geolocator.geocode(str(data_c[12]))
		with self.assertRaises(AttributeError):
			location.latitude
		

	def test2_1(self):
		location = self.geolocator.reverse(str(data_a[1]))
		address = str(location.address)
		self.assertEqual(data_a[0], address)


	def test2_2(self):
		location = self.geolocator.reverse(str(data_a[3]))
		address = str(location.address)
		self.assertEqual(data_a[2], address)

	
	def test2_3(self):
		location = self.geolocator.reverse(str(data_a[5]))
		address = str(location.address)
		self.assertEqual(data_a[4], address)

			
	def test2_4(self):
		with self.assertRaises(ValueError):
			self.geolocator.reverse(str(data_a[6]))

	def test2_5(self):
		with self.assertRaises(ValueError):
			self.geolocator.reverse(str(data_a[7]))

	
	def test2_6(self):
		with self.assertRaises(ValueError):
			self.geolocator.reverse(str(data_a[8]))


	def test2_7(self):
		with self.assertRaises(ValueError):
			self.geolocator.reverse(str(data_a[9]))


	def test2_8(self):
		with self.assertRaises(ValueError):
			self.geolocator.reverse(str(data_a[10]))
	

	def test2_9(self):
		with self.assertRaises(ValueError):
			self.geolocator.reverse(str(data_a[11]))

			
	def test2_10(self):
		with self.assertRaises(ValueError):
			self.geolocator.reverse(str(data_a[12]))

	
	def test2_11(self):
		with self.assertRaises(ValueError):
			self.geolocator.reverse(str(data_a[13]))
	


if __name__ == '__main__':
	unittest.main()

