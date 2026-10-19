# Valós idejű személyfelismerő és számláló

Ez a projekt egy Python alapú alkalmazás, amely a legmodernebb YOLOv8 objektumfelismerő modellt és az OpenCV könyvtárat használja. A program képes a webkamera élőképén valós időben felismerni, bekeretezni és megszámolni a képernyőn látható embereket.

## Telepítés lépésről lépésre

Le kell tölteni a programhoz szükséges külső könyvtárakat (`opencv-python` és `ultralytics`):

1. Nyiss meg egy parancssort CMD.
2. Futtasd a következő parancsot a telepítéséhez:
   ```bash
   pip install opencv-python ultralytics

## Funkciók
- **Valós idejű személyfelismerés:** YOLOv8 nano (`yolov8n.pt`) modell segítségével.
- **Képi visszajelzés:** Felismert személyek bekeretezése zöld kerettel (bounding box) és feliratozása ("Szemely").
- **Számláló:** A képernyőn lévő személyek folyamatos, valós idejű számolása a kijelző sarkában.
- **Élő megjelenítés:** A kamerakép és a felismerési adatok élő videófolyamként való megjelenítése.
