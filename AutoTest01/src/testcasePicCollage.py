'''
Created on Apr 24, 2013

@author: bach
'''
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()

device.installPackage('/home/bach/pic-collage-android/CollageProtoApp/bin/CollageProtoApp.apk')

package = 'com.cardinalblue.android.piccollage.multitouch.photoproto'

activity = '.MainActivity'

runComponent = package + '/' + activity

device.startActivity(component=runComponent)

MonkeyRunner.sleep(2)

device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

MonkeyRunner.sleep(2)

device.touch(200, 390, 'DOWN_AND_UP')

MonkeyRunner.sleep(2)

result = device.takeSnapshot()

MonkeyRunner.sleep(2)

result.writeToFile('/home/bach/pic-collage-android/CollageProtoApp/status_update.png','png')
