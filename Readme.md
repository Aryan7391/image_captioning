# CaptionNet — Image Caption Generator

CNN + LSTM based image captioning using GIT-base-COCO pretrained model.

## Requirements
- Python 3.8+
- Internet connection (first run only, to download model)

## Setup (run once on any new device)

1. Clone or copy the project folder
2. Open terminal in project folder
3. Run setup script:
   python setup.py

## Run the app
   python app.py

## Open in browser
   http://localhost:5000

## Project Structure
image_captioning/
├── model/
│   ├── encoder.py        
│   ├── decoder.py        
│   ├── vocab.py          
│   └── vocab.pkl         
├── templates/
│   └── index.html        
├── static/
│   └── uploads/          
├── app.py                
├── caption.py            
├── requirements.txt      
├── setup.py              
└── README.md             
```

---

## Your Final Project Structure
```
image_captioning/
├── model/
│   ├── encoder.py
│   ├── decoder.py
│   ├── vocab.py
│   └── vocab.pkl
├── templates/
│   └── index.html
├── static/
│   └── uploads/
├── app.py
├── caption.py
├── requirements.txt   ← new
├── setup.py           ← new
└── README.md          ← new