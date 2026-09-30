# Command reference

## Diagnóstico

```powershell
adb version
adb start-server
adb devices -l
scrcpy --version
scrcpy --help
```

## Selección

```powershell
scrcpy --serial=<SERIAL>
scrcpy --select-usb
scrcpy --select-tcpip
```

## Wi-Fi

```powershell
scrcpy --tcpip
adb pair <IP>:<PAIR_PORT>
adb connect <IP>:<ADB_PORT>
adb disconnect <IP>:<ADB_PORT>
```

## Desarrollo

```powershell
scrcpy --serial=<SERIAL> --stay-awake
scrcpy --serial=<SERIAL> --show-touches
scrcpy --serial=<SERIAL> --start-app=<PACKAGE>
scrcpy --serial=<SERIAL> --no-control
scrcpy --serial=<SERIAL> --max-size=1280 --max-fps=60
```

## Emulador

```powershell
emulator -list-avds
emulator -avd <AVD_NAME>
adb -s <SERIAL> wait-for-device
```
