from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub,SubscribeListener
from pubnub.enums import PNStatusCategory
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-2d2de682-b0a1-11e8-bf00-aaab7b0b8683'
pnconfig.publish_key = 'pub-c-55664c77-0d80-4e16-b2d8-0f3a0b0a4079'
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


