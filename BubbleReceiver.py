from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub,SubscribeListener
from pubnub.enums import PNStatusCategory
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-ec257da0-b468-11e8-bfaa-a64428e1f03d'
pnconfig.publish_key = 'pub-c-7e20d64c-a4f3-4e74-a0f0-09d0e3d2e213'
pnconfig.ssl = False
 
pubnub = PubNub(pnconfig)
bChannel = 'Bubble-Channel'

print('listening...')


class MyListener(SubscribeCallback):
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNConnectedCategory:
            pubnub.publish().channel(bChannel).message({'fieldA': 'begin'}).sync()
 
    def message(self, pubnub, message):
        print(message.text)
 
    def presence(self, pubnub, presence):
        pass
 
my_listener = MyListener()
 
pubnub.add_listener(my_listener)

pubnub.subscribe().channels(bChannel).execute()


