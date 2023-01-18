
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
 

$csv_header = @("Nimed;Kasutajanimi;email;password")
 

$csv_header | Set-Content $dir\emails.csv
 
$users = Import-Csv $dir\users.csv
 
ForEach($user in $users){
    $fname = $user.first_name
    $lname = $user.last_name

    $fullname = $fname +" "+$lname

    $kasutajanimi = $fname[0]+$lname
 
    $pass = 1..3 | ForEach-Object { Get-Random -Maximum $lname.Length }
    $pass = -join $lname[$pass] 
    $pass += Get-Random  -minimum 10 -Maximum 99
 
    $row = $fullname+";"+$kasutajanimi+";"+$fname.ToLower()+"."+$lname.ToLower()+"@hkhk.edu.ee;"+$pass
    Add-Content $dir\emails.csv $row
}