$nimi = "Karl Robert Masing"
$Email = "karlrobertmasing@gmail.com"
${kuu paev} = get-date -Format "dd.MM.yy"
$skriptiAsukoht = $MyInvocation.MyCommand.Path
$dir = Split-Path $skriptiAsukoht
$emailid = Get-Content -path $dir\emailid.txt

$nimi
"**********************"
$Email
"**********************"
$kp
"**********************"
$emailid += $email
$kasutajad = $emailid.split(",")
"Esimene kasutaja on: "+$kasutajad[0]
"Viimane kasutaja on: "+$kasutajad[-1]
"kasutajaid kokku on: "+$kasutajad.Count