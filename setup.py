# setup.py — Run this once on any new device to set up everything

import subprocess
import sys
import os

print("📦 Installing dependencies...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
print("✅ Dependencies installed")

print("\n📁 Creating folders...")
os.makedirs('model', exist_ok=True)
os.makedirs('static/uploads', exist_ok=True)
os.makedirs('templates', exist_ok=True)
print("✅ Folders ready")

print("\n📥 Downloading pretrained model (one time, ~700MB)...")
from transformers import AutoProcessor, AutoModelForCausalLM
processor = AutoProcessor.from_pretrained('microsoft/git-base-coco')
model     = AutoModelForCausalLM.from_pretrained('microsoft/git-base-coco')
print("✅ Model downloaded and cached")

print("\n🧠 Building vocabulary...")
import pickle
import sys
sys.path.insert(0, '.')
from model.vocab import Vocabulary

vocab = Vocabulary()
for token in ['<pad>', '<start>', '<end>', '<unk>']:
    vocab.add_word(token)

words = ['a','an','the','is','are','on','in','of','with','and','to','at','man','woman','person','people','dog','cat','car','street','road','tree','water','sky','grass','building','white','black','red','blue','green','large','small','standing','sitting','walking','running','holding','riding','playing','eating','looking','wearing','two','three','group','next','front','top','side','near','down','up','bicycle','bike','bus','train','truck','boat','horse','bird','cow','sheep','elephant','bear','zebra','giraffe','backpack','umbrella','handbag','tie','suitcase','frisbee','skis','snowboard','ball','kite','bat','glove','skateboard','surfboard','racket','bottle','glass','cup','fork','knife','spoon','bowl','banana','apple','sandwich','orange','broccoli','carrot','pizza','donut','cake','chair','couch','bed','table','toilet','laptop','mouse','remote','keyboard','phone','microwave','oven','sink','refrigerator','book','clock','vase','scissors','toothbrush','field','beach','park','kitchen','bathroom','bedroom','living','room','city','snow','rain','sun','light','dark','background','photo','image','picture','young','old','little','big','long','short','tall','each','other','another','some','its','their','his','her','there','that','this','which','who','what','through','over','under','between','behind','brown','yellow','orange','pink','purple','gray','wooden','metal','food','head','hand','face','hair','eye','mouth','leg','arm','body','floor','wall','window','door','sign','line','air','ground','area','way','day','night','home','fire','hat','shirt','pants','shoes','jacket','dress','glasses','court','game','sport','team','player','net','pool','wave','rock','mountain','hill','river','lake','ocean','bridge','tower','church','store','station','airport','post']
for w in words:
    vocab.add_word(w)

with open('model/vocab.pkl', 'wb') as f:
    pickle.dump(vocab, f)
print("✅ Vocabulary built")

print("\n🚀 Setup complete! Run the app with:")
print("   python app.py")