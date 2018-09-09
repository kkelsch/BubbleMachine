# Pubnub setup
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub,SubscribeListener
from pubnub.enums import PNStatusCategory
from pubnub.callbacks import SubscribeCallback

# gpio setup
import RPi.GPIO as GPIO
import time 
PinNum = 4
GPIO.setmode(GPIO.BCM)   #use BCM pin numbering
GPIO.setup(PinNum, GPIO.OUT)

print('testing...')
GPIO.output(PinNum,GPIO.HIGH)
time.sleep(5)
GPIO.output(PinNum,GPIO.LOW)
print('done')


# Pubnub config
pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-ec257da0-b468-11e8-bfaa-a64428e1f03d'
pnconfig.publish_key = 'pub-c-7e20d64c-a4f3-4e74-a0f0-09d0e3d2e213'
pnconfig.ssl = False
 
pubnub = PubNub(pnconfig)
bChannel = 'Bubble-Channel'

print('listening...')


#pubnub listener

class MyListener(SubscribeCallback):
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNConnectedCategory:
            pubnub.publish().channel(bChannel).message({'status': 'start'}).sync()
 
    def message(self, pubnub, response):
        print(response.message)
 
    def presence(self, pubnub, presence):
        pass
 
my_listener = MyListener()
 
pubnub.add_listener(my_listener)

pubnub.subscribe().channels(bChannel).execute()
