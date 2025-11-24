[app]
title = Jarvis AI
package.name = jarvis.ai.pro
package.domain = org.vinay
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd,requests,gtts,android,pyjnius,pillow
android.permissions = INTERNET,RECORD_AUDIO,CALL_PHONE
android.api = 34
android.minapi = 24
android.accept_sdk_license = True
orientation = portrait
fullscreen = 1
​[buildozer]
log_level = 2
warn_on_root = 1
