# Valós idejű személyfelismerő és számláló

Ez a projekt egy Python alapú alkalmazás, amely a YOLOv8 objektumfelismerő modellt és az OpenCV könyvtárat használja. A program képes a webkamera élőképén valós időben felismerni, bekeretezni és megszámolja a képernyőn látható embereket.

## Telepítés lépésről lépésre

Le kell tölteni a programhoz szükséges külső könyvtárakat (`opencv-python` és `ultralytics`):

1. Nyiss meg egy parancssort (CMD).
2. Futtasd a következő parancsot a telepítéshez:
   ```bash
   pip install opencv-python ultralytics
   ```

## Funkciók
- **Valós idejű személyfelismerés:** YOLOv8 nano (`yolov8n.pt`) modell segítségével.
- **Képi visszajelzés:** Felismert személyek bekeretezése zöld kerettel (bounding box) és feliratozása ("Szemely").
- **Számláló:** A képernyőn lévő személyek folyamatos, valós idejű számolása a kijelző sarkában.
- **Élő megjelenítés:** A kamerakép és a felismerési adatok élő videófolyamként való megjelenítése.

## Használat

1. Indítsd el a programot a parancssorból:
3. A megjelenő ablakban látható a webkamera élő képe.
4. A programból az **`x`** billentyű megnyomásával tud kilépni.

## Kód magyarázata

- `import cv2` / `from ultralytics import YOLO`: Könyvtárak betöltése a videókezeléshez és a mesterséges intelligencia modellhez.
- `model = YOLO('yolov8n.pt')`: A YOLOv8 nano objektumdetektáló modell betöltése (az első futáskor automatikusan letölti).
- `cap = cv2.VideoCapture(0)`: Csatlakozás az alapértelmezett webkamerához.
- `while cv2.waitKey(1) != ord('x'):`: Fő ciklus, amely addig fut folyamatosan, amíg az 'x' gombot meg nem nyomjuk.
- `ret, frame = cap.read()`: Aktuális képkocka beolvasása a webkamerából.
- `results = model(frame, verbose=False)`: A kép elemzése a YOLO modellel. A `verbose=False` elrejti a konzolos naplózást.
- `if class_id == 0:`: Ellenőrzi, hogy a felismert objektum személy-e (a COCO adatbázisban a 0-s azonosító jelenti a "person" osztályt).
- `cv2.rectangle(...)` és `cv2.putText(...)`: Zöld keret rajzolása a megtalált személy köré, feliratozás, számláló kiírása.
- `cv2.imshow(...)`: A rajzokkal kiegészített képkocka megjelenítése az asztalon.
- `cap.release()` és `cv2.destroyAllWindows()`: Kamera kapcsolatának lezárása és az ablakok bezárása a programból való kilépéskor.
