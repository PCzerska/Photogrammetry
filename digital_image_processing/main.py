import cv2 as cv
import numpy as np
from funkcje_zew import transform,usuwanie


rysowanie = False
ix, iy = -1, -1
tlowe = 'tlowe.txt'
img_gray = cv.imread('724.tif', 0)
img_rgb = cv.imread('724.tif',1)
punkciki = []

def info():

    height, width, channels = img_rgb.shape
    num_pixels = height * width
    data_type = img_rgb.dtype
    pixel_range = (img_rgb.min(), img_rgb.max())
    print("Wysokość obrazu:", height)
    print("Szerokość obrazu:", width)
    print("Liczba kanałów obrazu:", channels)
    print("Liczba pikseli obrazu:", num_pixels)
    print("Typ danych pikseli:", data_type)
    print("Zakres wartości pikseli:", pixel_range)

info()

#Okienka
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, rysowanie
    if event == cv.EVENT_LBUTTONDOWN:
        rysowanie = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if rysowanie:
            img_draw = img_gray.copy()
            cv.rectangle(img_draw, (ix, iy), (x, y), (255, 255, 255), 2)
            cv.imshow('image', img_draw)
    elif event == cv.EVENT_LBUTTONUP:
        rysowanie = False
        mask = np.zeros_like(img_gray)
        cv.rectangle(mask, (ix, iy), (x, y), (255, 255, 255), -1)
        masked_image = cv.bitwise_and(img_gray, mask)
        prostokat(masked_image, (ix, iy), (x, y))


def prostokat(image, punkt1, punkt2):
    global template, punkciki
    x1, y1 = punkt1
    x2, y2 = punkt2
    template = image[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
    template_pow = cv.resize(template, None, fx=5, fy=5)  # Powiększenie obrazka
    cv.imshow('template', template_pow)
    cv.waitKey(0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.65
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        x = pt[0] + w // 2
        y = pt[1] + h // 2
        srodek = (x, y)
        punkciki.append(srodek)
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
    punkciki = usuwanie(punkciki)
    cv.imwrite(r'D:\studia\4sem\foto\projekt2.1\wynik.png', img_rgb)
    cv.namedWindow('img_rgb', cv.WINDOW_NORMAL)
    cv.imshow('img_rgb', img_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()
    L, A, Xn = transform(tlowe, punkciki)
    print("L: \n",L,"\n","A: \n",A,"\n","Xn: \n", Xn)

cv.imshow('image', img_gray)
cv.setMouseCallback('image', draw_rectangle)

while True:
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
























