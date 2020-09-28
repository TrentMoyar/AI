import PIL
from PIL import Image
import urllib.request
import io, sys, os, random

def distance(pixel_one, pixel_two):
   return (pixel_one[0] - pixel_two[0])**2 + (pixel_one[1] - pixel_two[1])**2 + (pixel_one[2] - pixel_two[2])**2

def main():
   k = int(sys.argv[1])
   file = sys.argv[2]
   if not os.path.isfile(file):
      file = io.BytesIO(urllib.request.urlopen(file).read())
   img = Image.open(file)
   pix = img.load()
   kvals = {(x,y):0 for x in range(img.size[0]) for y in range(img.size[1])}
   distinct = {}
   for index in kvals:
      if pix[index] in distinct:
         distinct[pix[index]] += 1
      else:
         distinct[pix[index]] = 1
   pixels = sorted(distinct.keys(), key=lambda x: distinct[x], reverse=True)[:20]
   kmeans = pixels[0:k]
   moved = True
   newvals = {x:min(list(range(k)), key=lambda y:distance(kmeans[y], x)) for x in distinct.keys()}
   while moved:
      moved = False
      averages = [(0, (0,0,0)) for x in range(k)]
      for color in newvals:
         averages[newvals[color]] = averages[newvals[color]][0] + distinct[color], tuple([averages[newvals[color]][1][x] + color[x]*distinct[color] for x in range(3)])
      for x in range(k):
         kmeans[x] = tuple([averages[x][1][y]/averages[x][0] for y in range(3)])
      distances = [min([distance(kmeans[x], kmeans[y]) for y in range(k) if y != x]) for x in range(k)]
      tomove = []
      for color in newvals:
         if distance(color, kmeans[newvals[color]]) > distances[newvals[color]]*0.25:
            tomove.append(color)
      for color in tomove:
         prev = newvals[color]
         newvals[color] = min(list(range(k)), key=lambda y:distance(kmeans[y], color))
         if prev != newvals[color]:
            moved = True
   for index in kvals:
      kvals[index] = newvals[pix[index]]
   counts = [0 for x in range(k)]
   for index in kvals:
      counts[kvals[index]] += 1
   print("Size: " + str(img.size[0]) + " x " + str(img.size[1]))
   print("Pixels: " + str(img.size[0]*img.size[1]))
   print("Distinct pixel count: " + str(len(distinct)))
   print("Most common pixel: " + str(pixels[0]) + " => " + str(distinct[pixels[0]]))
   print("Final means:")
   for x in range(len(kmeans)):
      print(str(x+1) + ": " + str(kmeans[x]) + " => " + str(counts[x]))
   regions = {x:0 for x in range(k)}
   for x in range(k):
      kmeans[x] = tuple(map(int, kmeans[x]))
   for index in kvals:
      pix[index] = kmeans[kvals[index]]
   for index in kvals:
      if kvals[index] != -1:
         regions[kvals[index]] += 1
         region_count(kvals, index, kvals[index])
   print("Region counts: " + str([regions[x] for x in range(k)])[1:-1])
   img.show()
   img.save("kmeans/{}.png".format("2021tmoyar"), "PNG")

def region_count(kvals, index, value):
   change = [-1, 0, 1]
   queue = [index]
   while len(queue) != 0:
      current = queue.pop(0)
      if current in kvals and kvals[current] == value:
         for x in change:
            for y in change:
               queue.append((current[0] + x, current[1] + y))
         kvals[current] = -1



if __name__ == "__main__":
   main()