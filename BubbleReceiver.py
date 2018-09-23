# Pubnub setup
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub,SubscribeListener
from pubnub.enums import PNStatusCategory
from pubnub.callbacks import SubscribeCallback

# gpio setup
import RPi.GPIO as GPIO
import time 
PinNum = 4
seconds_run = 5
GPIO.setmode(GPIO.BCM)   #use BCM pin numbering
GPIO.setup(PinNum, GPIO.OUT)

print('Testing Machine...')
GPIO.output(PinNum,GPIO.HIGH)
time.sleep(seconds_run)
GPIO.output(PinNum,GPIO.LOW)
print('done')


# Pubnub config
pnconfig = PNConfiguration()
pnconfig.subscribe_key = '<secret>'
pnconfig.publish_key = '<secret>'
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
        GPIO.output(PinNum,GPIO.HIGH)
        time.sleep(seconds_run)
        GPIO.output(PinNum,GPIO.LOW)
 
    def presence(self, pubnub, presence):
        pass
 
my_listener = MyListener()
 
pubnub.add_listener(my_listener)

pubnub.subscribe().channels(bChannel).execute()
