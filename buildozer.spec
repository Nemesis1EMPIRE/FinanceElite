[app]
title = Financia Pro Gabon
package.name = ga.financia.pro
package.domain = ga.financia
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0
requirements = python3,kivy,kivymd,requests
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

# Configuration Android
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.ndk_api = 21
android.gradle_dependencies = ''
android.arch = armeabi-v7a

[ios]
# Configuration iOS
