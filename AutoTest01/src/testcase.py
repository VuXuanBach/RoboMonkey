'''
Created on Apr 24, 2013

@author: bach
'''
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()

device.installPackage('/home/bach/Programs/workspace/mokasocial-MokaTest-36b0b1d/AndroidTesting/bin/AndroidTesting.apk')

package = 'com.mokasocial.androidtesting'

activity = '.MainActivity'

runComponent = package + '/' + activity

device.startActivity(component=runComponent)

MonkeyRunner.sleep(2)

result = device.takeSnapshot()

MonkeyRunner.sleep(2)

result.writeToFile('/home/bach/Programs/workspace/mokasocial-MokaTest-36b0b1d/AndroidTesting/status_update.png','png')
