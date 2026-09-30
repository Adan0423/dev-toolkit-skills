[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

function Resolve-Tool([string]$Name) {
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    return $null
}

$scrcpy = Resolve-Tool 'scrcpy.exe'
$adb = Resolve-Tool 'adb.exe'

[pscustomobject]@{
    Scrcpy = $scrcpy
    Adb = $adb
    AndroidSdkRoot = $env:ANDROID_SDK_ROOT
    AndroidHome = $env:ANDROID_HOME
} | Format-List

if ($adb) {
    & $adb start-server | Out-Host
    & $adb devices -l | Out-Host
}
