$arvutinimi = hostname
$kovakettad = Get-WmiObject -Class win32_logicaldisk | Format-Table DeviceId, MediaType, @{n="Size";e={[math]::Round($_.Size/1GB,2)}},@{n="FreeSpace";e={[math]::Round($_.FreeSpace/1GB,2)}}
$vaba = (Get-CimInstance -ClassName Win32_LogicalDisk).FreeSpace[0]
$suurus = (Get-CimInstance -ClassName Win32_LogicalDisk).Size[0]
$tehe = [float]$vaba/[float]$suurus
$tehe

